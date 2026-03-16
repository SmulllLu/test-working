# Month 18 工作报告 24/12/02-24/12/27

## RuyiSDK

+ Ruyi v0.23.0 测试完成 pr [!54](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/54) [!55](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/55)
+ Ruyi v0.24.0 使用 ruyi-litester 进行测试，提交了初步报告；后对部分平台进行了重测，并提交重测后的报告和日志 pr [!56](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/56) [!57](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/57)
+ Ruyi v0.24.0 提出 2 个 issue
  | issue 标题                                        | issue 链接                                         |
  | ------------------------------------------------- | -------------------------------------------------- |
  | 配置文件中 upload\_consent 似乎不生效（已 close）  | [#246](https://github.com/ruyisdk/ruyi/issues/246) |
  | 打包 whl 包安装在 arpy 1.1.1 环境报错（已 close） | [#247](https://github.com/ruyisdk/ruyi/issues/247) |
    #246 实际上是 README 中的示例时间 [15:61:00](https://github.com/ruyisdk/ruyi/blob/fc7f3f4b2b79b809e8b91d1359359c909df14a06/README.md?plain=1#L76) 不存在
+ deb/rpm 打包脚本上游到 [ruyisdk/ruyi-packaging](https://github.com/ruyisdk/ruyi-packaging/tree/6e09c68dc86de2aec68c281dfe5bfb37ef2982b2)，并完成在 Github Workflow 的源码包打包流程
+ 回复 ruyi issue [#243](https://github.com/ruyisdk/ruyi/issues/243) 并更新 extra/wps-office 版本到 12.1.0.17900 [#20](https://github.com/ruyisdk/packages-index/pull/20)
+ ruyi-litester
    + 修复部分 shellcheck 报错和警告
    + 增加 GitHub Workflow 自动运行 litester 单元测试
    + 支持两种 yq —— mikefarah/yq 和 kislyuk/yq
    + 修复 jq 1.6 不支持的格式
    + 适配 Deepin [3df7b64f](https://github.com/weilinfox/ruyi-litester/commit/3df7b64fcf8d634f2b9025df1657163a76bafbb7) [9690b2e3](https://github.com/weilinfox/ruyi-litester/commit/9690b2e3d11b81161bbd4a8dd2b7547a12005b98)
    + 新的用例 ruyi-box64 和 ruyi-wps-office [fe99815c](https://github.com/weilinfox/ruyi-litester/commit/fe99815c6f4fd6af19e430bf19c0b373b06245a3) [004d6224](https://github.com/weilinfox/ruyi-litester/commit/004d6224f3062f5421805c2c073b83e4b9cbb96a)
    + 合并艺灵 [#1](https://github.com/weilinfox/ruyi-litester/pull/1) [#2](https://github.com/weilinfox/ruyi-litester/pull/2) [#3](https://github.com/weilinfox/ruyi-litester/pull/3) [#6](https://github.com/weilinfox/ruyi-litester/pull/6) [#8](https://github.com/weilinfox/ruyi-litester/pull/8)
+ [ruyi-litester-reports](https://github.com/weilinfox/ruyi-litester-reports)
    + 全新的测试报告生成脚本
    + 添加新用例信息 [3aa60df9](https://github.com/weilinfox/ruyi-litester-reports/commit/3aa60df9afb9fc6f40f9c9a7a3b20d0f4f6d4b5c)
    + 添加 Deepin 23 测试报告模板 [a828fc52](https://github.com/weilinfox/ruyi-litester-reports/commit/a828fc52525d0823ac639ef00c441c1b0d96a493)
+ [ruyi-reimu](github.com/weilinfox/ruyi-reimu/) 自动化测试调度程序更新
    + 改用 litester 进行测试
    + 使用 ruyi-litester-reports 生成报告
+ PLCT 开放日闪电演讲 ruyi-litester [ppt](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyi-litester/ruyi-litester-PLCT%E5%BC%80%E6%94%BE%E6%97%A5.odp)
+ deb/rpm 与 Nultka 打包性能对比文档 [nultka\_vs\_deb](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyi-packaging/nultka_vs_deb.md)
+ box64 运行 wps 文档 [box64\_wps](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyisdk/box64_wps.md)
+ ruyisdk/docs 仓库更新，写了一个修改提纲 [ruyisdk-docs\_0.24.0](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyisdk/ruyisdk-docs_0.24.0.md)，文档已有部分的更新已经在 [#64](https://github.com/ruyisdk/docs/pull/64) 中实现，缺少的新内容还需要进一步的编写工作
+ 新的测试平台搭建 Deepin 23 riscv64 和 x86\_64，用于 v0.25.0 版本测试
+ Cyl 实习生面试

