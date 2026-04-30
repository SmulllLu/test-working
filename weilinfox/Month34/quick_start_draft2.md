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

注意在本文档中，对 ruyi 使用方法对介绍无法详尽，可以在命令后添加 -h 参数来获取所有子命令、参数、子命令和参数的别名、子命令和参数对应的功能介绍。

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

ruyi 使用 packages-index 作为软件包索引，这个索引以 git 仓库的形式存在。 RuyiSDK 提供了一个软件包索引用于获取 RuyiSDK 提供的软件包，这个索引有一个主源和一个与主源同步的同步源：

+ 主源： <https://github.com/ruyisdk/packages-index.git>
+ 同步源： <https://mirror.iscas.ac.cn/git/ruyisdk/packages-index.git>

其中主源为 ruyi 默认采用的软件包索引源，若该源由于网络原因难以拉取，可以将软件包索引源配置成同步源：

```bash
$ ruyi config set repo.remote https://mirror.iscas.ac.cn/git/ruyisdk/packages-index.git
```

### ruyi 的用户协议和遥测

在首次使用 ruyi 的功能时（通常指除 ``ruyi version`` 以外的命令）， ruyi 将打印用户协议要求用户同意：

```

```

在同意用户协议以后， ruyi 将打印遥测相关的信息要求用户同意。

```
info: Welcome to RuyiSDK! This appears to be your first run of ruyi.

RuyiSDK collects minimal usage data in the form of just a version number of
the running ruyi, to help us improve the product. With your consent,
RuyiSDK may also collect additional non-tracking usage data to be sent
periodically. The data will be recorded and processed by RuyiSDK team-managed
servers located in the Chinese mainland.

By default, nothing leaves your machine, and you can also turn off usage data
collection completely. Only with your explicit permission can ruyi collect and
upload more usage data. You can change this setting at any time by running
ruyi telemetry consent, ruyi telemetry local, or ruyi telemetry optout.

We'll also send a one-time report from this ruyi installation so the RuyiSDK
team can better understand adoption. If you choose to opt out, this will be the
only data to be ever uploaded, without any tracking ID being generated or kept.
Thank you for helping us build a better experience!

Do you agree to have usage data periodically uploaded? (y/N)

Do you want to opt out of telemetry entirely? (y/N)
```

```
信息：Welcome to RuyiSDK! This appears to be your first run of ruyi.

RuyiSDK 仅以运行中的 ruyi 版本号的形式最小化地收集使用数据，以帮助我们改进产品。经您同意，
RuyiSDK 也可以收集并定期发送额外的、无法用来追踪用户身份的使用数据。数据将由位于中国大陆的、
由 RuyiSDK 团队管理的服务器记录和处理。

默认情况下，任何内容都不会离开您的计算机，您也可以完全关闭使用数据收集。
只有在您明确许可的情况下，ruyi 才能收集和上传更多使用数据。您随时可以通过运行
ruyi telemetry consent、ruyi telemetry local 或 ruyi telemetry optout 更改设置。

我们还将一次性从本台 ruyi 实例发送单条报告，以便 RuyiSDK 团队更好地了解产品用户增长情况。
如果您选择不同意，这将是唯一被上传的数据，我们不会生成或保留任何跟踪用的 ID。
感谢您帮助我们构建更好的体验！

您是否同意定期上传使用数据？ (y/N)

您是否要完全禁用遥测？ (y/N)
```

为了帮助 RuyiSDK 改进 ruyi，建议用户同意上传匿名遥测信息。

```bash
$ ruyi telemetry consent
```

遥测信息通常在一周中的某一天上传，这个时间是随机生成的。

### ruyi 的配置文件

虽然 ruyi 不推荐直接编辑配置文件，但了解配置文件的结构有助于灵活使用 ruyi config 命令。

ruyi 的配置文件通常存放在 ~/.config/ruyi/config.toml。 ruyi 支持 XDG_CONFIG_PATH 环境变量，当这个环境变量被设置时 ruyi 的配置文件路径为 $XDG_CONFIG_PATH/ruyi/config.toml。

一个典型的 ruyi 配置文件如下：

