# RuyiSDK 测试组周志 24/10/21-24/10/25

## v0.20.0 测试周

~~+ ruyi 打包共享文档，好像还没有更新~~
+ ruyi admin manifest --restrict 命令暂时不知道 --restrict 可选参数
+ ruyi v0.20.0 测试完成 pr [!51](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/51)
+ ruyi 提出两个新增 issue
  | issue 标题                                          | issue 链接                                         |
  | --------------------------------------------------- | -------------------------------------------------- |
  | ruyi admin format-manifest 接受 json 文件但处理出错 | [#217](https://github.com/ruyisdk/ruyi/issues/217) |
  | ruyi self clean --telemetry 无法完全删除本地遥测信息    | [#218](https://github.com/ruyisdk/ruyi/issues/218) |
+ ruyi-mugen 测试添加 admin format-manifest 测试 pr [!23](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/23)
+ ruyi-litester lit 测试套，由 ruyi-advance 测试套迁移两个较复杂的 ruyi-mugen 测试用例
  + [ruyi-basic](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-basic)
    + ruyi-admin 测试用例添加 format-manifest 测试
  + [ruyi-advance](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-advance)
    + ruyi-xdg
    + ruyi-config

