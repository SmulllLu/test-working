# 其他相关微信沟通

新工具链配置有问题，关联 commit [fbc6cea4](https://github.com/ruyisdk/packages-index/commit/fbc6cea4e5e8705710d30aef8f84f51bc9c5119c) [ebfcce4f](https://github.com/ruyisdk/packages-index/commit/ebfcce4f0de4a7207dff2cc836ea2640021888b1)

+ me: @xen0n manifests/toolchain/gnu-plct-rv64ilp32-elf/0.20240906.0-ruyi.20240906+git.df9313313b45.toml 这个 toml 多了一个逗号
+ me: github.com/ruyisdk/packages-index/tree/main/manifests/toolchain/gnu-plct-rv64ilp32-elf/0.20240906.0-ruyi.20240906+git.df9313313b45.toml 这个
+ xen0n: fixed
+ me: 第五行那个 vendor 后面还有一个 冒号 要改等号来着
+ xen0n: fixed

Duo 相关工具链 profile 问题，关联 issue [#197](https://github.com/ruyisdk/ruyi/issues/197)

+ me: 我这边试了一下都能正常用，针对 milkv-duo 的话，不知道还需不需要做一个 profile 加上 -march=rv64gcv0p7xthead
+ （省略）沟通认为需要

