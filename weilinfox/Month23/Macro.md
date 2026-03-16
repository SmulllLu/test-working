# Marco 面试考核

考核时间 2025/05/06-2025/05/18

考核题目需要产出代码并提交 pr 到对应的仓库（找到正确的仓库也是考核的一部分）， pr 会被 review。考核题目需要在考核时间范围内尽力完成，有疑问及时沟通。已经全部完成，或已经到了截止时间但只是部分完成，都可以约面试；提前完成可以用余下的时间寻找考核题目以外的贡献点。若后续面试通过，考核题目的产出会计入实习产出。

面试方式为腾讯会议，需要开麦和共享屏幕，不需要开摄像头。需要有一个能用的 Linux 环境来解一些小问题，不限发行版，自己用得舒服就行。整个面试过程在共享屏幕时可以 Google 也可以 ChatGPT，当然我们推荐不使用。面试时长会尽量控制在 1 小时以内。

1. 向 ruyisdk.org 文档贡献内容
    + 观察 <https://ruyisdk.org/docs/Package-Manager/installation> 和 <https://ruyisdk.org/download> 两个页面可以发现，一个页面的下载链接是从 api 获取的，另一个页面则是硬编码的。将硬编码改为从 api 获取
    + 阅读 <https://ruyisdk.org/docs/Package-Manager/installation#使用系统包管理器安装> 中的内容，可以发现只有 Archlinux 的内容，实际上 RuyiSDK 提供了 [ruyisdk-overlay](https://github.com/ruyisdk/ruyisdk-overlay/) 供 Gentoo 用户使用。添加相关内容
    + 阅读 <https://ruyisdk.org/docs/Package-Manager/packages#ruyi-update-拉取失败> 中的内容，可以发现这里手动修改了 ``~/.config/ruyi/config.toml`` 配置，实际上最新版本的 Ruyi 包管理器已经有了更好的办法实现。修改相关内容
2. 优化 [ruyisdk.org](https://ruyisdk.org/) 首页
    + 首页横幅新闻（SlideNews）当前存在而需要修复的一些问题：
        1. 背景图片过大（1.55MB，2.80MB，3.05MB）
        2. 美观性欠缺（虽然因人而异，但大多数用户认为不美观）
        3. 信息量过少（比如文字内容不丰富）
    + 首页横幅新闻（SlideNews）相关的参考资料
        1. issue [【需求】删除掉首页的左右滚动的新闻，改成静态的，上下滚动 #79](https://github.com/ruyisdk/ruyisdk-website/issues/79)
        2. issue [网页改进方案 #92](https://github.com/ruyisdk/ruyisdk-website/issues/92)
        3. pr [beautify homepage & add demoboardpages & fix some statistic pages bugs #115](https://github.com/ruyisdk/ruyisdk-website/pull/115)
        4. pr [pages: use blured slide news background #123](https://github.com/ruyisdk/ruyisdk-website/pull/123)
    + 将顶栏（navbar）和底栏（footer）改为白底黑字

