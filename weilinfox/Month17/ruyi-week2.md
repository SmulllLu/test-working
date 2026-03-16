# RuyiSDK 测试组周志 24/11/11-24/11/15

## v0.22.0 开发周

+ ruyi deb/rpm 打包问题讨论，关联 issue [#228](https://github.com/ruyisdk/ruyi/issues/228)。 [comment-2469537248](https://github.com/ruyisdk/ruyi/pull/229#issuecomment-2469537248)、 [comment-2469924528](https://github.com/ruyisdk/ruyi/pull/229#issuecomment-2469924528)
  + 调研了 Debian 12-sid、 openkylin 2.0、 Fedora 38-41 上 ruyi 主要依赖的版本
  + ~~老板评论 openKylin 不用考虑。如果确实去除，则在 0.22.0 版本去除该项测试~~ 未来再看
  + 老板评论 Debian 支持 1 个版本。测试增加当前稳定版本 Debian 12 x86\_64，印象里 ruyi 在上面没有兼容性问题。 0.23.0 之前。
  + 老板评论 Deepin 考虑一下。暂时没有调研，经验判断 ruyi 在上面没有兼容性问题。 0.23.0 之前。
  + 老板评论 RuyiOS 支持 1 个版本。暂时没有调研。
+ ruyi-litester [b681eec..b98b740](https://github.com/weilinfox/ruyi-litester/compare/b681eec..b98b740) 计 30 个 commit， 700 增加 44 删除
  + 内部模块参数传递设计，统一一些全局变量和测试套获取变量的方式
    + 见 [README_zh.md#内部变量](https://github.com/weilinfox/ruyi-litester/blob/master/README_zh.md#内部变量)
  + 基于结构化脚本的测试设计，采用 mugen 格式，正在设计和实现必要的函数
    + 见 [README_zh.md#mugen-兼容](https://github.com/weilinfox/ruyi-litester/blob/master/README_zh.md#mugen-兼容)
  + [ruyi-mugen](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-mugen) 测试套
    + 移植好的 ruyi_test_binaries 测试用例
  + ruyi-basic
    + v0.21.0 ruyi admin checksum 默认 toml，而旧的 manifest 默认 json（之前没注意到这个变化，而 mugen 测试则没有这么严格不会受影响）
  + *既采用 DDT 又采用格式化脚本的思路是， DDT 是格式化脚本一种特例的抽象，所以不能抽象为 DDT 的测试依然需要格式化脚本作为补充*

## WIP

+ ruyi-advance 还有一些测试点尚有问题

## TODO

+ ruyi entrypoint

