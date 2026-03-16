# RuyiSDK 测试组周志 24/11/15-24/11/29

## v0.23.0 开发周

+ ruyi-litester [b7dde2a..005df86](https://github.com/weilinfox/ruyi-litester/compare/b7dde2a..005df86) 计 30 个 commit， 534 增加 34 删除
  + 增加 SIGINT/SIGERR 异常退出的信号处理
    + Rit 只允许单实例，故会生成一个 .rit.bash.lock
  + **增加 --lit,--mugen** 允许向 Lit 和 mugen driver 直接传递参数
  + **--match 用法**，正则表达式传参和处理有点烦，最终还是采用和 ``pytest -k`` 一样使用子字符串匹配
    + 比如某个 profile 中包括了测试 ``ab-a``、 ``ab-b``、 ``ab-f``、 ``bc-d``，而我不希望运行 ``ab-f``。使用 ``--match`` 传入表达式 ``'ab- and ( -a or -b ) or bc-'`` 或 ``'ab- and not -f or bc-'`` 或 ``'not ab-f'`` 都是可以的，注意括号前后加空格
    + 具体参见 [README_zh.md#选择性运行测试](https://github.com/weilinfox/ruyi-litester/blob/master/README_zh.md#选择性运行测试)
  + **可用的 mugen 用例运行和日志输出**
    + 甚至日志格式都是一样的，支持和上游 mugen 一样的 ``-f``、 ``-r``、 ``-x`` 参数
    + 这个 mugen driver 增加支持了前面提到的 --match 功能，只是选项改为 ``-m``
  + **ruyi-litester 单元测试**自己测试自己
    + rit-unit 测试套

## WIP

+ ruyi deb/rpm pr https://github.com/ruyisdk/ruyi/pull/238

## TODO

+ shellcheck
+ github action
+ 允许 root 用户运行测试
  + sudo -> $SUDO
  + Ruyi Lit 测试套 RIT* 环境变量
  + https://github.com/ruyisdk/ruyi/pull/236

