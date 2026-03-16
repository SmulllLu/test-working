# Month 8 工作报告 24/02/05-24/02/08 24/02/21-24/02/29

## RUYI 包管理 RPM 打包

+ RUYI 包管理基于 openEuler 23.09 的 RPM 包构建。由于 RUYI 的部分 python3 依赖包版本较高，需要重新打包
   依赖包列表：
   | 包名                   | 版本            |
   | ---------------------- | --------------- |
   | python3-semver         | 3.0.2           |
   | python3-markdown-it-py | 3.0.0           |
   | python3-mdurl          | 0.1.2           |
   | python3-rich           | 13.5.2          |
   | python3-tqdm           | 4.66.1          |
   | python3-types-pyxdg    | 0.28.0.20240106 |
   | python3-frontmatter    | 1.1.0           |

   RUYI RPM 包：
   | 包名         | 版本  |
   | ------------ | ----- |
   | python3-ruyi | 0.4.0 |
+ 建立 ruyi-rpms 仓库托管 RPM 包于 [Gitee](https://gitee.com/weilinfox/ruyi-rpms/) [GitHub](https://github.com/weilinfox/ruyi-rpms/)
+ 对 python3-ruyi 运行 mugen 测试，其中 ruyi\_test\_common 、ruyi\_test\_xdg 出现失败，分析认为这是 RUYI 识别到了打包方式的不同而对相关操作做出不同的反应，而非缺陷； ruyi\_test\_device 出现失败，分析认为这是打包方式不同导致命令输出有不同，影响了测试用例的判断，亦非缺陷。完整[日志](https://gitlab.inuyasha.love/weilinfox/plct-working/-/tree/master/Done/Month08/Week1/logs/ruyi)
+ 给出一个 RUYI 包管理在 openEuler 23.09 独立发行版本的安装文档 [ruyi-rpm.md](https://gitlab.inuyasha.love/weilinfox/plct-working/-/tree/master/Done/Month08/Week1/ruyi-rpm.md)

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

