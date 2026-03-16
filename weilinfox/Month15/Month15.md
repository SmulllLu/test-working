# Month 15 工作报告 24/09/02-24/09/29

## RuyiSDK

+ Ruyi 包管理器 v0.17.0 的自动化测试和报告 pr [!48](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/48)
+ 完成 0.18.0-alpha.20240909 和 0.18.0-beta.20240911 版本的测试，认为满足发版要求
+ 0.18.0 的 26 个平台的自动化测试完成 [pr](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/49)
+ Ruyi issue
  | issue 标题 | 链接 |
  | :--: | :--: |
  | ruyi 的 python-frontmatter 依赖问题 | [#191](https://github.com/ruyisdk/ruyi/issues/191) |
  | ruyi venv 多工具链支持 | [#119](https://github.com/ruyisdk/ruyi/issues/199) |
+ Ruyi 其他相关沟通 [doc](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month15/other.md)
+ 完成在 PPA 的 Ubuntu 22.04 打包，临时打包仓库 [ppa.launchpad.net/ruyi](https://launchpad.net/~weilinfox/+archive/ubuntu/ruyi)
+ 调研了 build.opensuse.org 打包支撑程度，认为不满足需求。临时打包仓库 [home:ruyi](https://build.opensuse.org/project/show/home:ruyi)
+ 调研了 build.tarsier-infra.isrc.ac.cn 打包支撑程度，认为不满足需求。临时打包仓库 [home:RuyiSDK](https://build.tarsier-infra.isrc.ac.cn/project/show/home:RuyiSDK)
+ 更新 Ruyi 打包方式，设计打包流程，计划还是使用 Jenkins CI 打包 [ruyi-packaging.md](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyi-packaging/ruyi-packaging.md)
+ Ruyi 包管理器进入 Arch Linux CN Community，支持 Arch Linux 和 Arch Linux ARM [python-xingque(arm)](https://github.com/archlinuxcn/repo/tree/master/alarmcn/python-xingque) [python-xingque](https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/python-xingque) [ruyi](https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/ruyi)
+ 完成 ruyi 的全架构打包，分为一般 python 打包方式和 Nuitka 二进制打包方式。分别维护在 [ruyi-builds](https://github.com/weilinfox/ruyi-builds) 和 [ruyi-bin-builds](https://github.com/weilinfox/ruyi-bin-builds) 中。
+ 山大服务器基于新的 RevyOS 评估认为环境稳定，建立新的 LXC 环境，开始测试机迁移
+ 完成 riscv64 架构测试机迁移共计 9 部
    + sdu0_debian-sid_0
    + sdu0_openEuler-24.03_0
    + sdu0_ubuntu-2404_0
    + sdu1_debian-sid_0
    + sdu1_fedora-38_0
    + sdu1_gentoo_openrc_0
    + sdu1_openEuler-23.09-V1-base-qemu-preview_0
    + sdu1_openkylin-1.0.1_0
    + sdu1_ubuntu-2204_0
