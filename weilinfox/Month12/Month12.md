# Month 12 工作报告 24/06/01-24/06/28

## RuyiSDK

+ ruyi mugen 更新 pr [!16](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/16) [!17](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/17) [!18](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/18)
   | 主要功能更新                                                 | 提交                                                                                               |
   | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
   | Ubuntu 24.04 x86\_64 和 riscv64 架构加入自动化测试平台       | [1321229](https://github.com/weilinfox/ruyi-mugen/commit/1321229dc7c0af3436f88ff244aa44c0e6966909) |
   | 测试 0.12.0-beta.20240607 版本                               | [dd05f64](https://github.com/weilinfox/ruyi-mugen/commit/dd05f647a56508bd650deae2c27b50a61117b3ea) |
   | 测试 0.12.0 版本                                             | [b0c1bce](https://github.com/weilinfox/ruyi-mugen/commit/b0c1bce49dea11245ba87c5fff9fb558f06a347b) |
   | 使用 Gitee 镜像仓库测试                                      | [f3477cf](https://github.com/weilinfox/ruyi-mugen/commit/f3477cf973d51ba9611bb31dd23aca1f4f3d34f0) |
   | device provision 文档连接测试                                | [3f3e16a](https://github.com/weilinfox/ruyi-mugen/commit/3f3e16afbb487d78d2e227dea6802b69108028a6) |
   | 测试 0.13.0-beta.20240624 版本                               | [0fe0898](https://github.com/weilinfox/ruyi-mugen/commit/0fe08989f52edce8e7f6ae03eb1e3a9d272feafe) |
   | 测试 0.13.0 版本                                             | [2995418](https://github.com/weilinfox/ruyi-mugen/commit/299541896952bd425f367d6e263ab4161dd0a9b8) |
   | openEuler 2403 LTS x86\_64 和 riscv64 架构加入自动化测试平台 | [e30023d](https://github.com/weilinfox/ruyi-mugen/commit/e30023d51b90667c05dabf2539ceec81335d35ae) |
+ 搭建 Ubuntu 24.04 LTS 的 x86\_64 和 riscv64 测试机，并纳入 0.12.0 测试范围
+ 搭建 openEuler 24.03 LTS 的 x86\_64 和 riscv64 测试机，并纳入 0.13.0 测试范围
+ 将软件所的一台 Pioneer Box 加入 Jenkins CI 测试节点
+ 在 Gitee 做 packages-index、 ruyi-mugen 的镜像，分别产出 Jenkinsfile [packages-index.groovy](https://github.com/weilinfox/ruyi-gitee-mirror/blob/master/packages-index.groovy) [ruyi-mugen.groovy](https://github.com/weilinfox/ruyi-gitee-mirror/blob/master/ruyi-mugen.groovy)。
+ 实习生面试，新实习生在 7 月开始实习
+ 测试了 0.12.0 版本，提交 issue
   | issue 标题                                                                           | issue 链接                                         |
   | ------------------------------------------------------------------------------------ | -------------------------------------------------- |
   | The behavior of the extract command varies for different version of coremark package | [#158](https://github.com/ruyisdk/ruyi/issues/158) |
   | Version matches not act correctly                                                    | [#159](https://github.com/ruyisdk/ruyi/issues/159) |
+ 完成 ruyi 0.12.0 版本在 22 个平台的 mugen 自动化测试并提交各平台日志报告和视频 [!41](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/41) [!42](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/42)
+ 完成 ruyi 0.13.0 版本在 24 个平台的 mugen 自动化测试并提交各平台日志报告和视频 [!43](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/43)
+ 给 [ruyisdk/ruyi](https://github.com/ruyisdk/ruyi/) 提交一个 pr 一处重复的类型标注 [#160](https://github.com/ruyisdk/ruyi/pull/160)

## 自动化测试平台

+ ruyi-reimu 更新，验证基本的版本比较算法，完成十一个镜像的上游版本检测和 issue 提交支持
   [详细代码更新](https://github.com/weilinfox/ruyi-reimu/compare/fde1bbb..440203)

