# Month 7 Week 3 工作报告 24/01/14-24/01/21

## RUYISDK

+ 增加 mugen 测试用例
   |      用例名      | 变更                             |
   |:----------------:|:-------------------------------- |
   |   oe_test_ruyi   | 增加 ~/.local/state 目录测试     |
   | oe_test_ruyi_xdg | 增加 $XDG_STATE_DIR 环境变量测试 |
   |   oe_test_news   | 新增用例， news 命令测试         |
   |  oe_test_device  | 新增用例， device 命令测试       |
+ RUYI 包管理 v0.3 测试，提交 x86_64 Fedora 38 、 x86_64 Ubuntu 22.04 LTS 、 x86_64 openEuler 23.09 、 riscv64 Container RevyOS 20231210 、 riscv64 openEuler 23.09 五个环境的测试结果
   |            pr 标题             |                         pr 链接                          |
   |:------------------------------:|:--------------------------------------------------------:|
   | 添加 ruyi-mugen 测试日志和报告 | [!2](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/2) |
   |     添加自动化测试相关视频     | [!5](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/5) |
+ RUYI 包管理 mugen 测试失败用例提交 issue
   |                          issue 标题                           |                    issue 链接                    |
   |:-------------------------------------------------------------:|:------------------------------------------------:|
   | 20240116 版本 self uninstall --purge 没有删除 state/ruyi 目录 | [#45](https://github.com/ruyisdk/ruyi/issues/45) |
+ RUYI 包管理文档添加，更新 ruyisdk/docs 仓库和 ruyisdk/doc4test 仓库
   |              pr 标题               |                     pr 链接                      |
   |:----------------------------------:|:------------------------------------------------:|
   |  Add new feature for v0.3 release  |  [#31](https://github.com/ruyisdk/docs/pull/31)  |
   
   |              commit 标题              |                                          commit 链接                                           |
   |:-------------------------------------:|:----------------------------------------------------------------------------------------------:|
   |       Add 20240116 new feature        |   [c443cf7](https://github.com/ruyisdk/docs/commit/c443cf7fe3b8551865ccf48a929950c5611b3ed2)   |
   | Add 20240116 page to vitepress config |   [b3da86d](https://github.com/ruyisdk/docs/commit/b3da86db9a689f570d5e483ea6d1cc1eda601fc8)   |
   |             Add v0.3 note             |   [26ec191](https://github.com/ruyisdk/docs/commit/26ec19107226c7bacf9912eb18382fa53f4d3382)   |
   |        Add github release note        |   [1c0311b](https://github.com/ruyisdk/docs/commit/1c0311bd37b0ebec41e1cce71702adda059e04dc)   |
   |      Add 20240116's new feature       | [2776153](https://github.com/ruyisdk/doc4test/commit/27761535219d2fb2ad69b9e91e77d5f28248f633) |
   |             Add sudo note             | [64dc1ac](https://github.com/ruyisdk/doc4test/commit/64dc1ac8828edee995458510be0dc77c2ebbde94) |
+ Jenkins CI 测试环境调整网络架构（详见下）

## Jenkins CI 架构调整

17 日开始 GitHub 无法裸连，需要添加一个旁路网关。由于测试 QEMU Agent 搭建在容器中，则需要一个新容器搭建网关。实体测试机则在同网段添加实体网关。

另外远程测试机使用 TCP 模式也出现无法稳定连接 Jenkins CI 的情况，已经改用 webSocket 。

```
                                           +---------+
+-------------------+                   +--| browser |
| main server       |      Hongkong     |  +---------+
|    +------------+ |   +------------+  |  +--------+
|  +-| Jenkins CI ======= web server |<-+->| github |
|  | +------------+ |   +------------+  |  +--------+
|  |    +---------+ |                   |  +------------------------+
|  +----+ Agent 0 | |                   |  |   +------------------+ |
|  |    +---------+ |                   |  | +-+ External Agent 1 | |
|  |    +---------+ |                   |  | | +------------------+ |
|  +----+ Agent 1 | |                   |  | | +------------------+ |
|  |    +---------+ |                   |  | +-+ External Agent 2 | |
| ...       ...     |                   +--+ | +------------------+ |
|  |    +---------+ |                      |...        ...          |
|  +----+ Agent N | |                      | | +------------------+ |
|  |    +---------+ |                      | +-+ External Agent N | |
|  |    +---------+ |                      | | +------------------+ |
|  +----+ Gateway | |                      | | +---------+          |
|       +---------+ |                      | +-+ Gateway |          |
+-------------------+                      |   +---------+          |
                                           +------------------------+
```

