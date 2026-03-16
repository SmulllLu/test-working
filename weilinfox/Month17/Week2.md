# Month 17 Week 2 工作报告 24/11/11-24/11/15

## RuyiSDK

+ ruyi deb/rpm 打包问题讨论，关联 issue [#228](https://github.com/ruyisdk/ruyi/issues/228)。 [comment-2469537248](https://github.com/ruyisdk/ruyi/pull/229#issuecomment-2469537248)、 [comment-2469924528](https://github.com/ruyisdk/ruyi/pull/229#issuecomment-2469924528)
  + 调研了 Debian 12-sid、 openkylin 2.0、 Fedora 38-41 上 ruyi 主要依赖的版本
  + v0.23.0 增加 Debian 12 x86\_64 测试
  + v0.23.0 增加 Deepin 测试
+ ruyi-litester [b681eec..b98b740](https://github.com/weilinfox/ruyi-litester/compare/b681eec..b98b740) 计 30 个 commit， 700 增加 44 删除
  + 内部模块参数传递设计，统一一些全局变量和测试套获取变量的方式
    + 见 [README\_zh.md#内部变量](https://github.com/weilinfox/ruyi-litester/blob/master/README_zh.md#内部变量)
  + 基于结构化脚本的测试设计，采用 mugen 格式，正在设计和实现必要的函数
    + 见 [README\_zh.md#mugen-兼容](https://github.com/weilinfox/ruyi-litester/blob/master/README_zh.md#mugen-兼容)
  + [ruyi-mugen](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-mugen) 测试套
    + 移植好的 ruyi\_test\_binaries 测试用例
  + ruyi-basic
    + v0.21.0 ruyi admin checksum 默认 toml，而旧的 manifest 默认 json（之前没注意到这个变化，而 mugen 测试则没有这么严格不会受影响）

