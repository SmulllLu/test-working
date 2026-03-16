# Month 10 工作报告 24/04/01-24/04/26

## RuyiSDK

+ ruyi mugen 更新 pr [!9](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/9) [!10](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/10) [!11](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/11) [!12](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/12)
   | 主要功能更新                                  | 提交                                                                                                                                                                                                    |
   | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | 同步报告和 tarball 中的目录名                 | [cc4c176](https://github.com/weilinfox/ruyi-mugen/commit/cc4c1768b4cce81ff980a26451deac00d84142cf)， [eee923b](https://github.com/weilinfox/ruyi-mugen/commit/eee923bcd62ec555dae2da5049785ec82d27c3c7) |
   | 测试 0.8.0-beta.20240406 版本                 | [54850fd](github.com/weilinfox/ruyi-mugen/commit/54850fde778f19e5400a8c5dfb1f547fd70591d1)                                                                                                              |
   | 测试时配置 RUYI_FORCE_ALLOW_ROOT 环境变量     | [1f2dcc8](https://github.com/weilinfox/ruyi-mugen/commit/1f2dcc832afd4e70635b765e74abc8f1ca8e22ad)                                                                                                      |
   | 添加 admin --format 测试点                    | [cc9743a](https://github.com/weilinfox/ruyi-mugen/commit/cc9743ae3f16927bff36d29a72d503bcebbf4c3a)                                                                                                      |
   | 使用普通用户运行 mugen 测试                   | [160e42e](https://github.com/weilinfox/ruyi-mugen/commit/160e42eaa48fcf880a0837a2c27f5ff91f094cba)                                                                                                      |
   | 测试 0.8.0-beta.20240407 版本                 | [fe79424](https://github.com/weilinfox/ruyi-mugen/commit/fe79424d1da0f8e688ecc39623d96be9db427714)                                                                                                      |
   | 测试 0.8.0 版本                               | [dd78d2c](https://github.com/weilinfox/ruyi-mugen/commit/dd78d2cf03e5f1fde19733971ca847d4b87b8289)                                                                                                      |
   | 测试 0.8.1 版本                               | [3900c8d](https://github.com/weilinfox/ruyi-mugen/commit/3900c8d23bb8868ca96c45f777e72feab0d82283)                                                                                                      |
   | 安装 mugen 依赖前更新系统到最新               | [f65fc3f](https://github.com/weilinfox/ruyi-mugen/commit/f65fc3f4aaf130c07d7863ef8f0207556af5ab14)                                                                                                      |
   | mugen 支持 Gentoo 测试环境                    | [bd4c232](https://github.com/weilinfox/ruyi-mugen/commit/bd4c232cda8d42eda6ff04af5ac1dda0453be08f)， [3c3a50b](https://github.com/weilinfox/ruyi-mugen/commit/3c3a50bbd7df376bf84fdca0d0c0c3a1d45d1da7) |
   | 测试用例支持 Gentoo 测试环境                  | [c5501e6](https://github.com/weilinfox/ruyi-mugen/commit/c5501e66166b4fd0b58f5d9e504019536af9cfb2)                                                                                                      |
   | 在 Gentoo riscv64 运行 mugen 测试             | [172ba24](https://github.com/weilinfox/ruyi-mugen/commit/172ba248ef9c82bb9c63ca40bdcbcf260a6044ba)                                                                                                      |
   | 建立独立的 ``device provision`` 测试          | [3b55c3d](https://github.com/weilinfox/ruyi-mugen/commit/3b55c3d04863d67fc4f295a9fc0d2627aa1b3ab8)                                                                                                      |
   | 添加 RUYI smoke 测试套                        | [30aa2a9](https://github.com/weilinfox/ruyi-mugen/commit/30aa2a9948f75e86ed27b12f598765e294365af0)                                                                                                      |
   | 更新 Debian 测试机软件包后不重启 systemd 服务 | [c893b49](https://github.com/weilinfox/ruyi-mugen/commit/c893b4928631d7c671c647f23b2fd4ff8212a2f1)                                                                                                      |
   | 将 Gentoo x86\_64 纳入自动化测试              | [4ecd30b](https://github.com/weilinfox/ruyi-mugen/commit/4ecd30bdcc12519f5d34b46f41e9f2953a88ae53)                                                                                                      |
   | mugen 兼容 emerge 二进制软件包                | [e0d5cca](https://github.com/weilinfox/ruyi-mugen/commit/e0d5cca61ef7c5a07a5487619378fdef8c9de19b)                                                                                                      |
   | 测试 0.9.0-beta.20240421 版本                 | [1f80891](https://github.com/weilinfox/ruyi-mugen/commit/1f808919eb0f0c581383f91c4e8a08e1b28475a2)                                                                                                      |
   | 测试 0.9.0 版本                               | [dd33588](https://github.com/weilinfox/ruyi-mugen/commit/dd33588344abe819509c0e0f5f7cb0b4c2422656)                                                                                                      |
   | 添加 RUYI 依赖 lz4                            | [695eec5](https://github.com/weilinfox/ruyi-mugen/commit/695eec5868ddc22abdc163bbd115662caa0a32d2)                                                                                                      |
   | 中文环境下的 apt-get 输出匹配                 | [3901023](https://github.com/weilinfox/ruyi-mugen/commit/3901023c80448da128d818244a77501e773cfa9d)                                                                                                      |
+ 测试了 0.8.0-beta.20240406 和 0.8.0-beta.20240407 版本，提交 issue
   | issue 标题                                                   | issue 链接                                         |
   | ------------------------------------------------------------ | -------------------------------------------------- |
   | ruyi device provision 在解包异常中断后无法识别损坏的解包产物 | [#123](https://github.com/ruyisdk/ruyi/issues/123) |
   | ruyi 0.8.0-beta.20240406 版本 list 命令 KeyError: 'kind'     | [#126](https://github.com/ruyisdk/ruyi/issues/126) |
+ 测试了 RUYI 包管理 0.8.0、 0.8.1、 和 0.9.0 版本，没有发现质量问题，提交测试报告、日志和视频 pr [!30](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/30) [!35](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/35)
+ ruyisdk/docs 文档更新 [提交 0.8.1 新增特性](https://github.com/ruyisdk/docs/pull/44) [提交 0.9.0 新增特性](https://github.com/ruyisdk/docs/pull/45)
+ 完成 Gentoo riscv64 QEMU 测试环境搭建，产出[搭建文档](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/gentoo/riscv64_installation.md)和[内核配置](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/gentoo/kernel/riscv/config/qemu_defconfig)
+ 完成 Gentoo x86\_64 QEMU 测试环境搭建，产出[搭建文档](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/gentoo/x86-64_installation.md)
+ 完成 openKylin x86\_64 和 riscv64 QEMU 测试环境搭建，下个 RUYI 版本的 mugen 自动化测试平台将增加到 16 个。
+ 对沁恒微电子 MCU 进行初步调研，产出初步[调研文档](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/wch_rv_mcu.md)

## RUYI 包管理 rpm 打包相关

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

## 自动化测试平台维护

1. Jenkins Worker 报错 ``Failed to exec spawn helper`` ，解决[文档](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/failed_to_exec_spawn_helper.md)，具体效果待观察。
2. 开始搭建 openQA 平台。

