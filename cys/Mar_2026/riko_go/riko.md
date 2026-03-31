# Riko Go - Ruyi 打包工具重构

## 项目概述

Riko 是 Ruyi 打包机器人的核心工具，用于自动检测上游软件版本更新并生成包清单。本项目是 Riko 的 Go 语言重构版本，与原 Python 版本功能对等。

- **原始仓库**: https://github.com/ruyisdk/ruyi-packaging
- **Go 版本仓库**: https://gitee.com/huoyi_chen/ruyi_package_go

## 技术实现

### 核心依赖

| 依赖包 | 用途 |
|--------|------|
| `github.com/google/go-github` | GitHub API 调用 |
| `github.com/Masterminds/semver` | 语义化版本比较 |
| `github.com/BurntSushi/toml` | TOML 配置解析 |


## 功能特性

### 1. 版本检测 (`riko check`)

执行完整的上游版本检测流程：

```bash
riko check
```
**支持的检测源**:
- **GitHub**: 通过 GitHub API 获取 tag 或 release
- **Regex**: 正则表达式匹配网页内容

### 2. 结果查询 (`riko list`)

查询和过滤版本检测结果：

```bash
# 列出有更新的包
riko list updated

# 列出有错误的包
riko list error

# 列出所有结果
riko list any
```


### 3. 清单生成 (`riko manifests`)

为指定上游生成 ruyi 包清单：

```bash
# 使用检测结果中的版本
riko manifests openwrt-sifiveu

# 指定版本
riko manifests openwrt-sifiveu 25.12.2

# 允许降级
riko manifests openwrt-sifiveu --downgrade
```

## 数据格式兼容性

内置测试脚本，diff两个项目的运行结果，Go 版本与 Python 版本生成的结果完全一致
