# 两周工作报告

## RuyiSDK

+ Ruyi v0.38.1 测试完成，并提交测试报告
+ ruyisdk-website 仓库提交 1 个 pr
    + pages: update community page translations #186
+ ruyisdk-website 仓库重新规范了项目结构，首页新闻添加了自动切换，新 codeblock 的灰度测试继续在德语页面进行，新社区页面已经合并还需要一些文字调整，同时有文档页面的内容和翻译上的微调。共审核 6 个实习生 pr。
    + mv files into appropriate location #183
    + Add toggle for main copy button #184
    + update the newcase #185
    + docs: update case1 English version #189
    + Optimize the copy button showing strategy and fix the code highlight cutoff #190
    + Feat/newscase auto switch #193
+ packages-index 仓库正在对现有软件包配置进行规范，提交 1 个 pr
    + board-image/\*: add missing upstream_version data #94
+ ruyi-packaging 仓库正在编写 packages-index 配置生成的工具，提交 9 个 pr，后续将使用该工具继续对已有软件包进行版本补全工作
    + riko: setup ruyi #18
    + riko: load packages-index and config nvchecker #19
    + riko: use nvchecker new_ver/old_ver features #20
    + riko: support cmdline parsing #21
    + workflow: check DCO on branch checker #22
    + misc: do some misc works #23
    + riko: subcommand list to print nvchecker results #24
    + riko: now we can get raw toml from packaging scripts #25
    + riko: subcommand manifests to generate new tomls #26
