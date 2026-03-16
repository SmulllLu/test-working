# Month 13 工作报告 24/07/01-24/07/26

## RuyiSDK

+ ruyi mugen 更新 pr [!19](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/19) [#20](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/20)
   | 主要功能更新                   | 提交                                                                                               |
   | ------------------------------ | -------------------------------------------------------------------------------------------------- |
   | 测试 0.14.0-alpha.20240702 版本 | [9abf0c4](https://github.com/weilinfox/ruyi-mugen/commit/9abf0c462f8d88b49cb08c2c9c7f72f28807d1da) |
   | 测试 0.14.0-beta.20240707 版本 | [83d16b1](https://github.com/weilinfox/ruyi-mugen/commit/83d16b1c68a89cd7852079db2aa2d429b35fd550) |
   | 测试 0.14.0-beta.20240708 版本 | [292b1c4](https://github.com/weilinfox/ruyi-mugen/commit/292b1c483c9ad6229f397d8dd7e981aa7e5b994d) |
   | 测试 0.14.0 版本 | [d738b0c](https://github.com/weilinfox/ruyi-mugen/commit/d738b0c576707caf316c76d30c87776185ffbae5) |
   | 修复 config.toml 存在的情况下 ruyi\_test\_config 测试异常 | [9fd5e27](https://github.com/weilinfox/ruyi-mugen/commit/9fd5e27d27b35e8ac80324d3f1d56de2b84a1cfb) |
   | 测试 0.15.0-beta.20240721 版本 | [1b3bf26](https://github.com/weilinfox/ruyi-mugen/commit/1b3bf26cd77ec896c24f2063fdf562f4ce469543) |
   | 修复 README 中的测试状态图标 | [c5882d4](https://github.com/weilinfox/ruyi-mugen/commit/c5882d4a804d263396a52fa114ea03d0ae053d33) |
   | 测试 0.15.0 版本 | [0a0d234](https://github.com/weilinfox/ruyi-mugen/commit/0a0d234a307b0ae099f036dd3a4d08687fce98e8) |
+ 测试 0.14.0-beta.20240707 到 0.15.0 版本，发现问题并提交 issue
   | issue 标题                                                                           | issue 链接                                         |
   | ------------------------------------------------------------------------------------ | -------------------------------------------------- |
   | 0.14.0-beta.20240707 无法正常安装软件包 | [#170](https://github.com/ruyisdk/ruyi/issues/170) |
   | 非 en\_US 和 zh\_CN locale 下 ruyi install 提示文字输出异常 | [#173](https://github.com/ruyisdk/ruyi/issues/173) |
   | box64 WPS 表格和 WPS pdf 启动异常 | [#174](https://github.com/ruyisdk/ruyi/issues/174) |
   | BPI-F3 Bianbu 无法正常使用 box64 启动 WPS | [#176](https://github.com/ruyisdk/ruyi/issues/176) |
   | openEuler RISC-V 2309 独立发行版本需要额外操作以正常使用 box64 启动 WPS | [#177](https://github.com/ruyisdk/ruyi/issues/177) |
   | wps-office 上游新版本 11.1.0.11720 | [#178](https://github.com/ruyisdk/ruyi/issues/178) |
   | ruyi news 功能换行缺字 | [#181](https://github.com/ruyisdk/ruyi/issues/181) |
+ 完成 ruyi 0.14.0 版本在 24 个平台的 mugen 自动化测试并提交各平台日志报告和视频，完成 Box64 运行 WPS 办公套件在三个系统平台的测试并提交报告和截图 [!44](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/44) [!45](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/45)
+ 完成 ruyi 0.15.0 版本在 24 个平台的 mugen 自动化测试,以及新版本 Box64 和 WPS 办公套件的可用性验证，提交完整的测试报告和日志 pr [#46](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/46)
+ 验证并关闭了 ruyi issue [box64 WPS 表格和 WPS pdf 启动异常](https://github.com/ruyisdk/ruyi/issues/174)
+ 验证并回复了 ruyi issue [openEuler RISC-V 2309 独立发行版本需要额外操作以正常使用 box64 启动 WPS](https://github.com/ruyisdk/ruyi/issues/177) 和 [using "ruyi install" behind a proxy to internet faced a problem.shall we have a proxy configs such as -proxy.](https://github.com/ruyisdk/ruyi/issues/180)
+ 为 ruyisdk/packages-index 提交一个 news 修复 pr [#4](https://github.com/ruyisdk/packages-index/pull/4)
+ ruyi-reimu 更新，完成基本的 jenkins 测试调度功能，用于 0.14.0 和 0.15.0 版本测试
   [详细代码更新](https://github.com/weilinfox/ruyi-reimu/compare/4402038..a40d0c4)，共计 27 个 commit， 1069 行增加， 259 行删除。
+ [k230\_linux\_sdk](https://github.com/ruyisdk/k230_linux_sdk) 自动化构建调研，产出文档 [k230\_linux\_sdk\_build.md](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month13/k230_linux_sdk_build.md)

## 实习生相关

+ 审核并合并了 ruyi-mugen pr [#7](https://github.com/weilinfox/ruyi-mugen/pull/7)
+ 审核并合并了 ruyi-reimu pr [#24](https://github.com/weilinfox/ruyi-reimu/pull/24)
+ 审核实习生 7 月 27 日技术分享 ppt
+ 新实习生面试考核题 [P119\_cy.md](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month13/P119_cy.md) 和追加考核试题 [P119\_cy\_add.md](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month13/P119_cy_add.md)，面试实习生暂没有提交追加考核题解答

## 其他工作

+ 对 openkylin 2.0-RC 进行 autopkgtest 测试，共计测试了 2875 个源码包，产出测试[日志](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month13/openkylin-test)，提交完整测试报告 pr [#1](https://gitee.com/yunxiangluo/openKylin-RISC-V-2.0-RC-Testing/pulls/1) [#2](https://gitee.com/yunxiangluo/openKylin-RISC-V-2.0-RC-Testing/pulls/2)

