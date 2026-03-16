# Month 7 工作报告 24/01/01-24/01/31

## RuyiSDK

+ 完成调研任务《基于 Eclipse 以任一个 demo 走通 RUST RISC-V 交叉编译和运行过程》，产出调研文档《Eclipse Rust 交叉编译环境的配置和简单调试的实现》 [任务页面](https://github.com/ruyisdk/pmd/issues/6) [文档](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/eclipse-riscv/rust.md)
+ 提交 Eclipse Rust 调研报告
   |              commit 标题              |                                          commit 链接                                           |
   |:-------------------------------------:|:----------------------------------------------------------------------------------------------:|
   |       Add rust on eclipse investigation        |   [898c108](https://github.com/ruyisdk/pmd/commit/898c108e91aa432993039487d5a20594930cb6a7)   |
+ 完成 SOC 系统集成调研条目 18 条，关联 GD32VF 系列、 CH32V 系列、 ESP32-C3 系列、INTEL Nios V 系列和 Renode 模拟器，产出调研文档 [mcu\_invest.md](https://gitlab.inuyasha.love/weilinfox/plct-working/-/tree/master/Note/ruyisdk/MCU/mcu_invest.md)
+ mugen-ruyi 测试仓库从 Gitee 迁移到 GitHub [ruyi-mugen](https://github.com/weilinfox/ruyi-mugen) ，同时清除上游无用测试套及其历史，缩减仓库体积。 Jenkins CI 在已有环境的基础上做 ruyi-mugen 仓库的 GitHub 集成。
+ ruyi-mugen 增加测试用例
   |      用例名         | 变更                               |
   |:-------------------:|:---------------------------------- |
   |   [ruyi\_test\_common](https://github.com/weilinfox/ruyi-mugen/blob/ruyisdk/testcases/cli-test/ruyi/ruyi_test_common.sh)    | 增加 ~/.local/state 目录测试       |
   | [ruyi\_test\_xdg](https://github.com/weilinfox/ruyi-mugen/blob/ruyisdk/testcases/cli-test/ruyi/ruyi_test_xdg.sh) | 增加 $XDG\_STATE\_DIR 环境变量测试 |
   |   [ruyi\_test\_news](https://github.com/weilinfox/ruyi-mugen/blob/ruyisdk/testcases/cli-test/ruyi/ruyi_test_news.sh)    | 新增用例， news 命令测试           |
   |  [ruyi\_test\_device](https://github.com/weilinfox/ruyi-mugen/blob/ruyisdk/testcases/cli-test/ruyi/ruyi_test_device/ruyi_test_device.sh)   | 新增用例， device 命令测试         |
+ ruyi-mugen 测试用例 ruyi\_test\_device 更新
   |                       commit 标题                       |                                            commit 链接                                             |
   |:-------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|
   |                   Update Jenkinsfile                    | [ea9e2c5](https://github.com/weilinfox/ruyi-mugen/commit/ea9e2c5e361485c4ad797f1743102289e133e025) |
   |                   Run test with sudo                    | [33d3bfa](https://github.com/weilinfox/ruyi-mugen/commit/33d3bfa9d0a83aabe035d536230ff58b5662c0e3) |
   |               Run dep\_install with sudo                | [8e32995](https://github.com/weilinfox/ruyi-mugen/commit/8e329950ed79d72796ba54ec41ca28ff7cd98f8b) |
   |             Delete huawei oErv 2309 support             | [829051f](https://github.com/weilinfox/ruyi-mugen/commit/829051f7edb239258fa9480a1f620a2487f7de75) |
   |                     chown log files                     | [b0d2de4](https://github.com/weilinfox/ruyi-mugen/commit/b0d2de43c9a8c2b680e96e9fa378710b1c2ef658) |
   |                      Update README                      | [842871d](https://github.com/weilinfox/ruyi-mugen/commit/842871df694d4986bdab297dff06af57022c3a3c) |
   | Update oe\_test\_ruyi\_cmake\_ninja execute time to 60m | [0a3d6e1](https://github.com/weilinfox/ruyi-mugen/commit/0a3d6e1c4b2267bdc7f53b5e897e1927adf5c7be) |
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
+ RUYI 包管理 v0.3 测试，提交 x86\_64 Fedora 38 、 x86\_64 Ubuntu 22.04 LTS 、 x86\_64 openEuler 23.09 、 riscv64 Container RevyOS 20231210 、 riscv64 openEuler 23.09 五个环境的测试结果
   |            pr 标题             |                         pr 链接                          |
   |:------------------------------:|:--------------------------------------------------------:|
   | 添加 ruyi-mugen 测试日志和报告 | [!2](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/2) |
   |     添加自动化测试相关视频     | [!5](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/5) |
+ RUYI 包管理 mugen 测试失败用例提交 issue
   |                          issue 标题                           |                    issue 链接                    |
   |:-------------------------------------------------------------:|:------------------------------------------------:|
   | 20240116 版本 self uninstall --purge 没有删除 state/ruyi 目录 | [#45](https://github.com/ruyisdk/ruyi/issues/45) |
   | 镜像下载是否需要支持断点续传                                  | [#64](https://github.com/ruyisdk/ruyi/issues/64) |
+ RUYI 包管理文档添加，更新 ruyisdk/docs 仓库和 ruyisdk/doc4test 仓库
   |              pr 标题               |                     pr 链接                      |
   |:----------------------------------:|:------------------------------------------------:|
   |  Add new feature for v0.3 release  |  [#31](https://github.com/ruyisdk/docs/pull/31)  |
   
   |              commit 标题              |                                          commit 链接                                           |
   |:-------------------------------------:|:----------------------------------------------------------------------------------------------:|
   |       Add 20240116 new feature        |   [c443cf7](https://github.com/ruyisdk/docs/commit/c443cf7fe3b8551865ccf48a929950c5611b3ed2)   |
   | Add 20240116 page to vitepress config |   [b3da86d](https://github.com/ruyisdk/docs/commit/b3da86db9a689f570d5e483ea6d1cc1eda601fc8)   |
   |             Add v0.3 note             |   [26ec191](https://github.com/ruyisdk/docs/commit/26ec19107226c7bacf9912eb18382fa53f4d3382)   |
   |        Add github release note        |   [1c0311b](https://github.com/ruyisdk/docs/commit/1c0311bd37b0ebec41e1cce71702adda059e04dc)   |
   |      Add 20240116's new feature       | [2776153](https://github.com/ruyisdk/doc4test/commit/27761535219d2fb2ad69b9e91e77d5f28248f633) |
   |             Add sudo note             | [64dc1ac](https://github.com/ruyisdk/doc4test/commit/64dc1ac8828edee995458510be0dc77c2ebbde94) |

## 技术分享

+ 1 月 24 日周三做技术分享《基于 Eclipse 介绍 Rust 在 IDE 上的交叉编译和调试》，[提纲](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/eclipse-riscv/eclipse-rust/eclipse-rust.md)和 [PPT](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/eclipse-riscv/eclipse-rust/%E5%9F%BA%E4%BA%8E_Eclipse_%E4%BB%8B%E7%BB%8D_Rust_%E5%9C%A8_IDE_%E4%B8%8A%E7%9A%84%E4%BA%A4%E5%8F%89%E7%BC%96%E8%AF%91%E5%92%8C%E8%B0%83%E8%AF%95.pptx)

## Jenkins CI 架构调整

17 日开始 GitHub 无法裸连，需要添加一个旁路网关。由于测试 QEMU Agent 搭建在容器中，则需要一个新容器搭建网关。实体测试机则在同网段添加实体网关。

另外远程测试机使用 TCP 模式也出现无法稳定连接 Jenkins CI 的情况，故将主页转移到境内。

```
                                           +---------+
+-------------------+                   +--| browser |
| main server       |      GuangZhou    |  +---------+
|    +------------+ |   +------------+  |  +--------+
|  +-| Jenkins CI ======= web server |<-+->| github |
|  | +------------+ |   +------------+  |  +--------+
|  |    +---------+ |                   |  +------------------------+
|  +----+ Agent 0 | |                   |  |   +------------------+ |
|  |    +---------+ |                   |  | +-+ External Agent 1 | |
|  |    +---------+ |                   |  | | +------------------+ |
|  +----+ Agent 1 | |                   |  | | +------------------+ |
|  |    +---------+ |                   |  | +-+ External Agent 2 | |
| ...       ...     |                   +--+ | +------------------+ |
|  |    +---------+ |                      |...        ...          |
|  +----+ Agent N | |                      | | +------------------+ |
|  |    +---------+ |                      | +-+ External Agent N | |
|  |    +---------+ |                      | | +------------------+ |
|  +----+ Gateway | |                      | | +---------+          |
|       +---------+ |                      | +-+ Gateway |          |
+-------------------+                      |   +---------+          |
                                           +------------------------+
```

## oErv

### mugen issue

|                         issue 链接                         | issue 标题                                                                                                                        |
|:----------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------- |
| [I8T734](https://gitee.com/openeuler/mugen/issues/I8T734)  | smoke-basic-os 测试套 oe\_test\_CPUinfo\_001 用例在 openEuler 2309 RISC-V 测试失败                                                |
| [I8T7KM](https://gitee.com/openeuler/mugen/issues/I8T7KM)  | smoke-basic-os 测试套 oe\_test\_skopeo 用例在 openEuler 2309 RISC-V 测试失败                                                      |
| [I8TABT](https://gitee.com/openeuler/mugen/issues/I8TABT)  | libreswan 测试套 oe\_test\_libreswan\_ipsec\_setup 和 oe\_test\_libreswan\_ipsec\_systemctl 用例在 openEuler 2309 RISC-V 测试失败 |
| [I8T97I](https://gitee.com/openeuler/RISC-V/issues/I8T97I) | 2309 版本 mugen 测试 vdo 测试套部分用例超时                                                                                       |
| [I8TIK4](https://gitee.com/openeuler/mugen/issues/I8TIK4)  | smoke-basic-os 测试套 oe\_test\_MEMinfo\_001 用例在 openEuler 2309 RISC-V 测试失败                                                |
| [I8TLYZ](https://gitee.com/openeuler/RISC-V/issues/I8TLYZ) | smoke-basic-os 测试套 oe\_test\_perf\_top\_01 用例在 openEuler 2309 RISC-V QEMU 环境测试失败                                      |
| [I8TM3K](https://gitee.com/openeuler/RISC-V/issues/I8TM3K) | smoke-basic-os 测试套 oe\_test\_yumgroup\_001 用例在 openEuler 2309 RISC-V 测试失败                                               |
| [I8TMKQ](https://gitee.com/openeuler/mugen/issues/I8TMKQ)  | iSulad 测试套部分用例使用的 docker 镜像只支持 x86\_64 和 aarch64 架构                                                             |
| [I8TMQ8](https://gitee.com/openeuler/RISC-V/issues/I8TMQ8) | iSulad 测试套部分用例在 openEuler 2309 RISC-V 测试失败                                                                            |
| [I8TNLH](https://gitee.com/openeuler/RISC-V/issues/I8TNLH) | audit 测试套部分用例在 openEuler 2309 RISC-V 异常超时                                                                             |
| [I8TNQ4](https://gitee.com/openeuler/mugen/issues/I8TNQ4)  | kernel 测试套 oe\_test\_kernel\_cmd\_01 用例在 openEuler 2309 测试失败                                                            |
| [I8TO6D](https://gitee.com/openeuler/RISC-V/issues/I8TO6D) | kernel 测试套 oe\_test\_hinic 用例在 openEuler 2309 RISC-V 测试失败                                                               |
| [I8TO66](https://gitee.com/openeuler/mugen/issues/I8TO66)  | kernel 测试套 oe\_test\_hinic 用例期望的内核模块名与实际不符                                                                      |
| [I8TPY5](https://gitee.com/openeuler/mugen/issues/I8TPY5)  | kernel 测试套 oe\_test\_nbd 用例在 openEuler 2309 有概率测试失败                                                                  |

### mugen pr

|                       pr 链接                        | pr 标题                                                                                                  |
|:----------------------------------------------------:|:-------------------------------------------------------------------------------------------------------- |
| [2313](https://gitee.com/openeuler/mugen/pulls/2313) | smoke-basic-os: oe\_test\_CPUinfo\_001 failed on riscv64                                                 |
| [2314](https://gitee.com/openeuler/mugen/pulls/2314) | smoke-basic-os: oe\_test\_skopeo failed on riscv64                                                       |
| [2319](https://gitee.com/openeuler/mugen/pulls/2319) | libreswan: oe\_test\_libreswan\_ipsec\_systemctl and oe\_test\_libreswan\_ipsec\_setup failed on riscv64 |
| [2325](https://gitee.com/openeuler/mugen/pulls/2325) | smoke-basic-os: oe\_test\_MEMinfo\_001 failed on riscv64                                                 |
| [2330](https://gitee.com/openeuler/mugen/pulls/2330) | kernel: oe\_test\_nbd add sleep time                                                                     |
| [2331](https://gitee.com/openeuler/mugen/pulls/2331) | kernel: oe\_test\_kernel\_cmd\_01 test failed on openEuler 2309                                          |

## mugen docs

1. mugen 测试详细文档 《 mugen 原理和扩展应用》 [文档](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/mugen-last/mugen-last.md)

