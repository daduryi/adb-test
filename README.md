### 添加AVD虚拟器
Android Studio 如何添加AVD模拟器
- 打开Android Studio，在右上角选择AVD Manager。
- 弹出窗口，选择左下角 “Create Virtual Device”

https://jingyan.baidu.com/article/ea24bc392f3e69da62b331f0.html

### 查看已有虚拟器
~/Library/Android/sdk/tools/emulator

```bash
emulator -list-avds
```

- AVD模拟设备所在的目录~/.android/avd/
- 每个设备会有一个@AVD_name.ini文件，和一个@AVD_name.avd目录

### 启动虚拟器
emulator @AVD_name

启动脚本emu.sh
```bash
pushd ${ANDROID_HOME}/tools
emulator -avd 本机的模拟器
popd
```

也可以在android studio中完成avd list 和 avd run.

### adb文档
[adb命令详解及操作大全](https://juejin.im/post/5b5683bcf265da0f9b4dea96#heading-97)
[Android Debug Bridge](https://developer.android.com/studio/command-line/adb)
[awesome-adb](https://github.com/mzlogin/awesome-adb)


### 测试(来自上边操作大全)
##### 屏幕截取
```bash
adb shell screencap -p /sdcard/sc.png
adb pull /sdcard/sc.png
```

##### 查看设备型号
```bash
adb shell getprop ro.product.model
```

##### 返回键
```bash
adb shell input keyevent 4
```

##### root权限运行虚拟机, 真机必须root
```bash
LixnMac:adb-test lixn$ adb shell ifconfig | grep Mask
ifconfig: ioctl 8927: Permission denied
```
```bash
adb root
```

##### 进入adb shell
```bash
LixnMac:adb-test lixn$ adb shell
generic_x86:/ # getprop ro.product.model
Android SDK built for x86
generic_x86:/ #
generic_x86:/ # su root
generic_x86:/ # ifconfig
generic_x86:/ # input --help
```

##### 部分input事件
```bash 
generic_x86:/ input swipe 500 500 500 200   # 滑屏
adb shell input swipe 200 200 201 201 2000 //在小的距离内，从（200，200）的位置滑动到（201，201）的位置，连续滑动2000毫秒，页面表现为长按的效果
input tap x y            # 点击
input touchscreen swipe x y x y duration(ms)  # 长按某点
input keyevent keyCode  # 单击某个键
input keyevent --longpress keyCode    # 长按某个键
```


##### monkey
```bash
adb shell monkey -p <packagename> -v 500
```
表示向 `packagename` 指定的应用程序发送 500 个伪随机事件。 Monkey 的详细用法参考 [官方文档](https://developer.android.com/studio/test/monkey.html)。

### dump页面内容
adb shell uiautomator dump /sdcard/uidump.xml

### 某blog
https://blog.csdn.net/slaron/article/details/78294833

### 豆瓣顶贴程序

### 关闭虚拟机
adb emu kill

### 通过 python 调用 adb 命令实现用元素名称、id、class 定位元素
https://testerhome.com/topics/1047

### adb shell input text 完美支持中文输入
https://blog.csdn.net/slimboy123/article/details/54140029
使用ADBKeyBoard.apk输入法


### 启动app
https://blog.csdn.net/ezconn/article/details/99885715

### 如何定位屏幕的坐标
在手机开发者选项，开启指针位置功能，就可以实时定位屏幕坐标了

### 操作和获取剪切板
https://github.com/majido/clipper
https://blog.csdn.net/lonewolf521125/article/details/93521197


# 引申
### Android设备唯一标识 
IMEI，MEID，ESN，IMSI,android_id 之间的区别

