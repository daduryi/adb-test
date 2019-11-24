import subprocess
import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET


class Element(object):
    """
    通过元素定位,需要Android 4.0以上
    """
    def __init__(self):
        """
        初始化，获取系统临时文件存储目录，定义匹配数字模式
        """
        # self.tempFile = tempfile.gettempdir()
        self.tempFile = '.'
        self.pattern = re.compile(r"\d+")

    def __uidump(self):
        """
        获取当前Activity控件树
        """
        os.system("adb shell uiautomator dump /sdcard/uidump.xml")
        os.system("adb pull /sdcard/uidump.xml " + self.tempFile)

    def __element(self, attrib, name):
        """
        同属性单个元素，返回单个坐标元组
        """
        self.__uidump()
        tree = ET.ElementTree(file=self.tempFile + "/uidump.xml")
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if elem.attrib[attrib] == name:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])

                return Xpoint, Ypoint

    def __elementRe(self, attrib, name):
        """
        同属性单个元素，返回单个坐标元组
        """
        self.__uidump()
        tree = ET.ElementTree(file=self.tempFile + "/uidump.xml")
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if name in elem.attrib[attrib]:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])

                return Xpoint, Ypoint


    def __elements(self, attrib, name):
        """
        同属性多个元素，返回坐标元组列表
        """
        list = []
        self.__uidump()
        tree = ET.ElementTree(file=self.tempFile + "/uidump.xml")
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if elem.attrib[attrib] == name:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
                list.append((Xpoint, Ypoint))
        return list

    def findElementByName(self, name):
        """
        通过元素名称定位
        usage: findElementByName(u"相机")
        """
        return self.__element("text", name)

    def find(self):
        '''
        查找符合某个包含关系的element
        :return: 
        '''

    def findElementByReName(self, name):
        """
        通过元素名称定位
        usage: findElementByName(u"相机")
        """
        return self.__elementRe("text", name)

    def findElementsByName(self, name):
        return self.__elements("text", name)

    def findElementByClass(self, className):
        """
        通过元素类名定位
        usage: findElementByClass("android.widget.TextView")
        """
        return self.__element("class", className)

    def findElementsByClass(self, className):
        return self.__elements("class", className)

    def findElementById(self, id):
        """
        通过元素的resource-id定位
        usage: findElementsById("com.android.deskclock:id/imageview")
        """
        return self.__element("resource-id",id)

    def findElementsById(self, id):
        return self.__elements("resource-id",id)


class Event(object):
    def __init__(self):
        os.system("adb wait-for-device ")
        self.default_time = 0.5
        self.touch_time = None
        self.text_time = None
        self.touch_back_time = None
        self.touch_home_time = None
        self.touch_time = None
        self.swipe_time = 0.3
        self.width, self.height = self.getSize()

    def startApp(self, package, activity):
        os.system('adb shell am start {}/.{}'.format(package, activity))

    def getSize(self):

        p = subprocess.Popen(['adb shell wm size'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                             universal_newlines=True)
        res = p.communicate()
        print(res[0].split(':')[-1].strip())
        width, height = res[0].split(':')[-1].strip().split('x')
        return int(width), int(height)

    def touch(self, dx, dy):
        """
        触摸事件
        usage: touch(500, 500)
        """
        os.system("adb shell input tap " + str(dx) + " " + str(dy))
        time.sleep(self.touch_time or self.default_time)

    def text(self, text):
        os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{}"'.format(text))
        time.sleep(self.text_time or self.default_time)

    def touchBack(self):
        os.system('adb shell input keyevent 4')
        time.sleep(self.touch_back_time or self.default_time)

    def touchHome(self):
        os.system('adb shell input keyevent 3')
        time.sleep(self.touch_home_time or self.default_time)

    def swipe(self, x0, y0, x1, y1):
        os.system('adb shell input swipe {} {} {} {}'.format(x0, y0, x1, y1))

    def swipe_int_wrapper(self, x0, y0, x1, y1):
        return self.swipe(int(x0), int(y0), int(x1), int(y1))

    def swipe_up(self, y):
        if y < 1:
            y = self.height * y
        self.swipe_int_wrapper(self.width * 0.7, self.height * 0.8, self.width * 0.7, self.height - y)

    def swipe_down(self, y):
        if y < 1:
            y = self.height * y
        self.swipe_int_wrapper(self.width * 0.7, self.height * 0.3, self.width * 0.7, self.height + y)

    def swipe_left(self, y):
        if y < 1:
            y = self.width * y
        self.swipe_int_wrapper(self.width * 0.7, self.height * 0.3, self.width * 0.7, self.height - y)

    def swipe_right(self, y):
        if y < 1:
            y = self.width * y
        self.swipe_int_wrapper(self.width * 0.7, self.height * 0.3, self.width * 0.7, self.height - y)

def test():
    element = Element()
    evevt = Event()

    e1 = element.findElementByName(u"1号店")
    evevt.touch(e1[0], e1[1])
    time.sleep(2)

    e2 = element.findElementByName(u"手机充值")
    evevt.touch(e2[0], e2[1])




