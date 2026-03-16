# Month 16 工作报告 24/10/07-24/10/31

## RuyiSDK

+ 完成 Ruyi 软件包的自动打包、上传和仓库合并
  + ruyi-nvchecker <https://github.com/weilinfox/ruyi-nvchecker> 版本监测
  + ruyi-build-source <https://gitlab.inuyasha.love/ruyisdk/ruyi-build-source> 打包脚本和自动打包
  + ruyi-builds <https://gitlab.inuyasha.love/ruyisdk/ruyi-builds> 自动推送到 GitLab 仓库
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
+ 补充 ruyi 打包流程/基础设施文档 [deb/rpm 打包部分](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyisdk/RuyiSDK%20DevSync-Linux%E6%89%93%E5%8C%85%E5%88%86%E5%8F%91%E5%8F%8A%E8%87%AA%E5%8A%A8%E5%8C%96%E7%8E%B0%E7%8A%B6%E5%8F%8A%E7%9B%AE%E6%A0%87.md)
+ 完成 RuyiSDK 官网基于 v0.19.0 的修正文档 [docx](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyisdk/RuyiSDK%20%E5%AE%98%E7%BD%91%E6%96%87%E6%A1%A3%E5%9F%BA%E4%BA%8E%20v0.19.0%20%E7%9A%84%E4%BF%AE%E6%AD%A3.docx)
+ ruyi-mugen 测试添加新测试用例 ruyi\_test\_milkv-duo [pr !22](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/22)
  + 双工具链 venv
  + milkv-duo 相关的三个工具链可用性
+ ruyi-mugen 测试添加 admin format-manifest 测试 pr [!23](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/23)
+ ruyi v0.19.0 测试完成 [pr !50](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/50)
+ ruyi v0.20.0 测试完成 pr [!51](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/51)
+ 0.19.0 版本发现一个问题提出 3 个 issue
  | issue 标题                                                                      | issue 链接                                         |
  | ------------------------------------------------------------------------------- | -------------------------------------------------- |
  | ruyi admin 工具不能正常输出 distfile                                            | [#207](https://github.com/ruyisdk/ruyi/issues/207) |
  | llvm-upstream: clang: fatal error: no configured target found for command clang | [#209](https://github.com/ruyisdk/ruyi/issues/209) |
  | ruyi self uninstall --purge 删除 state 目录不完全                               | [#210](https://github.com/ruyisdk/ruyi/issues/210) |
+ ruyi v0.20.0-beta.20241020 版本发现以下 issue 没有完全修复并重开
  | issue 标题                                 | issue 链接                                         |
  | ------------------------------------------------------------------------------- | -------------------------------------------------- |
  |  llvm-upstream: clang: fatal error: no configured target found for command clang | [#209](https://github.com/ruyisdk/ruyi/issues/209) |
+ ruyi v0.20.0 提出两个新增 issue
  | issue 标题                                          | issue 链接                                         |
  | --------------------------------------------------- | -------------------------------------------------- |
  | ruyi admin format-manifest 接受 json 文件但处理出错 | [#217](https://github.com/ruyisdk/ruyi/issues/217) |
  | ruyi self clean --telemetry 无法完全删除本地遥测信息    | [#218](https://github.com/ruyisdk/ruyi/issues/218) |
+ ruyi 主线分支 [d83e1a8](https://github.com/ruyisdk/ruyi/tree/d83e1a85816bbb5212f082239130aee4c2b27d5f) 提出一个 issue
  | issue 标题                                                 | issue 链接                                         |
  | ---------------------------------------------------------- | -------------------------------------------------- |
  | ruyi 新增依赖 typing_extensions 未出现在 pyproject.toml 中 | [#220](https://github.com/ruyisdk/ruyi/issues/220) |
+ 设计编写了新的测试框架 ruyi-litester，框架设计参考文档 [README_zh.md](https://github.com/weilinfox/ruyi-litester/blob/master/README_zh.md)。[92ef02b..9902939](https://github.com/weilinfox/ruyi-litester/compare/92ef02b..9902939) 共计 72 个 commit， 1485 行增加
+ 编写 ruyi-litester lit 测试套，迁移了除 ruyi_test_device、 ruyi_test_binaries、 ruyi_test_cmake 外的 mugen 测试用例，设计了 ruyi-help 和 ruyi-i18n 两个新的测试套
  + [ruyi-basic](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-basic)
     + ruyi-admin
     + ruyi-make
     + ruyi-extract
     + ruyi-install
     + ruyi-list
     + ruyi-llvm
     + ruyi-news
     + ruyi-qemu
     + ruyi-toolchain_gnu-milkv
     + ruyi-toolchain_gnu-plct-rv64ilp32-elf
     + ruyi-toolchain_gnu-plct-xthead
     + ruyi-toolchain_gnu-plct_xiangshan-nanhu
     + ruyi-venv
  + [ruyi-advance](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-advance)
    + ruyi-xdg
    + ruyi-config
  + [ruyi-help](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-help)
     + ruyi-help
  + [ruyi-i18n](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-i18n)
     + 这部分主要是进行了模板设计
+ 编写 ruyi-litester 与 ruyi 测试相关的环境配置脚本，上线 ruyi 仓库主线的每日测试 [配置脚本目录](https://github.com/weilinfox/ruyi-litester/tree/master/scripts/ruyi)
+ 10 月 30 日技术分享《用 lit 测试 ruyi 包管理器》 [Slide](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/ruyi-litester/ruyi-litester.odp)

