## 关于这个版本的测试

现在 packages-index 和 docs 都各放了几个 issue

+ [BananaPi BPI-F3 eMMC storage variant did not refer to any combo #101](https://github.com/ruyisdk/packages-index/issues/101)
    + 香蕉派 F3 有 eMMC 的选项，但是没有这个包
+ [有一部分包无法下载 #37](https://github.com/ruyisdk/packages-index/issues/37)
    + 这是一个很老的 issue，且没有修完
+ [关于 fastboot 的文档提示 #95](https://github.com/ruyisdk/docs/issues/95)
    + Ruyi 对 fastboot 做了提示，但是用户看不明白；文档写了，用户也没有看明白
    + 需要对文档进行重新修订

文档测试不通过， packages-index 测试不通过。从我这边的角度看质量没有达到发布标准。

Ruyi 那边提了两个 Feature Request，还没有 bug 要提交

+ [[Feature Request] check mounted partition before ruyi device provision dd block device #345](https://github.com/ruyisdk/ruyi/issues/345)
+ [[Feature Request] a command line interface as an alternative to device provision wizard #346](https://github.com/ruyisdk/ruyi/issues/346)

### 关于集成测试的范畴

注意现在的集测它是一个黑盒测试，甚至不是集测，而是系统测试，不是拿来分支覆盖的。大家都跑过 openEuler 的 mugen，比如 mugen 测一个 ssh 命令，不可能保证每个命令的功能细节都好，只是说这个东西正常用不会有问题。

这里举个例子，比如[第 50 期双周报](https://github.com/ruyisdk/wechat-articles/blob/main/20250812-ruyisdk-biweekly-50.md?plain=1#L29)：

>如用户自定义了软件源 Git 仓库的存放路径，当该仓库当前分支的远端 URL 与 ruyi 的相应配置项不同时，ruyi update 会报错退出了，而不再将用户配置覆盖。

我们知道如果用户没有自定义软件源的本地存放路径， ruyi update 会直接覆盖。但是我们的集成测试默认只使用一个软件源，因为无法保证每个测试机都能正常访问 GitHub，备份也只有一个。然而这种测试需要两个软件源参与测试。理论上和实际上都不可能放进现在的集成测试。

所以还需要单元测试了， Ruyi 现在也没有完备的单元测试。一个正常的测试流程是要先单元测试，后集成测试。

也就是说测试这边保证的，只在集成测试的范畴之内。集成测试、回归测试、系统测试，测不到的，测试这边管不了；至于那些用例可以加，合适加，这个测试这边会斟酌。

其他集成测试测不到的东西：

+ packages-index 以前说可以测是东西少，现在多了。测试这边的建议是不做完版本补全，不做完已有 manifest 的修复，都不算达到发布标准。已知没有做完的事情上周已经同步过了，本周各种事情比较多所以做了一部分没做完，具体可以看仓库的 pr 列表
+ 文档。测试这边的建议是文档需要重新规划重新写，对于测试这边来说，测试对象是没有准备好，所以也谈不上测试

## 关于 Community 页面

由于老板提到了，“RuyiSDK社区如何定义的问题”，所以相关页面文案需要，吴干琼老师来定一下，可以向 ruyisdk-website 仓库直接提 pr。

关于合作伙伴的部分，现在没有单独页面是因为展示的厂商太少。我这这边不清楚具体有哪些合作厂商，所以后续也需要有一个列表，具体如何展示可能也需要吴干琼老师来定义一下。

## 其他杂项

+ [Jupiter and Megrez missing for MilkV product line support #104](https://github.com/ruyisdk/packages-index/issues/104)

packages-index 对于 MilkV 产品线的支持当前缺少 Jupiter 和 Megrez，支持矩阵也有对应的测试报告，结论为 Good，如果这两个没有什么问题的话后续会添加。

