# 山大 sg2048 2U 服务器配置和组网

## 概况

服务器版本为 SG2042 SERVER V1.2 ，具有两颗 SG2042 CPU ， 256G 内存和 1T 固态存储。

## 系统安装

系统安装通常需要取下 SSD 进行烧写。为了方便烧写这里采用从 USB 启动后，再用 USB 系统对 SSD 进行 ``dd`` 操作的方式烧写。

注意 VGA 可能无法点亮屏幕，建议直接由局域网进入 BMC 操作。

### 进入 BMC

在浏览器地址框键入 BMC 的 IP 地址并访问。注意需要使用 https 协议，遇到证书安全提示直接信任即可。

默认的 BMC 账户为 root ，密码为 root 。

### 使用官方 Fedora 镜像建立 USB 启动盘

由于启动参数以分区标签指定根目录分区，而以 ``dd`` 方式烧写系统并不会改变该标签。故在不更改烧写到 USB 后的分区标签的情形下，实际启动的根目录将会具有一定的随机性。这样的情况在出厂带有两块 SSD 的服务器上也会发生，因为出场自带的两块 SSD 都刷写了同样的镜像。

使用 dd 工具写入镜像：

```bash
$ sudo dd if=Fedora.img of=/dev/sda bs=100M status=progress
```

查看根分区标签：

```bash
$ sudo e2label /dev/sda3
ROOT
```

默认分区标签应当为 ROOT 。

修改分区标签：

```bash
$ sudo tune2fs -L USB /dev/sda3
```

检查根分区标签：

```bash
$ sudo e2label /dev/sda3
USB
```

更改标签成功。

随后修改启动参数，指定为新的分区标签：

```bash
$ sudo mount /dev/sda2 /mnt/boot
$ cat /mnt/boot/extlinux/extlinux.conf
## /boot/extlinux/extlinux.conf

default fedora_sophgo
menu title linuxboot menu
prompt 0
timeout 50

label fedora_sophgo
        menu label Fedora Sophgo in SD
        linux /vmlinuz-6.1.31
        initrd /initramfs-6.1.31.img
        append  console=ttyS0,115200 root=LABEL=ROOT rootfstype=ext4 rootwait rw earlycon selinux=0 LANG=en_US.UTF-8
```

对启动配置应用下面的 patch ：

```
--- extlinux.conf.old   2023-12-25 20:22:17.247727278 +0800
+++ extlinux.conf       2023-12-25 20:22:27.267705346 +0800
@@ -9,4 +9,4 @@
        menu label Fedora Sophgo in SD
        linux /vmlinuz-6.1.31
        initrd /initramfs-6.1.31.img
-       append  console=ttyS0,115200 root=LABEL=ROOT rootfstype=ext4 rootwait rw earlycon selinux=0 LANG=en_US.UTF-8
+       append  console=ttyS0,115200 root=LABEL=USB rootfstype=ext4 rootwait rw earlycon selinux=0 LANG=en_US.UTF-8
```

由于 2U 服务器尚有一些 bug ，使用官方 Fedora 镜像烧写 USB 无法正常进入系统，当前推荐使用 RevyOS 制作启动盘。

另外注意在 Fedora 中运行 ``sudo reboot`` 是不能正常重启的，请**不要用这个方法重启服务器**。

### 使用 RevyOS 镜像建立 USB 启动盘

下载并解包镜像：

```bash
$ wget https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20231220/revyos-pisces-20231220-004504.img.zst
$ zstd -d revyos-pisces-20231220-004504.img.zst
```

烧写镜像：

```bash
$ sudo dd if=revyos-pisces-20231220-004504.img of=/dev/sda bs=100M status=progress
$ sudo sync
```

RevyOS 制作的 USB 启动盘可以直接用于重装 Fedora 。

在 BMC 的 Operations 选项卡中的 Server power operations 标签页中，在 Boot settings override 中选择 Usb ，在 Reboot server 中按需选择 Orderly 或 Immediate ，点击 Reboot 按钮即可重启。注意由于固件 Bug ，**可能会重启失败**。

重启后在 SOL Console 选项卡选择 CPU0_UART0 ，点击 Set port ，查看重启状态。在 LinuxBoot 中选择正确的启动设备即可启动到 USB 启动盘。

