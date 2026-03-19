# P119 面试考核题 cyh

考核时间 2026/03/19-2026/03/26

考核题解答方式有两种，一种是 fork 某个仓库并在该仓库中完成，另一种是新开一个仓库并将题解存放在仓库中。请根据题面选择合适的方式。

完成考核题后可以约面试，面试方式为腾讯会议，需要开麦和共享屏幕，不需要开摄像头。面试期间可能会有考核题以外的问题现场解答，故需要有一个能用的 Linux 环境来解一些面试期间提出的问题，发行版不限，但不可以使用 WSL。整个面试过程可以 Google 也可以 LLM，但是使用的过程也应当投屏。面试时长会尽量控制在 1 小时以内。

阅读 RuyiSDK [文档](https://ruyisdk.org/docs/intro/) 安装并使用 ruyi 包管理器、 Eclipse 插件和 VS Code 插件。查看 ruyi 包管理器 [测试仓](https://github.com/ruyisdk-test/ruyi-litester/)、 Eclipse 插件 [测试仓](https://github.com/ruyisdk-test/ruyisdk-eclipse-plugins-test) 和 VS Code 插件 [测试仓](https://github.com/ruyisdk-test/ruyisdk-vscode-extension-test)。其中 ruyi 包管理器使用 github action 运行自动化测试， Eclipse 和 VS Code 插件为人工进行手动测试。

1. Fork ruyi 包管理器测试仓，测试 ruyi 包管理器 [0.48.0-alpha.20260317](https://github.com/ruyisdk/ruyi/releases/tag/0.48.0-alpha.20260317) 版本
2. （可选） VS Code 和 Eclipse 插件选其一执行手动测试
3. 针对 ruyi 包管理器和两种图形化插件的特性，调研测试方案。提出可行的迁移方案，或在现有方案基础上提出改进意见
