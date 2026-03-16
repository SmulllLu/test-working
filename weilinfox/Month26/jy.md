# Robert J162 面试考核题

考核时间 2025/08/30-2025/09/07

考核题解答方式在题面中均有注明，有疑问及时沟通，完成考核题后可以约面试。若提前完成考核题则可以提前约面试，若考核时间不足以完成全部考核题则在有限的时间内尽可能展示自己。

面试方式为腾讯会议，需要开麦和共享屏幕，不需要开摄像头。面试期间会有考核题以外的问题现场解答，故需要有一个能用的 Linux 环境来解一些面试期间提出的问题，发行版不限，可以使用 WSL。整个面试过程可以 Google 也可以 ChatGPT，但是这些使用都以共享屏幕为前提，当然我们推荐不使用。面试时长会尽量控制在 1 小时以内。

+ RuyiSDK 文档当前并不完善，这主要体现在无法向读者有效传达技术细节，而是大量依赖读者自身的知识储备。这两个考核题只需要文字解答，且文字解答需要以评论（comment）的形式发在对应的 issue 下方。
    1. 阅读 issue [#95](https://github.com/ruyisdk/docs/issues/95)，调研不同 Linux 发行版对 fastboot 权限授予的处理方式，调研范围覆盖 RuyiSDK [支持范围](https://ruyisdk.org/docs/Other/platform-support/)中一级和二级支持的操作系统发行版。
    2. 阅读 issue [#96](https://github.com/ruyisdk/docs/issues/96)，调研不同 Linux 发行版对从 PyPI 安装 Ruyi 包管理器的支持情况，调研范围覆盖 RuyiSDK 支持范围中一级和二级支持的操作系统发行版， Ruyi 包管理器的 python 依赖情况参考 [ruyi 的依赖兼容基线](https://github.com/ruyisdk/ruyi/blob/main/docs/dep-baseline.md)
+ 好了你现在已经明白（或者还不太明白）一些技术细节了，根据上面了解到的内容对下面的帖子给出分析和建议。这个部分只需要准备文字解答，并在面试时交流。
    1. [幽默ruyisdk硬控我一个小时](https://ruyisdk.cn/t/topic/506)
    2. [请问复现ruyisdk官网文档示例时编译coremark失败怎么办](https://ruyisdk.cn/t/topic/521)
    3. [参考RuyiSDK文档使用meson编译Taisei失败，请问如何解决](https://ruyisdk.cn/t/topic/1147)


下面这个题目属于 RuyiSDK 测试范围但是不属于 J162 的范围，一开始没有注意到是 J162。有能力的话也可以选做。

+ Ruyi 包管理器当前有多种发布方式，包括 Nuitka 单二进制和 PyPI 源两种。测试使用 [ruyi-litester](https://github.com/weilinfox/ruyi-litester)，这是一个基于 [LLVM Lit](https://llvm.org/docs/CommandGuide/lit.html) 的测试工具。 Ruyi 包
管理器的每个版本都由 [Jenkins CI 工程](https://jenkins.inuyasha.love/job/ruyi-reimu-mugen-auto-test/)调度测试。问：
    1. 该 Jenkins CI 工程所包含的测试，可以实现哪些测试步骤，不能实现哪些步骤。分析和提出改进意见。（有效的软件测试实际上分为4步进行，即单元测试、集成测试、确认测试和系统测试。）
    2. ruyi-litester 当前支持从 PyPI 源安装并测试 Ruyi 包管理器吗？如果不支持，向仓库提出 pr 来支持对其进行测试。
    3. 使用 ruyi-litester 对 Ruyi 包管理器在 PyPI 发布的 0.39.0 版本，在 openkylin 2.0 RISC-V 环境开展测试，产出测
试日志，并分析测试结果。测试环境搭建方式不限，可以是虚拟机、物理机也可以是容器。

