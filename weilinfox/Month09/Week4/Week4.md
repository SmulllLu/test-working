# Month 9 Week 4 工作报告 24/03/25-24/03/29

## RuyiSDK 测试

+ 完善 mugen 自动化测试，测试报告将自动化生成，主要 commit [6f55e28](github.com/weilinfox/ruyi-mugen/commit/6f55e2845a4e2b1d6897d285840a2a476cfa33b2) [6f55e28](https://github.com/weilinfox/ruyi-mugen/commit/6f55e2845a4e2b1d6897d285840a2a476cfa33b2)，并提交 pr [!8](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/8)
+ 为 0.8.0 版本做测试准备，编写 gnu-plct 工具链的 xiangshan-nanhu 配置测试，主要 commit [900b64f](https://github.com/weilinfox/ruyi-mugen/commit/900b64ff4dbd2a51e23c7adb97578c631e13e8b1)
+ 测试了 ruyi 0.7.0-beta.20240323 pre-release 版本，和 gnu-plct 的 xiangshan-nanhu 配置，发现问题并提交 issue [#103](https://github.com/ruyisdk/ruyi/issues/103) [#104](https://github.com/ruyisdk/ruyi/issues/104) [#112](https://github.com/ruyisdk/ruyi/issues/112)
+ 在 12 个测试平台进行 0.7.0 版本的 mugen 自动化测试，产出测试日志、报告和解说视频，提交 pr [!24](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/24)
   + x86\_64 Debian 12
   + x86\_64 Fedora 38
   + x86\_64 Ubuntu 22.04 LTS
   + x86\_64 openEuler 23.09
   + x86\_64 Archlinux
   + riscv64 Debian sid
   + riscv64 Fedora 38
   + riscv64 Ubuntu 22.04 LTS
   + riscv64 RevyOS 20231210
   + riscv64 openEuler 23.09
   + riscv64 Archlinux
   + aarch64 Debian 12
+ 提交文档，包含 0.7.0 新增特性、香山南湖编译环境配置和一些其他修复 pr [#41](https://github.com/ruyisdk/docs/pull/41)