```
[packages]
# Consider pre-release versions when matching packages in repositories.
prereleases = false

[repo]
# Path to the local RuyiSDK metadata repository. Must be absolute or the setting
# will be ignored.
# If unset or empty, $XDG_CACHE_HOME/ruyi/packages-index is used.
local = ""
# Remote location of RuyiSDK metadata repository.
# If unset or empty, this default value is used.
remote = "https://github.com/ruyisdk/packages-index.git"
# Name of the branch to use.
# If unset or empty, this default value is used.
branch = "main"

[telemetry]
# Whether to collect telemetry information for improving RuyiSDK's developer
# experience, and whether to send the data periodically to RuyiSDK team.
# Valid values are `local`, `off` and `on` -- see the documentation for
# details.
#
# If unset or empty, this default value is used: data will be collected and
# stored locally; nothing will be uploaded automatically.
mode = "local"
# The time the user's consent is given to telemetry data uploading. If the
# system time is later than the time given here, telemetry consent banner will
# not be displayed any more each time `ruyi` is executed. The exact consent
# time is also useful should the telemetry policy get updated in the future.
#
# To hide the consent banner, set it to the current local time, for example:
#
#     upload_consent = 2024-12-02T15:61:00+08:00
#
# The timestamp is intentionally invalid for you to notice and modify to your
# need.
upload_consent = ""
# Override the telemetry server URL of the RuyiSDK package manager scope.
# If unset, the repo-configured default is used; if set to empty, telemetry
# uploading is disabled.
#pm_telemetry_url = ""
```

根据 ruyi 的安装方式不同，可能会存在另一个配置文件 /usr/share/ruyi/config.toml。这个配置文件在当前 ruyi 版本下只有在使用系统包管理器安装 ruyi 时才有可能出现，用户无需关心。

一个典型的 /usr/share/ruyi/config.toml 的内容如下：

```
[installation]
externally_managed = true  # by the system package manager
```

该配置表示 ruyi 是由系统包管理器安装的。该配置存在时， ruyi 将禁用诸如 ruyi self uninstall 这样的功能。

### 同步软件包索引

使用如下命令来拉取软件包索引 packages-index，将本地索引与远端索引同步：

```bash
$ ruyi update
```

本地索引通常存放在 ~/.cache/ruyi/packages-index 下， ruyi 支持 XDG_CACHE_DIR 环境变量，当该环境变量被配置时本地索引将存放在 $XDG_CACHE_DIR/ruyi/packages-index 下。

ruyi update 的输出示例如下：

```
info: syncing repo 'ruyisdk'
info: updating the package repository
info: the package repository does not exist at /home/hachi/.cache/ruyi/repos/ruyisdk
info: cloning from https://mirror.iscas.ac.cn/git/ruyisdk/packages-index.git
Enumerating objects: 3589, done.
Counting objects: 100% (279/279)Counting objects: 100% (279/279), done.
Compressing objects: 100% (264/264), done.
Total 3589 (delta 143), reused 0 (delta 0), pack-reused 3310
transferring objects ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   0% 0:00:01
processing deltas    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
info: package repository is updated

There are 44 new news item(s):

 No.   ID                                  Title                                                  
──────────────────────────────────────────────────────────────────────────────────────────────────
 1     2024-01-14-ruyi-news                RuyiSDK now supports displaying news                   
 2     2024-01-15-new-board-images         New board images available (2024-01-15)                
 3     2024-01-29-new-board-images         New board images available (2024-01-29)                
 4     2024-01-29-ruyi-0.4                 Release notes for RuyiSDK 0.4                          
 5     2024-04-23-ruyi-0.9                 Release notes for RuyiSDK 0.9                          
 6     2024-05-14-ruyi-0.10                Release notes for RuyiSDK 0.10                         
 7     2024-05-28-ruyi-0.11                Release notes for RuyiSDK 0.11                         
 8     2024-06-11-ruyi-0.12                Release notes for RuyiSDK 0.12

You can read them with ruyi news read.
```

