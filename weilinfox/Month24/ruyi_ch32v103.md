# 使用 Ruyi 包管理器点亮沁恒开发板

## 所需硬件

+ 开发板，型号 CH32V103C8T6-EVT-R1，丝印 CH32V103C-R1-1v1
+ WCH Link，型号 WCH-LinkE，丝印 WCH-LinkE-R0-1v3
+ 杜邦线，母对母， 8 根

## Ruyi 工具链和下载器

版本为 Ruyi 0.35.0

安装工具链

```bash
ruyi extract wch-ch32v103-evt
ruyi install gnu-wch-mrs-toolchain-gcc12-bin wlink
```

gnu-wch-mrs-toolchain-gcc12-bin 为沁恒发布的闭源工具链， wlink 为开源的 WCH-Link(RV) 命令行工具，可以从项目[主页](https://github.com/ch32-rs/wlink)查看介绍

## Ruyi 以外的软件

由于 Ruyi 无法解析 MounRiver Studio 工程，所以这里使用 [MounRiver_Studio_Community_V190](http://file-oss.mounriver.com/upgrade/MounRiver_Studio_Community_Linux_x64_V190.tar.xz)（基于 Eclipse）将工程解析为 Make 项目

## 开发板连接

开发板可以直接从 WCH Link 取电，注意 P10 上的 5V 是直通 1117 的，而 P8 上的则 5V 是受开关控制的。 P8 为在线调试口， P9 为串口 1。

P8 引脚从 1-5 分别为 +5V、 PA13、 PA14、 NRST、 GND。其中 5V 和 GND 可直接作为开发板供电，从 WCH-Link 取电即可，且受板载电源开关控制； PA13 为 SWDIO， PA14 为 SWCLK，分别与 WCH-Link 的同名引脚相连；NRST 与 WCH-Link 的 RST 连接。 P9 引脚 TX(PA9) 和 RX(PA10) 分别与 WCH-Link 的 RX 和 TX 连接，这里不需要再单独做共地。 P1 和 P2 为外设引出，将其中的 PA0 与 LED1 连接。

将 WCH-Link 连接计算机， ``lsusb`` 应当可以看到设备 ``ID 1a86:8010 QinHeng Electronics WCH-Link``，同时应有新的串口设备出现，如 ``/dev/ttyACM0``

检查电源开关 S2，将其拨到 ON，电源指示灯 D1 亮。电源开关未打开时 D1 可能也是亮的，这是因为连接了串口，但是此时亮度明显低。

## 官方例程 USART/USART_Printf

首先用 MounRiver Studio 解析工程，在 MounRiver Studio 的 Project Explorer 中选中该工程，右键， Build Project，可以看到构建成功。此时在这个工程下就可以看到 obj 目录了，这是 MounRiver Studio 生成的构建目录，将使用 Make 工具构建。

由于 MounRiver Studio 默认使用的是内建工具链，为了测试，将所有工具链替换成 ruyi 安装的工具链

```bash
sed -i  "s|riscv-none-embed-gcc|~/.local/share/ruyi/binaries/x86_64/gnu-wch-mrs-toolchain-gcc12-bin-2.1.0/bin/riscv-wch-elf-gcc|" */*.mk makefile
sed -i  "s|riscv-none-embed-objcopy|~/.local/share/ruyi/binaries/x86_64/gnu-wch-mrs-toolchain-gcc12-bin-2.1.0/bin/riscv-wch-elf-objcopy|" makefile
sed -i  "s|riscv-none-embed-objdump|~/.local/share/ruyi/binaries/x86_64/gnu-wch-mrs-toolchain-gcc12-bin-2.1.0/bin/riscv-wch-elf-objdump|" makefile
sed -i  "s|riscv-none-embed-size|~/.local/share/ruyi/binaries/x86_64/gnu-wch-mrs-toolchain-gcc12-bin-2.1.0/bin/riscv-wch-elf-size|" makefile
```

清除旧的构建，用 ruyi 重新构建

```bash
make clean
make all
```

构建产物为 ``obj/USART_Printf.hex``

由于芯片刷写后会立即复位，此时打开串口监看

```bash
sudo minicom -D /dev/ttyACM0
```

使用 wlink 刷写片上 flash

```bash
~/.local/share/ruyi/binaries/x86_64/wlink-0.1.1-ruyi.20250524+git.217f0e51/bin/wlink flash --address 0x08000000 ./USART_Printf.hex
```

wlink 命令输出如下

```
06:16:50 [INFO] Connected to WCH-Link v2.12(v32) (WCH-LinkE-CH32V305)
06:16:50 [INFO] Attached chip: CH32V103
06:16:50 [INFO] Chip ESIG: FlashSize(16386KB) UID(41-11-13-67-17-00-98-c3)
06:16:50 [INFO] Flash protected: true
06:16:50 [WARN] Flash is protected, debug access is not available
06:16:50 [INFO] Read ./USART_Printf.hex as IntelHex format
06:16:50 [WARN] --address is ignored when flashing ELF or ihex
06:16:50 [INFO] Flashing 7228 bytes to 0x08000000
06:16:50 [INFO] Flash already unprotected
06:16:50 [INFO] Read protected: true
██████████████████████████████████████████████████ 7228/722806:16:50 [INFO] Flash done
06:16:51 [INFO] Now reset...
```

同时 ``minicom`` 应有如下结果。注意该输出只在芯片启动（复位）时输出一次，若没有观察到，可以尝试按开发板上的复位按钮 S1 手动复位

```
SystemClk:72000000
ChipID:2500410f
This is printf example
```

## 官方例程 GPIO/GPIO_Toggle

同样，首先用 MounRiver Studio 解析工程。

测试使用 Ruyi 虚拟环境构建。

```bash
cd GPIO/GPIO_Toggle/obj
ruyi venv -t gnu-wch-mrs-toolchain-gcc12-bin --extra-commands-from wlink --without-sysroot generic wch_venv
source wch_venv/bin/ruyi-activate
```

将所有工具链替换成 ruyi 安装的工具链

```bash
sed -i  "s/riscv-none-embed-gcc/riscv-wch-elf-gcc/" */*.mk makefile
sed -i  "s/riscv-none-embed-objcopy/riscv-wch-elf-objcopy/" makefile
sed -i  "s/riscv-none-embed-objdump/riscv-wch-elf-objdump/" makefile
sed -i  "s/riscv-none-embed-size/riscv-wch-elf-size/" makefile
```

清除旧的构建，用 ruyi 重新构建

```bash
make clean
make all
```

构建产物为 ``obj/GPIO_Toggle.hex``

```bash
wlink flash --address 0x08000000 ./GPIO_Toggle.hex
```

输出如下

```
07:13:27 [INFO] Connected to WCH-Link v2.12(v32) (WCH-LinkE-CH32V305)
07:13:27 [INFO] Attached chip: CH32V103 (ChipID: 0x2500410f)
07:13:27 [INFO] Chip ESIG: FlashSize(64KB) UID(cd-ab-d5-0d-f4-bc-96-76)
07:13:27 [INFO] Flash protected: false
07:13:27 [INFO] Read ./GPIO_Toggle.hex as IntelHex format
07:13:27 [WARN] --address is ignored when flashing ELF or ihex
07:13:27 [INFO] Flashing 7368 bytes to 0x08000000
07:13:27 [INFO] Read protected: false
██████████████████████████████████████████████████ 7368/736807:13:28 [INFO] Flash done
07:13:28 [INFO] Now reset...
```

串口应有如下结果

```
SystemClk:72000000
ChipID:2500410f
GPIO Toggle TEST
```

LED1 应当以 0.5s 为周期不断闪烁

