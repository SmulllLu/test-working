# 2026年3月

## 新增

### 提交：[新增armbian的新riscv板子](https://github.com/ruyisdk-test/riko-bot/commit/4db35ef400ce70649d72ba69594105ba763a901a)
- 新增了`armbian-musepipro`/`armbian-orangepirv2`/`armbian-visionfive2`/`armbian-uefi-riscv64`三个板子的`riko.py`、`riko.toml`、`riko.yaml`文件
- 在`https://github.com/armbian/community/tags`进行镜像下载

### 提交：[将version-sync保存日志](https://github.com/ruyisdk-test/riko-bot/commit/ee278246d6e0e415d951dc5606a25c7c6ddac081)
  - 在 dry-run 模式下，将日志同时输出到 /version-dry-run_docs 文件夹                         
  - 生成带时间戳的日志文件名（如 version-sync-20260424_150949.log）                   
  - 保持 stdout 输出以便实时查看

### 提交：[更新版本更新机制](https://github.com/ruyisdk-test/riko-bot/commit/387a050387cb071fff1d51912b3524805a728f20)                                                    
  - 新增 get_cache_versions_info 方法，用于获取本地 cache 中已有版本信息                                 
  - 重构 VersionDiff 类，区分 cache（实际要增删的）和 remote（仅展示参考）两个维度                         
  - 同时计算 cache vs upstream 和 remote vs upstream 的版本差异                                           
  - 修复 git pull 使用 --ff-only 避免 divergent branches 问题                                        
  - 改进 git push 认证方式，使用 token 嵌入 URL 并在 finally 中恢复原始 URL 避免泄露

## 修改

### 提交：[修改freebsd/riko.py的url](https://github.com/ruyisdk-test/riko-bot/commit/293e534aaac6290807f24aa9d5bde95a07619e5b)
- 原来的`https://mirror.iscas.ac.cn/FreeBSD/releases/riscv/riscv64/ISO-IMAGES/`无法访问，将其riko.toml的url修改成`https://download.freebsd.org/releases/riscv/riscv64/ISO-IMAGES/`
- `riko.py`按照同样的逻辑进行修改

### 提交：[Ruyi镜像源配置逻辑修复](https://github.com/ruyisdk-test/riko-bot/commit/fefe377e6de38f4888140e007fa77dc713d33c95)
- 修复了镜像源切换失效的问题，现在可以通过环境变量 USE_RUYI_ISCAS_MIRROR=true 正确切换到国内加速源
- 提高了配置的安全性，避免空值覆盖导致的配置异常
  
### 提交：[将原有单一的 armbian 板卡配置拆分为 minimal 和 desktop](https://github.com/ruyisdk-test/riko-bot/commit/ee278246d6e0e415d951dc5606a25c7c6ddac081)
  - armbian-orangepirv2：拆分为 armbian-orangepirv2-minimal 和  armbian-orangepirv2-desktop             
  - armbian-uefi-riscv64：拆分为 armbian-uefi-riscv64-minimal 和armbian-uefi-riscv64-desktop  
  - armbian-visionfive2：拆分为 minimal 和 desktop 两个版本                      
                                        

### 提交：[修复-trunk 版本文件名和keep_back 策略空指针问题](https://github.com/ruyisdk-test/riko-bot/commit/3b71a3b6293a514c2fe00bb354d97b70d81bdba9)
 - 修复 keep_back 策略空指针问题：当 pkg_ver 为 None 时，使用占位版本 0.0.0 替代，避免程序崩溃
 - 修复 -trunk 版本文件名问题：对于包含 -trunk 的upstream_version（如 armbian-musepipro），使用完整的upstream_version 作为 manifest 文件名，而非解析后的 semver 版本

## PR

### #190：[board-image/armbian-spacemit-musepipro: add new packages](https://github.com/ruyisdk/packages-index/pull/190)
- 新增armbian-spacemit-musepipro包
### #184：[Add armbian-orangepirv2-desktop manifest](https://github.com/ruyisdk/packages-index/pull/184)
- 新增 armbian-orangepirv2-desktop 包

### #185：[Add armbian-orangepirv2-minimal manifest](https://github.com/ruyisdk/packages-index/pull/185)
- 新增 armbian-orangepirv2-minimal 包

### #188：[Add armbian-visionfive2-desktop manifest](https://github.com/ruyisdk/packages-index/pull/188)
- 新增 armbian-visionfive2-desktop 包

### #189：[Add armbian-visionfive2-minimal manifest](https://github.com/ruyisdk/packages-index/pull/189)
- 新增 armbian-visionfive2-minimal 包
