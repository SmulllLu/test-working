# Month 10 Week 1 工作报告 24/04/01-24/04/07

## RuyiSDK

+ ruyi mugen 更新 pr [!9](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/9)
   | 主要功能更新                              | 提交                                                                                                                                                                                                    |
   | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | 同步报告和 tarball 中的目录名             | [cc4c176](https://github.com/weilinfox/ruyi-mugen/commit/cc4c1768b4cce81ff980a26451deac00d84142cf)， [eee923b](https://github.com/weilinfox/ruyi-mugen/commit/eee923bcd62ec555dae2da5049785ec82d27c3c7) |
   | 测试 0.8.0-beta.20240406 版本             | [54850fd](github.com/weilinfox/ruyi-mugen/commit/54850fde778f19e5400a8c5dfb1f547fd70591d1)                                                                                                              |
   | 测试时配置 RUYI_FORCE_ALLOW_ROOT 环境变量 | [1f2dcc8](https://github.com/weilinfox/ruyi-mugen/commit/1f2dcc832afd4e70635b765e74abc8f1ca8e22ad)                                                                                                      |
   | 添加 admin --format 测试点                | [cc9743a](https://github.com/weilinfox/ruyi-mugen/commit/cc9743ae3f16927bff36d29a72d503bcebbf4c3a)                                                                                                      |
   | 使用普通用户运行 mugen 测试               | [160e42e](https://github.com/weilinfox/ruyi-mugen/commit/160e42eaa48fcf880a0837a2c27f5ff91f094cba)                                                                                                      |
   | 测试 0.8.0-beta.20240407 版本             | [fe79424](https://github.com/weilinfox/ruyi-mugen/commit/fe79424d1da0f8e688ecc39623d96be9db427714)                                                                                                      |
+ 测试了 0.8.0-beta.20240406 和 0.8.0-beta.20240407 版本，提交 issue
   | issue 标题                                                   | issue 链接                                         |
   | ------------------------------------------------------------ | -------------------------------------------------- |
   | ruyi device provision 在解包异常中断后无法识别损坏的解包产物 | [#123](https://github.com/ruyisdk/ruyi/issues/123) |
   | ruyi 0.8.0-beta.20240406 版本 list 命令 KeyError: 'kind'     | [#126](https://github.com/ruyisdk/ruyi/issues/126) |

# RUYI 包管理 rpm 打包相关

+ ruyi rpm 包打包，根据 0.8.0 的 ``pyproject.toml``，预计新增如下依赖。其中 python-tomlkit 触发了 11 个包的 rebuild
   依赖包列表：
   | 包名                  | 版本            |
   | --------------------- | --------------- |
   | python-certifi        | 2024.2.2        |
   | python-packaging      | 24.0            |
   | python-tomlkit        | 0.12.4          |
   | python-types-PyYAML   | 6.0.12.20240311 |
   | python-types-requests | 2.31.0.20240402 |
+ 尝试向 src-openeuler 提交包版本更新
   + [python-packaging](https://gitee.com/src-openeuler/python-packaging/pulls/25)
   + [python-tomlkit](https://gitee.com/src-openeuler/python-tomlkit/pulls/6)

