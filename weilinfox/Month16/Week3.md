# Month 16 Week 3 工作报告 24/10/14-24/10/21

## RuyiSDK

+ 补充 ruyi 打包流程/基础设施共享文档
+ 设计编写了新的测试框架 ruyi-litester，框架设计参考文档 <https://github.com/weilinfox/ruyi-litester/blob/master/README_zh.md>。[92ef02b..6a9c57b](https://github.com/weilinfox/ruyi-litester/compare/92ef02b..6a9c57b) 共计 39 个 commit， 1191 行增加
+ ruyi-litester lit 测试套，迁移了大部分 mugen 测试用例
  + [ruyi-basic](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-basic)
     + ruyi-admin
     + ruyi-cmake
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
  + [ruyi-help](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-help)
     + ruyi-help
  + [ruyi-i18n](https://github.com/weilinfox/ruyi-litester/tree/master/testcases/ruyi-i18n)
     + 这部分主要是进行了模板设计
+ 0.20.0-beta.20241020  版本发现以下 issue 没有完全修复并重开
  | issue 标题                                 | issue 链接                                         |
  | ------------------------------------------------------------------------------- | -------------------------------------------------- |
  |  llvm-upstream: clang: fatal error: no configured target found for command clang | [#209](https://github.com/ruyisdk/ruyi/issues/209) |
