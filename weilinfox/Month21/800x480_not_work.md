# 800x480 屏幕无法在荔枝派 4A 使用

[原 issue](https://github.com/revyos/revyos/issues/117)

我这边有一块微雪的 7inch HDMI LCD (B) Rev2.1，显示分辨率为 800x480 pixel，屏驱动为 TFP401APZP。

某种程度上复现了这个问题。

首先验证该显示屏可以正常工作。上电后使用 HDMI 连接松下 CF-SZ6， Archlinux 正常识别到显示屏并显示。

```
$ xrandr --display :0
Screen 0: minimum 320 x 200, current 2720 x 1200, maximum 16384 x 16384
eDP-1 connected primary 1920x1200+0+0 (normal left inverted right x axis y axis) 264mm x 166mm
   1920x1200     60.08*+  59.88    59.95    48.06
   <此处省略余下的 mode>
DP-1 connected 800x480+1920+0 (normal left inverted right x axis y axis) 150mm x 100mm
   800x480       65.68*+
DP-2 disconnected (normal left inverted right x axis y axis)
```

添加 --verbose 参数后信息如下：

```
DP-1 connected 800x480+1920+0 (0x503) normal (normal left inverted right x axis y axis) 150mm x 100mm
        Identifier: 0x42
        Timestamp:  9696320
        Subpixel:   unknown
        Gamma:      1.0:1.0:1.0
        Brightness: 1.0
        Clones:    
        CRTC:       1
        CRTCs:      0 1 2
        Transform:  1.000000 0.000000 0.000000
                    0.000000 1.000000 0.000000
                    0.000000 0.000000 1.000000
                   filter: 
        EDID: 
                00ffffffffffff000481040001000000
                01110103800f0a000a00000000000000
                00000000000001010101010101010101
                010101010101800c208030e02d102830
                d3006c44000000180000001000000000
                00000000000000000000000000100000
                00000000000000000000000000000010
                00000000000000000000000000000017
        _KDE_SCREEN_INDEX: 2 
        HDCP Content Type: HDCP Type0 
                supported: HDCP Type0, HDCP Type1
        Content Protection: Undesired 
                supported: Undesired, Desired, Enabled
        Colorspace: Default 
                supported: Default, SMPTE_170M_YCC, BT709_YCC, XVYCC_601, XVYCC_709, SYCC_601, opYCC_601, opRGB, BT2020_CYCC, BT2020_RGB, BT2020_YCC, DCI-P3_RGB_D65, DCI-P3_RGB_Theater
        content type: No Data 
                supported: No Data, Graphics, Photo, Cinema, Game
        max bpc: 12 
                range: (6, 12)
        Broadcast RGB: Automatic 
                supported: Automatic, Full, Limited 16:235
        audio: auto 
                supported: force-dvi, off, auto, on
        subconnector: HDMI 
                supported: Unknown, VGA, DVI-D, HDMI, DP, Wireless, Native
        link-status: Good 
                supported: Good, Bad
        CTM:    1.000000 0.000000 0.000000
                0.000000 1.000000 0.000000
                0.000000 0.000000 1.000000
        CONNECTOR_ID: 107 
                supported: 107
        non-desktop: 0 
                range: (0, 1)
  800x480 (0x503) 32.000MHz -HSync -VSync *current +preferred
        h: width   800 start  840 end  888 total  928 skew    0 clock  34.48KHz
        v: height  480 start  493 end  496 total  525           clock  65.68Hz
```

附加信息，应当是只支持这一种显示分辨率：

```bash
$ hexdump /sys/class/drm/card1-DP-1/edid 
0000000 ff00 ffff ffff 00ff 8104 0004 0001 0000
0000010 1101 0301 0f80 000a 000a 0000 0000 0000
0000020 0000 0000 0000 0101 0101 0101 0101 0101
0000030 0101 0101 0101 0c80 8020 e030 102d 3028
0000040 00d3 446c 0000 1800 0000 1000 0000 0000
0000050 0000 0000 0000 0000 0000 0000 1000 0000
0000060 0000 0000 0000 0000 0000 0000 0000 1000
0000070 0000 0000 0000 0000 0000 0000 0000 1700
0000080
$ cat /sys/class/drm/card1-DP-1/modes 
800x480
```

连接荔枝派 4A 8G 版本后，上电无显示：

```bash
$ hexdump /sys/class/drm/card0-HDMI-A-1/edid
0000000 ff00 ffff ffff 00ff 8104 0004 0001 0000
0000010 1101 0301 0f80 000a 000a 0000 0000 0000
0000020 0000 0000 0000 0101 0101 0101 0101 0101
0000030 0101 0101 0101 0c80 8020 e030 102d 3028
0000040 00d3 446c 0000 1800 0000 1000 0000 0000
0000050 0000 0000 0000 0000 0000 0000 1000 0000
0000060 0000 0000 0000 0000 0000 0000 0000 1000
0000070 0000 0000 0000 0000 0000 0000 0000 1700
0000080
$ cat /sys/class/drm/card0-HDMI-A-1/modes
```

用其他显示屏登陆到桌面后再重新连接，获取 xrandr 输出可以看到没有可用的模式：

```
$ xrandr --display :0 --verbose
xrandr: Output HDMI-1 is not disconnected but has no modes
Screen 0: minimum 0 x 0, current 1024 x 768, maximum 4096 x 4096
HDMI-1 connected (normal left inverted right x axis y axis)
        Identifier: 0x3f
        Timestamp:  1065943
        Subpixel:   unknown
        Clones:    
        CRTCs:      1
        Transform:  1.000000 0.000000 0.000000
                    0.000000 1.000000 0.000000
                    0.000000 0.000000 1.000000
                   filter: 
        EDID: 
                00ffffffffffff000481040001000000
                01110103800f0a000a00000000000000
                00000000000001010101010101010101
                010101010101800c208030e02d102830
                d3006c44000000180000001000000000
                00000000000000000000000000100000
                00000000000000000000000000000010
                00000000000000000000000000000017
        max bpc: 0 
                range: (8, 16)
        link-status: Good 
                supported: Good, Bad
        non-desktop: 0 
                range: (0, 1)
```

若手动指定，则报 ``xrandr: Configure crtc 1 failed``：

```bash
$ xrandr --display :0 --newmode "800x480_65.68" 32.00 800 840 888 928 480 493 496 525 -hsync -hsync
$ xrandr --display :0 --addmode HDMI-1 800x480_65.68
$ xrandr --display :0 --output HDMI-1  --mode 800x480_65.68
xrandr: Configure crtc 1 failed
```

有一种情况可以显示，即只连接 HDMI 线，不上电。此时荔枝派 4A 识别到 HDMI 插入但无法读取 edid 信息，默认以 1024x768 输出：

```
$ hexdump /sys/class/drm/card0-HDMI-A-1/edid
$ cat /sys/class/drm/card0-HDMI-A-1/modes 
1024x768
800x600
800x600
848x480
640x480
$ xrandr --display :0 --verbose
Screen 0: minimum 0 x 0, current 1024 x 768, maximum 4096 x 4096
HDMI-1 connected 1024x768+0+0 (0x40) normal (normal left inverted right x axis y axis) 0mm x 0mm
        Identifier: 0x3f
        Timestamp:  1633160
        Subpixel:   unknown
        Gamma:      1.0:1.0:1.0
        Brightness: 1.0
        Clones:    
        CRTC:       1
        CRTCs:      1
        Transform:  1.000000 0.000000 0.000000
                    0.000000 1.000000 0.000000
                    0.000000 0.000000 1.000000
                   filter: 
        max bpc: 0 
                range: (8, 16)
        link-status: Good 
                supported: Good, Bad
        non-desktop: 0 
                range: (0, 1)
  1024x768 (0x40) 65.000MHz -HSync -VSync *current
        h: width  1024 start 1048 end 1184 total 1344 skew    0 clock  48.36KHz
        v: height  768 start  771 end  777 total  806           clock  60.00Hz
  800x600 (0x41) 40.000MHz +HSync +VSync
        h: width   800 start  840 end  968 total 1056 skew    0 clock  37.88KHz
        v: height  600 start  601 end  605 total  628           clock  60.32Hz
  800x600 (0x42) 36.000MHz +HSync +VSync
        h: width   800 start  824 end  896 total 1024 skew    0 clock  35.16KHz
        v: height  600 start  601 end  603 total  625           clock  56.25Hz
  848x480 (0x43) 33.750MHz +HSync +VSync
        h: width   848 start  864 end  976 total 1088 skew    0 clock  31.02KHz
        v: height  480 start  486 end  494 total  517           clock  60.00Hz
  640x480 (0x44) 25.175MHz -HSync -VSync
        h: width   640 start  656 end  752 total  800 skew    0 clock  31.47KHz
        v: height  480 start  490 end  492 total  525           clock  59.94Hz
```

再上电显示屏，显示屏将显示桌面的左上角部分。可见显示屏功能正常，但平常使用不可能这样。

RevyOS 版本：

```bash
$ cat /etc/revyos-release
BUILD_ID=20250123_195216
BUILD_DATE=20250123
BOARD_NAME=lpi4a
RELEASE_ID=20250123
COMMIT_ID=66c225950886e61d142d39d26acc493a24960a92
RUNNER_ID=12921029931
```

类似的工控屏分辨率： 480x272、 1024x600、 1280x800。没有设备暂无法一一测试。

