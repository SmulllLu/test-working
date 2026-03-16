# Month 11 Week 2 工作报告 24/05/14-24/05/20

## RuyiSDK

+ ruyi mugen 更新 pr [!14](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/14)
   | 主要功能更新                             | 提交                                                                                                                                                                                                   |
   | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | 在 device provision 测试中识别仅文档内容 | [fbb6a1c](https://github.com/weilinfox/ruyi-mugen/commit/fbb6a1c40d8826600152ff1792e8f3cb0d1d4e6c), [80fed38](https://github.com/weilinfox/ruyi-mugen/commit/80fed38e9259744531a4d2d060b9c84efa48dfb6) |
   | 测试 0.10.0 版本                         | [13842bb](https://github.com/weilinfox/ruyi-mugen/commit/13842bb981e9659d04d59e1ea2ed5d70cfb9014a)                                                                                                     |
   | 提升测试超时时间为 60 小时               | [580ed2d](https://github.com/weilinfox/ruyi-mugen/commit/580ed2d1f130d79e79c89b16f87171181b7a9262)                                                                                                     |
+ 提交两个 ruyi issue
   | issue 标题                                      | issue 链接                                         |
   | ----------------------------------------------- | -------------------------------------------------- |
   | ruyi list 输出格式发生变化                      | [#142](https://github.com/ruyisdk/ruyi/issues/142) |
   | ruyi device provision dd 相关 sudo 输出格式问题 | [#146](https://github.com/ruyisdk/ruyi/issues/146) |
+ 提交 ruyi 0.10.0 版本文档 [#47](https://github.com/ruyisdk/docs/pull/47)
+ 完成 ruyi 0.10.0 版本已有 20 个平台的 mugen 自动化测试并提交日志报告和视频 [!37](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/37) [!38](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/38)
+ aarch64 海外测试机往内地网络修复（效果不佳，可能需要考虑更换为本地测试机）
+ 公众科学日准备，准备 ruyi、 ruyi test 和 ruyi device provision 三个展示主题，产出[配置文档和介绍 PPT](https://github.com/weilinfox/ruyi-device-gui/releases/tag/docs)
+ 公众科学日准备， ruyi 和 [ruyi-device-gui](https://github.com/weilinfox/ruyi-device-gui) 提供了 RevyOS 下便于安装的 [deb 包](https://github.com/weilinfox/ruyi-device-gui/releases/tag/0.10.0)，引用了所有依赖，并预提供了 udev rules
+ 公众科学日交互式活动，为 ruyi 和 ruyi device provision 分别准备了交互式活动，前者使用 kate 实现基本图形化的 RISC-V 架构程序开发，后者配合 [ruyi-device-gui](https://github.com/weilinfox/ruyi-device-gui) 实现 device provision 功能的图形化互动

