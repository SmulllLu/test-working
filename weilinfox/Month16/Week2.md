# Month 16 Week 1-2 工作报告 24/10/07-24/10/11

## RuyiSDK

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
+ 新测试用例 ruyi\_test\_milkv-duo [pr !22](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/22)
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
  + x86\_64 架构测试机迁移共计 10 部
    + iscas0\_archlinux\_0
    + iscas0\_debian-12\_0
    + iscas0\_fedora-38\_0
    + iscas0\_fedora-39\_0
    + iscas0\_gentoo\_openrc\_0
    + iscas0\_openEuler-23.09\_0
    + iscas0\_openEuler-24.03\_0
    + iscas0\_openkylin-1.0\_0
    + iscas0\_ubuntu-22.04\_0
    + iscas0\_ubuntu-24.04\_0

