# Month 7 Week 5 工作报告 24/01/28-24/02/01

## RuyiSDK

+ RUYI 包管理 issue
   |                          issue 标题                           |                    issue 链接                    |
   |:-------------------------------------------------------------:|:------------------------------------------------:|
   | 镜像下载是否需要支持断点续传                                  | [#64](https://github.com/ruyisdk/ruyi/issues/64) |
+ ruyi-mugen 测试用例 ruyi\_test\_device 更新
   |                       commit 标题                       |                                            commit 链接                                             |
   |:-------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|
   | Update ruyi test version and remove oe from test names  | [22f7d72](https://github.com/weilinfox/ruyi-mugen/commit/22f7d726cfdbff928a8fd931344b6a54c5481171) |
   |    Merge pull request #1 from KotorinMinami/ruyisdk     | [6f656fb](https://github.com/weilinfox/ruyi-mugen/commit/6f656fb2a638d16f67497229bd77170877df45de) |
   |               Change device test tmp dir                | [d984e0d](https://github.com/weilinfox/ruyi-mugen/commit/d984e0d529085ed88c1df376788db72a355d7752) |
   |                     Fix device test                     | [b845e1f](https://github.com/weilinfox/ruyi-mugen/commit/b845e1fbab16560e0fec64d9ad7c12c9dcb3f6e3) |
   |           Check ruyi install failure message            | [7638bb4](https://github.com/weilinfox/ruyi-mugen/commit/7638bb451541b0b96e1a8d8a27855fc56b4ef886) |
   |                   Backup device logs                    | [1fd449f](https://github.com/weilinfox/ruyi-mugen/commit/1fd449f423bb1594be5e36a35a0c7ab7315d4adf) |
   |         Update device test timeout to 1440 min          | [56dcce6](https://github.com/weilinfox/ruyi-mugen/commit/56dcce6e6d68b35c52fbf5a2f975e86f731e446a) |
   |                Add ruyi unzip dependency                | [916c6ba](https://github.com/weilinfox/ruyi-mugen/commit/916c6ba41b1a3684c74319069abc29b4afcab802) |
   |          Update jenkins testing time to 24 hrs          | [1400e23](https://github.com/weilinfox/ruyi-mugen/commit/1400e232b4510507f27715e87ef644adc4e384c3) |
   |               Clean after each image test               | [c5c70c5](https://github.com/weilinfox/ruyi-mugen/commit/c5c70c5ef0bc4acc0d04b1c8420ce6d91ac8a309) |
   |              Add recursion\_run check point             | [5b48c59](https://github.com/weilinfox/ruyi-mugen/commit/5b48c5915e8567a049c62b1a72c90e2d93d836bc) |
   |             Update device log tarball name              | [b303609](https://github.com/weilinfox/ruyi-mugen/commit/b303609247e524de7b700e097be3f65bff50f895) |
   |                 Check parameter length                  | [8023e22](https://github.com/weilinfox/ruyi-mugen/commit/8023e2289146a35c7abe85ebc63c5ffc26653b26) |
   |                     Fix source libs                     | [9bdd1e6](https://github.com/weilinfox/ruyi-mugen/commit/9bdd1e6e17fc2c479107d372036059fa5b465ac2) |
   |                      Fix log files                      | [a02b4ec](https://github.com/weilinfox/ruyi-mugen/commit/a02b4ecb87b88c8297c24ea5a4ecb853cf454eba) |
   |                    Update test admin                    | [af89fae](https://github.com/weilinfox/ruyi-mugen/commit/af89fae5505903dcbcb7718ff7436b8e7ca4da2c) |
   |                       Update ruyi                       | [bd64974](https://github.com/weilinfox/ruyi-mugen/commit/bd649745b064797606604116c85d8b7cc7a04f51) |
   |               Retry when download failed                | [a38f1f3](https://github.com/weilinfox/ruyi-mugen/commit/a38f1f3cf5771eae7b0470bc0260980f0cbd553b) |
   |          Redirect full log to tmp output file           | [98ae4d7](https://github.com/weilinfox/ruyi-mugen/commit/98ae4d725b3f01025a36dcd2181e1d1f2f49791c) |
   | Device test stop at download age | [e9b9d8d](https://github.com/weilinfox/ruyi-mugen/commit/e9b9d8d9712e308f16448dd21e00d821140c7a9d) |
   | Fix some amazing bugs | [1f177aa](https://github.com/weilinfox/ruyi-mugen/commit/1f177aacc387605f877d8d4fd98339a9713939f9) |
   | Open some test point | [7f14471](https://github.com/weilinfox/ruyi-mugen/commit/7f144718195ec0001152c1123fd9efaf5f646f5e) |
   | Use nohup to replase SLEEP\_WAIT | [c2b11d9](https://github.com/weilinfox/ruyi-mugen/commit/c2b11d925180becc67d09a632464257856c34b44) |
   | Fix wget output checking | [12a9045](https://github.com/weilinfox/ruyi-mugen/commit/12a9045dd51890a416ec194ce64ffbb68f88b211) |
   | Test release binary | [6be17ec](https://github.com/weilinfox/ruyi-mugen/commit/6be17ec3725783f6d63e259c00e4ebbc947a31d0) |
   | Fix corner cases | [679c92c](https://github.com/weilinfox/ruyi-mugen/commit/679c92cc00dd0d05180f831d5030c72ee975c719) |
   | Make some variable local | [e9f441e](https://github.com/weilinfox/ruyi-mugen/commit/e9f441e722d430266606e4404d6407359fdf7ede) |
   | Update default mugen timeout to 60m | [c5fc046](https://github.com/weilinfox/ruyi-mugen/commit/c5fc0465227c367cd3eab014e12a3b8835ace86a) |
+ 同步 ruyi-mugen 代码到 Gitee mugen-ruyi 仓库
   |            pr 标题             |                         pr 链接                          |
   |:------------------------------:|:--------------------------------------------------------:|
   | Update test cases | [!2](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/2) |
   | Update device test | [!3](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/3) |
+ RUYI 包管理 v0.4.0 测试，提交 x86\_64 Fedora 38 、 x86\_64 Ubuntu 22.04 LTS 、 x86\_64 openEuler 23.09 、 riscv64 Container RevyOS 20231210 、 riscv64 openEuler 23.09 五个环境的测试结果
   |            pr 标题             |                         pr 链接                          |
   |:------------------------------:|:--------------------------------------------------------:|
   | 提交 RevyOS 容器测试报告 | [!6](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/6) |
   | 提交 RUYI 0.4.0 QEMU 测试报告 | [!9](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/9) |
   |     Fix broken video links      | [!11](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/11) |
+ RUYI 包管理文档添加，更新 ruyisdk/docs 仓库和 ruyisdk/doc4test 仓库
   |              pr 标题               |                     pr 链接                      |
   |:----------------------------------:|:------------------------------------------------:|
   |  Add v0.4.0 features  |  [#33](https://github.com/ruyisdk/docs/pull/33)  |
   
   |              commit 标题              |                                          commit 链接                                           |
   |:-------------------------------------:|:----------------------------------------------------------------------------------------------:|
   | Add 0.4.0 update note | [c4ac41f](https://github.com/ruyisdk/doc4test/commit/c4ac41f17dc0aa7a182823b47d84d07ad677d362) |
   | Update v0.3.0 path | [e63cf70](https://github.com/ruyisdk/docs/pull/33/commits/e63cf70aa2000576f4ccf60f60af77f7ddb6132c) |
   | Add v0.4.0 feature | [a0dfc05](https://github.com/ruyisdk/docs/pull/33/commits/a0dfc059f57e6d0a8e1cff210f4f42db8f5ff960) |

