# 2026年4月 第1周

## 修改

### 提交：[修改freebsd/riko.py的url](https://github.com/ruyisdk-test/riko-bot/commit/293e534aaac6290807f24aa9d5bde95a07619e5b)
- 原来的`https://mirror.iscas.ac.cn/FreeBSD/releases/riscv/riscv64/ISO-IMAGES/`无法访问，将其riko.toml的url修改成`https://download.freebsd.org/releases/riscv/riscv64/ISO-IMAGES/`
- `riko.py`按照同样的逻辑进行修改

### 提交：[Ruyi镜像源配置逻辑修复](https://github.com/ruyisdk-test/riko-bot/commit/fefe377e6de38f4888140e007fa77dc713d33c95)
- 修复了镜像源切换失效的问题，现在可以通过环境变量 USE_RUYI_ISCAS_MIRROR=true 正确切换到国内加速源
- 提高了配置的安全性，避免空值覆盖导致的配置异常


## 新增

### 提交：[新增armbian的新riscv板子](https://github.com/ruyisdk-test/riko-bot/commit/4db35ef400ce70649d72ba69594105ba763a901a)
- 新增了`armbian-musepipro`/`armbian-orangepirv2`/`armbian-visionfive2`/`armbian-uefi-riscv64`三个板子的`riko.py`、`riko.toml`、`riko.yaml`文件
- 在`https://github.com/armbian/community/tags`进行镜像下载


