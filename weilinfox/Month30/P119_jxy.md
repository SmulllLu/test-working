# P119 面试考核题 jxy

考核时间 2025/12/17-2025/12/25

考核题解答方式在题面中均有注明，有疑问及时沟通，完成考核题后可以约面试。若提前完成考核题则可以提前约面试，若考核时间不足以完成全部考核题则在有限的时间内尽可能展示自己（即无法全部完成时允许部分作答）。

面试方式为腾讯会议，需要开麦和共享屏幕，不需要开摄像头。面试期间会有考核题以外的问题现场解答，故需要有一个能用的 Linux 环境来解一些面试期间提出的问题，发行版不限，但不可以使用 WSL。整个面试过程可以 Google 也可以 ChatGPT，但是这些使用都以共享屏幕为前提，当然我们推荐不使用。面试时长会尽量控制在 1 小时以内。

1. 阅读 ruyi 包管理器[文档](https://ruyisdk.org/docs/intro/) 安装并使用 ruyi 包管理器；安装 ruyisdk-vscode-extension 基于 ff88d84 分支的[构建](https://github.com/ruyisdk/ruyisdk-vscode-extension/actions/runs/19812469918)，阅读其[测试文档](https://www.notion.so/u2fsdgvkx1/RuyiSDK-VSCode-2ababfe305d4808ca0f5c98998d23881)，从用户视角出发寻找功能缺陷。将测试报告以 md 文档辅以图片的形式提交到个人 GitHub 账号下的公开仓库中。
2. 为 [ruyi-packaging](https://github.com/ruyisdk/ruyi-packaging/) 选择一个依赖管理和构建工具，编写 pyproject.toml，提交到 fork 的仓库中。
3. 理解 [ruyi-packaging](https://github.com/ruyisdk/ruyi-packaging/) 项目，这个项目试图实现 [packages-index/board-image](https://github.com/ruyisdk/packages-index/tree/main/manifests/board-image) 的自动更新，使用 ``check`` 命令检查上游更新，使用 ``manifests`` 命令生成指定版本的 toml 配置。其中 ``manifests`` 命令的使用方法是指定要生成的版本，若不指定版本则生成最新版本的 toml。请完善该命令，使其自动检测缺少的版本，并补全这些版本。提交到 fork 的仓库中名为 new 的分支中。
