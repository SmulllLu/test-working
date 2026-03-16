# Month 26 工作报告 25/08/11-25/08/29

## RuyiSDK

1. 指导 Web 实习生重新设计了官网的数据统计页面，更新博客和双周报，同时有一些其他零散的更新
2. 在 ruyi-packaging 仓库完善打包工具，并使用打包工具生成配置，向 packages-index 提交 pr
3. 将文档、 packages-index 之前已知问题同步到 issue
4. 提交对 Ruyi 的新功能请求
5. 整理已有的 Ruyi 的 deb 包打包到新的仓库

## 产出列表

+ Ruyi v0.39.0 测试完成 [pr](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/78)
+ ruyi 仓库提交两个 Feature Request
    + [[Feature Request] check mounted partition before ruyi device provision dd block device #345](https://github.com/ruyisdk/ruyi/issues/345)
    + [[Feature Request] a command line interface as an alternative to device provision wizard #346](https://github.com/ruyisdk/ruyi/issues/346)
+ ruyisdk-website 仓库审核 18 个 pr
    + [docs: update case1 English version #189](https://github.com/ruyisdk/ruyisdk-website/pull/189)
    + [Optimize the copy button showing strategy and fix the code highlight cutoff #190](https://github.com/ruyisdk/ruyisdk-website/pull/190)（修复长代码行，灰底只渲染一次导致滚动后没有底色的问题，但测试感觉没有解决问题）
    + [Update RuyiInLive for more data and a clear indicator to stats page #192](https://github.com/ruyisdk/ruyisdk-website/pull/192)
    + [Feat/newscase auto switch #193](https://github.com/ruyisdk/ruyisdk-website/pull/193)
    + [NewsShowcase with better visuals #194](https://github.com/ruyisdk/ruyisdk-website/pull/194) 优化了鼠标移上去时的图片放大圆角
    + [Improved image spacing for popups #195](https://github.com/ruyisdk/ruyisdk-website/pull/195)
    + [deleted some code #198](https://github.com/ruyisdk/ruyisdk-website/pull/198)
    + [Synchronize ruyisdk biweekly #202](https://github.com/ruyisdk/ruyisdk-website/pull/202)
    + [Update/blogs #203](https://github.com/ruyisdk/ruyisdk-website/pull/203)
    + [docs: Shorten titles to improve typography #206](https://github.com/ruyisdk/ruyisdk-website/pull/206)
    + [Feat/bar chart #199](https://github.com/ruyisdk/ruyisdk-website/pull/199)
    + [Feat/newscase auto switch #200](https://github.com/ruyisdk/ruyisdk-website/pull/200)
    + [Re-patch for codeblock update #201](https://github.com/ruyisdk/ruyisdk-website/pull/201)
    + [feat: add UnoCSS integration #208](https://github.com/ruyisdk/ruyisdk-website/pull/208)
    + [Feat/add slide #209](https://github.com/ruyisdk/ruyisdk-website/pull/209)
    + [Update/newscase #210](https://github.com/ruyisdk/ruyisdk-website/pull/210)
    + [Optimize stats page colouring #211](https://github.com/ruyisdk/ruyisdk-website/pull/211)
    + [Update stats page's colouring to ensure visibility #212](https://github.com/ruyisdk/ruyisdk-website/pull/212)
+ ruyisdk-website 仓库提交 1 个 pr
    + [pages: modify statistical data page text #196](https://github.com/ruyisdk/ruyisdk-website/pull/196)
+ ruyi-packaging 仓库提交 10 个 pr
    + [riko: subcommand manifests to generate new tomls #26](https://github.com/ruyisdk/ruyi-packaging/pull/26)
    + [riko: fix unexpected behaviour when generating buildroot-sdk-sipeed-licheervnano tomls #27](https://github.com/ruyisdk/ruyi-packaging/pull/27)
    + [riko: raise exception when provisionable strategy not supported #28](https://github.com/ruyisdk/ruyi-packaging/pull/28)
    + [riko: add armbian riko.py #29](https://github.com/ruyisdk/ruyi-packaging/pull/29)
    + [riko: skip armbian #30](https://github.com/ruyisdk/ruyi-packaging/pull/30)
    + [riko: add support for nvchecker source regex and new policies config #31](https://github.com/ruyisdk/ruyi-packaging/pull/31)
    + [riko: better regex source support for new package revyos-lpi4a #32](https://github.com/ruyisdk/ruyi-packaging/pull/32)
    + [ruyi_packaging: new packages revyos-{meles,lcon4a} #33](https://github.com/ruyisdk/ruyi-packaging/pull/33)
    + [riko: allow generating downgrade manifests #34](https://github.com/ruyisdk/ruyi-packaging/pull/34)
    + [New package mars-buildroot-sdk and make riko easier to use #35](https://github.com/ruyisdk/ruyi-packaging/pull/35)
+ packages-index 仓库提交 2 个 issue
    + [BananaPi BPI-F3 eMMC storage variant did not refer to any combo #101](https://github.com/ruyisdk/packages-index/issues/101)
    + [Jupiter and Megrez missing for MilkV product line support #104](https://github.com/ruyisdk/packages-index/issues/104)
+ packages-index 仓库提交 8 个 pr
    + [board-image/buildroot-sdk-sipeed-licheervnano: add missing versions #95](https://github.com/ruyisdk/packages-index/pull/95)
    + [board-image/revyos-sipeed-lpi4a: new version 0.20250729.0 #96](https://github.com/ruyisdk/packages-index/pull/96)
    + [board-image/revyos-sipeed-lcon4a: new versions 0.20240720.0 and 0.20250729.0 #97](https://github.com/ruyisdk/packages-index/pull/97)
    + [board-image/revyos-milkv-meles: new version 1.20250729.0 #98](https://github.com/ruyisdk/packages-index/pull/98)
    + [Fix broken bianbu-bpi-f3 manifest and unify bianbu upstream_version format #99](https://github.com/ruyisdk/packages-index/pull/99)
    + [board-image/bianbu-{desktop,minimal}-spacemit-k1-sd: new versions from v2.0.0 to v3.0.0 #100](https://github.com/ruyisdk/packages-index/pull/100)
    + [Update board-image/bianbu-{desktop,minimal}-spacemit-k1-sd manifests #102](https://github.com/ruyisdk/packages-index/pull/102)
    + [board-image/debian-desktop-sdk-milkv-mars-cm-sd: add old version 1.0.5+3.6.1 #103](https://github.com/ruyisdk/packages-index/pull/103)
+ support-matrix 仓库提交 1 个 issue
    + [[Image Check] Pine64 Star64 images disappeared on armbian community release #353](https://github.com/ruyisdk/support-matrix/issues/353)
+ docs 仓库提交 4 个 issue
    + [文档代码块格式不统一 #93](https://github.com/ruyisdk/docs/issues/93)
    + [链接中的 RuyiSDK 大小写问题 #94](https://github.com/ruyisdk/docs/issues/94)
    + [关于 fastboot 的文档提示 #95](https://github.com/ruyisdk/docs/issues/95)
    + [关于使用 pip 安装 ruyi 的文档提示 #96](https://github.com/ruyisdk/docs/issues/96)
+ 08/08 北京 World RISC-V Days 2025 参会和演示
+ 08/26 深圳 Elexcon 参展
+ 新的 ruyi deb 包下载源 [launchpad.net](https://launchpad.net/~ruyisdk-test/+archive/ubuntu/ruyi)
+ 实习生面试考核题 [J162](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month26/jy.md)

