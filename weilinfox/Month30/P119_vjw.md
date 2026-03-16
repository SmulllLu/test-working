# P119 面试考核题 vjw

考核时间 2025/12/22-2025/12/30

考核题解答方式在题面中均有注明，有疑问及时沟通，完成考核题后可以约面试。若提前完成考核题则可以提前约面试，若考核时间不足以完成全部考核题则在有限的时间内尽可能展示自己（即无法全部完成时允许部分作答）。

面试方式为腾讯会议，需要开麦和共享屏幕，不需要开摄像头。面试期间可能会有考核题以外的问题现场解答，故需要有一个能用的 Linux 环境来解一些面试期间提出的问题，发行版不限，但不可以使用 WSL。整个面试过程可以 Google 也可以 ChatGPT，但是这些使用都以共享屏幕为前提，当然我们推荐不使用。面试时长会尽量控制在 1 小时以内。

1. 阅读 ruyi 包管理器[文档](https://ruyisdk.org/docs/intro/) 安装并使用 ruyi 包管理器；安装 ruyisdk-eclipse-plugins 的[最新 pre-release](https://github.com/ruyisdk/ruyisdk-eclipse-plugins/releases/tag/continuous)，阅读其[旧版文档](https://www.notion.so/u2fsdgvkx1/RuyiSDK-VSCode-2ababfe305d4808ca0f5c98998d23881)，从用户视角出发寻找功能更新和功能缺陷。将测试报告以 md 文档辅以图片的形式提交到个人 GitHub 账号下的公开仓库中。
2. 为 [ruyi-packaging](https://github.com/ruyisdk/ruyi-packaging/) 选择一个依赖管理和构建工具，编写 pyproject.toml，提交到 fork 的仓库中。
3. 理解 [ruyi-packaging](https://github.com/ruyisdk/ruyi-packaging/) 项目，这个项目试图实现 [packages-index/board-image](https://github.com/ruyisdk/packages-index/tree/main/manifests/board-image) 的自动更新，使用 ``check`` 命令检查上游更新，使用 ``manifests`` 命令生成指定版本的 toml 配置。其中以 [openbsd-riscv64-live](https://github.com/ruyisdk/packages-index/blob/main/manifests/board-image/openbsd-riscv64-live/7.6.0.toml#L12) 为例，其使用了 ``mirror://`` 格式的 url，其声明见 [config.toml](https://github.com/ruyisdk/packages-index/blob/main/config.toml#L47)，不难发现 ``openbsd`` 声明的 url 中并不是每个 url 都有相关资源可供下载。请实现一个 bot，定期检查这些资源的可用性（url 是否可达），并以 Fast API 的方式提供查询接口。对于 ``mirror://`` 格式 url 的资源，则需要标记其中每个 url 的可用性。将代码提交到个人 GitHub 账号下的公开仓库中。

