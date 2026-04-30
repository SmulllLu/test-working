# 2. 快速开始

## 安装前说明

在开始之前，建议用户先确认以下几点：

1. 当前系统是否满足 Ruyi 的运行要求；
2. 是否具备基本的命令行使用能力；

### ruyi 的平台兼容性

由于 ruyi 是以平台无关的 Python 编写，您通常可以在任何拥有 Python 包管理器的系统上安装它。但由于 ruyi 本身并不提供编译和软件模拟在内的各种功能，真正使用起来还是需要考虑 RuyiSDK 的整体平台支持情况。

当前 ruyi 只对 RISC-V 64 和 x86_64 两种架构的 **Linux 发行版**提供最佳支持；所有 Linux 发行版中，以还在生命周期中的 Debian、 Ubuntu、 openEuler 和 openRuyi 支持最佳。

详细的 RuyiSDK 平台支持情况请参考 [RuyiSDK 的平台支持情况](/docs/Other/platform-support)。

如果用户只是希望快速体验 Ruyi，可以先完成安装并浏览可用资源；如果已经有明确的目标，则建议在安装后立即查看与目标平台相关的工具链或板卡资源。

### ruyi 的安装方式选择

由于 ruyi 是一个命令行程序，使用和安装它需要具备一定的 Linux 命令行和程序语言基础。 RuyiSDK 还提供了两种插件将 ruyi 和 IDE 集成，由插件来提供安装和使用 ruyi 的 GUI 用户界面。

点击下面的链接来跳转到插件的文档：

+ [Eclipse 插件](/docs/IDE/)
+ [VS Code 扩展](/docs/VSCode-Plugins/)

或继续了解如何使用 ruyi 工具↓

### 第一次使用 Ruyi 的典型流程

一个最典型的首次使用流程通常如下：

1. 安装 ruyi；
2. 配置遥测和同步软件包索引；
3. 搜索需要的工具链或资源；
4. 安装目标包；
5. 进入或创建合适的开发环境；
6. 验证工具是否可用。

本文档也将以该流程展开。

## 安装 ruyi

为了最大程度方便用户安装 ruyi，最大程度考虑 Linux 用户的使用习惯，并尽力保持用户系统干净， ruyi 提供了多种安装方式供选择，包括：

1. 使用 Nuitka 构建的单二进制安装
2. 从 PyPI 源安装
3. 使用系统包管理器安装（部分发行版）

其中前两种方式安装的 ruyi 依赖用户手动升级版本，而使用系统包管理器安装的 ruyi 可以跟随系统软件包的升级而一同升级版本。

需要额外指出的是，出于不重复实现功能的考虑， ruyi 的一些功能依赖 Linux 命令实现，除在使用系统包管理器安装的情形下可以通过依赖关系自动引入，用户需要自行处理这些 Linux 命令依赖。在最坏的情况下， ruyi 在发现某项操作依赖的 Linux 命令不存在时，将抛出相关报错并终止运行。

### Nuitka 构建的 ruyi 单二进制

