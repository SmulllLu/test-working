# Month 26 Week 3 工作报告 25/08/18-25/08/22

## RuyiSDK

1. 将文档、 packages-index 之前已知问题同步到 issue
2. 提交对 Ruyi 的功能请求
3. 在 ruyi-packaging 仓库完善打包工具，并使用打包工具生成配置，向 packages-index 提交 2 个 pr
4. 官网更新博客和双周报。官网还有 7 个 pr 待审核
5. 整理已有的 Ruyi 的 deb 包打包到新的仓库

## 产出列表

+ Ruyi v0.39.0 测试完成 [pr](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/78)
+ packages-index 仓库提交 2 issue
    + [BananaPi BPI-F3 eMMC storage variant did not refer to any combo #101](https://github.com/ruyisdk/packages-index/issues/101)
    + [Jupiter and Megrez missing for MilkV product line support #104](https://github.com/ruyisdk/packages-index/issues/104)
+ packages-index 仓库提交 2 pr
    + [Update board-image/bianbu-{desktop,minimal}-spacemit-k1-sd manifests #102](https://github.com/ruyisdk/packages-index/pull/102)
    + [board-image/debian-desktop-sdk-milkv-mars-cm-sd: add old version 1.0.5+3.6.1 #103](https://github.com/ruyisdk/packages-index/pull/103)
+ ruyi-packaging 仓库提交 1 个 pr
    + [New package mars-buildroot-sdk and make riko easier to use #35](https://github.com/ruyisdk/ruyi-packaging/pull/35)
+ ruyi 仓库提交两个 Feature Request
    + [[Feature Request] check mounted partition before ruyi device provision dd block device #345](https://github.com/ruyisdk/ruyi/issues/345)
    + [[Feature Request] a command line interface as an alternative to device provision wizard #346](https://github.com/ruyisdk/ruyi/issues/346)
+ docs 仓库提交 4 个 issue
    + [文档代码块格式不统一 #93](https://github.com/ruyisdk/docs/issues/93)
    + [链接中的 RuyiSDK 大小写问题 #94](https://github.com/ruyisdk/docs/issues/94)
    + [关于 fastboot 的文档提示 #95](https://github.com/ruyisdk/docs/issues/95)
    + [关于使用 pip 安装 ruyi 的文档提示 #96](https://github.com/ruyisdk/docs/issues/96)
+ ruyisdk-website 审核 3 个 pr 
    + [Synchronize ruyisdk biweekly #202](https://github.com/ruyisdk/ruyisdk-website/pull/202)
    + [Update/blogs #203](https://github.com/ruyisdk/ruyisdk-website/pull/203)
    + [docs: Shorten titles to improve typography #206](https://github.com/ruyisdk/ruyisdk-website/pull/206)
    + 上周官网还有 7 个 pr 待审核，正在审核
+ 新的 ruyi deb 包下载源 [launchpad.net](https://launchpad.net/~ruyisdk-test/+archive/ubuntu/ruyi)
