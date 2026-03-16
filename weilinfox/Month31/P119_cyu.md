# P119 面试考核题 cyu

考核时间 2026/01/19-2026/01/26

考核题解答方式在题面中均有注明，有疑问及时沟通，完成考核题后可以约面试。若提前完成考核题则可以提前约面试，若考核时间不足以完成全部考核题则在有限的时间内尽可能展示自己（即无法全部完成时允许部分作答）。

面试方式为腾讯会议，需要开麦和共享屏幕，不需要开摄像头。面试期间可能会有考核题以外的问题现场解答，故需要有一个能用的 Linux 环境来解一些面试期间提出的问题，发行版不限，但不可以使用 WSL。整个面试过程可以 Google 也可以 ChatGPT，但是这些使用都以共享屏幕为前提，当然我们推荐不使用。面试时长会尽量控制在 1 小时以内。

1. 阅读 ruyi 包管理器[文档](https://ruyisdk.org/docs/intro/) 安装并使用 ruyi 包管理器，理解 ruyi 包管理器和 ruyi 软件包索引 [packages-index](https://github.com/ruyisdk/packages-index) 之间的关系。改造 [ruyi-packaging](https://github.com/ruyisdk/ruyi-packaging/) 已有的代码，向 packages-index 自动提交 PR 以实现 packages-index/manifests/board-image 的自动更新，同时将相关更新提醒同步推送到 telegram 群组。

