# Month 10 Week 4 工作报告 24/04/23-24/04/26

## RuyiSDK

+ ruyi mugen 更新 pr [!12](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/12)
   | 主要功能更新                                  | 提交                                                                                               |
   | --------------------------------------------- | -------------------------------------------------------------------------------------------------- |
   | 测试 0.9.0 版本          | [dd33588](https://github.com/weilinfox/ruyi-mugen/commit/dd33588344abe819509c0e0f5f7cb0b4c2422656) |
   | 添加 RUYI 依赖 lz4                        | [695eec5](https://github.com/weilinfox/ruyi-mugen/commit/695eec5868ddc22abdc163bbd115662caa0a32d2) |
   | 中文环境下的 apt-get 输出匹配 | [3901023](https://github.com/weilinfox/ruyi-mugen/commit/3901023c80448da128d818244a77501e773cfa9d) |
+ 完成 openKylin x86\_64 和 riscv64 QEMU 测试环境测试。产出 riscv64 环境 RUYI 0.9.0 测试报告。
+ 完成 RUYI 包管理 0.9.0 mugen 自动化测试，产出 15 个平台的测试日志、报告以及解释视频 pr [!35](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/35)

## 自动化测试平台维护

1. Jenkins Worker 报错 [Failed to exec spawn helper](https://blog.csdn.net/Hsk_03/article/details/134399956)。由于问题原因不清晰，只能试图[解决](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Note/failed_to_exec_spawn_helper.md)，但是具体效果待观察。

