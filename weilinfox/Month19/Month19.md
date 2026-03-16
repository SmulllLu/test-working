# Month 19 工作报告 24/12/30-25/01/27

## RuyiSDK

+ Ruyi v0.25.0 测试完成 pr [!58](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/58) [!59](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/59)
+ Ruyi v0.26.0 测试完成 pr [!60](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/60) [!62](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/62)
+ Ruyi 测试时的统计数据上传，测试数据也将上传
    + ruyi telemetry concent [efbc41db](https://github.com/weilinfox/ruyi-litester/commit/efbc41db81faaf58ee5409b552a4bd6aa7e9048e)
    + ruyi telemetry upload [8dbd60fc](https://github.com/weilinfox/ruyi-litester/commit/8dbd60fcc6f29b443ad8069fcc991b4415aa6186)
+ ruyisdk.org 审核合并了
    + [Update author status #18](https://github.com/ruyisdk/ruyisdk-website/pull/18)
    + [Update biweekly/highlights #19](https://github.com/ruyisdk/ruyisdk-website/pull/19)
    + [Fixlink #20](https://github.com/ruyisdk/ruyisdk-website/pull/20)
    + [update contact page ，update ruyisdk introduce #31](https://github.com/ruyisdk/ruyisdk-website/pull/31) 关闭 [#30](https://github.com/ruyisdk/ruyisdk-website/issues/30)
    + [在联系页面与底边栏添加了微信公众号与qq群的二维码 #32](https://github.com/ruyisdk/ruyisdk-website/pull/32) 关闭 [#21](https://github.com/ruyisdk/ruyisdk-website/issues/21) [#27](https://github.com/ruyisdk/ruyisdk-website/issues/27)
    + [处理了两个语言相关issue #42](https://github.com/ruyisdk/ruyisdk-website/pull/42)
    + [Fix the image display bug/add some translations #48](https://github.com/ruyisdk/ruyisdk-website/pull/48) 关闭 [#36](https://github.com/ruyisdk/ruyisdk-website/issues/36) [#38](https://github.com/ruyisdk/ruyisdk-website/issues/38)
+ ruyisdk.org 提交 pr
    + [Remove X, telegram and wechat helper info #16](https://github.com/ruyisdk/ruyisdk-website/pull/16)
    + [增加 pr check #33](https://github.com/ruyisdk/ruyisdk-website/pull/33)
    + [删除韩语支持 #34](https://github.com/ruyisdk/ruyisdk-website/pull/34) 关闭 [#26](https://github.com/ruyisdk/ruyisdk-website/issues/26)
    + [隐藏日语和俄语支持 #37](https://github.com/ruyisdk/ruyisdk-website/pull/37)
    + [更新下载页面和对应的英语翻译 #39](https://github.com/ruyisdk/ruyisdk-website/pull/39) 关闭 [#28](https://github.com/ruyisdk/ruyisdk-website/issues/28)
    + “文档”页面内容通过 submodule 链接到 [#47](https://github.com/ruyisdk/ruyisdk-website/pull/47) 关闭 [#15](https://github.com/ruyisdk/ruyisdk-website/issues/15)
        + docs 仓库主文档（中文）放到 zh 分支 [docs#69](https://github.com/ruyisdk/docs/pull/69)
    + “下载”页面的德语翻译、“联系我们”页面的英语和德语翻译、“文档”侧栏的英语和德语翻译更新 [#49](https://github.com/ruyisdk/ruyisdk-website/pull/49) 关闭 [#40](https://github.com/ruyisdk/ruyisdk-website/issues/40) [#43](https://github.com/ruyisdk/ruyisdk-website/issues/43)
    + “联系我们”页面删除下方的评论区，以及相关代码 [#52](https://github.com/ruyisdk/ruyisdk-website/pull/52)
    + 底栏添加 RevyOS 文档链接，修复错误的 copyright 信息 [#51](https://github.com/ruyisdk/ruyisdk-website/pull/51)
    + “下载”页面 Ruyi 版本 [docs#70](https://github.com/ruyisdk/docs/pull/70) [#50](https://github.com/ruyisdk/ruyisdk-website/pull/50)
    + 审核前端实习生 pr 
+ ruyisdk/docs 仓库审核 cyl pr [#66](https://github.com/ruyisdk/docs/pull/66)，没有问题，已经合并
+ ruyisdk/docs 仓库中文文档与官网对齐，提交 pr [#67](https://github.com/ruyisdk/docs/pull/67)
    + 微调了 Ruyi 包管理器部分的文档结构
    + 更新了 Ruyi 包管理器相关文档内容
    + 增加 MilkV Duo 镜像刷写示例（将 fastboot 和 dd 分开叙述）
    + 微调了使用案例的标题和顺序
    + 将原有的“使用案例”板块移动到 Ruyi 包管理器下（结构上是 RuyiSDK 的案例，实际上全部是包管理器的案例），为未来编写 IDE 的使用案例板块预留空间
    + 将 IDE 的 TODO 状态改为 v0.0.2 可供尝鲜
    + 去掉了 Community 部分（在 ruyisdk.org 中已有该部分的独立板块且内容相对一致，同时去掉了本仓库中的 tg 和微信小助手信息）
    + 将 ruyisdk.org 中新增的文档内容同步到本仓库（RuyiSDK 的平台支持情况、 K230D 和隐私政策）
+ ruyisdk/docs 仓库解决 zh 分支构建的问题 [#71](https://github.com/ruyisdk/docs/pull/71)
+ 检查发现 <https://mirror.iscas.ac.cn/git/ruyisdk/packages-index> 处于完全不与主 GitHub 仓库同步且已经出现冲突的状态，故从文档删除与之相关的信息，向 ruyisdk/docs 仓库提交修复 pr [#72](https://github.com/ruyisdk/docs/pull/72)
+ 因为之前部分测试使用了 <https://mirror.iscas.ac.cn/git/ruyisdk/packages-index> 需要重新检查。检查发现 [packages-index](https://github.com/ruyisdk/packages-index) 出现许多失败的链接，同时检查 Ruyi 的相关特性已有文档记录。已经私戳相应实习生修复，并提交 issue 记录事件 [#28](https://github.com/ruyisdk/packages-index/issues/28)
+ Pioneer Box 炸了，修。检查发现 [packages-index](https://github.com/ruyisdk/packages-index) Milkv Pioneer Box 1.3 和 Milkv Meles 的 RevyOS 镜像落后于上游版本一年左右， support-matrix 亦落后，即新镜像未测试。提交 issue [#154](https://github.com/ruyisdk/support-matrix/issues/154) [#155](https://github.com/ruyisdk/support-matrix/issues/155)
+ 制作和提交 RV Day Tokyo 2025 Spring Submission 2 [Poster](https://easychair.org/conferences/submission?submission=7135387&track=329308&a=33962157)
+ 2024 年度报告 [slice](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyisdk/2024%E5%B9%B4%E5%BA%A6%E6%8A%A5%E5%91%8A.odp)
+ RuyiSDK 与 Xuantie 的 [视频提纲](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyisdk/ruyisdk_x_xuantie.md)
+ Archlinux CN 更新 [PKGBUILD](https://github.com/archlinuxcn/repo/commit/784eb583c582f17e0ba7377423f999e1020aed6e)
+ P119 新实习生考核题面 [p119](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month19/p119%E8%80%83%E6%A0%B8%E9%A2%98%E9%9D%A2.md) 实习生考核超时未回复提交，理论上考核失败

