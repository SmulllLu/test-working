# RuyiSDK 测试组周志 24/10/07-24/10/11

## v0.19.0 测试周

+ 完成 Ruyi 软件包的自动打包和上传，后续包从新的 ruyi-builds 仓库同步（**应当通过 Access Token**）
  + ruyi-nvchecker <https://github.com/weilinfox/ruyi-nvchecker> 版本监测
  + ruyi-build-source <https://gitlab.inuyasha.love/ruyisdk/ruyi-build-source> 打包脚本和自动打包
  + ruyi-builds <https://gitlab.inuyasha.love/ruyisdk/ruyi-builds> 自动推送到 GitLab 仓库
    + diff0: 添加默认的 /usr/share/ruyi/config.toml 配置
    + diff1: 更新到 v0.19.0
  + **关于自动打包**
    + 正常出包时间在版本发布两小时内
    + 如果测试发现问题会不定时提交新包， ISCAS 源应当定时同步
    + 新增依赖应当是发行版普遍打包的包，否则 Arch Linux CN 将可能无法打包
    + 新增依赖版本需要提前沟通，否则无法保证打包时效

  打包在 GitHub Action 的话需要在其他地方做源，打包脚本三部分 deb/oE_rpm/fc_rpm； Nuitka 二进制丢不掉吧，有支持范围的问题（不同发行版的依赖版本）
+ 新测试用例 ruyi_test_milkv-duo [pr !22](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/22)
  + 双工具链 venv
  + milkv-duo 相关的三个工具链可用性
+ 完成 0.19.0 测试 [pr !50](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/50)
+ 0.19.0 版本发现一个问题提出 3 个 issue
  | issue 标题                                                                      | issue 链接                                         |
  | ------------------------------------------------------------------------------- | -------------------------------------------------- |
  | ruyi admin 工具不能正常输出 distfile                                            | [#207](https://github.com/ruyisdk/ruyi/issues/207) |
  | llvm-upstream: clang: fatal error: no configured target found for command clang | [#209](https://github.com/ruyisdk/ruyi/issues/209) |
  | ruyi self uninstall --purge 删除 state 目录不完全                               | [#210](https://github.com/ruyisdk/ruyi/issues/210) |
+ 完成测试机迁移，一轮完整测试时间缩短至 1.5 天
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
  + x86_64 架构测试机迁移共计 10 部
    + iscas0_archlinux_0
    + iscas0_debian-12_0
    + iscas0_fedora-38_0
    + iscas0_fedora-39_0
    + iscas0_gentoo_openrc_0
    + iscas0_openEuler-23.09_0
    + iscas0_openEuler-24.03_0
    + iscas0_openkylin-1.0_0
    + iscas0_ubuntu-22.04_0
    + iscas0_ubuntu-24.04_0

## ruyi deb/rpm 自动构建逻辑

ruyi-nvchecker 监测 ruyi 的 GitHub 和 ISCAS mirror， ISCAS mirror 完成二进制的同步时，触发 ruyi-build-source 打包

ruyi-builds 扫描到 ruyi-build-source 的构建产物后自动更新 ruyi-builds 仓库。

## todo

+ ruyi-reimu 集成 ruyi-nvchecker 触发测试
+ 每日测试
  [ ] lit
  [ ] schroot
  [ ] gotify