```
信息：现已启用遥测数据上传
信息：您可以随时通过运行 ruyi telemetry optout 退出遥测
信息：正在同步仓库 'ruyisdk'
信息：正在更新软件包仓库
信息：软件包仓库不存在于 /home/hachi/.cache/ruyi/repos/ruyisdk
信息：正在从 https://mirror.iscas.ac.cn/git/ruyisdk/packages-index.git 克隆
Enumerating objects: 3589, done.
Counting objects: 100% (279/279)Counting objects: 100% (279/279), done.
Compressing objects: 100% (264/264), done.
Total 3589 (delta 144), reused 0 (delta 0), pack-reused 3310
正在传输对象    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   0% 0:00:01
正在处理 deltas ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
信息：软件包仓库已更新

有 44 条新的新闻条目：

 序号   ID                                  标题                                             
─────────────────────────────────────────────────────────────────────────────────────────────
 1      2024-01-14-ruyi-news                RuyiSDK 支持展示新闻了                           
 2      2024-01-15-new-board-images         新增板卡支持 (2024-01-15)                        
 3      2024-01-29-new-board-images         新增板卡支持 (2024-01-29)                        
 4      2024-01-29-ruyi-0.4                 RuyiSDK 0.4 版本更新说明                         
 5      2024-04-23-ruyi-0.9                 RuyiSDK 0.9 版本更新说明                         
 6      2024-05-14-ruyi-0.10                RuyiSDK 0.10 版本更新说明                        
 7      2024-05-28-ruyi-0.11                RuyiSDK 0.11 版本更新说明                        
 8      2024-06-11-ruyi-0.12                RuyiSDK 0.12 版本更新说

您可以使用 ruyi news read 阅读它们
```

可以从进度条获知 ruyi 拉取远端数据的进度，在获取成功后 ruyi 将打印未读新闻。首次运行时打印的新闻列表可能很长。

### 阅读新闻

ruyi 提供了灵活的新闻阅读和状态标记功能。

若不希望阅读任何新闻，只是标记所有新闻已读：

```bash
$ ruyi news read -q
```

若希望将所有未读新闻的内容全部打印到终端：

```bash
$ ruyi news read
```

注意该命令没有翻页功能，所有内容将一次性打印在终端上。若希望根据终端的大小逐页显示，可以利用 less 命令：

```bash
$ ruyi news read | less
```

若希望打印某条新闻：

```bash
$ ruyi news read 1
```

该命令将打印上一节 ruyi update 输出中标题为  “RuyiSDK 支持展示新闻了” 的新闻。该命令无论该条新闻已读状态如何均有效。

若希望标记某条新闻为已读：

```bash
$ ruyi news read 1 -q
```

新闻的已读和未读由 ~/.local/state/ruyi/news.read.txt. 记录。同样的， ruyi 支持 XDG_STATUS_PATH 环境变量，当该变量被配置时，路径将使用 $XDG_STATUS_PATH/ruyi/news.read.txt。 ruyi 并不推荐用户自行编辑该文件。

## 搜索需要的工具链或资源

软件包索引 packages-index 将所有软件包分为如下几个类别：

| categary | 类别 | 描述 |
| -------- | ---- | ---- |
| toolchain | 工具链 | 如 GCC、 LLVM、 香山 XSCC |
| emulator | 模拟器 | 如 QEMU、 Box64 |
| source | 源码包 | 如 milkv-duo-examples、 wiringx |
| board-image | 开发板固件和镜像 | 如发行版镜像 img、 uboot |
| board-util | 开发板工具 | 如 wlink |
| analyzer | 分析器工具 | 如 dynamorio |
| extra | 其他未分类软件包 |  |

ruyi 支持通过类别和字符串匹配的方式搜索软件包。

可以通过 --name-contains 参数来搜索包名中包含指定子字符串 gnu- 的软件包：

```bash
$ ruyi list --name-contains gnu-
```

一个输出示例如下：

```
List of available packages:

* toolchain/gnu-milkv-milkv-duo-elf-bin
  - 0.20240731.0+git.67688c7335e7 (latest)
* toolchain/gnu-milkv-milkv-duo-bin
  - 0.20240731.0+git.67688c7335e7 (latest)
* toolchain/gnu-upstream
  - 0.20260201.0 (latest)
  - 0.20250401.0
  - 0.20231212.0 slug: gnu-upstream-20231212
  - 0.20231118.0 slug: gnu-upstream-20231118
* toolchain/gnu-milkv-milkv-duo-musl-bin
  - 0.20240731.0+git.67688c7335e7 (latest)
* toolchain/gnu-wch-mrs-toolchain-gcc12-bin
  - 2.1.0 (latest)
* toolchain/gnu-wch-mrs-toolchain-gcc8-bin
  - 2.1.0 (latest)
* source/riscv-gnu-toolchain-ruyi
  - 0.20251030.0+git.50720624 (latest)
```

