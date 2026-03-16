# Month 17 Week 3 工作报告 24/11/18-24/11/22

## RuyiSDK

+ 完成 0.22.0 mugen 测试 pr [!53](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/53)
+ 0.22.0 附加测试
  + ruyi 按照 python 标准方式引出 entrypoint
    + Archlinux CN 打包脚本修改 [commit](https://github.com/archlinuxcn/repo/commit/a29ca4c448c4f50338995d8a8117226cafb3403b)
    + deb/rpm 打包脚本修改 [commit](https://gitlab.inuyasha.love/ruyisdk/ruyi-build-source/-/commit/5f7278af553b5938de39e7abda7d299daf1ba64c)
  + ruyi 降级 python 依赖版本到 3.10，降级 python 依赖
    + deb/rpm 打包脚本中去除版本限制，[自动出包](https://gitlab.inuyasha.love/ruyisdk/ruyi-builds/-/commit/3b0ce1195c419015c109ce9febb2b86aed80925a)
    + 在 Archlinux/Debian/Gentoo/Ubuntu 进行了 litester 测试，发行版打包附加测试 [测试报告](https://gitee.com/yunxiangluo/ruyisdk-test/blob/master/20241119/RUYI_%E5%8F%91%E8%A1%8C%E7%89%88%E6%89%93%E5%8C%85%E9%99%84%E5%8A%A0%E6%B5%8B%E8%AF%95.md)
+ 0.22.0 附加测试发现一个问题提出 1 个 issue
  | issue 标题                                                                   | issue 链接                                         |
  | ---------------------------------------------------------------------------- | -------------------------------------------------- |
  | 在 python-semver 2.10 下无法使用 `ruyi install 'gnu-upstream(0.20231118.0)'` | [#232](https://github.com/ruyisdk/ruyi/issues/232) |
+ ruyi-litester [b98b740..b7dde2a](https://github.com/weilinfox/ruyi-litester/compare/b98b740..b7dde2a) 计 34 个 commit， 401 增加 12 删除
  + ruyi-advance 修好了
  + 最主要的 mugen 兼容函数的实现
    + PKG\_INSTALL/PKG\_REMOVE
      + 比如 PKG\_INSTALL --debian --ubuntu --fedora yq --gentoo app-misc/yq
      + APT\_INSTALL/APT\_REMOVE
      + DNF\_INSTALL/DNF\_REMOVE
      + EMERGE\_INSTALL/EMERGE\_REMOVE
      + PACMAN\_INSTALL/PACMAN\_REMOVE
  + 规范框架中需要提权的操作，新增 -s --sudo 参数
  + 调研 lit 和 yq 在各发行版的测试可用性， debian/ubuntu 并没有提供方便调用的 lit/FileCheck 工具， openEuler 没有提供 yq，注释在 README 中 [commit](https://github.com/weilinfox/ruyi-litester/commit/91eaa87258bc9260680361bdce7ea6286cf324d8)
  + 一些发行版的 FileCheck 和 lit 不在预期位置
    + debian/ubuntu 的 lit 和 FileCheck 需要特殊操作 [commit](https://github.com/weilinfox/ruyi-litester/commit/d32946b52183b9535b8a2621c665ffa45a96ca02)
    + gentoo 的 FileCheck 需要特殊操作 [commit](https://github.com/weilinfox/ruyi-litester/commit/f8894818647a9bfb59a55fda39a9307084b2176b)
+ gentoo riscv64 测试机维护，遇到 x11-libs/pixman-0.44.0 构建失败，根据上游 [issue](https://gitlab.freedesktop.org/pixman/pixman/-/issues/115) 0.44.3 才工作

