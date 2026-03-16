# Month 6 Week 1 工作报告 23/12/01-23/12/08

## RUYI 包管理测试

+ pre_round4 、 pre_round5 、 部分 round1 ，的测试报告。提交 pr [!5](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/5) [!7](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/7) [!11](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/11) [!12](https://gitee.com/yunxiangluo/ruyi-sdk-v0.2-test/pulls/12)
+ [mugen-ruyi](https://gitee.com/weilinfox/mugen-ruyi) 仓库的 mugen 用例更新，现有 8 个用例。由于 list 命令输出改变，特别是在 QEMU 终端环境本来应该在一行中的内容出现自动换行的情况下，处理难度加大
+ 内部文档仓库维护 [doc4test](https://github.com/ruyisdk/doc4test/blob/main/README.md)
+ 公开文档仓库的文档同步 pr [#21](https://github.com/ruyisdk/docs/pull/21)
+ 向 ruyi 仓库提出 issue ：
   |                    issue 链接                    |                      issue 标题                       |
   |:------------------------------------------------:|:-----------------------------------------------------:|
   | [#18](https://github.com/ruyisdk/ruyi/issues/18) |  在 RUYI 环境中使用绝对路径/相对路径调用工具链时失败  |
   | [#19](https://github.com/ruyisdk/ruyi/issues/19) | ruyi install slug:llvm-upstream-20231121 找不到软件包 |
   | [#21](https://github.com/ruyisdk/ruyi/issues/21) |         plct-xthead 工具链构建 C 程序无法运行         |
   | [#24](https://github.com/ruyisdk/ruyi/issues/24) |        gdb 依赖 libpython3.8.so.1.0 （未关闭）        |
+ 向 ruyi 仓库提出 pr ：
   |                   issue 链接                   |  issue 标题  |
   |:----------------------------------------------:|:------------:|
   | [#17](https://github.com/ruyisdk/ruyi/pull/17) | Fix spelling |

## mugen-ruyi 代办

+ 遍历组合
+ 遍历工具链
