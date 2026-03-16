# Month 9 工作报告 24/03/4-24/03/29

## RuyiSDK 测试

+ 测试从 0.6.0 到 0.7.0 的版本，发现问题并发 issue
   |                                                    issue 标题                                                    |                     issue 链接                     |
   |:----------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------:|
   |                               ruyi 0.6.0 版本二进制 "ImportError: libgit2.so.1.7"                                |  [#81](https://github.com/ruyisdk/ruyi/issues/81)  |
   |                    ruyi 0.6.0 版本 x86-64 二进制 "OpenSSL error: failed to load certificates"                    |  [#82](https://github.com/ruyisdk/ruyi/issues/81)  |
   |            ruyi 0.6.0 版本 RISC-V 二进制在 oErv 2309 报 "OpenSSL error: failed to load certificates"             |  [#88](https://github.com/ruyisdk/ruyi/issues/88)  |
   |       gnu-plct 20231212 版本配合 milkv-duo profile 交叉编译动态二进制无法在最新 milkv duo v1.0.9 镜像运行        |  [#91](https://github.com/ruyisdk/ruyi/issues/91)  |
   | ruyi 0.7.0-alpha.20240315 版本 RISC-V 二进制在 Archlinux riscv64 报 "OpenSSL error: failed to load certificates" |  [#97](https://github.com/ruyisdk/ruyi/issues/97)  |
   |             ruyi 0.7.0-beta.20240323 版本 riscv64 二进制在 Fedora38 和 oErv 2309 依赖 openssl-devel              | [#103](https://github.com/ruyisdk/ruyi/issues/103) |
   |                       ruyi 0.7.0-beta.20240323 版本 riscv64 二进制在 ubuntu22.04 无法运行                        | [#104](https://github.com/ruyisdk/ruyi/issues/104) |
   |                          gnu-plct-0.20240324.0 -mcpu=xiangshan-nanhu 无法正常构建二进制                          | [#112](https://github.com/ruyisdk/ruyi/issues/112) |
+ 完成 ruyi-mugen 从 0.6.0 版本到 0.8.0-alpha.20240326 版本测试用例开发，增加自动化测试平台到 12 个，并可以自动生成报告 pr [!6](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/6) [!7](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/7) [!8](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/8)
   |                  主要功能修复和更新                  |                                            关联 commit                                             |
   |:----------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|
   |             新增用例 ruyi\_test\_config              | [5234f52](https://github.com/weilinfox/ruyi-mugen/commit/5234f5296f7a2cbd38b0d85298c4f87492814e66) |
   |         在 RUYI 运行失败时使用 RUYI\_DEBUG=x         | [b447cea](https://github.com/weilinfox/ruyi-mugen/commit/b447cea6a7ee3276735f6b08b984fdd838bef5bc) |
   |                   开始 0.6.0 测试                    | [2a5a689](https://github.com/weilinfox/ruyi-mugen/commit/2a5a689c385e47df8565fae04d72ed4f3b75316e) |
   |            新增用例 ruyi\_test\_binaries             |     [b04440a](github.com/weilinfox/ruyi-mugen/commit/b04440a886c5e5708787b800e3861f1d1b61f083)     |
   | 添加 debian12-x86\_64 和 debiansid-riscv64 测试平台  |     [b05f9c6](github.com/weilinfox/ruyi-mugen/commit/b05f9c63c37f580af2dc536bf003d9c92681fae8)     |
   |            支持 Archlinux pacman 包管理器            | [b05f9c6](https://github.com/weilinfox/ruyi-mugen/commit/b05f9c63c37f580af2dc536bf003d9c92681fae8) |
   | 添加 archlinux-x86\_64 和 archlinux-riscv64 测试平台 | [238fd69](https://github.com/weilinfox/ruyi-mugen/commit/238fd69f7c5db7a5a079265a0ebaadeb88039688) |
   |           开始 0.7.0-alpha.20240315  测试            | [b398dc5](https://github.com/weilinfox/ruyi-mugen/commit/b398dc52e1e1ffe7d603b0fb6ad3cd359ecd8b38) |
   | 添加 ubuntu2204-riscv64 和 fedora38-riscv64 测试平台 | [dd98e7d](https://github.com/weilinfox/ruyi-mugen/commit/dd98e7d7be2bc1427500f9ac5b416aa51ccf7680) |
   |            添加 debian12-aarch64 测试平台            | [1d601a7](https://github.com/weilinfox/ruyi-mugen/commit/1d601a77adc58ed2fceaf5bd03c0c017666fbc9b) |
   |            开始 0.7.0-beta.20240323 测试             | [d0d2f86](https://github.com/weilinfox/ruyi-mugen/commit/d0d2f8655e585acf5b26be53487232d9ad3e52ec) |
   |                在下载 ruyi 失败时重试                | [68674f9](https://github.com/weilinfox/ruyi-mugen/commit/68674f9ba58803322698d66421bc69ecdfc2d536) |
   |           测试  0.8.0-alpha.20240325 版本            | [cb1cc9b](https://github.com/weilinfox/ruyi-mugen/commit/cb1cc9b12678dcc091d0cd13635834dcf040acb6) |
   |              添加报告生成脚本和生成模板              | [6f55e28](https://github.com/weilinfox/ruyi-mugen/commit/6f55e2845a4e2b1d6897d285840a2a476cfa33b2) |
   |                   开始 0.7.0 测试                    | [cb1cc9b](https://github.com/weilinfox/ruyi-mugen/commit/cb1cc9b12678dcc091d0cd13635834dcf040acb6) |
   |            开始 0.8.0-alpha.20240326 测试            | [9b3b55a](https://github.com/weilinfox/ruyi-mugen/commit/9b3b55a347afe7de0e85b0de268ab4c3fb5f06c9) |
   |              添加 gnu-plct 香山南湖测试              | [900b64f](https://github.com/weilinfox/ruyi-mugen/commit/900b64ff4dbd2a51e23c7adb97578c631e13e8b1) |
   |                   开始 0.7.1 测试                    | [6f2e2e0](https://github.com/weilinfox/ruyi-mugen/commit/6f2e2e0655d91d317e61be9ff677981fff4728cc) |
+ RUYI 包管理 0.6.0 mugen 自动化测试在 x86\_64 QEMU Fedora 38、 x86\_64 QEMU Ubuntu 22.04 LTS、 x86\_64 QEMU openEuler 23.09、 riscv64 Container RevyOS 20231210、 riscv64 QEMU openEuler 23.09 环境运行，测试发现 riscv64 架构二进制在 openEuler riscv 2309 无法正常使用。提交测试报告日志和视频 pr [!21](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/21)
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
+ 提交文档，包含 0.6.0 和 0.7.0 新增特性、香山南湖编译环境配置和一些其他修复 pr [#40](https://github.com/ruyisdk/docs/pull/40) [#41](https://github.com/ruyisdk/docs/pull/41)

## RUYI 包管理 RPM 打包

+ RUYI 包管理基于 openEuler 23.09 的 RPM 包构建。由于 RUYI 0.6.0 将 git 依赖改为 pygit2 依赖，新增了一些依赖包。
   新增依赖包列表：
   | 包名                   | 版本            |
   | ---------------------- | --------------- |
   | python-cffi            | 1.16.0          |
   | python-pygit2          | 1.14.1          |
   | python-types-cffi      | 1.16.0.20240106 |
   | python-types-pygit2    | 1.14.0.20240317 |
   | python-types-setuptools| 69.1.0.20240310 |
   | libgit2                | 1.7.2           |

   RUYI RPM 包：
   | 包名         | 版本  |
   | ------------ | ----- |
   | python3-ruyi | 0.6.0 |
   | python3-ruyi | 0.7.0 |
   | python3-ruyi | 0.7.1 |

## openEuler mugen

+ 更新 pr [!1993](https://gitee.com/openeuler/mugen/pulls/1993)，添加 x86\_64 测试截图
+ 根据上游评论更新 pr [!2330](https://gitee.com/openeuler/mugen/pulls/2330)
+ 2309 测试时向 mugen 上游提交的 9 个 pr 已经全部合并

