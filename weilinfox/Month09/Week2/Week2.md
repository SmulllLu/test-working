# Month 9 Week 2 工作报告 24/03/11-24/03/18

## RUYI 包管理 RPM 打包

+ RUYI 包管理基于 openEuler 23.09 的 RPM 包构建。由于 RUYI 0.6.0 将 git 依赖改为 pygit2 依赖，新增了一些依赖包。
   新增依赖包列表：
   | 包名                   | 版本            |
   | ---------------------- | --------------- |
   | python-cffi            | 1.16.0          |
   | python-pygit2          | 1.14.1          |
   | python-types-cffi      | 1.16.0.20240106 |
   | python-types-setuptools| 69.1.0.20240310 |
   | libgit2                | 1.7.2           |

   RUYI RPM 包：
   | 包名         | 版本  |
   | ------------ | ----- |
   | python3-ruyi | 0.6.0 |

## RuyiSDK 测试

+ 完成 ruyi-mugen 0.6.0 版本测试用例开发 pr [!6](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/6)
   | 主要功能更新                                          |                                            关联 commit                                             |
   | ----------------------------------------------------- |:--------------------------------------------------------------------------------------------------:|
   | 新增用例 ruyi\_test\_config             | [5234f52](https://github.com/weilinfox/ruyi-mugen/commit/5234f5296f7a2cbd38b0d85298c4f87492814e66) |
   | 在 RUYI 运行失败时使用 RUYI\_DEBUG=x  | [b447cea](https://github.com/weilinfox/ruyi-mugen/commit/b447cea6a7ee3276735f6b08b984fdd838bef5bc) |
   | 新增用力 ruyi\_test\_binaries | [b04440a](github.com/weilinfox/ruyi-mugen/commit/b04440a886c5e5708787b800e3861f1d1b61f083) |
   | 更新 README.md                     | [b04440a](https://github.com/weilinfox/ruyi-mugen/commit/b04440a886c5e5708787b800e3861f1d1b61f083) |
+ RUYI 包管理 0.6.0 mugen 自动化测试在 x86\_64 QEMU Fedora 38、 x86\_64 QEMU Ubuntu 22.04 LTS、 x86\_64 QEMU openEuler 23.09、 riscv64 Container RevyOS 20231210、 riscv64 QEMU openEuler 23.09 环境运行，测试发现 riscv64 架构二进制在 openEuler riscv 2309 无法正常使用。提交测试报告日志和视频 pr [!21](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/21) 提交 issue [#81](https://github.com/ruyisdk/ruyi/issues/81) [#82](https://github.com/ruyisdk/ruyi/issues/82) [#88](https://github.com/ruyisdk/ruyi/issues/88)
+ 另外发现 gnu-plct 工具链交叉编译得到的 Milkv Duo 动态链接二进制在 Milkv Duo 1.0.9 镜像无法运行，且官方工具链也是如此，可能需要添加进文档， issue [#91](https://github.com/ruyisdk/ruyi/issues/91)

## openEuler mugen

+ 更新 pr [!1993](https://gitee.com/openeuler/mugen/pulls/1993)，添加 x86\_64 测试截图
+ 根据上游评论更新 pr [!2330](https://gitee.com/openeuler/mugen/pulls/2330)
+ 2309 测试时向 mugen 上游提交的 9 个 pr 已经全部合并

