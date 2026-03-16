# ruyi_task

See https://github.com/hush-coder/ruyi_task

## 引子

1. 自我介绍
2. 在大学期间的项目中，主要担任了什么角色
3. 熟悉哪些编程语言
4. Linux 发行版的话，熟悉哪些发行版，熟悉到什么程度，对发行版进行一个简单分类（国内外？包管理？元发行版？）
5. 熟悉 RISC-V 吗，玩过 RISC-V 的板子吗
6. 熟悉 GitHub Actions 吗
7. 熟悉 Jenkins 吗
8. 预期的实习工资，每个周工作时长

## 考核题目

1. 检查该 issue https://github.com/ruyisdk/packages-index/issues/28 是否已经解决
2. 基于 nvchecker https://github.com/lilydjwg/nvchecker 做 https://github.com/ruyisdk/packages-index/ 中软件包的新版本监测，至少完成 extra/wps-office、 board-image/revyos-sg2042-milkv-pioneer、 board-image/buildroot-sdk-milkv-duo256m-python 三个
3. 站在 Archlinux 打包者的角度修复该 issue https://github.com/ruyisdk/ruyi/issues/261

解题要求：

1. 只允许使用 Bash 和 Python 两种语言

提交：

1. 截止日期 2025 年 2 月 24 日，充分利用时间。允许提前提交。提交后约面试
2. 在个人 GitHub 账号新开仓库存放解答代码
3. 保留运行成功的截图或得到的日志，推荐文本日志

## 实习生解答

1. 检查了 issue 的 open/close 状态
2. 检查了 milkv-duo/duo-buildroot-sdk 而不是 milkv-duo/duo-buildroot-sdk-v2；检查了 packages-index 中的 manifests/extra/wps-office 而不是 upstream
3. 思路正确

## 评价

1. 那这个 issue 是应该保持 open 还是已经可以 close 了呢？这个解答的价值存疑
2. 要仔细关注上游的公开信息，特别是在 packages-index 中已有 v2.0.0 版本时依然检查了老版本仓库；要理解我们做这个事情是在干什么
3. 这个解答的思路是正确的，解题相关就没有更多评论；但是这个 PKGBUILD 是有一些问题的，比如 makedepends 里怎么有 git、 depends 里怎么有 python-poetry， depends 列表也不是完整的。会后可以去参考 AUR 上的 PKGBUILD

