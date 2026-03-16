# Month 6 工作报告 23/12/02-23/12/28

## mugen 测试工具

+ 将黄烁改进的 KotorinMinami/mugen-riscv 工具与 brsf11/mugen-riscv 进行合并，完成了整体功能的合并，修正了一些函数不匹配和模块匹配问题。还有一些其他 bug 正在和黄烁一起处理
   |                                             commit 链接                                             | commit 标题                                                            |
   |:---------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------- |
   | [b905d48](https://github.com/weilinfox/mugen-riscv/commit/b905d48c5e283edd43d69d95ffec7d94b448c637) | Merge branch 'qemu' of github.com:KotorinMinami/mugen-riscv into riscv |
   | [b2b34df](https://github.com/weilinfox/mugen-riscv/commit/b2b34df66e089c5403327c1bda0ec4b57487c90b) | Auto create shared directories                                         |
   | [7ae0a95](https://github.com/weilinfox/mugen-riscv/commit/7ae0a95d2c80d6faa41870f95b1ca30ee139d272) | Update qemuVM.py                                                       |
   | [d05db0a](https://github.com/weilinfox/mugen-riscv/commit/d05db0ac4bbe21d4542256e1a1730441301c390e) | Fix qemu_test import error                                             |
   | [7c2ab54](https://github.com/weilinfox/mugen-riscv/commit/7c2ab54479d655dd2d96bf90490230b5b1c6913a) | Fix OET_PATH env missing                                               |
   | [b55bcc0](https://github.com/weilinfox/mugen-riscv/commit/b55bcc0eb1211505e526e0ba8bcb4bc0b10958fa) | Fix mugen_riscv                                                        |
   | [1c3f40f](https://github.com/weilinfox/mugen-riscv/commit/1c3f40ff027abf2799a7564554f7d4f5fc54d393) | Remove kparms                                                          |
   | [cd77e7b](https://github.com/weilinfox/mugen-riscv/commit/cd77e7bd875eeda7199816d8c7c83d2a7d9c4e1a) | Fix combination_parser.py clear_one_testsuite error                    |
   | [05fc5a1](https://github.com/weilinfox/mugen-riscv/commit/05fc5a1b8a6453a5541b70bf1e6b5b038162de74) | Remove ls print                                                        |
   | [236b8f3](https://github.com/weilinfox/mugen-riscv/commit/236b8f3eb7515d22eb707e1b3f40c6da619d4b32) | Fix bugs                                                               |

## mugen issue

+ 分析 2309 独立发版测试的日志并进行 issue 提交
   |                         issue 链接                         | issue 标题                                                                                       |
   |:----------------------------------------------------------:|:------------------------------------------------------------------------------------------------ |
   | [I8S2FJ](https://gitee.com/openeuler/mugen/issues/I8S2FJ)  | embedded_os_basic_test 测试套 oe_test_basic_cmd_dmesg 用例在 openEuler 2309 RISC-V 测试失败      |
   | [I8S2M4](https://gitee.com/openeuler/mugen/issues/I8S2M4)  | curl 测试套 oe_test_curl_curl_001 用例测试条件脆弱                                               |
   | [I8S3MZ](https://gitee.com/openeuler/mugen/issues/I8S3MZ)  | tpm-tools_20.03 测试套在 openEuler 2309 x86_64 测试失败                                          |
   | [I8S4BB](https://gitee.com/openeuler/mugen/issues/I8S4BB)  | selinux 测试套 oe_test_identify_selinux_rejects 用例依赖 audit 软件包                            |
   | [I8S5LF](https://gitee.com/openeuler/mugen/issues/I8S5LF)  | podman_3.4.4.2 测试套配置的 docker 镜像只适用于 x86_64 和 aarch64 架构                           |
   | [I8S5O0](https://gitee.com/openeuler/mugen/issues/I8S5O0)  | podman 与 podman_3.4.4.2 测试套一些用例需要的 docker 镜像上游并没有适配 riscv64 架构导致测试失败 |
   | [I8S0T5](https://gitee.com/openeuler/RISC-V/issues/I8S0T5) | 2309 独立发版 Qemu 镜像默认时区 timedatectl 输出为 n/a                                           |
   | [I8S1SF](https://gitee.com/openeuler/RISC-V/issues/I8S1SF) | 2309 独立发版软件源中包含版本结尾非 oe2309 的软件包                                              |
   | [I8S2UK](https://gitee.com/openeuler/RISC-V/issues/I8S2UK) | 2309 独立发版镜像默认情况下 yumdownloader 无法下载到 nototools 的源码包                          |
   | [I8S3YN](https://gitee.com/openeuler/RISC-V/issues/I8S3YN) | 2309 独立发版软件源中缺失 stratovirt 软件包                                                      |
+ 针对 2309 独立发版测试的已经发现的一个需要适配 RISC-V 的测试用例进行适配
   |                        pr 链接                        | pr 标题                                                                  |
   |:-----------------------------------------------------:|:------------------------------------------------------------------------ |
   | [!2289](https://gitee.com/openeuler/mugen/pulls/2289) | embedded_os_basic_test: oe_test_basic_cmd_dmesg fix riscv64 test failure |

## RUYISDK 测试

+ pre_round4 、 pre_round5 、 部分 round1 和 round2 的测试报告。提交 pr [!5](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/5) [!7](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/7) [!11](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/11) [!12](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/12) [!15](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/15)
+ [mugen-ruyi](https://gitee.com/weilinfox/mugen-ruyi) 仓库的 mugen 用例更新，现有 8 个用例
   |                                            commit 链接                                            | commit 标题                                             |
   |:-------------------------------------------------------------------------------------------------:|:------------------------------------------------------- |
   | [df3d0de](https://gitee.com/weilinfox/mugen-ruyi/commit/df3d0de4170b3369efc34613205be72c81a9b61e) | Not check expect in common_lib.sh                       |
   | [fdb5099](https://gitee.com/weilinfox/mugen-ruyi/commit/fdb509990493928b43c98ffc2efdae59fc9f5c7c) | Install ruyi dependencies                               |
   | [8ec98c5](https://gitee.com/weilinfox/mugen-ruyi/commit/8ec98c5df276942f94b6baf2391843f315dd3e83) | Add ruyi admin test                                     |
   | [e106801](https://gitee.com/weilinfox/mugen-ruyi/commit/e106801de909e9a4aa34afa909a8752fafb1accb) | Add ruyi issue 10 test                                  |
   | [be0f778](https://gitee.com/weilinfox/mugen-ruyi/commit/be0f778dc7cd282de4e7331b6549e684fcc08197) | Fix INSTALL error                                       |
   | [c2bedfe](https://gitee.com/weilinfox/mugen-ruyi/commit/c2bedfe9b8633b24d49c48df4e128cf5192eb35a) | Fix cmake_ninja test check failure                      |
   | [0c90a06](https://gitee.com/weilinfox/mugen-ruyi/commit/0c90a06949012765736b2c3dab9c4b10dd1086e4) | Update test to 20231203                                 |
   | [5c630d9](https://gitee.com/weilinfox/mugen-ruyi/commit/5c630d9959d6c19800c2790646fe120b36c083fb) | Add XDG_DATA_HOME test                                  |
   | [77b61ee](https://gitee.com/weilinfox/mugen-ruyi/commit/77b61ee577f5a3f44154bca7c504f2f437f05436) | Add self uninstall tests                                |
   | [7488e4a](https://gitee.com/weilinfox/mugen-ruyi/commit/7488e4ab9779985be39219327af802dcbe335a79) | Add ruyi bzip2 dependency                               |
   | [9a9c7ce](https://gitee.com/weilinfox/mugen-ruyi/commit/9a9c7cecee3be44a9a0f12e64213f4186aa9bd89) | Add "no binary for current host" check in install tests |
   | [bfd43b4](https://gitee.com/weilinfox/mugen-ruyi/commit/bfd43b424a3523acbe7f41503d546d5305ad02fd) | Merge wrong proxy test into main test                   |
   | [d705246](https://gitee.com/weilinfox/mugen-ruyi/commit/d7052462b664223ddfbfa57aba4d0c57029ec48c) | Fix missmatch return code of apt-get --simulate option  |
   | [509f2bd](https://gitee.com/weilinfox/mugen-ruyi/commit/509f2bd24cf0c8ef6b6d196558932b20eb4a4744) | Fix filt support package failure                        |
   | [e431f97](https://gitee.com/weilinfox/mugen-ruyi/commit/e431f975a5e06d5e6c46c1cf5b1fce0c9a526722) | Remove empty command line test                          |
   | [cd5dc4c](https://gitee.com/weilinfox/mugen-ruyi/commit/cd5dc4cf654f1b9b9a7edaea580b1e3036501a49) | Fix directory check error                               |
   | [e8608bd](https://gitee.com/weilinfox/mugen-ruyi/commit/e8608bdf0ea7aa7e5c11e468680ad75cbfa228e1) | Add ruyi qemu test                                      |
   | [1fab2b8](https://gitee.com/weilinfox/mugen-ruyi/commit/1fab2b85a76227d3d8581cdaf80214307136afd7) | Skip qemu test on riscv64 host                          |
   | [9ef109b](https://gitee.com/weilinfox/mugen-ruyi/commit/9ef109be9fbdc3d880e6dc016850a0bf56f1c92f) | Update test version to 20231203                         |
   | [5e4a7b9](https://gitee.com/weilinfox/mugen-ruyi/commit/5e4a7b9eb684f79fb6cdfe5aa4d2c8c85f111ba5) | Add llvm test                                           |
   | [9ace185](https://gitee.com/weilinfox/mugen-ruyi/commit/9ace18596eb5a968f17362be6be7655582d54205) | Make oe_test_ruyi_llvm suites riscv64 host              |
   | [46d495f](https://gitee.com/weilinfox/mugen-ruyi/commit/46d495fc2790e0b5ac36d36f6ed49c434b351f16) | Check binaries for test host before testing             |
   | [4e84d57](https://gitee.com/weilinfox/mugen-ruyi/commit/4e84d57efe1f168c80c1679b05123f6453d2a987) | Add xthead qemu test                                    |
   | [4ab8eae](https://gitee.com/weilinfox/mugen-ruyi/commit/4ab8eaebbc8a5409c3723fc3c7fd7214f775146c) | Fix awk regex failure                                   |
   | [16147f4](https://gitee.com/weilinfox/mugen-ruyi/commit/16147f4a5e1b142d8023b3ea9f837d583bb1de6e) | Fix awk issue at unexpected newline                     |
   | [8d36c3a](https://gitee.com/weilinfox/mugen-ruyi/commit/8d36c3af10700c560023309852e32523ad3e99c4) | Update ruyi version 20231211                            |
   | [fb594e7](https://gitee.com/weilinfox/mugen-ruyi/commit/fb594e76fe72feb192881c905101de674a44d705) | !1 Use URLs in dnf install                              |
+ 内部文档仓库维护 [doc4test](https://github.com/ruyisdk/doc4test/blob/main/README.md)
   |                                          commit 链接                                           | commit 标题                       |
   |:----------------------------------------------------------------------------------------------:|:--------------------------------- |
   | [1732ac2](https://github.com/ruyisdk/doc4test/commit/1732ac2fc6dbc8cac14508efcc249ad2ddb256c8) | Fit v0.2                          |
   | [4eba815](https://github.com/ruyisdk/doc4test/commit/4eba8152f1789fae158189ad45fafed447acba10) | Add upstream venv cases           |
   | [fc4034a](https://github.com/ruyisdk/doc4test/commit/fc4034a8c9b4cd68c44ef970b465a8a9418c1b69) | Add sipeed-lpi4a profile manual   |
   | [cbbb8b5](https://github.com/ruyisdk/doc4test/commit/cbbb8b5bfb137390f501c416c687cee36beada0e) | Add llvm manual                   |
   | [953705a](https://github.com/ruyisdk/doc4test/commit/953705ae245e6f9145c70255837550cd3ba43a9f) | Add qemu manual                   |
   | [2e8d4ed](https://github.com/ruyisdk/doc4test/commit/2e8d4edec327ee1649b3996bb543a9c72d68a856) | Add self uninstall manual         |
   | [4674209](https://github.com/ruyisdk/doc4test/commit/46742091576b08de50ea314135e462cf8f03c40a) | Modify uninstall desc             |
   | [069f146](https://github.com/ruyisdk/doc4test/commit/069f1462000522cad68e197b4cc6e67d20aad7d9) | Modify PS1 in codeblocks          |
   | [cc49c14](https://github.com/ruyisdk/doc4test/commit/cc49c14ca223adcb7151a659756640b4d1285ad4) | Add desc about llvm-upstream slug |
   | [149ecb3](https://github.com/ruyisdk/doc4test/commit/149ecb3aeae762cae61d2e0c94695af8cbb891cf) | Add support platform links        |
   | [5da5b22](https://github.com/ruyisdk/doc4test/commit/5da5b226c04475361e8e9245782f2c87e3d7ee10) | Modify func desc                  |
   | [f49f401](https://github.com/ruyisdk/doc4test/commit/f49f401eba0245998cba385f3a9fe26d1cb86e46) | Correct self uninstall command    |
   | [65213aa](https://github.com/ruyisdk/doc4test/commit/65213aab7af648141945ae09c6fab80e7310fdea) | Add xthead qemu                   |
   | [492cf90](https://github.com/ruyisdk/doc4test/commit/492cf901e2e507702ac353b9aaf238ce1de81b63) | Update commands                   |
   | [951748f](https://github.com/ruyisdk/doc4test/commit/951748fd7e89251de5e9a8c32f3174e914a1dbc4) | Update list                       |
   | [5d4a84b](https://github.com/ruyisdk/doc4test/commit/5d4a84b91d180ac29ea1291260e6ba0a62b975a3) | Fix revyos version                |
+ 公开文档仓库的文档同步 pr [#21](https://github.com/ruyisdk/docs/pull/21) [#22](https://github.com/ruyisdk/docs/pull/22) [#28](https://github.com/ruyisdk/docs/pull/28)
+ 向 RUYI 仓库提出 issue ：
   |                    issue 链接                    | issue 标题                                            |
   |:------------------------------------------------:|:----------------------------------------------------- |
   | [#18](https://github.com/ruyisdk/ruyi/issues/18) | 在 RUYI 环境中使用绝对路径/相对路径调用工具链时失败   |
   | [#19](https://github.com/ruyisdk/ruyi/issues/19) | ruyi install slug:llvm-upstream-20231121 找不到软件包 |
   | [#21](https://github.com/ruyisdk/ruyi/issues/21) | plct-xthead 工具链构建 C 程序无法运行                 |
   | [#24](https://github.com/ruyisdk/ruyi/issues/24) | gdb 依赖 libpython3.8.so.1.0                          |
+ 向 RUYI 仓库提出 pr ：
   |                    pr 链接                     | pr 标题      |
   |:----------------------------------------------:|:------------ |
   | [#17](https://github.com/ruyisdk/ruyi/pull/17) | Fix spelling |


## 单项测试

+ ncnn 移植和优化 ppt 单项测试，发现一些问题并提出[修改意见](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month06/Week2/%E5%8D%95%E9%A1%B9%E6%B5%8B%E8%AF%95%E4%BF%AE%E6%94%B9%E6%84%8F%E8%A7%81.md)

## RevyOS issue

+ 发现 LXC 容器无法在 RevyOS 20231026 运行，这是由于 RevyOS 内核没有打开 ``CONFIG_IP_NF_MANGLE`` 、 ``CONFIG_IP6_NF_MANGLE`` 、 ``CONFIG_NETFILTER_XT_TARGET_CHECKSUM`` 等内核选项，而 lxc-net 依赖这些模块导致的
   |                    issue 链接                     | issue 标题                                                                         |
   |:-------------------------------------------------:|:---------------------------------------------------------------------------------- |
   | [#39](https://github.com/revyos/revyos/issues/39) | lxc-net: iptables: can't initialize iptables table \`mangle': Table does not exist |
   
   该问题已经修复，并在 20231210 版本发布。

## 其他工作

+ 12 月 15 日做了开放日报告《基于 Jenkins CI 的 mugen 自动化测试框架研究》。[提纲与 ppt](https://gitlab.inuyasha.love/weilinfox/plct-working/-/tree/master/Note/mugen-jenkins) 提交 pr [#189](https://github.com/plctlab/PLCT-Open-Reports/pull/189)

## 出差

+ 去往山大配置 SG2042 2U 服务器
   山大尚没有给出远程连接服务器的方式，暂时使用个人服务器进行组网实现远程连接，现在连接正常可以正常访问
+ 产出 SG2042 2U 服务器配置记录 [sg2042_2u_manual.md](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month06/Week3/sg2042_2u_manual.md)

## 关联的提交

+ mugen 上游 openeuler/mugen pr [!2289](https://gitee.com/openeuler/mugen/pulls/2289)
+ ruyiSDK v0.2 Test yunxiangluo/ruyi-sdk-v0.2-test pr [!5](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/5) [!7](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/7) [!11](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/11) [!12](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/12) [!15](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/15)
+ RUYI 包管理仓库 pr [#17](https://github.com/ruyisdk/ruyi/pull/17)
+ RUYISDK 文档仓库 ruyisdk/docs pr [#21](https://github.com/ruyisdk/docs/pull/21) [#22](https://github.com/ruyisdk/docs/pull/22) [#28](https://github.com/ruyisdk/docs/pull/28)
+ 公开演讲仓库 plctlab/PLCT-Open-Reports pr [#189](https://github.com/plctlab/PLCT-Open-Reports/pull/189)
+ doc4test ruyisdk/doc4test commit [1732ac2](https://github.com/ruyisdk/doc4test/commit/1732ac2fc6dbc8cac14508efcc249ad2ddb256c8) [4eba815](https://github.com/ruyisdk/doc4test/commit/4eba8152f1789fae158189ad45fafed447acba10) [fc4034a](https://github.com/ruyisdk/doc4test/commit/fc4034a8c9b4cd68c44ef970b465a8a9418c1b69) [cbbb8b5](https://github.com/ruyisdk/doc4test/commit/cbbb8b5bfb137390f501c416c687cee36beada0e) [953705a](https://github.com/ruyisdk/doc4test/commit/953705ae245e6f9145c70255837550cd3ba43a9f) [2e8d4ed](https://github.com/ruyisdk/doc4test/commit/2e8d4edec327ee1649b3996bb543a9c72d68a856) [4674209](https://github.com/ruyisdk/doc4test/commit/46742091576b08de50ea314135e462cf8f03c40a) [069f146](https://github.com/ruyisdk/doc4test/commit/069f1462000522cad68e197b4cc6e67d20aad7d9) [cc49c14](https://github.com/ruyisdk/doc4test/commit/cc49c14ca223adcb7151a659756640b4d1285ad4) [149ecb3](https://github.com/ruyisdk/doc4test/commit/149ecb3aeae762cae61d2e0c94695af8cbb891cf) [5da5b22](https://github.com/ruyisdk/doc4test/commit/5da5b226c04475361e8e9245782f2c87e3d7ee10) [f49f401](https://github.com/ruyisdk/doc4test/commit/f49f401eba0245998cba385f3a9fe26d1cb86e46) [65213aa](https://github.com/ruyisdk/doc4test/commit/65213aab7af648141945ae09c6fab80e7310fdea) [492cf90](https://github.com/ruyisdk/doc4test/commit/492cf901e2e507702ac353b9aaf238ce1de81b63) [951748f](https://github.com/ruyisdk/doc4test/commit/951748fd7e89251de5e9a8c32f3174e914a1dbc4) [5d4a84b](https://github.com/ruyisdk/doc4test/commit/5d4a84b91d180ac29ea1291260e6ba0a62b975a3)
+ mugen-ruyi 仓库 weilinfox/mugen-ruyi commit [df3d0de](https://gitee.com/weilinfox/mugen-ruyi/commit/df3d0de4170b3369efc34613205be72c81a9b61e) [fdb5099](https://gitee.com/weilinfox/mugen-ruyi/commit/fdb509990493928b43c98ffc2efdae59fc9f5c7c) [8ec98c5](https://gitee.com/weilinfox/mugen-ruyi/commit/8ec98c5df276942f94b6baf2391843f315dd3e83) [e106801](https://gitee.com/weilinfox/mugen-ruyi/commit/e106801de909e9a4aa34afa909a8752fafb1accb) [be0f778](https://gitee.com/weilinfox/mugen-ruyi/commit/be0f778dc7cd282de4e7331b6549e684fcc08197) [c2bedfe](https://gitee.com/weilinfox/mugen-ruyi/commit/c2bedfe9b8633b24d49c48df4e128cf5192eb35a) [0c90a06](https://gitee.com/weilinfox/mugen-ruyi/commit/0c90a06949012765736b2c3dab9c4b10dd1086e4) [5c630d9](https://gitee.com/weilinfox/mugen-ruyi/commit/5c630d9959d6c19800c2790646fe120b36c083fb) [77b61ee](https://gitee.com/weilinfox/mugen-ruyi/commit/77b61ee577f5a3f44154bca7c504f2f437f05436) [7488e4a](https://gitee.com/weilinfox/mugen-ruyi/commit/7488e4ab9779985be39219327af802dcbe335a79) [9a9c7ce](https://gitee.com/weilinfox/mugen-ruyi/commit/9a9c7cecee3be44a9a0f12e64213f4186aa9bd89) [bfd43b4](https://gitee.com/weilinfox/mugen-ruyi/commit/bfd43b424a3523acbe7f41503d546d5305ad02fd) [d705246](https://gitee.com/weilinfox/mugen-ruyi/commit/d7052462b664223ddfbfa57aba4d0c57029ec48c) [509f2bd](https://gitee.com/weilinfox/mugen-ruyi/commit/509f2bd24cf0c8ef6b6d196558932b20eb4a4744) [e431f97](https://gitee.com/weilinfox/mugen-ruyi/commit/e431f975a5e06d5e6c46c1cf5b1fce0c9a526722) [cd5dc4c](https://gitee.com/weilinfox/mugen-ruyi/commit/cd5dc4cf654f1b9b9a7edaea580b1e3036501a49) [e8608bd](https://gitee.com/weilinfox/mugen-ruyi/commit/e8608bdf0ea7aa7e5c11e468680ad75cbfa228e1) [1fab2b8](https://gitee.com/weilinfox/mugen-ruyi/commit/1fab2b85a76227d3d8581cdaf80214307136afd7) [9ef109b](https://gitee.com/weilinfox/mugen-ruyi/commit/9ef109be9fbdc3d880e6dc016850a0bf56f1c92f) [5e4a7b9](https://gitee.com/weilinfox/mugen-ruyi/commit/5e4a7b9eb684f79fb6cdfe5aa4d2c8c85f111ba5) [9ace185](https://gitee.com/weilinfox/mugen-ruyi/commit/9ace18596eb5a968f17362be6be7655582d54205) [46d495f](https://gitee.com/weilinfox/mugen-ruyi/commit/46d495fc2790e0b5ac36d36f6ed49c434b351f16) [4e84d57](https://gitee.com/weilinfox/mugen-ruyi/commit/4e84d57efe1f168c80c1679b05123f6453d2a987) [4ab8eae](https://gitee.com/weilinfox/mugen-ruyi/commit/4ab8eaebbc8a5409c3723fc3c7fd7214f775146c) [16147f4](https://gitee.com/weilinfox/mugen-ruyi/commit/16147f4a5e1b142d8023b3ea9f837d583bb1de6e) [8d36c3a](https://gitee.com/weilinfox/mugen-ruyi/commit/8d36c3af10700c560023309852e32523ad3e99c4) [fb594e7](https://gitee.com/weilinfox/mugen-ruyi/commit/fb594e76fe72feb192881c905101de674a44d705)
+ mugen-riscv 个人仓 weilinfox/mugen-riscv commit [b905d48](https://github.com/weilinfox/mugen-riscv/commit/b905d48c5e283edd43d69d95ffec7d94b448c637) [b2b34df](https://github.com/weilinfox/mugen-riscv/commit/b2b34df66e089c5403327c1bda0ec4b57487c90b) [7ae0a95](https://github.com/weilinfox/mugen-riscv/commit/7ae0a95d2c80d6faa41870f95b1ca30ee139d272) [d05db0a](https://github.com/weilinfox/mugen-riscv/commit/d05db0ac4bbe21d4542256e1a1730441301c390e) [7c2ab54](https://github.com/weilinfox/mugen-riscv/commit/7c2ab54479d655dd2d96bf90490230b5b1c6913a) [b55bcc0](https://github.com/weilinfox/mugen-riscv/commit/b55bcc0eb1211505e526e0ba8bcb4bc0b10958fa) [1c3f40f](https://github.com/weilinfox/mugen-riscv/commit/1c3f40ff027abf2799a7564554f7d4f5fc54d393) [cd77e7b](https://github.com/weilinfox/mugen-riscv/commit/cd77e7bd875eeda7199816d8c7c83d2a7d9c4e1a) [05fc5a1](https://github.com/weilinfox/mugen-riscv/commit/05fc5a1b8a6453a5541b70bf1e6b5b038162de74) [236b8f3](https://github.com/weilinfox/mugen-riscv/commit/236b8f3eb7515d22eb707e1b3f40c6da619d4b32)
