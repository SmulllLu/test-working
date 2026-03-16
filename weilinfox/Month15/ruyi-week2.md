# RuyiSDK 测试工作总结 24/09/09-24/09/13

## Ruyi 测试

保持 mugen 测试基本保持当前状态，只根据 Ruyi 特性更新。

研究设计基于 lit（LLVM Integrated Tester） 的 DDT 测试，提升测试覆盖率。

## Ruyi 打包

Arch Linux CN Community，预计从 v0.18.0 开始将 Ruyi 包管理器推入 Arch Linux CN 社区源，包名 ruyi。当前仅 x86\_64。

其他平台使用我的 Jenkins CI 构建，不再基于现有可达的公开构建平台。

即使使用四个平台（<https://build.opensuse.org/>， <https://build.tarsier-infra.isrc.ac.cn>， <https://launchpad.net/>， <https://eur.openeuler.openatom.cn/>）依然无法满足需求；每个平台依赖管理策略不一样导致巨大的维护成本； PPA 取包有限制不易自动化。

10 月 1 日前完成在 Gitee/Github 做源， x86\_64 和 riscv64 优先，未 EOF 发行版本优先。 aarch64 和 Fedora38 后续支持完善。

~~## Ruyi Mirror 上游版本动态监测（Blocked）~~

~~无更新。~~

~~监测逻辑已经完成，但是需要开发的协助才能完成完整流程。~~

~~## IDE 测试（Blocked）~~

~~无更新。~~

~~已经完成 openQA 构建，随时可以开展测试。~~

