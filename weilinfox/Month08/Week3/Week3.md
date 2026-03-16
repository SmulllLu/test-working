# Week3 工作报告 24/02/21-24/02/29

## RuyiSDK 测试

+ 完成 ruyi-mugen 0.5.0 版本测试用例开发 pr [!5](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/5)
   | 主要功能更新                                          |                                            关联 commit                                             |
   | ----------------------------------------------------- |:--------------------------------------------------------------------------------------------------:|
   | 新增用例 ruyi\_test\_gnu-plct-rv64ilp32-elf             | [394f954](https://github.com/weilinfox/ruyi-mugen/commit/39e4f9547ca60a59aada08754df324224bf6a98f) |
   | 测试平头哥工具链交叉编译得到的二进制在 RevyOS 的运行  | [44760e5](https://github.com/weilinfox/ruyi-mugen/commit/44760e53979b9e6cf581e80beb77afc663575674) |
   | 修复 mugen 框架在用例超时时无法正常杀死测试进程的问题 | [0c5f51e](https://github.com/weilinfox/ruyi-mugen/commit/0c5f51e31795d2106bf6e2bbdb1f3503819914f8) |
   | 优化 mugen 框架用例超时的判断逻辑                     | [df1c53c](https://github.com/weilinfox/ruyi-mugen/commit/df1c53c329c77927c189587877c17ae4a3c16156) |
+ RUYI 包管理 0.5.0 版本新增 CanMV-K230 镜像刷写，测试了镜像刷写功能的可用性并提交测试报告 pr [!14](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/14)
+ RUYI 包管理 0.5.0 mugen 自动化测试在 x86\_64 QEMU Fedora 38、 x86\_64 QEMU Ubuntu 22.04 LTS、 x86\_64 QEMU openEuler 23.09、 riscv64 Container RevyOS 20231210、 riscv64 QEMU openEuler 23.09 环境运行，测试没有发现失败并提交测试报告 pr [!16](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/16)
+ 文档添加 0.5.0 版本新增特性 pr [!34](https://github.com/ruyisdk/docs/pull/34)

