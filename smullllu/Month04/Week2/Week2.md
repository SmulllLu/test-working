# 2026年4月 第2周

## 修改
  
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


