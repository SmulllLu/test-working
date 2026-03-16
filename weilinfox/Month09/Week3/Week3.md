# Month 9 Week 3 工作报告 24/03/18-24/03/22

## RuyiSDK 测试

+ mugen 适配 Archlinux 的 pacman 包管理器，并新增测试平台 pr [!7](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/7)
   + x86\_64 Debian 12
   + x86\_64 Archlinux
   + riscv64 Debian sid
   + riscv64 Fedora 38
   + riscv64 Ubuntu 22.04 LTS
   + riscv64 Archlinux
+ 放了一个实验性 aarch64 测试容器，也加入了测试队列 commit [1d601a7](https://github.com/weilinfox/ruyi-mugen/commit/1d601a77adc58ed2fceaf5bd03c0c017666fbc9b)
   + aarch64 Debian 12
+ 测试了0.7.0-alpha.20240315 pre-release 版本，发现其不能在 Archlinux riscv64 上运行，并提交 issue [#97](https://github.com/ruyisdk/ruyi/issues/97)
+ 在使用 RUYI 进行 Milkv Duo 的开发时发现在较新的 Milkv Duo 镜像上需要用 musl 工具链，这在 RUYI 上没有对应的包，在之前提交的 issue [!91](https://github.com/ruyisdk/ruyi/issues/91) 下面进行了[评论](https://github.com/ruyisdk/ruyi/issues/91#issuecomment-2008690712)

