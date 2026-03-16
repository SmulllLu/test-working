# RuyiSDK Weekly Meeting 25/08/15

+ 官网主要更新了数据统计页面，也有一些其他零散的更新
+ ruyi-packaging 的 checker 分支做了打包工具，基本功能已经完成
    ```bash
    $ python -m riko -h
    usage: riko [-h] {check,list,manifests} ...

    Riko: the Ruyi Packaging Bot

    positional arguments:
      {check,list,manifests}
                            sub-commands
        check               Fetch data and refresh local cache
        list                List nvchecker result event or level
        manifests           Generate new packages-index manifests from old ones

    options:
      -h, --help            show this help message and exit
   ```
+ 使用打包工具向 packages-index 提交了 5 个 pr
    + [buildroot-sdk-sipeed-licheervnano 补全了缺失的版本](https://github.com/ruyisdk/packages-index/pull/95)
    + [revyos-sipeed-lpi4a 更新版本到 20250729](https://github.com/ruyisdk/packages-index/pull/96)
    + [revyos-sipeed-lcon4a 补全缺失的版本 20240720 和最新版本 20250729](https://github.com/ruyisdk/packages-index/pull/97)
    + [revyos-milkv-meles 更新版本到 20250729](https://github.com/ruyisdk/packages-index/pull/98)
    + [bianbu-bpi-f3 修复了损坏的配置，统一了所有 bianbu 相关镜像的 upstream_version 格式](https://github.com/ruyisdk/packages-index/pull/99)
    + 在做上一个的时候发现 [bianbu-bpi-f3](https://github.com/ruyisdk/packages-index/blob/main/manifests/board-image/bianbu-bpi-f3/) 和 bianbu-desktop-spacemit-k1-sd 是相同的东西，而 bianbu-bpi-f3 并没有实体引用
    + [移除 bianbu-bpi-f3, 并为 bianbu-{desktop,minimal}-spacemit-k1-sd 补全版本](https://github.com/ruyisdk/packages-index/pull/100)
    + 在做 armbian 的新版本检查时发现 Pine64 Star64 的镜像从 github.com/armbian/community 的 release 中消失了
        + 现在 armbian-pine64-star64 下的所有 manifest 都是坏的
        + 这是由于 armbian/community 会在发 release 时删除旧的 release
        + 所以可能也需要移除 [armbian-pine64-star64](https://github.com/ruyisdk/packages-index/tree/main/manifests/board-image/armbian-pine64-star64)
+ 打包工具方便待进行的工作
    + ruyi-packaging 待支持的 combo
        + oerv-* （大部分需要检查新版本支持状态）
        + freebsd-riscv64-mini-live
        + openkylin-riscv64-sifive-unmatched
        + ubuntu-server-riscv64-sifive-unmatched
        + openwrt-sifive-unmatched
    + packages-index 已知需要补全版本但暂未补全的
        + debian-fishwaldo-sg200x-sipeed-licheervnano
        + mars-buildroot-sdk
