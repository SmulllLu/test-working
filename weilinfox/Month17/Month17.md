# Month 17 工作报告 24/11/04-24/11/29

+ ruyi v0.21.0 测试完成 pr [!52](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/52)
+ ruyi v0.22.0 测试完成 pr [!53](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/53)
+ ruyi v0.21.0 测试提出 2 个新增 issue
  | issue 标题                                               | issue 链接                                         |
  | -------------------------------------------------------- | -------------------------------------------------- |
  | ruyi self uninstall --purge 残留本地遥测信息（影响 beta 版本，已 close） | [#226](https://github.com/ruyisdk/ruyi/issues/226) |
  | ruyi deb/rpm 打包问题                                    | [#228](https://github.com/ruyisdk/ruyi/issues/228) |
+ ruyi v0.22.0 附加测试发现一个问题提出 1 个 issue
  | issue 标题                                                                                | issue 链接                                         |
  | ----------------------------------------------------------------------------------------- | -------------------------------------------------- |
  | 在 python-semver 2.10 下无法使用 `ruyi install 'gnu-upstream(0.20231118.0)'` （已 close） | [#232](https://github.com/ruyisdk/ruyi/issues/232) |
+ ruyi v0.21.0 Archlinux CN 打包忽略 pluginhost/test_api.py 测试，它需要在安装了 ruyi 的环境下运行，否则在 collect 阶段失败 [085515d](https://github.com/archlinuxcn/repo/commit/085515d2206c8346cec6fcd29c686de87c0d8ed4)
+ ruyi v0.22.0 deb/rpm 打包问题讨论，关联 issue [#228](https://github.com/ruyisdk/ruyi/issues/228)。 [comment-2469537248](https://github.com/ruyisdk/ruyi/pull/229#issuecomment-2469537248)、 [comment-2469924528](https://github.com/ruyisdk/ruyi/pull/229#issuecomment-2469924528)
  + 调研了 Debian 12-sid、 openkylin 2.0、 Fedora 38-41 上 ruyi 主要依赖的版本
+ ruyi v0.22.0 rpm/deb 打包相关附加测试和打包脚本更新
  + ruyi 已经按照 python 标准方式引出 entrypoint
    + Archlinux CN 打包脚本修改 [commit](https://github.com/archlinuxcn/repo/commit/a29ca4c448c4f50338995d8a8117226cafb3403b)
    + deb/rpm 打包脚本修改 [commit](https://gitlab.inuyasha.love/ruyisdk/ruyi-build-source/-/commit/5f7278af553b5938de39e7abda7d299daf1ba64c)
  + ruyi 已经降级 python 依赖版本到 3.10，降级 python 依赖
    + deb/rpm 打包脚本中去除版本限制，[自动出包](https://gitlab.inuyasha.love/ruyisdk/ruyi-builds/-/commit/3b0ce1195c419015c109ce9febb2b86aed80925a)
    + 在 Archlinux/Debian/Gentoo/Ubuntu 进行了 litester 测试，发行版打包附加测试 [测试报告](https://gitee.com/yunxiangluo/ruyisdk-test/blob/master/20241119/RUYI_%E5%8F%91%E8%A1%8C%E7%89%88%E6%89%93%E5%8C%85%E9%99%84%E5%8A%A0%E6%B5%8B%E8%AF%95.md)
+ ruyi deb/rpm 提交打包脚本到 ruyi 仓库 pr [#238](https://github.com/ruyisdk/ruyi/pull/238)
+ ruyi-mugen 测试添加 admin checksum 测试 pr [!24](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/24)
+ ruyi-litester [9902939..005df86](https://github.com/weilinfox/ruyi-litester/compare/9902939..005df86) 102 个 commit， 1644 增加 81 删除
  + ruyi-help
    + ruyi-help 适配 v0.21.0 改变的输出，增加 checksum/run-plugin-cmd 测试
  + ruyi-basic
    + ruyi-admin manifest 改为 checksum
    + v0.21.0 ruyi admin checksum 默认 toml，而旧的 manifest 默认 json
  + ruyi-advance
    + ruyi 的配置文件和环境变量测试
  + ruyi-mugen
    + 一些比较复杂而采用 mugen 格式的用例
    + 移植好的 ruyi\_test\_binaries 测试用例
  + rit-unit
    + ruyi-litester 单元测试，自己测试自己
  + 内部模块参数传递设计，统一一些全局变量和测试套获取变量的方式
    + 见 [README\_zh.md#内部变量](https://github.com/weilinfox/ruyi-litester/blob/master/README_zh.md#内部变量)
  + mugen 测试用例兼容函数，对设计不合理的函数进行重新设计
    + PKG\_INSTALL/PKG\_REMOVE
      + 比如 PKG\_INSTALL --debian --ubuntu --fedora yq --gentoo app-misc/yq
      + APT\_INSTALL/APT\_REMOVE
      + DNF\_INSTALL/DNF\_REMOVE
      + EMERGE\_INSTALL/EMERGE\_REMOVE
      + PACMAN\_INSTALL/PACMAN\_REMOVE
    + 见 [README\_zh.md#mugen-兼容](https://github.com/weilinfox/ruyi-litester/blob/master/README_zh.md#mugen-兼容)
  + 可用的 mugen 用例运行和日志输出
    + 甚至日志格式都是一样的，支持和上游 mugen 一样的 ``-f``、 ``-r``、 ``-x`` 参数
    + 这个 mugen driver 也支持 --match 功能，只是选项改为 ``-m``
  + 增加 SIGINT/SIGERR 异常退出的信号处理
    + Rit 只允许单实例，故会生成一个 .rit.bash.lock
  + 规范框架中需要提权的操作，新增 -s --sudo 参数
  + 增加 --lit,--mugen 允许向 Lit 和 mugen driver 直接传递参数
  + --match 用法，用法和 ``pytest -k`` 基本一致
    + 比如某个 profile 中包括了测试 ``ab-a``、 ``ab-b``、 ``ab-f``、 ``bc-d``，而我不希望运行 ``ab-f``。使用 ``--match`` 传入表达式 ``'ab- and ( -a or -b ) or bc-'`` 或 ``'ab- and not -f or bc-'`` 或 ``'not ab-f'`` 都是可以的，注意括号前后加空格
    + 具体参见 [README_zh.md#选择性运行测试](https://github.com/weilinfox/ruyi-litester/blob/master/README_zh.md#选择性运行测试)
  + 调研 yq 在各发行版的可用性， openEuler 没有提供 yq，注释在 README 中 [commit](https://github.com/weilinfox/ruyi-litester/commit/91eaa87258bc9260680361bdce7ea6286cf324d8)
  + 调研 lit 和 FileCheck 在各发行版的可用性
    + debian/ubuntu 的 lit 和 FileCheck 需要特殊操作 [commit](https://github.com/weilinfox/ruyi-litester/commit/d32946b52183b9535b8a2621c665ffa45a96ca02)
    + gentoo 的 FileCheck 需要特殊操作 [commit](https://github.com/weilinfox/ruyi-litester/commit/f8894818647a9bfb59a55fda39a9307084b2176b)
+ gentoo riscv64 测试机维护，遇到 x11-libs/pixman-0.44.0 构建失败，根据上游 [issue](https://gitlab.freedesktop.org/pixman/pixman/-/issues/115) 0.44.3 才工作

