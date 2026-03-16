# Month 9 Week 1 工作报告 24/03/4-24/03/10

## RuyiSDK

+ ruyi-mugen 添加配置文件测试，并测试 0.6.0-beta.20240307
   |       commit 标题        |                                            commit 链接                                             |
   |:------------------------:|:--------------------------------------------------------------------------------------------------:|
   |   Add config file test   | [5234f52](https://github.com/weilinfox/ruyi-mugen/commit/5234f5296f7a2cbd38b0d85298c4f87492814e66) |
   | Test 0.6.0-beta.20240307 |     [9f5e23b](github.com/weilinfox/ruyi-mugen/commit/9f5e23bf569fc2398cf1b47973c0e03f6be0999d)     |
+ 测试 0.6.0-beta.20240307 发现打包问题，缺少 libgit2 动态链接库，并发 issue
   |                     issue 标题                     |                                            issue 链接                                             |
   |:---------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|
   |                 ruyi 0.6.0 版本二进制 "ImportError: libgit2.so.1.7"                  | [!81](https://github.com/ruyisdk/ruyi/issues/81) |
+ ruyi rpm 包打包，由于 0.6.0 新增 types-cffi 与 pygit2 依赖，部分 oErv 已有包版本低于所需，新增四个包
   依赖包列表：
   | 包名              | 版本            |
   | ----------------- | --------------- |
   | libgit2           | 1.7.2           |
   | python-cffi       | 1.16.1          |
   | python-pygit2     | 1.14.1          |
   | python-types-cffi | 1.16.0.20240106 |

