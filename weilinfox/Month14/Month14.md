# Month 14 工作报告 24/08/12-24/08/30

## RuyiSDK

+ ruyi mugen 更新 pr [!21](https://gitee.com/yunxiangluo/mugen-ruyi/pulls/21)
   | 主要功能更新                   | 提交                                                                                               |
   | ------------------------------ | -------------------------------------------------------------------------------------------------- |
   | Add support for licheepi4a oErv2403 | [601abc6](https://github.com/weilinfox/ruyi-mugen/commit/601abc6678697baba60a9276a7965a1d3ba6ba1b) |
   | Update fedora38 x86\_64 to fedora39 | [467a13e](https://github.com/weilinfox/ruyi-mugen/commit/467a13e1ca28d59c463873f336b097709ee5a935) |
   | Add support for pioneer box oErv2403 | [26582f6](https://github.com/weilinfox/ruyi-mugen/commit/26582f6e5379f8d075ff7f7fc57ac896d63b1630) |
   | Now we have env and choose test link automatically by this | [00e7134](https://github.com/weilinfox/ruyi-mugen/commit/00e7134b03b5e3b6ae6649c0a10c894c40fae7f0)
+ 在 26 个平台测试了 ruyi v0.16.0 版本，提交测试日志、报告和视频 [!47](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/47)
+ 提交 v0.16.0 版本缺陷 issue
   | issue 标题                                                                           | issue 链接                                         |
   | ------------------------------------------------------------------------------------ | -------------------------------------------------- |
   | wps-office 上游新版本 11.1.0.11723 | [#183](https://github.com/ruyisdk/ruyi/issues/183) |
+ ruyi-reimu 更新，完成自动化
   [详细代码更新](https://github.com/weilinfox/ruyi-reimu/compare/a40d0c4..67a062e)，共计 36 个 commit， 555 行增加， 44 行删除。
+ 向 AUR 提交 ruyi 包管理器打包脚本 [ruyi](https://aur.archlinux.org/packages/ruyi)，以及其依赖 xingque 的打包脚本 [python-xingque](https://aur.archlinux.org/packages/python-xingque)，目前支持 Archlinux 官方和社区的 5 个架构
+ 完成 ruyi 包管理器在 openEuler 23.09、 24.03 LTS 以及 24.09 的依赖情况，在 EUR 完成了 ruyi v0.16.0 在 openEuler 24.03 LTS 的打包。关注加粗包名，在最新的 24.09 版本中，有 3 个包版本过低， 4 个包没有打包。
  | 包名 | 发行版本过低 | 备注 |
  | :--: | :--: | :--: |
  | clang | 23.09 | 23.09 Rust 版本过低不足以构建 xingque |
  | libgit2 | 23.09 |  |
  | **python-arpy** | \* | 20.09 后被废弃 |
  | python-certifi | 23.09 |  |
  | python-cffi | 23.09 |  |
  | **python-frontmatter** | \* | 没有打包该包 |
  | python-markdown-it-py | 23.09 |  | Depends: python-mdurl |
  | **python-maturin** | 23.09, 24.03 LTS, 24.09  |  |
  | python-mdurl | 23.09 |  |
  | **python-packaging** | 23.09, 24.03 LTS, 24.09 |  |
  | **python-pygit2** | \* | Builddepends/Depends: libgit2, python-cffi; 没有打包该包 |
  | python-rich | 23.09 | Builddepends/Depends: python-markdown-it-py |
  | python-semver | 23.09  |  |
  | **python-tomlkit** | 23.09, 24.03 LTS, 24.09 |  |
  | python-xingque | \* | Builddepends: python-maturin, rust; 没有打包该包 |
  | rust | 23.09 | Builddepends: clang |
+ 自动化测试平台中心节点带宽由原来的 3Mbps 升为 100Mbps，提升远程测试机数据交互容量

## RVSC

+ 制作了演讲 PPT [《Ruyi包管理器的自动化测试》](https://gitlab.inuyasha.love/weilinfox/plct-working/-/blob/master/Done/Month14/Ruyi包管理器的自动化测试.odp)