在 ``dd`` 系统镜像到 SSD 时需要注意，除了 SSD 外，服务器还板载了两颗 32G 的 emmc 。

### 使用 WireGuard 组网

在没有可以公网访问的跳板机用于内网访问的情况下，可以使用 WireGuard 与公网服务器进行组网，使用公网远程服务器作为跳板机。

公网服务端配置 ``/etc/wireguard/wg0.conf`` ：

```
[Interface]
Address    = 172.16.5.1/24
PrivateKey = 
ListenPort = 50406
#PostUp     = iptables -A FORWARD -i %i -j ACCEPT; iptables -A FORWARD -o %i -j ACCEPT
#PostDown   = iptables -D FORWARD -i %i -j ACCEPT; iptables -D FORWARD -o %i -j ACCEPT

# 1
[Peer]
PublicKey = 
PresharedKey = 
AllowedIPs = 172.16.5.5/32
PersistentKeepalive = 25

# 2
[Peer]
PublicKey = 
PresharedKey = 
AllowedIPs = 172.16.5.6/32
PersistentKeepalive = 25
```

内网服务器 1 配置：

```
[Interface]
Address = 172.16.5.5/32
PrivateKey = 

[Peer]
PublicKey = 
PresharedKey = 
AllowedIPs =  172.16.5.1/24
Endpoint = <server ip>:50406
PersistentKeepalive = 25
```

内网服务器 2 配置：

```
[Interface]
Address = 172.16.5.6/32
PrivateKey = 

[Peer]
PublicKey = 
PresharedKey = 
AllowedIPs =  172.16.5.1/24
Endpoint = <server ip>:50406
PersistentKeepalive = 25
```

其中 ``<server ip>`` 为公网跳板机 IP 地址。

在三台机器开启 WireGuard 服务：

```bash
$ sudo systemctl enable --now wg-quick@wg0
```

当握手成功时应当有双向流量，即发送和接收流量均不应为 0 ，随着交换数据的增加统计数值也将增加：

```bash
$ sudo wg | grep transfer
  transfer: 1.31 MiB received, 780.43 KiB sent
  transfer: 20.23 MiB received, 4.92 MiB sent
```

### 使用远程跳板机实现内网服务器访问

由上一节的方法实现内网服务器与远程服务器的组网后，这里将远程服务器作为跳板机实现与内网服务器的 ssh 连接。

配置 ssh ：

```
Host public_server
  HostName <server ip>
  Port 50406
  IdentityFile ~/.ssh/id_rsa
  User youmu_jump

Host sdu0
  HostName 172.16.5.5
  Port 22
  ProxyJump public_server
  IdentityFile ~/.ssh/id_rsa
  User youmu

Host sdu1
  HostName 172.16.5.6
  Port 22
  ProxyJump public_server
  IdentityFile ~/.ssh/id_rsa
  User youmu
```

注意这里使用的服务器内网 IP 为 WireGuard 组网的 IP ，如果需要使用实际内网 IP 则需要额外的配置，或者使用下一节的方法映射任意内网 IP 地址和端口。

连接服务器：

```bash
$ ssh sdu0
$ ssh sdu1
```

### 使用远程跳板机实现服务器 BMC 访问

由于 BMC 的 IP 地址和服务器本身的 IP 地址不同，这里使用 ssh 端口映射实现服务器 BMC 的访问。

```bash
ssh -N -L 50406:<bmc ip>:443 sdu0
```

这里以 sdu0 为跳板，映射内网的 BMC 地址到本地 50406 端口。

此时访问 ``https://localhost:50406`` 即可访问 ``<bmc ip>`` 指向的服务器 BMC 网页。注意该 ``<bmc ip>`` 指向的 BMC 并不一定是 sdu0 服务器的 BMC ，只要是 sdu0 服务器可以访问到的内网 IP 地址和端口均可以映射。

## 服务器手册

+ [算能 SR0-2208A0 产品使用手册V0.4](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/docs/sg2042_2U/%E7%AE%97%E8%83%BD%20SR0-2208A0%20%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8CV0.4.pdf)

## 外部链接

+ [官方镜像 Fedora+Ubuntu](https://sophon-file.sophon.cn/sophon-prod-s3/drive/23/11/23/21/multi_chip.zip)
+ [RevyOS 20231220](https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20231220/revyos-pisces-20231220-004504.img.zst)

