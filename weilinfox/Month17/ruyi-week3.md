# RuyiSDK 测试组周志 24/11/18-24/11/22

## v0.22.0 测试周

+ ruyi entrypoint https://github.com/archlinuxcn/repo/commit/a29ca4c448c4f50338995d8a8117226cafb3403b https://gitlab.inuyasha.love/ruyisdk/ruyi-build-source/-/commit/5f7278af553b5938de39e7abda7d299daf1ba64c
+ 调研 lit 和 yq 在各发行版的测试可用性， debian/ubuntu 并没有提供方便调用的 lit/FileCheck 工具， openEuler 没有提供 yq  https://github.com/weilinfox/ruyi-litester/commit/91eaa87258bc9260680361bdce7ea6286cf324d8
+ debian/ubuntu 的 lit 和 FileCheck 需要特殊操作，首先为 debian/ubuntu 提供了一个备用的 ppa llvm-lit https://launchpad.net/~weilinfox/+archive/ubuntu/llvm-lit https://github.com/weilinfox/ruyi-litester/commit/d32946b52183b9535b8a2621c665ffa45a96ca02 ，后面考虑了一下还是由 Rit 提供软链接 https://github.com/weilinfox/ruyi-litester/commit/12fd10a715b36e05eaa8c34d49ca363a6bd6b4b8； gentoo 的 FileCheck 特殊操作 https://github.com/weilinfox/ruyi-litester/commit/f8894818647a9bfb59a55fda39a9307084b2176b
+ 0.22.0-beta.20241116 在 Ubuntu 22.04 使用 python3.10 进行了 litester 测试，没有发现问题 https://jenkins.inuyasha.love/job/ruyi-litester/job/ruyi-litester-test-python310/3/
+ 0.22.0 附加测试
  + ruyi 按照 python 标准方式引出 entrypoint
    + Archlinux CN PK
  + deb/rpm 打包脚本中去除版本限制，[自动出包](https://gitlab.inuyasha.love/ruyisdk/ruyi-builds/-/commit/3b0ce1195c419015c109ce9febb2b86aed80925a)
+ 0.22.0 在 Archlinux/Debian/Gentoo/Ubuntu 进行了 litester 测试，见 发行版打包附加测试 测试报告
+ ruyi-litester [b98b740..b7dde2a](https://github.com/weilinfox/ruyi-litester/compare/b98b740..b7dde2a) 计 34 个 commit， 401 增加 12 删除
  + 最主要的 mugen 兼容函数的实现
    + PKG_INSTALL/PKG_REMOVE
      + 比如 PKG_INSTALL --debian --ubuntu --fedora yq --gentoo app-misc/yq
      + APT_INSTALL/APT_REMOVE
      + DNF_INSTALL/DNF_REMOVE
      + EMERGE_INSTALL/EMERGE_REMOVE
      + PACMAN_INSTALL/PACMAN_REMOVE
  + ruyi-advance 修好了
  + 需要提权的操作 -s --sudo 参数
+ gentoo riscv64 测试机维护， blocked，遇到 x11-libs/pixman-0.44.0 构建失败 https://gitlab.freedesktop.org/pixman/pixman/-/issues/115 根据 issue 0.44.3 worked
+ ruyi-advance 修好了

## TODO

+ ruyi-litester 支持从配置中使用正则去除一些测试，类似 pytest -K
+ ruyi-litester mugen driver 兼容主程序

