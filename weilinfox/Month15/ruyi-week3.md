# RuyiSDK 测试组周志 24/09/16-24/09/20

## v0.18.0 测试周

+ ruyi 进入 archlinuxcn 源 x86_64/aarch64 [repo](https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/ruyi)
  + 可以自由安装测试
+ 0.18.0 测试 [pr](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/49)
  + 关于 ruyi 本身， Alpha/Beta 发现所有 bug，正式版没有 issue
  + 镜像相关 bug 随发现随提
+ 测试用例相关
  + Milkv Duo 工具链手动验证
  + 相关自动化用例随 ruyi venv 多工具链功能一起编写
+ ruyi 打包 x86_64 架构 [mirror](https://github.com/weilinfox/ruyi-builds/tree/master)
  待解决事项：
  + 源码包 License 问题，写了 debian/copyright 但是不见得写得准确。主要问题在几十个 rust 依赖方面，未来需要摸清
  + 软件包签名（在源码包 License 解决后考虑）

