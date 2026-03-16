# Month 24 Week 2 工作报告 25/06/09-25/06/13

## RuyiSDK

+ ruyisdk-website 合作 1 个 pr
    + [New data load mechenism, better UI, and improved NewsShowcase #144](https://github.com/ruyisdk/ruyisdk-website/pull/144)
+ ruyisdk-website 提交 1 个 pr
    + [pages: update homepage news with AsiaLLVM 2025 #147](https://github.com/ruyisdk/ruyisdk-website/pull/147)
+ ruyisdk-website 提出 2 个 issue
    + [博客双周报的合并 #145](https://github.com/ruyisdk/ruyisdk-website/issues/145)（未分配）
    + [社区板块的更新 #146](https://github.com/ruyisdk/ruyisdk-website/issues/146)（已分配实习生任务）
+ ruyi-litester 测试套件更新
    + [0.35.0: fix ruyi-basic/ruyi-admin test](https://github.com/weilinfox/ruyi-litester/commit/0374f3e721208c3f0d72cbc3178d3a2e3af396be)
    + [0.35.0: fix ruyi-basic/ruyi-install test](https://github.com/weilinfox/ruyi-litester/commit/679847d82dcd008b3a3d3d746502bd9b011ebdde)
    + [0.35.0: fix ruyi-basic/ruyi-list test](https://github.com/weilinfox/ruyi-litester/commit/755f149a44b8238047b9cbbfe31eba50ca9c0ef8)
+ Ruyi v0.25.0 测试新增 Fedora 41 RISC-V 测试
    + [Add fedora41 riscv64 report](https://github.com/weilinfox/ruyi-litester-reports/commit/ee60f206ff65dc704a8737a387b1abe82053c7b1)

### metadata 的定位问题，整个更新流程怎么走（RuyiSDK 周会已决策）

```
upstream ->  support matrix
         \          ↓
          -> packages index
```

1. manifests 中有 level 字段记录 support matrix 是否已经验证
2. packages index 可以向上游对齐，同时 support matrix 测试完以后更新 level 字段，这是异步的
3. 机读 metadata 可以单开仓库，同时运行上游检查的 bot
4. https://github.com/ruyisdk/ruyi-packaging/issues/17