```
可用软件包列表：

* toolchain/gnu-milkv-milkv-duo-elf-bin
  - 0.20240731.0+git.67688c7335e7 (最新)
* toolchain/gnu-milkv-milkv-duo-bin
  - 0.20240731.0+git.67688c7335e7 (最新)
* toolchain/gnu-upstream
  - 0.20260201.0 (最新)
  - 0.20250401.0
  - 0.20231212.0 slug: gnu-upstream-20231212
  - 0.20231118.0 slug: gnu-upstream-20231118
* toolchain/gnu-milkv-milkv-duo-musl-bin
  - 0.20240731.0+git.67688c7335e7 (最新)
* toolchain/gnu-wch-mrs-toolchain-gcc12-bin
  - 2.1.0 (最新)
* toolchain/gnu-wch-mrs-toolchain-gcc8-bin
  - 2.1.0 (最新)
* source/riscv-gnu-toolchain-ruyi
  - 0.20251030.0+git.50720624 (最新)
```

可以同时组合 --category-is 参数指定在 toolchain 类别中搜索：

```bash
$ ruyi list --category-is source --name-contains gnu-
```

一个输出示例如下：

```
List of available packages:

* source/riscv-gnu-toolchain-plct
  - 0.20251030.0+git.50720624 (latest)
```

```
可用软件包列表：

* source/riscv-gnu-toolchain-plct
  - 0.20251030.0+git.50720624 (最新)
```

可见搜索结果被限定在 source 类别下， toolchain 类别被过滤。

可以使用 -v 参数列出软件包的详细信息：

```bash
$ ruyi list -v --name-contains gnu-milkv-milkv-duo-elf-bin
```

输出示例：

```
## toolchain/gnu-milkv-milkv-duo-elf-bin 0.20240731.0+git.67688c7335e7

* Slug: (none)
* Package kind: ['binary', 'toolchain']
* Vendor: Milk-V
* Upstream version number: (undeclared)

Package declares 1 distfile(s):

* gnu-milkv-milkv-duo-elf-bin.67688c7335e7.tar.zst
    - Size: 86068322 bytes
    - SHA256: 851694a3b2a5250972db4d6a029f783c44c13a25435ead6a0aa5394348366d14
    - SHA512: fd0d6803c6ae87bd76d57e7d813d7c00c21e796689cba4eead9575b2a2082b92bd3c70536085beb1fac38202a956e5b22ed7bd4076b82b1ff1b171c4e2548235

### Binary artifacts

* Host linux/x86_64:
    - Distfiles: ['gnu-milkv-milkv-duo-elf-bin.67688c7335e7.tar.zst']

### Toolchain metadata

* Target: riscv64-unknown-elf
* Quirks: ['xthead']
* Components:
    - binutils 2.32
    - gcc 10.2.0
    - gdb 8.2
```

```
## toolchain/gnu-milkv-milkv-duo-elf-bin 0.20240731.0+git.67688c7335e7

* Slug：（无）
* 软件包类型：['binary', 'toolchain']
* 供应商：Milk-V
* 上游版本号：（未声明）

软件包声明了 1 个分发文件：

* gnu-milkv-milkv-duo-elf-bin.67688c7335e7.tar.zst
    - 大小：86068322 字节
    - SHA256: 851694a3b2a5250972db4d6a029f783c44c13a25435ead6a0aa5394348366d14
    - SHA512: fd0d6803c6ae87bd76d57e7d813d7c00c21e796689cba4eead9575b2a2082b92bd3c70536085beb1fac38202a956e5b22ed7bd4076b82b1ff1b171c4e2548235

### 二进制制品

* 主机 linux/x86_64：
    - 分发文件：['gnu-milkv-milkv-duo-elf-bin.67688c7335e7.tar.zst']

### 工具链元数据

* 目标：riscv64-unknown-elf
* 特殊特性：['xthead']
* 组件：
    - binutils 2.32
    - gcc 10.2.0
    - gdb 8.2
```

