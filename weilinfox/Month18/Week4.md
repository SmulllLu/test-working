# Month 18 Week 4 工作报告 24/12/23-24/12/27

## RuyiSDK

+ ruyi v0.24.0 提出 2 个 issue
  | issue 标题                                        | issue 链接                                         |
  | ------------------------------------------------- | -------------------------------------------------- |
  | 配置文件中 upload\_consent 似乎不生效（已 close）  | [#246](https://github.com/ruyisdk/ruyi/issues/246) |
  | 打包 whl 包安装在 arpy 1.1.1 环境报错（已 close） | [#247](https://github.com/ruyisdk/ruyi/issues/247) |
    #246 实际上是 README 中的示例时间 [15:61:00](https://github.com/ruyisdk/ruyi/blob/fc7f3f4b2b79b809e8b91d1359359c909df14a06/README.md?plain=1#L76) 不存在
+ 新的测试平台搭建 Deepin 23 riscv64 和 x86\_64，用于 v0.25.0 版本测试
+ 文档方面写了一个修改提纲 [ruyisdk-docs\_0.24.0](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyisdk/ruyisdk-docs_0.24.0.md)，部分已经在 [#64](https://github.com/ruyisdk/docs/pull/64) 中实现，未实现的还需要进一步的工作
+ [ruyi-litester](https://github.com/weilinfox/ruyi-litester)
    + 适配 Deepin [3df7b64f](https://github.com/weilinfox/ruyi-litester/commit/3df7b64fcf8d634f2b9025df1657163a76bafbb7) [9690b2e3](https://github.com/weilinfox/ruyi-litester/commit/9690b2e3d11b81161bbd4a8dd2b7547a12005b98)
    + 新的用例 ruyi-box64 和 ruyi-wps-office [fe99815c](https://github.com/weilinfox/ruyi-litester/commit/fe99815c6f4fd6af19e430bf19c0b373b06245a3) [004d6224](https://github.com/weilinfox/ruyi-litester/commit/004d6224f3062f5421805c2c073b83e4b9cbb96a)
    + 合并艺灵 [#2](https://github.com/weilinfox/ruyi-litester/pull/2) [#8](https://github.com/weilinfox/ruyi-litester/pull/8)
+ [ruyi-litester-reports](https://github.com/weilinfox/ruyi-litester-reports)
    + 添加新用例信息 [3aa60df9](https://github.com/weilinfox/ruyi-litester-reports/commit/3aa60df9afb9fc6f40f9c9a7a3b20d0f4f6d4b5c)
    + 添加 Deepin 23 测试报告模板 [a828fc52](https://github.com/weilinfox/ruyi-litester-reports/commit/a828fc52525d0823ac639ef00c441c1b0d96a493)

