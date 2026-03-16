# Month 7 Week 1 工作报告 24/1/2-24/1/5

## mugen issue

|                         issue 链接                         | issue 标题                                                                                                                |
|:----------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------- |
| [I8T734](https://gitee.com/openeuler/mugen/issues/I8T734)  | smoke-basic-os 测试套 oe_test_CPUinfo_001 用例在 openEuler 2309 RISC-V 测试失败                                           |
| [I8T7KM](https://gitee.com/openeuler/mugen/issues/I8T7KM)  | smoke-basic-os 测试套 oe_test_skopeo 用例在 openEuler 2309 RISC-V 测试失败                                                |
| [I8TABT](https://gitee.com/openeuler/mugen/issues/I8TABT)  | libreswan 测试套 oe_test_libreswan_ipsec_setup 和 oe_test_libreswan_ipsec_systemctl 用例在 openEuler 2309 RISC-V 测试失败 |
| [I8T97I](https://gitee.com/openeuler/RISC-V/issues/I8T97I) | 2309 版本 mugen 测试 vdo 测试套部分用例超时                                                                               |
| [I8TIK4](https://gitee.com/openeuler/mugen/issues/I8TIK4)  | smoke-basic-os 测试套 oe_test_MEMinfo_001 用例在 openEuler 2309 RISC-V 测试失败                                           |
| [I8TLYZ](https://gitee.com/openeuler/RISC-V/issues/I8TLYZ) | smoke-basic-os 测试套 oe_test_perf_top_01 用例在 openEuler 2309 RISC-V QEMU 环境测试失败                                  |
| [I8TM3K](https://gitee.com/openeuler/RISC-V/issues/I8TM3K) | smoke-basic-os 测试套 oe_test_yumgroup_001 用例在 openEuler 2309 RISC-V 测试失败                                          |
| [I8TMKQ](https://gitee.com/openeuler/mugen/issues/I8TMKQ)  | iSulad 测试套部分用例使用的 docker 镜像只支持 x86_64 和 aarch64 架构                                                      |
| [I8TMQ8](https://gitee.com/openeuler/RISC-V/issues/I8TMQ8) | iSulad 测试套部分用例在 openEuler 2309 RISC-V 测试失败                                                                    |
| [I8TNLH](https://gitee.com/openeuler/RISC-V/issues/I8TNLH) | audit 测试套部分用例在 openEuler 2309 RISC-V 异常超时                                                                     |
| [I8TNQ4](https://gitee.com/openeuler/mugen/issues/I8TNQ4)  | kernel 测试套 oe_test_kernel_cmd_01 用例在 openEuler 2309 测试失败                                                        |
| [I8TO6D](https://gitee.com/openeuler/RISC-V/issues/I8TO6D) | kernel 测试套 oe_test_hinic 用例在 openEuler 2309 RISC-V 测试失败                                                         |
| [I8TO66](https://gitee.com/openeuler/mugen/issues/I8TO66)  | kernel 测试套 oe_test_hinic 用例期望的内核模块名与实际不符                                                                |
| [I8TPY5](https://gitee.com/openeuler/mugen/issues/I8TPY5)  | kernel 测试套 oe_test_nbd 用例在 openEuler 2309 有概率测试失败                                                            |

## mugen pr

|                       pr 链接                        | pr 标题                                                                                          |
|:----------------------------------------------------:|:------------------------------------------------------------------------------------------------ |
| [2313](https://gitee.com/openeuler/mugen/pulls/2313) | smoke-basic-os: oe_test_CPUinfo_001 failed on riscv64                                            |
| [2314](https://gitee.com/openeuler/mugen/pulls/2314) | smoke-basic-os: oe_test_skopeo failed on riscv64                                                 |
| [2319](https://gitee.com/openeuler/mugen/pulls/2319) | libreswan: oe_test_libreswan_ipsec_systemctl and oe_test_libreswan_ipsec_setup failed on riscv64 |
| [2325](https://gitee.com/openeuler/mugen/pulls/2325) | smoke-basic-os: oe_test_MEMinfo_001 failed on riscv64                                            |
| [2330](https://gitee.com/openeuler/mugen/pulls/2330) | kernel: oe_test_nbd add sleep time                                                               |
| [2331](https://gitee.com/openeuler/mugen/pulls/2331) | kernel: oe_test_kernel_cmd_01 test failed on openEuler 2309                                      |

## RUYI CI 接入方案

1. 总体架构：
   ```
                                              +---------+
   +-------------------+                   +--| browser |
   | main server       |  Hang Zhou Aliyun |  +---------+
   |    +------------+ |   +------------+  |  +--------+
   |  +-| Jenkins CI ======= web server |<-+->| github |
   |  | +------------+ |   +-----+------+     +--------+
   |  |    +---------+ |         |     +-----------+
   |  +----+ Agent 0 | |         +<--->+ Agent N+1 |
   |  |    +---------+ |         |     +-----------+
   |  |    +---------+ |         |     +-----------+
   |  +----+ Agent 1 | |         +<--->+ Agent N+2 |
   |  |    +---------+ |         |     +-----------+
   | ...       ...     |        ...        ...
   |  |    +---------+ |         |     +----------+
   |  +----+ Agent N | |         +<--->+ Agent 2N |
   |       +---------+ |               +----------+
   +-------------------+
   ```
2. 具体实施：在内网服务器上再搭建一个 Jenkins CI ，新开一个 Debian LXC 容器并配置必要的 ``/dev`` 节点； webhook 需要公网可访问，用国内云服务器做 Web 服务器。

