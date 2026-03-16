# Month 26 Week 2 工作报告 25/08/11-25/08/15

## RuyiSDK

1. 指导 Web 实习生重新设计了官网的数据统计页面，同时有一些其他零散的更新
2. 在 ruyi-packaging 仓库完善打包工具，并使用打包工具生成配置，向 packages-index 提交 pr

## 产出列表

+ ruyisdk-website 仓库审核 7 个 pr
    + [docs: update case1 English version #189](https://github.com/ruyisdk/ruyisdk-website/pull/189)
    + [Optimize the copy button showing strategy and fix the code highlight cutoff #190](https://github.com/ruyisdk/ruyisdk-website/pull/190)（修复长代码行，灰底只渲染一次导致滚动后没有底色的问题，但测试感觉没有解决问题）
    + [Update RuyiInLive for more data and a clear indicator to stats page #192](https://github.com/ruyisdk/ruyisdk-website/pull/192)
    + [Feat/newscase auto switch #193](https://github.com/ruyisdk/ruyisdk-website/pull/193)
    + [NewsShowcase with better visuals #194](https://github.com/ruyisdk/ruyisdk-website/pull/194) 优化了鼠标移上去时的图片放大圆角
    + [Improved image spacing for popups #195](https://github.com/ruyisdk/ruyisdk-website/pull/195)
    + [deleted some code #198](https://github.com/ruyisdk/ruyisdk-website/pull/198)
+ ruyisdk-website 仓库提交 1 个 pr
    + [pages: modify statistical data page text #196](https://github.com/ruyisdk/ruyisdk-website/pull/196)
+ ruyi-packaging 仓库提交 9 个 pr
    + [riko: subcommand manifests to generate new tomls #26](https://github.com/ruyisdk/ruyi-packaging/pull/26)
    + [riko: fix unexpected behaviour when generating buildroot-sdk-sipeed-licheervnano tomls #27](https://github.com/ruyisdk/ruyi-packaging/pull/27)
    + [riko: raise exception when provisionable strategy not supported #28](https://github.com/ruyisdk/ruyi-packaging/pull/28)
    + [riko: add armbian riko.py #29](https://github.com/ruyisdk/ruyi-packaging/pull/29)
    + [riko: skip armbian #30](https://github.com/ruyisdk/ruyi-packaging/pull/30)
    + [riko: add support for nvchecker source regex and new policies config #31](https://github.com/ruyisdk/ruyi-packaging/pull/31)
    + [riko: better regex source support for new package revyos-lpi4a #32](https://github.com/ruyisdk/ruyi-packaging/pull/32)
    + [ruyi_packaging: new packages revyos-{meles,lcon4a} #33](https://github.com/ruyisdk/ruyi-packaging/pull/33)
    + [riko: allow generating downgrade manifests #34](https://github.com/ruyisdk/ruyi-packaging/pull/34)
+ packages-index 仓库提交 6 个 pr
    + [board-image/buildroot-sdk-sipeed-licheervnano: add missing versions #95](https://github.com/ruyisdk/packages-index/pull/95)
    + [board-image/revyos-sipeed-lpi4a: new version 0.20250729.0 #96](https://github.com/ruyisdk/packages-index/pull/96)
    + [board-image/revyos-sipeed-lcon4a: new versions 0.20240720.0 and 0.20250729.0 #97](https://github.com/ruyisdk/packages-index/pull/97)
    + [board-image/revyos-milkv-meles: new version 1.20250729.0 #98](https://github.com/ruyisdk/packages-index/pull/98)
    + [Fix broken bianbu-bpi-f3 manifest and unify bianbu upstream_version format #99](https://github.com/ruyisdk/packages-index/pull/99)
    + [board-image/bianbu-{desktop,minimal}-spacemit-k1-sd: new versions from v2.0.0 to v3.0.0 #100](https://github.com/ruyisdk/packages-index/pull/100)
+ support-matrix 仓库提交 1 个 issue
    + [[Image Check] Pine64 Star64 images disappeared on armbian community release #353](https://github.com/ruyisdk/support-matrix/issues/353)
+ 08/08 北京 World RISC-V Days 2025 参会和演示

## TODO

+ ruyi-packaging 待补全支持的 combo
    + oerv-* （大部分需要检查新版本支持状态）
    + freebsd-riscv64-mini-live
    + openkylin-riscv64-sifive-unmatched
    + ubuntu-server-riscv64-sifive-unmatched
    + openwrt-sifive-unmatched
+ packages-index 已知需要补全版本但暂未补全的
    + debian-fishwaldo-sg200x-sipeed-licheervnano
    + mars-buildroot-sdk

