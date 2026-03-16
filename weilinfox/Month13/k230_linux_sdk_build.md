# k230\_linux\_sdk 构建

整个构建过程按照文档要求需要在 Ubuntu 22.04 或 24.04  进行，工具链和工具亦是为 Ubuntu 构建的。

经过测试 Ubuntu 24.04 可以完成整个构建流程。

构建脚本如下：

```bash
#!/bin/bash

sudo apt-get update
sudo apt-get install -y git sed make binutils build-essential diffutils gcc  g++ bash patch gzip \
        bzip2 perl  tar cpio unzip rsync file  bc findutils wget  libncurses-dev python3  \
        libssl-dev gawk cmake bison flex  bash-completion
git clone https://github.com/ruyisdk/k230_linux_sdk.git

# sudo mkdir -p /opt/toolchain
sudo mkdir -p /opt/toolchain/riscv64ilp32-elf-ubuntu-22.04-gcc-nightly-2024.06.25/
wget https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1721095219235/Xuantie-900-gcc-linux-6.6.0-glibc-x86_64-V2.10.1-20240712.tar.gz
wget https://github.com/ruyisdk/riscv-gnu-toolchain-rv64ilp32/releases/download/2024.06.25/riscv64ilp32-elf-ubuntu-22.04-gcc-nightly-2024.06.25-nightly.tar.gz
sudo tar -zxvf riscv64ilp32-elf-ubuntu-22.04-gcc-nightly-2024.06.25-nightly.tar.gz -C /opt/toolchain/riscv64ilp32-elf-ubuntu-22.04-gcc-nightly-2024.06.25/
sudo tar -zxvf Xuantie-900-gcc-linux-6.6.0-glibc-x86_64-V2.10.1-20240712.tar.gz -C /opt/toolchain

cd k230_linux_sdk
make CONF=k230d_canmv_ilp32_defconfig
cd ..

ls k230_linux_sdk/output/k230d_canmv_ilp32_defconfig/images/sysimage-sdcard.img
sudo rm -rf /opt/toolchain
```

应当可以正常得到镜像。

## 附

Archlinux 构建 k230\_linux\_sdk v0.2 失败日志：

```
$ make CONF=k230d_canmv_ilp32_defconfig
make -f tools/sync.mk sync   BR_SRC_DIR=output/buildroot-2024.02.1  BR_OVERLAY_DIR=buildroot-overlay  BR_NAME=buildroot-2024.02.1
make[1]: Entering directory '/home/hachi/Documents/Working/k230_linux_sdk-0.2'
make[1]: Leaving directory '/home/hachi/Documents/Working/k230_linux_sdk-0.2'
make -C output/buildroot-2024.02.1 k230d_canmv_ilp32_defconfig O=/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig
make[1]: Entering directory '/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/buildroot-2024.02.1'
  GEN     /home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/Makefile
#
# configuration written to /home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/.config
#
make[1]: Leaving directory '/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/buildroot-2024.02.1'
touch /home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/.config
make -C /home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig all
/usr/bin/make -j1  O=/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig HOSTCC="/usr/bin/gcc" HOSTCXX="/usr/bin/g++" syncconfig
  GEN     /home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/Makefile
>>> host-libffi 3.4.4 Building
GIT_DIR=. PATH="/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/bin:/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/sbin:/home/hachi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl" PKG_CONFIG="/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/bin/pkg-config" PKG_CONFIG_SYSROOT_DIR="/" PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1 PKG_CONFIG_ALLOW_SYSTEM_LIBS=1 PKG_CONFIG_LIBDIR="/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/lib/pkgconfig:/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/share/pkgconfig"  /usr/bin/make -j5  -C /home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/build/host-libffi-3.4.4/
MAKE x86_64-pc-linux-gnu : 0 * all-all
/usr/bin/make  all-recursive
Making all in include
make[6]: Nothing to be done for 'all'.
Making all in testsuite
make[6]: Nothing to be done for 'all'.
Making all in man
make[6]: Nothing to be done for 'all'.
/bin/sh ./libtool  --tag=CC   --mode=compile /usr/bin/gcc -DHAVE_CONFIG_H -I. -I..  -I. -I../include -Iinclude -I../src -I/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/include  -Wall -O2 -I/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/include -fexceptions -c -o src/tramp.lo ../src/tramp.c
/bin/sh ./libtool  --tag=CC   --mode=compile /usr/bin/gcc -DHAVE_CONFIG_H -I. -I..  -I. -I../include -Iinclude -I../src -I/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/include -I. -I../include -Iinclude -I../src -O2 -I/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/include -c -o src/x86/win64.lo ../src/x86/win64.S
libtool: compile:  /usr/bin/gcc -DHAVE_CONFIG_H -I. -I.. -I. -I../include -Iinclude -I../src -I/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/include -I. -I../include -Iinclude -I../src -O2 -I/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/include -c ../src/x86/win64.S  -fPIC -DPIC -o src/x86/.libs/win64.o
libtool: compile:  /usr/bin/gcc -DHAVE_CONFIG_H -I. -I.. -I. -I../include -Iinclude -I../src -I/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/include -Wall -O2 -I/home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/host/include -fexceptions -c ../src/tramp.c  -fPIC -DPIC -o src/.libs/tramp.o
../src/tramp.c: In function ‘ffi_tramp_get_temp_file’:
../src/tramp.c:262:22: error: implicit declaration of function ‘open_temp_exec_file’ [-Wimplicit-function-declaration]
  262 |   tramp_globals.fd = open_temp_exec_file ();
      |                      ^~~~~~~~~~~~~~~~~~~
make[6]: *** [Makefile:1323: src/tramp.lo] Error 1
make[5]: *** [Makefile:1395: all-recursive] Error 1
make[4]: *** [Makefile:623: all] Error 2
make[3]: *** [Makefile:591: all-all] Error 2
make[2]: *** [package/pkg-generic.mk:283: /home/hachi/Documents/Working/k230_linux_sdk-0.2/output/k230d_canmv_ilp32_defconfig/build/host-libffi-3.4.4/.stamp_built] Error 2
make[1]: *** [Makefile:23: _all] Error 2
make: *** [Makefile:22: buildroot] Error 2
```

