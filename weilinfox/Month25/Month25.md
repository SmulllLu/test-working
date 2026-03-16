# Month 25 工作报告 25/07/28-25/07/31

## RuyiSDK

+ Ruyi v0.37.1 测试完成 [pr](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/76)
+ Ruyi v0.38.1 测试完成 pr [!77](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/77)
+ ruyi 仓库提出 2 个 issue
    + [在 Ubuntu jammy 上 pytest 失败 #330](https://github.com/ruyisdk/ruyi/issues/330)
    + [ruyi refresh local packages-index before running any command #335](https://github.com/ruyisdk/ruyi/issues/335)
+ docs 仓库提交 1 个 pr
    + [Add milkv-duo-examples tips #88](https://github.com/ruyisdk/docs/pull/88)
+ packages-index 仓库提交 1 个 issue
    + [需要更新 milkv-duo-examples 包 #86](https://github.com/ruyisdk/packages-index/issues/86)
+ packages-index 仓库合作 2 个 pr
    + [board-image/arduino-milkv-{duo,duo256m}-sd: add version 1.1.2 and 1.1.4 #88](https://github.com/ruyisdk/packages-index/pull/88)
    + [Add missing versions and reformat old tomls for RevyOS LicheePi 4A #89](https://github.com/ruyisdk/packages-index/pull/89)
+ packages-index 仓库提交 5 个 pr
    + [board-image/revyos-milkv-pioneer: add missing versions and update upstream_versions #90](https://github.com/ruyisdk/packages-index/pull/90)
    + [RevyOS MilkV Meles: add missing versions and reformat some old versions #91](https://github.com/ruyisdk/packages-index/pull/91)
    + [workflows: test manifests with format-manifest #92](https://github.com/ruyisdk/packages-index/pull/92)
    + [board-image/\*: reformat old tomls by format-manifest #93](https://github.com/ruyisdk/packages-index/pull/93)
    + [board-image/\*: add missing upstream_version data #94](https://github.com/ruyisdk/packages-index/pull/94)
+ ruyisdk-website 仓库审核 8 个 pr
    + [New CodeBlock for documentation #164](https://github.com/ruyisdk/ruyisdk-website/pull/164)
    + [第一部分考核题作答 #165](https://github.com/ruyisdk/ruyisdk-website/pull/165)（重新分为多个 pr 合并）
    + [Task02 #166](https://github.com/ruyisdk/ruyisdk-website/pull/166)（由其他 pr 合并）
    + [chore: add Prettier configuration and plugins to project #169](https://github.com/ruyisdk/ruyisdk-website/pull/169)
    + [docs: update the English version for case7 #171](https://github.com/ruyisdk/ruyisdk-website/pull/171)
    + [mv files into appropriate location #183](https://github.com/ruyisdk/ruyisdk-website/pull/183)
    + [Add toggle for main copy button #184](https://github.com/ruyisdk/ruyisdk-website/pull/184)
    + [update the newcase #185](https://github.com/ruyisdk/ruyisdk-website/pull/185)
+ ruyisdk-website 仓库合作 10 个 pr
    + [Add footer link and translations for ruyi community #167](https://github.com/ruyisdk/ruyisdk-website/pull/167)
    + [Homepage finetune #172](https://github.com/ruyisdk/ruyisdk-website/pull/173)
    + [Update 'de' documentations for new CodeBlock #173](https://github.com/ruyisdk/ruyisdk-website/pull/173)
    + [Fix issue #163](https://github.com/ruyisdk/ruyisdk-website/pull/174)
    + [Making Maindisplay display elegantly on XL screens #175](https://github.com/ruyisdk/ruyisdk-website/pull/175)
    + [Fix/wechat qqgroup styling #177](https://github.com/ruyisdk/ruyisdk-website/pull/177)
    + [Fix/homepage revyos links #179](https://github.com/ruyisdk/ruyisdk-website/pull/179)
    + [Feat/custom footer style #180](https://github.com/ruyisdk/ruyisdk-website/pull/180)
    + [Feat/static page #181](https://github.com/ruyisdk/ruyisdk-website/pull/181)
    + [Feat/custom footer style #182](https://github.com/ruyisdk/ruyisdk-website/pull/182)
+ ruyisdk-website 仓库提交 5 个 pr
    + [pages: fix index header spaces #158](https://github.com/ruyisdk/ruyisdk-website/pull/158)
    + [pages: change index community page to ruyisdk.org #168](https://github.com/ruyisdk/ruyisdk-website/pull/168)
    + [docs: add milkv-duo-examples tips #170](https://github.com/ruyisdk/ruyisdk-website/pull/170)
    + [pages: modify copyright info #176](https://github.com/ruyisdk/ruyisdk-website/pull/176)
    + [pages: update community page translations #186](https://github.com/ruyisdk/ruyisdk-website/pull/186)
+ ruyi-packaging 仓库提交 8 个 pr，为 packages-index 重新设计的打包工具，打包功能已经完成 90%，预计个工作周开始使用该工具生成 manifest
    + [riko: setup ruyi #18](https://github.com/ruyisdk/ruyi-packaging/pull/18)
    + [riko: load packages-index and config nvchecker #19](https://github.com/ruyisdk/ruyi-packaging/pull/19)
    + [riko: use nvchecker new_ver/old_ver features #20](https://github.com/ruyisdk/ruyi-packaging/pull/20)
    + [riko: support cmdline parsing #21](https://github.com/ruyisdk/ruyi-packaging/pull/21)
    + [workflow: check DCO on branch checker #22](https://github.com/ruyisdk/ruyi-packaging/pull/22)
    + [misc: do some misc works #23](https://github.com/ruyisdk/ruyi-packaging/pull/23)
    + [riko: subcommand list to print nvchecker results #24](https://github.com/ruyisdk/ruyi-packaging/pull/24)
    + [riko: now we can get raw toml from packaging scripts #25](https://github.com/ruyisdk/ruyi-packaging/pull/25)
+ 香港海报 《RuyiSDK A Unified and Extensible Platform for RISC-V Ecosystem Development》 之 Extended Abstract [V3](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month25/RuyiSDK%20-%20A%20Unified%20and%20Extensible%20Platform_2P_V3.pdf) [V4](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month25/RuyiSDK%20-%20A%20Unified%20and%20Extensible%20Platform_2P_V4.pdf)
+ 香港海报 《RuyiSDK A Unified and Extensible Platform for RISC-V Ecosystem Development》 [PDF](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month25/RuyiSDK_A_Unified_and_Extensible_Platform_for_RISC_V_Ecosystem_Development.pdf)
+ RISC-V 中国峰会 RV 学院试讲 ppt [未使用玄铁模板的版本](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month25/玩转RISC-V开发板，从RuyiSDK开始.pdf)
+ J154 新实习生面试，[考核题](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month25/vdx_面试考核.md)
+ 使用 Ruyi 建立 milkv-duo-examples 的运行环境 [envsetup.sh](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month25/envsetup.sh)
+ Ruyi 在 Ubuntu Launchpad 进行新版本的实验性打包 [仓库](https://launchpad.net/~weilinfox/+archive/ubuntu/ruyi/+build/31008991)（后将改用新仓库用于正式发布）
+ RVSC 现场 RV 学院试讲
+ 0725 RISCV Infra [PPT](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month25/玄铁_x_PLCT_联合课程_RISC_V_中国峰会主场前_1_天.pdf)