其中“特殊特性”是一个常用的工具链软件包信息。

## 安装目标包

在搜索到希望安装的软件包后，可以安装它，这里以 GCC 工具链 gnu-upstream 为例：

```bash
$ ruyi install gnu-upstream llvm-upstream
```

该命令会选中这些软件包的最新版本并安装它。

ruyi 支持选择软件包的某个特定版本并安装它：

```bash
$ ruyi install 'gnu-plct(0.20250401.0)'
```

注意在使用括号时需要添加单引号以避免语法错误。

该方法支持通过以下运算符来指定版本 <、 >、 ==、 <=、 >=、 !=：

```bash
$ ruyi install 'gnu-plct(>0.20250401.0)'
```

该命令可能选中 0.20260201.0 版本的软件包。

### ruyi 提供的编译工具链

RuyiSDK 提供了一系列编译工具链，参考 [RuyiSDK 编译工具](/docs/Other/GNU-type/)

## 进入或创建合适的虚拟环境

软件包索引 packages-index 中提供了一套[实体清单](https://github.com/ruyisdk/packages-index/tree/main/entities)，由实体清单将 CPU、 SoC、开发板、软件包联系起来；同时提供了一套虚拟环境配置，只需要根据开发板选定虚拟环境配置，虚拟环境将自动向工具链传递架构相关的参数，包括 ``-march``、 ``-mcpu`` 和 ``-mabi``。

使用下面的命令列出全部的虚拟环境配置：

```bash
$ ruyi list profiles
```

```
manual-rv32（架构：riscv32）
generic-rv32ec（架构：riscv32）
generic-rv32gc（架构：riscv32）
generic-rv32imac（架构：riscv32）
wch-qingke-v2a（架构：riscv32，需要特殊特性：wch）
wch-qingke-v2c（架构：riscv32，需要特殊特性：wch）
wch-qingke-v3a（架构：riscv32，需要特殊特性：wch）
wch-qingke-v3b（架构：riscv32，需要特殊特性：wch）
wch-qingke-v3c（架构：riscv32，需要特殊特性：wch）
wch-qingke-v4a（架构：riscv32，需要特殊特性：wch）
wch-qingke-v4b（架构：riscv32，需要特殊特性：wch）
wch-qingke-v4c（架构：riscv32，需要特殊特性：wch）
wch-qingke-v4f（架构：riscv32，需要特殊特性：wch）
wch-qingke-v4j（架构：riscv32，需要特殊特性：wch）
wch-qingke-v5a（架构：riscv32，需要特殊特性：wch）
wch-ch32v103-evb（架构：riscv32，需要特殊特性：wch）
wch-ch32v203-evb（架构：riscv32，需要特殊特性：wch）
wch-ch32v208-evb（架构：riscv32，需要特殊特性：wch）
wch-ch32v303-evb（架构：riscv32，需要特殊特性：wch）
wch-ch32v305-evb（架构：riscv32，需要特殊特性：wch）
wch-ch32v307-evb（架构：riscv32，需要特殊特性：wch）
wch-ch582f-evb（架构：riscv32，需要特殊特性：wch）
wch-ch592x-evb（架构：riscv32，需要特殊特性：wch）
manual（架构：riscv64）
generic（架构：riscv64）
baremetal-rv64ilp32（架构：riscv64，需要特殊特性：rv64ilp32）
xiangshan-nanhu（架构：riscv64）
sipeed-lpi4a（架构：riscv64，需要特殊特性：xthead）
milkv-duo（架构：riscv64
```

```
manual (arch: riscv64)
generic (arch: riscv64)
baremetal-rv64ilp32 (arch: riscv64, needs quirks: rv64ilp32)
xiangshan-nanhu (arch: riscv64)
sipeed-lpi4a (arch: riscv64, needs quirks: xthead)
milkv-duo (arch: riscv64)
manual-rv32 (arch: riscv32)
generic-rv32ec (arch: riscv32)
generic-rv32gc (arch: riscv32)
generic-rv32imac (arch: riscv32)
wch-qingke-v2a (arch: riscv32, needs quirks: wch)
wch-qingke-v2c (arch: riscv32, needs quirks: wch)
wch-qingke-v3a (arch: riscv32, needs quirks: wch)
wch-qingke-v3b (arch: riscv32, needs quirks: wch)
wch-qingke-v3c (arch: riscv32, needs quirks: wch)
wch-qingke-v4a (arch: riscv32, needs quirks: wch)
wch-qingke-v4b (arch: riscv32, needs quirks: wch)
wch-qingke-v4c (arch: riscv32, needs quirks: wch)
wch-qingke-v4f (arch: riscv32, needs quirks: wch)
wch-qingke-v4j (arch: riscv32, needs quirks: wch)
wch-qingke-v5a (arch: riscv32, needs quirks: wch)
wch-ch32v103-evb (arch: riscv32, needs quirks: wch)
wch-ch32v203-evb (arch: riscv32, needs quirks: wch)
wch-ch32v208-evb (arch: riscv32, needs quirks: wch)
wch-ch32v303-evb (arch: riscv32, needs quirks: wch)
wch-ch32v305-evb (arch: riscv32, needs quirks: wch)
wch-ch32v307-evb (arch: riscv32, needs quirks: wch)
wch-ch582f-evb (arch: riscv32, needs quirks: wch)
wch-ch592x-evb (arch: riscv32, needs quirks: wch)
```

GCC 工具链通常按目标整体分发，包含编译器二进制和目标头文件和库；而 LLVM 只分发工具链二进制，需要引用 GCC 的目标头文件和库。这些目标头文件和库被存放在 sysroot 中。建立虚拟环境需要指定一个或多个工具链，并按照需要指定或由 ruyi 决策引用 sysroot。在用于交叉编译的虚拟环境中，通常还需要为虚拟环境指定一个模拟器来本地模拟运行交叉编译得到的二进制。

这里以 gnu-upstream 为例，其包名中的 ``gnu-`` 表示这是一个 GCC 工具链，而 ``upstream`` 表示这个工具链直接使用上游发布的源码构建。使用 gnu-upstream 建立一个虚拟环境：

```bash
$ ruyi venv -t gnu-upstream generic ./test-venv
```

这个虚拟环境使用了 generic profile，其构建目标为 rv64gc；虚拟环境被建立在 ``./test-venv`` 路径下。由于 gnu-upstream 这个 GCC 工具链本身分发了目标头文件和库， ruyi 将自动引入该 sysroot。

这里再以 llvm-upstream 为例，显式引用 gnu-upstream 分发的目标头文件和库作为 sysroot：

```bash
$ ruyi venv -t llvm-upstream --sysroot-from gnu-upstream generic ./test-venv
```

若希望在虚拟环境中绑定 qemu-user-riscv-upstream 包作为模拟器：

```bash
$ ruyi venv -t llvm-upstream --sysroot-from gnu-upstream -e qemu-user-riscv-upstream generic ./test-venv
```

### 以某个特定开发板为目标建立虚拟环境

与上面的用法一样，现在以另一个 profile milkv-duo 为例建立以 Milk-V Duo 系列开发板为构建目标的虚拟环境：

TODO: quirks https://github.com/ruyisdk/packages-index/issues/181

```bash
$ ruyi venv -t gnu-milkv-milkv-duo-musl-bin -e qemu-user-riscv-upstream milkv-duo ./duo-venv
```

若所需软件包尚没有安装，则安装这些软件包：

```bash
$ ruyi install gnu-milkv-milkv-duo-musl-bin qemu-user-riscv-upstream
```

该虚拟环境构建得到的二进制将适用于包括采用 CV1800B、 SG2000、 SG2002 SoC 的运行 musl 镜像的 Milk-V Duo、 Duo256M、 Duo S 开发板，这些 SoC 都使用了 C906 CPU。

一个典型的命令输出如下：

```
info: Creating a Ruyi virtual environment at duo-venv...
info: The virtual environment is now created.

You may activate it by sourcing the appropriate activation script in the
bin directory, and deactivate by invoking `ruyi-deactivate`.

A fresh sysroot/prefix is also provisioned in the virtual environment.
It is available at the following path:

    /home/we/test_venv/duo-venv/sysroot

The virtual environment also comes with ready-made CMake toolchain file
and Meson cross file. Check the virtual environment root for those;
comments in the files contain usage instructions.
```

```
信息：正在在 duo-venv 创建 Ruyi 虚拟环境...
信息：现已创建完成虚拟环境。

您可“source” bin 目录下合适的激活脚本，以激活此虚拟环境；而后可调用 ruyi-deactivate
以离开它。

在此虚拟环境中，亦为您部署了一套新的 sysroot/prefix 在以下路径：

    /home/we/test_venv/duo-venv/sysroot

此虚拟环境还内置了开箱即用的 CMake 工具链配置文件（CMake toolchain file）与 Meson
交叉编译文件（Meson cross file）。您可在虚拟环境的根目录找到它们；文件的注释中有使用说明。
```

### 检查虚拟环境中的文件

一个典型的虚拟环境包含了工具链、 sysroot 和模拟器相关文件。

上一节在 ./duo-venv 建立的虚拟环境将包含以下典型内容：

|            文件/目录             |                     描述                     |
|:--------------------------------:|:--------------------------------------------:|
| bin/riscv64-unknown-linux-musl-* |              工具链脚本和二进制              |
|          bin/ruyi-qemu           |           虚拟环境包含的模拟器工具           |
|        bin/ruyi-activate         | 虚拟环境激活脚本（适用于 bash 兼容的 shell） |
|      bin/ruyi-activate.fish      | 虚拟环境激活脚本（适用于 fish 兼容的 shell） |
|           sysroot 目录           |           包含编译目标的头文件和库           |
|         meson-cross.ini          |              meson 交叉编译配置              |
|         toolchain.cmake          |              cmake 交叉编译配置              |
|           binfmt.conf            |      虚拟环境所包含模拟器的 binfmt 配置      |

若引用了 LLVM 工具链，则 bin/ 目录下将存在 LLVM 工具链二进制；若使用 --without-sysroot 指定不引用任何 sysroot，则 sysroot 目录将不存在；若没有引用任何模拟器，则和模拟器相关的文件将不存在。

### 激活和退出虚拟环境

这里以 bash 为例，激活虚拟环境。在激活虚拟环境后， ``$PS1`` 环境变量的内容将被改变，以提示当前已激活虚拟环境：

```bash
$ source ./duo-venv/bin/ruyi-activate
«Ruyi duo-venv» $
```

在激活虚拟环境并完成构建后可以使用 ``ruyi-deactivate`` 命令退出虚拟环境， ``$PS1`` 环境变量的内容将被还原：

```bash
«Ruyi duo-venv» $ ruyi-deactivate
$
```

### 验证工具是否可用

```bash
$ ruyi extract coremark
$ cd coremark-1.0.1
$ sed -i 's/\bgcc\b/riscv64-unknown-linux-musl-gcc/g' linux64/core_portme.mak
$ make PORT_DIR=linux64 link
$ ruyi-qemu coremark.exe
```

coremark 运行结果如下：

```
qemu-riscv64: warning: disabling zfa extension because privilege spec version does not match
2K performance run parameters for coremark.
CoreMark Size    : 666
Total ticks      : 17396
Total time (secs): 17.396000
Iterations/Sec   : 17245.343757
Iterations       : 300000
Compiler version : GCC10.2.0
Compiler flags   : -O2   -lrt
Memory location  : Please put data memory location here
			(e.g. code in flash, data on heap etc)
seedcrc          : 0xe9f5
[0]crclist       : 0xe714
[0]crcmatrix     : 0x1fd7
[0]crcstate      : 0x8e3a
[0]crcfinal      : 0xcc42
Correct operation validated. See readme.txt for run and reporting rules.
CoreMark 1.0 : 17245.343757 / GCC10.2.0 -O2   -lrt / Heap
```

https://lists.nongnu.org/archive/html/qemu-devel/2024-01/msg04766.html
https://forums.100ask.net/uploads/short-url/4Wvk1aRo3SjySm2vodgfzlbjXpM.pdf
