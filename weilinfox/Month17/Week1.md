# Month 17 Week 1 工作报告 24/11/04-24/11/08

## RuyiSDK

+ ruyi v0.21.0 测试完成 pr [!52](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/52)
+ ruyi 提出两个新增 issue
  | issue 标题                                               | issue 链接                                         |
  | -------------------------------------------------------- | -------------------------------------------------- |
  | ruyi self uninstall --purge 残留本地遥测信息（影响 beta 版本，已 close） | [#226](https://github.com/ruyisdk/ruyi/issues/226) |
  | ruyi deb/rpm 打包问题                                    | [#228](https://github.com/ruyisdk/ruyi/issues/228) |
+ ruyi 0.21.0 Archlinux CN 打包忽略 pluginhost/test_api.py 测试，它需要在安装了 ruyi 的环境下运行，否则在 collect 阶段失败 [085515d](https://github.com/archlinuxcn/repo/commit/085515d2206c8346cec6fcd29c686de87c0d8ed4)
+ ruyi-mugen 测试添加 admin checksum 测试 pr [!24](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/24)
+ ruyi-litester [9902939..b681eec](https://github.com/weilinfox/ruyi-litester/compare/9902939..b681eec) 8 个 commit
  + ruyi-help
    + ruyi-help 适配 v0.21.0 改变的输出，增加 checksum/run-plugin-cmd 测试
  + ruyi-basic
    + ruyi-admin manifest 改为 checksum
  + ruyi-advance
    + 加入 ruyi-src 默认测试

