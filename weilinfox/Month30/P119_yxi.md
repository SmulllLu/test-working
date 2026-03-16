# P119 面试考核题

考核时间 2025/12/04-2025/12/11

考核题解答方式在题面中均有注明，有疑问及时沟通，完成考核题后可以约面试。若提前完成考核题则可以提前约面试，若考核时间不足以完成全部考核题则在有限的时间内尽可能展示自己。

面试方式为腾讯会议，需要开麦和共享屏幕，不需要开摄像头。面试期间会有考核题以外的问题现场解答，故需要有一个能用的 Linux 环境来解一些面试期间提出的问题，发行版不限，但不可以使用 WSL。整个面试过程可以 Google 也可以 ChatGPT，但是这些使用都以共享屏幕为前提，当然我们推荐不使用。面试时长会尽量控制在 1 小时以内。

1. 查看 ruyi 系统测试仓库 [ruyi-litester](https://github.com/weilinfox/ruyi-litester)， fork 并在自己的仓库中修复 workflow job [56989372352](https://github.com/weilinfox/ruyi-litester/actions/runs/19884655186/job/56989372352) 显示的相关错误，并成功实现符合 [b77cb2e](https://github.com/weilinfox/ruyi-litester/commit/b77cb2e890313e08666c75a69bff7432b54136a8) 预期的测试功能。
2. 查看 ruyi 系统测试仓库中的 [x86_64 测试](https://github.com/weilinfox/ruyi-litester/blob/master/.github/workflows/test-x86_64.yml)，在题 1 的仓库中实现针对 aarch64 架构的测试。
3. 阅读 ruyi 包管理器[文档](https://ruyisdk.org/docs/intro/) 安装并使用 ruyi 包管理器；安装 ruyisdk-vscode-extension 基于 ff88d84 分支的[构建](https://github.com/ruyisdk/ruyisdk-vscode-extension/actions/runs/19812469918)，阅读其[测试文档](https://www.notion.so/u2fsdgvkx1/RuyiSDK-VSCode-2ababfe305d4808ca0f5c98998d23881)，从用户视角出发寻找功能缺陷。将测试报告以 md 文档辅以图片的形式提交到个人 GitHub 账号下的公开仓库中。
4. 理解 [packages-index](https://github.com/ruyisdk/packages-index/)，用 python 实现一个后端接口，以 REST API 的方式，实现对 packages-index 中软件包信息的查询。将 python 工程以 md 文档辅以图片的形式提交到个人 GitHub 账号下的公开仓库中。

