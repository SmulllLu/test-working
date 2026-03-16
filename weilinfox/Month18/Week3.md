# Month 18 Week 3 工作报告 24/12/16-24/12/20

## RuyiSDK

+ 回复 ruyi issue [#243](https://github.com/ruyisdk/ruyi/issues/243) 并更新 extra/wps-office 版本到 12.1.0.17900 [#20](https://github.com/ruyisdk/packages-index/pull/20)
+ [ruyi-litester](https://github.com/weilinfox/ruyi-litester)
    + 增加 GitHub Workflow 自动运行 litester 单元测试
    + 支持两种 yq —— mikefarah/yq 和 kislyuk/yq
    + 修复 jq 1.6 不支持的格式
    + 合并 [#1](https://github.com/weilinfox/ruyi-litester/pull/1) [#3](https://github.com/weilinfox/ruyi-litester/pull/3) [#6](https://github.com/weilinfox/ruyi-litester/pull/6)
+ [ruyi-litester-reports](https://github.com/weilinfox/ruyi-litester-reports) 测试报告生成脚本
+ [ruyi-reimu](github.com/weilinfox/ruyi-reimu/) 自动化测试调度程序适配
    + 改用 litester 进行测试
    + 使用 ruyi-litester-reports 生成报告
+ Ruyi v0.24.0 进行测试，提交了初步报告；对部分平台进行了重测，并提交重测后的报告和日志 pr [!56](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/56) [!57](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/57)