ruyi 发布的每个版本都包含 amd64、 riscv64 和 arm64 三种架构的二进制以及一个源码 tarball。这些发布产物会同时发布在 [GitHub Rleases](https://github.com/ruyisdk/ruyi/releases) 和 [ISCAS 开源镜像站](https://mirror.iscas.ac.cn/ruyisdk/ruyi/releases/)。 ruyi 推荐发行版在打包 ruyi 时使用这个源码 tarball 打包，替代 GitHub 提供的针对某个 tag 打包的 tarball，来保证源码包的哈希永远是一致的。

将该二进制下载后放置在系统 ``$PATH`` 包含的目录下，保证文件名为 ``ruyi``，赋予可执行权限。下面假定刚下载下来的 ruyi 二进制文件名为 ``ruyi.arch``：

```bash
$ sudo cp ruyi.arch /usr/bin/ruyi
$ sudo chmod +x /usr/bin/ruyi
```

若需要升级 ruyi 的版本，请下载新版本的二进制，使用与首次安装相同的安装流程覆盖旧版本二进制。

使用这种方法安装 ruyi 还需要安装 ruyi 依赖的 Linux 命令。

### ruyi 在 PyPI 的版本发布

ruyi 发布的每个版本都会同步上传到 [PyPI 上](https://pypi.org/project/ruyi/)。由于 ruyi 依赖的部分 Python 库在 PyPI 上并没有提供 RISC-V 64 架构的预编译包，在使用这个方法安装 ruyi 时这些 Python 依赖将会从源代码开始构建，这不仅会耗费大量时间，而且大概率是会构建失败的，所以我们不推荐 RISC-V 用户选择这个方法安装。

[**pipx**](https://pipx.pypa.io/) 是一个用于安装 Python CLI 工具的工具， ``pipx`` 会将每个包安装到独立的环境中，并自动将可执行文件链接到 ``$PATH``，这个目录默认是 ``~/.local/bin``：

```bash
$ pipx install ruyi
```

若需要升级 ruyi 的版本：

```bash
$ pipx upgrade ruyi
```

[**pip**](https://pip.pypa.io/) 是一个更为基础的 Python 包管理工具，这里使用 ``pip`` 将 ruyi 安装到某个 Python 虚拟环境中：

```bash
$ /path/to/some/venv/bin/pip install ruyi
```

若需要升级 ruyi 的版本：

```bash
$ /path/to/some/venv/bin/pip install --upgrade ruyi
```

使用这种方法安装 ruyi 还需要安装 ruyi 依赖的 Linux 命令。

### 安装 ruyi 依赖的 Linux 命令

ruyi 依赖一些 Linux 命令来进行压缩包的解包：

+ bzip2
+ gunzip
+ lz4
+ tar
+ xz
+ zstd
+ unzip

ruyi 还依赖一些 Linux 命令来实现系统镜像的刷写：

+ sudo
+ dd
+ fastboot

下面将给出一些常见发行版对应的命令来安装这些依赖。

#### Debian/Ubuntu

#### openKylin

#### Bianbu

#### RevyOS

#### Fedora

#### openRuyi

#### openEuler

#### Arch Linux

推荐从 AUR 或 Arch Linux CN 源安装 ruyi。

#### Gentoo Linux

推荐使用 [ruyisdk-overlay](https://github.com/ruyisdk/ruyisdk-overlay) 安装。

### 使用系统包管理器安装 ruyi

下面给出部分已有社区支持的发行版，注意这些都是由社区提供的有限支持支撑的，软件包的更新并不严格和 ruyi 上游版本发布同步，若包过期或打包有问题请提交到它们对应的社区发布页面。

#### Arch Linux

ruyi 已有发布在 [AUR](https://aur.archlinux.org/packages/ruyi) 上，可以使用 AUR 助手安装，这里给出一个 ``yay`` 的示例：

```bash
$ yay -S ruyi
```

从 Arch Linux CN 软件源安装，以 ISCAS 开源镜像站为例添加配置：

```ini
[archlinuxcn]
Server = https://mirror.iscas.ac.cn/archlinuxcn/$arch
```

使用 pacman 刷新缓存并安装：

```bash
$ sudo pacman -Sy                 
$ sudo pacman -S ruyi
```

#### Gentoo Linux

注意，虽然发布 ruyi 的 ruyisdk-overlay 在 RuyiSDK 组织下，但 Gentoo 目前并不在 RuyiSDK 宣称提供支持的发行版范围内。

环境标签： GentooLinux x86_64 riscv64

如系统尚未安装 `eselect-repository` 或 Git，请先安装：

```bash
$ sudo emerge --ask --noreplace app-eselect/eselect-repository dev-vcs/git
```

添加 ``ruyisdk-overlay``：

```bash
$ sudo eselect repository add ruyisdk git https://github.com/ruyisdk/ruyisdk-overlay.git
```

同步仓库：

```bash
$ sudo emaint sync -r ruyisdk
```

``dev-util/ruyi`` 当前仅提供 ``~amd64`` 与 ``~riscv`` keyword，若你的系统未启用对应 unstable keyword，需要先在 ``package.accept_keywords`` 中为该包接受相应 keyword 后再安装：

```bash
$ sudo emerge dev-util/ruyi --autounmask-write --autounmask
$ sudo dispatch-conf
```

安装 ruyi：

```bash
$ sudo emerge --ask dev-util/ruyi
```

### 验证安装

首先确保 ruyi 的安装位置在 ``$PATH`` 内，若安装在 Python 虚拟环境中则请先进入虚拟环境。

打印已安装的 ruyi 的版本：

```bash
$ ruyi version
```

命令输出的信息可能随架构、版本和安装方法的不同而有些许区别，但一定包含版权信息。

中文版权信息如下：

```
版权所有 (C) 中国科学院软件研究所 (ISCAS)。所有权利保留。
许可证：Apache-2.0 <https://www.apache.org/licenses/LICENSE-2.0>
```

英文版权信息如下：

```
Copyright (C) Institute of Software, Chinese Academy of Sciences (ISCAS).
All rights reserved.
License: Apache-2.0 <https://www.apache.org/licenses/LICENSE-2.0>
```

## 配置遥测和同步软件包索引

TODO: 遥测

ruyi 使用 packages-index 作为软件包索引，这个索引以 git 仓库的形式存在。 RuyiSDK 提供了一个软件包索引用于获取 RuyiSDK 提供的软件包，这个索引有一个主源和一个与主源同步的同步源：

+ 主源： <https://github.com/ruyisdk/packages-index.git>
+ 同步源： <https://mirror.iscas.ac.cn/git/ruyisdk/packages-index.git>

其中主源为 ruyi 默认采用的软件包索引源，若该源由于网络原因难以拉取，可以将软件包索引源配置成同步源：

```bash
$ ruyi config set repo.remote https://mirror.iscas.ac.cn/git/ruyisdk/packages-index.git
```

### ruyi 的遥测

### ruyi 的配置文件
