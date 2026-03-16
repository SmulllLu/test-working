# Month 15 Week 1 工作报告 24/09/02-24/09/09

## RuyiSDK

+ 完成 Ruyi 包管理器 v0.17.0 的自动化测试和报告 pr [!48](https://gitee.com/yunxiangluo/ruyisdk-test/pulls/48)
+ Ruyi issue
  | issue 标题 | 链接 |
  | :--: | :--: |
  | ruyi 的 python-frontmatter 依赖问题 | [#191](https://github.com/ruyisdk/ruyi/issues/191) |
+ 完成 Ubuntu/Debian 上 Ruyi 软件包打包的调研并打出 v0.17.0 版本 Ruyi 软件包
  | 包名 | 发行版本过低 | 备注 |
  | :--: | :--: | :--: |
  | libgit2 | 22.04 |  |
  | python3-cffi | 22.04 |  |
  | python3-frontmatter | 22.04, 24.04 | 上游未打包 |
  | python3-maturin | 22.04, 24.04 | Debian sid 也需要升版本<br/>Builddepends: python3-setuptools-rust |
  | python3-pygments | 22.04 | python3-pytest 版本过低只能跳过测试 |
  | python3-rich | 22.04 | Builddepends/Depends: python3-pygments |
  | python3-packaging | 22.04 |  |
  | python3-pygit2 | 22.04 | Builddepends/Depends: libgit2, python3-cffi |
  | python3-semver | 22.04, 24.04 | Debian sid 也需要升版本 |
  | python3-setuptools | 22.04 |  |
  | python3-setuptools-rust | 22.04 | Builddepends: python3-setuptools |
  | python3-tomlkit | 22.04 |  |
  | python3-xingque | 22.04, 24.04 | Builddepends: python3-maturin |
  临时打包仓库 [ppa.launchpad.net/ruyi](https://launchpad.net/~weilinfox/+archive/ubuntu/ruyi)

