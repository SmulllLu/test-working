# Month 11 工作报告 24/05/06-24/05/31

## RuyiSDK

+ ruyi mugen 更新 pr [!13](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/13)
   | 主要功能更新                                        | 提交                                                                                                                                                                                                                                                                                                         |
   | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | openKylin x86\_64 和 riscv64 架构加入自动化测试平台 | [42bc45d](https://github.com/weilinfox/ruyi-mugen/commit/42bc45d3567644a19f7c0054c84266a17b2e59c1)、 [83c575c](https://github.com/weilinfox/ruyi-mugen/commit/83c575c1838255bb2989013472d4b583908ee693)、 [d48e93a](https://github.com/weilinfox/ruyi-mugen/commit/d48e93abc20157a07b4d46fcaf56e4c39be9308b) |
   | 添加 LicheePi4A openEuler 2309 硬件平台测试         | [6ac5d92](https://github.com/weilinfox/ruyi-mugen/commit/6ac5d92fc79c7c73911ef49ef98aea87f9605941)                                                                                                                                                                                                           |
   | 添加 LicheePi4A RevyOS 硬件平台测试                 | [62fa4ae](https://github.com/weilinfox/ruyi-mugen/commit/62fa4ae41e1b5ef9a059a0c12edcf245a3faf878)                                                                                                                                                                                                           |
   | 添加 Pioneer Box openEuler 2309 硬件平台测试        | [394870b](https://github.com/weilinfox/ruyi-mugen/commit/394870bd4f142db94cb82b27f2d39511584a73a6)                                                                                                                                                                                                           |
   | 添加 Pioneer Box Fedora 38 硬件平台测试             | [2d35197](https://github.com/weilinfox/ruyi-mugen/commit/2d35197a2201a839f3015e4134b1dadf9bbd2186)                                                                                                                                                                                                           |
   | 测试 0.10.0-beta.20240512 pre release 版本          | [1013fd3](https://github.com/weilinfox/ruyi-mugen/commit/1013fd39a83e429181ec4197b6c90e5f35f47d62)                                                                                                                                                                                                           |
   | 测试 0.10.0-beta.20240513 pre release 版本          | [c70e8e8](https://github.com/weilinfox/ruyi-mugen/commit/c70e8e89de3ab81801ca2c80c151ce18a092b2d2)                                                                                                                                                                                                           |
   | 在 device provision 测试中识别仅文档内容            | [fbb6a1c](https://github.com/weilinfox/ruyi-mugen/commit/fbb6a1c40d8826600152ff1792e8f3cb0d1d4e6c)、 [80fed38](https://github.com/weilinfox/ruyi-mugen/commit/80fed38e9259744531a4d2d060b9c84efa48dfb6)                                                                                                       |
   | 测试 0.10.0 版本                                    | [13842bb](https://github.com/weilinfox/ruyi-mugen/commit/13842bb981e9659d04d59e1ea2ed5d70cfb9014a)                                                                                                                                                                                                           |
   | 提升测试超时时间为 60 小时                          | [580ed2d](https://github.com/weilinfox/ruyi-mugen/commit/580ed2d1f130d79e79c89b16f87171181b7a9262)                                                                                                                                                                                                           |
   | 测试 0.11.0-beta.20240527  pre release 版本         | [8a88334](https://github.com/weilinfox/ruyi-mugen/commit/8a88334f5968aa47ab8f6e521e4a96cc4caab4fe)                                                                                                                                                                                                           |
   | 测试 0.11.0 版本                                    | [6f0ad76](https://github.com/weilinfox/ruyi-mugen/commit/6f0ad762d1e5df2b43afbf2aff74e30679f083b1)                                                                                                                                                                                                           |
+ 测试了 0.11.0 版本，提交 issue
   | issue 标题                                       | issue 链接                                               |
   | ------------------------------------------------ | -------------------------------------------------------- |
   | ruyi 0.11.0 does not respect XDG\_STATE\_HOME      | [#151](https://github.com/ruyisdk/ruyi/issues/151)       |
   | Ruyi failed to fetch Pine64 Star64 Armbian image | [#2](https://github.com/ruyisdk/packages-index/issues/2) |
+ 完成 ruyi 0.10.0 版本 mugen 自动化测试并提交日志报告和视频 [!37](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/37) [!38](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/38)
+ 部分完成 ruyi 0.11.0 版本 mugen 自动化测试并提交日志报告和视频 [!39](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/39)
+ ruyisdk/docs 文档更新：0.10.0 版本文档 [#47](https://github.com/ruyisdk/docs/pull/47)；0.11.0 版本文档 [#48](https://github.com/ruyisdk/docs/pull/48) 

## 公众科学日

+ 公众科学日准备，为 ``ruyi device provision`` 预备了一个演示用 GUI 程序 [ruyi-device-gui](https://github.com/weilinfox/ruyi-device-gui)
+ 公众科学日准备，准备 ruyi、 ruyi test 和 ruyi device provision 三个展示主题，产出[配置文档和介绍 PPT](https://github.com/weilinfox/ruyi-device-gui/releases/tag/docs)
+ 公众科学日准备， ruyi 和 [ruyi-device-gui](https://github.com/weilinfox/ruyi-device-gui) 提供了 RevyOS 下便于安装的 [deb 包](https://github.com/weilinfox/ruyi-device-gui/releases/tag/0.10.0)，引用了所有依赖，并预提供了 udev rules
+ 公众科学日交互式活动，为 ruyi 和 ruyi device provision 分别准备了交互式活动，前者使用 kate 实现基本图形化的 RISC-V 架构程序开发，后者配合 [ruyi-device-gui](https://github.com/weilinfox/ruyi-device-gui) 实现 device provision 功能的图形化互动
+ 根据公众科学日的 ruyi device provision 交互式活动，在 22 日进行了一次技术分享《用于公众科学日的 ruyi device provision 图形化演示程序》，产出[文档](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyi-device-gui/ruyi-device-gui.md)和 [slice](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyi-device-gui/%E7%94%A8%E4%BA%8E%E5%85%AC%E4%BC%97%E7%A7%91%E5%AD%A6%E6%97%A5%E7%9A%84_ruyi_device_provision_%E5%9B%BE%E5%BD%A2%E5%8C%96%E6%BC%94%E7%A4%BA%E7%A8%8B%E5%BA%8F.odp)

## 自动化测试平台

+ aarch64 海外测试机往内地网络修复，效果不佳，已经更换为本地测试机
+ 硬件测试平台纳入自动化测试，自动化测试平台已有 20 个平台的测试能力
+ openQA 搭建 openEuler RISC-V QEMU 测试环境，开始尝试编写测试用例 demo
+ P119 实习生招聘信息，实习生工作方向为自动化测试平台设计和实现 pr [#142](https://github.com/lazyparser/weloveinterns/pull/142)
+ 提出 ruyi-mugen 的年度更新计划 issue [#5](https://github.com/weilinfox/ruyi-mugen/issues/5)，意图实现从新版本检测到测试报告输出的完全自动化

