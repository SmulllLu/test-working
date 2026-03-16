# Month 8 工作报告 24/02/05-24/02/08

## RuyiSDK

+ RUYI 包管理基于 openEuler 23.09 的 RPM 包构建。由于 RUYI 的部分 python3 依赖包版本较高，需要重新打包
   依赖包列表：
   | 包名                   | 版本            |
   | ---------------------- | --------------- |
   | python3-semver         | 3.0.2           |
   | python3-markdown-it-py | 3.0.0           |
   | python3-mdurl          | 0.1.2           |
   | python3-rich           | 13.5.2          |
   | python3-tqdm           | 4.66.1          |
   | python3-types-pyxdg    | 0.28.0.20240106 |
   | python3-frontmatter    | 1.1.0           |

   RUYI RPM 包：
   | 包名         | 版本  |
   | ------------ | ----- |
   | python3-ruyi | 0.4.0 |
+ 建立 ruyi-rpms 仓库托管 RPM 包于 [gitee](https://gitee.com/weilinfox/ruyi-rpms/) [github](https://github.com/weilinfox/ruyi-rpms/)
+ 对 python3-ruyi 运行 mugen 测试，其中 ruyi_test_common 、ruyi_test_xdg 出现失败，分析认为这是 RUYI 识别到了打包方式的不同而对相关操作做出不同的反应，而非缺陷； ruyi_test_device 出现失败，分析认为这是打包方式不同导致命令输出有不同，影响了测试用例的判断，亦非缺陷。完整[日志](https://gitlab.inuyasha.love/weilinfox/plct-working/-/tree/master/Done/Month08/Week1/logs/ruyi)
+ 给出一个 RUYI 包管理在 openEuler 23.09 独立发行版本的安装文档 [ruyi-rpm.md](https://gitlab.inuyasha.love/weilinfox/plct-working/-/tree/master/Done/Month08/Week1/ruyi-rpm.md)

