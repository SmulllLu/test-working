# 09/05 RuyiSDK 周会代主持

会议纪要已经发给席老师

+ ruyi 本周发了 0.40.0-beta.20250902 版本，仓库 CI 整合了 python 3.10 到 python 3.13 的集成测试，测试通过再发版。后续打算加入对 whl 包和单文件二进制的集成测试
+ ruyi 0.40.0-beta.20250902 测试暂时没有发现更多问题，罗列了各个相关仓库的已知问题，新的测试报告将加入详细的已知问题信息
+ ruyi 新的云服务器上搭建的测试 CI 后续打算将 x86_64 的测试更多使用 GitHub Workflow 拉取 docker 镜像解决，不能解决的使用云服务器搭建
+ ruyisdk-website 本周改了很多细节展示的问题；文档页面的代码块改进扩展到 en 页面灰度测试，中文页面后续推进；数据统计页面正在暗色改亮色，配色后续还会改几版； news 页面合并了第一版，等待后续更多的 PR
+ packages-index 补全了 debian-fishwaldo-sg200x-sipeed-licheervnano 旧版本，加入了 revyos-milkv-pioneer 新版本 20250901，修复了 1 个 bug， CI 加入了对整体数据结构的测试
+ ruyi-backend API 加入了 downloads_by_categories_v1 字段，添加 IDE 分 GitHub 和镜像下载量以及 Ruyi 包管理器的 PyPI 下载量。后续官网需要更新相关页面展示
+ support-matrix 更新了 MilkV DuoS 的 Archlinux 测试报告
+ ruyisdk-website 当前的 Community 页面可以细分为“贡献者”、“社区共建计划”和“贡献者公约”（已有）三个页面，“贡献者”页面可以参考 moonbit 官网类似页面。具体内容填充等待后续讨论
+ 会议还讨论了 GNU 相关的验收测试事项

## 下面是测试报告预计会添加的内容

测试报告发布时间，按照之前周会的约定，测试时间一周。发版时间为 09/02 下班以后，故测试报告发布时间最早为 09/10 上班时间。由于本版本改动较小，可以在 09/09 上班时间发布。

## 0.40.0-beta.20250902 测试的初步结论

从 0.40.0 版本开始，发版流程改为先提交测试报告后发版，故从这个版本开始，测试报告公开发版相关的提示信息。

### 文档测试

遗留 4 个缺陷

+ [文档代码块格式不统一 #93](https://github.com/ruyisdk/docs/issues/93)
+ [链接中的 RuyiSDK 大小写问题 #94](https://github.com/ruyisdk/docs/issues/94)
+ [关于 fastboot 的文档提示 #95](https://github.com/ruyisdk/docs/issues/95)
+ [关于使用 pip 安装 ruyi 的文档提示 #96](https://github.com/ruyisdk/docs/issues/96)

回归测试未通过，故本版本不执行回归测试之后的测试流程。

### packages-index 测试

本版本测试开始前发现并修复 1 个问题，提交 2 个修复 pr

+ [board-image/debian-desktop-sdk-milkv-mars-cm-sd: fix 1.0.5+3.6.1 manifest #105](https://github.com/ruyisdk/packages-index/pull/105)
+ [workflows: test manifests data structure with ruyi list #108](https://github.com/ruyisdk/packages-index/pull/108)

遗留缺陷：

+ [有一部分包无法下载 #37](https://github.com/ruyisdk/packages-index/issues/37)
+ [BananaPi BPI-F3 eMMC storage variant did not refer to any combo #101](https://github.com/ruyisdk/packages-index/issues/101)
+ [Jupiter and Megrez missing for MilkV product line support #104](https://github.com/ruyisdk/packages-index/issues/104)

回归测试未通过，故本版本不执行回归测试之后的测试流程。

### RuyiSDK IDE 测试

RuyiSDK Eclipse Plugins 0.0.5 版本遗留 issue 如下：

+ [未配置 PATH 导致无法轻松访问 ruyi #38](https://github.com/ruyisdk/ruyisdk-eclipse-plugins/issues/38)
+ [Ruyi 安装下载完成不够明显 #39](https://github.com/ruyisdk/ruyisdk-eclipse-plugins/issues/39)

回归测试未通过，故本版本不执行回归测试之后的测试流程。

### Ruyi 包管理器测试

#### ruyi-litester 系统测试

例行的 ruyi-litester 系统测试所发现的问题已经在 ruyisdk/packages-index#105 修复。

#### 新增特性测试

本版本新增特性如下：

1. 去掉了 ruyi version 输出中的版权年份信息

已经通过手动测试验证，该特性的测试不加入 ruyi-litester。

### 总结

包管理器本身功能，均已经通过了测试流程中所包含的测试。但需要关注文档、 packages-index 和 RuyiSDK IDE 遗留缺陷对 Ruyi 包管理器的实际用户体验产生的影响。

