# coding = UTF-8

'''_________________界面程序所用的模块_________________
'''

import sys


import win32gui
import win32con
import winreg
import  os
from PyQt6 import QtGui
from PyQt6.QtMultimedia import *
from PyQt6.QtMultimediaWidgets import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class bootAutoStart():
    def __init__(self):
        pass

    '''创建注册表值'''

    def create_value(self):


        try:
            # 查询注册表启动项路径
            first_test = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER,
                                          r'Software\Microsoft\Windows\CurrentVersion\Run',
                                          0,
                                          winreg.KEY_ALL_ACCESS)
            # 第一次引发查询注册表值的异常,此后不引发
            winreg.QueryValueEx(winreg.HKEY_CURRENT_USER,
                                'TC')
        except:
            # 异常处理：创建注册表值path.abspath(__file__)
            value_path = os.getcwd()  # 获取当前文件路径,用"\"表示
            land_VP = value_path + "\TC.exe"
            winreg.SetValueEx(first_test,
                              'TC',
                              0,
                              1,
                              land_VP)
            winreg.CloseKey(first_test)  # 关闭路径
        else:
            # 异常处理后结束此程序
            winreg.CloseKey(first_test)  # 与上同,不引发异常


    '''删除注册表值'''

    def delete_value(self):
        try:
            # 查询注册表启动项路径
            second_test = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER,
                                          r'Software\Microsoft\Windows\CurrentVersion\Run',
                                          0,
                                          winreg.KEY_ALL_ACCESS)

        except:
            pass

        else:

            winreg.DeleteValue(second_test,
                           'TC')
            winreg.CloseKey(second_test)

'''________________回调, WorkerW显示________________
'''

def iwork(hwnd, lpm):
    # 获取SHELLDll_DefView句柄及定位到WorkerW-1
    s = win32gui.FindWindowEx(hwnd, 0, 'SHELLDll_DefView', None)
    if s != 0:
        # 获取WorkerW-2的句柄并隐藏
        c = win32gui.FindWindowEx(0, hwnd, 'WorkerW', None)
        win32gui.ShowWindow(c, win32con.SW_HIDE)
        return True


'''________________创建界面显示功能_________________
'''

class myWindow(QWidget, QSystemTrayIcon, bootAutoStart):
    def __init__(self):
        super().__init__()
        '''_________________初始化窗口__________________
        '''
        self.setWindowTitle("TC")
        self.setFixedSize(400, 300)  # 设置固定大小
        self.setWindowIcon(QIcon("./img_main.ico"))
        self.show()


        '''___________________实例化____________________
        '''
        # 组件实例化
        self.init_layout()
        self.init_button()
        self.init_buttons_UI()
        self.init_stackwidget()
        self.but_link()
        self.function_link()


    '''___________________初始化布局__________________
    '''

    def init_layout(self):
        # 全局布局
        self.global_layout = QHBoxLayout()
        # 左菜单栏布局
        self.menu_bar_layout = QVBoxLayout()
        self.global_layout.addLayout(self.menu_bar_layout, 150)
        # 右内容栏布局
        self.content_bar_layout = QStackedLayout()
        self.global_layout.addLayout(self.content_bar_layout, 250)
        # 配置全局布局
        self.setLayout(self.global_layout)

    '''_______________初始化菜单栏按钮________________
    '''

    def init_button(self):
        # 菜单按钮
        self.menu_button = QPushButton("菜单")
        self.menu_bar_layout.addWidget(self.menu_button)
        # 任务栏按钮
        self.taskbar_button = QPushButton("任务栏")
        self.menu_bar_layout.addWidget(self.taskbar_button)
        # 动态壁纸按钮啊
        self.wallpaper_button = QPushButton("动态壁纸")
        self.menu_bar_layout.addWidget(self.wallpaper_button)
        # 桌面宠物按钮
        self.deskpet_button = QPushButton("桌面助手")
        self.menu_bar_layout.addWidget(self.deskpet_button)
        # 添加弹簧
        self.menu_bar_layout.addStretch()

    '''_______________初始化堆叠窗口__________________
    '''

    def init_stackwidget(self):
        # 创建堆叠窗口
        self.stackwidget = QStackedWidget()
        self.content_bar_layout.addWidget(self.stackwidget)
        # 接收窗口
        self.stackwidget.addWidget(self.menubar_ui)
        self.stackwidget.addWidget(self.taskbar_ui)
        self.stackwidget.addWidget(self.wallpaper_ui)
        self.stackwidget.addWidget(self.deskpet_ui)

    '''_____________初始化菜单栏界面UI________________
    '''

    def init_buttons_UI(self):

        # 菜单UI
        self.menubar_ui = QWidget()
        self.m_lay = QVBoxLayout(self.menubar_ui)
        ##开机自启动按钮
        self.boot_auto_start_but = QCheckBox("开机自启动")
        self.m_lay.addWidget(self.boot_auto_start_but)

        ##最小化托盘按钮
        self.tray_mini_but = QCheckBox("最小化托盘")
        self.m_lay.addWidget(self.tray_mini_but)
        self.m_lay.addStretch()

        # 任务栏UI
        self.taskbar_ui = QWidget()
        self.t_lay = QVBoxLayout(self.taskbar_ui)
        #任务栏UI按钮
        self.tb_clarity_but = QCheckBox("任务栏透明")
        self.t_lay.addWidget(self.tb_clarity_but)
        self.t_lay.addStretch()

        # 动态壁纸UI
        self.wallpaper_ui = QWidget()
        self.w_lay = QVBoxLayout(self.wallpaper_ui)
        ##动态壁纸UI按钮
        self.wp_add_but = QPushButton("自定义动态壁纸")
        self.w_lay.addWidget(self.wp_add_but)
        self.w_lay.addStretch()

        # 桌面宠物UI
        self.deskpet_ui = QWidget()
        self.d_lay = QVBoxLayout(self.deskpet_ui)
        #桌面宠物UI按钮
        self.dp_enable_but = QPushButton("启用桌面助手")
        self.d_lay.addWidget(self.dp_enable_but)
        self.d_lay.addStretch()


    '''_______________菜单栏按钮链接__________________
    '''

    def but_link(self):
        # 菜单按钮链接
        self.menu_button.clicked.connect(self.UI_menu)
        # 任务栏按钮链接
        self.taskbar_button.clicked.connect(self.UI_taskbar)
        # 动态壁纸按钮链接
        self.wallpaper_button.clicked.connect(self.UI_wallpaper)
        # 桌面宠物按钮链接
        self.deskpet_button.clicked.connect(self.UI_deskpet)

    '''___________________界面排序____________________
    '''

    #菜单界面
    def UI_menu(self):
        self.stackwidget.setCurrentIndex(0)
    #任务栏界面
    def UI_taskbar(self):
        self.stackwidget.setCurrentIndex(1)
    #动态壁纸界面
    def UI_wallpaper(self):
        self.stackwidget.setCurrentIndex(2)
    #桌面宠物界面
    def UI_deskpet(self):
        self.stackwidget.setCurrentIndex(3)


    '''_________________功能按钮链接__________________
    '''

    def function_link(self):
        # 开机自启动功能链接(BAS为BootAutoStart)
        self.boot_auto_start_but.clicked.connect(self.open_BAS)
        # 最小化到托盘功能链接
        self.tray_mini_but.clicked.connect(self.tray_mini)
        # 自定义动态壁纸按钮功能链接
        self.wp_add_but.clicked.connect(self.def_wallpaper)


    '''_______________开机自启动功能__________________
    '''

    def open_BAS(self):

        # BAS为boot-auto-start
        if self.boot_auto_start_but.isChecked():

            self.create_value()
        else:
            self.delete_value()




    '''_____________最小化到托盘功能__________________
    '''

    def tray_mini(self):
        # 检查是否被点击
        if self.tray_mini_but.isChecked():
            # 创建托盘最小化程序
            self.tray_exe = QSystemTrayIcon(self)
            self.tray_exe.setIcon(QIcon("./img_main.ico"))
            # 显示托盘程序
            self.tray_exe.show()
            # 忽略主窗口(或最后一个窗口)关闭的事件
            QApplication.setQuitOnLastWindowClosed(False)
            # 创建菜单栏选项
            self.tray_menu = QMenu()
            # 建立action与链接程序
            self.enter_app = QAction("进入应用", triggered=self.showNormal)
            self.exit_app = QAction("退出程序", triggered=sys.exit)
            self.tray_menu.addAction(self.enter_app)
            self.tray_menu.addAction(self.exit_app)
            self.tray_exe.setContextMenu(self.tray_menu)
        else:
            # 隐藏托盘程序,减少报错
            try:
                self.tray_exe.hide()
            except:
                pass
            else:
                pass

    '''______________自定义动态壁纸功能________________
    '''

    def def_wallpaper(self):
        # 获取Progman的句柄
        self.progman = win32gui.FindWindow('Progman', None)
        # 向Progman发送0x52c消息
        win32gui.SendMessageTimeout(self.progman, 0x52c, 0, 0, 0, 100)
        '''播放器窗口设置'''
        # 设置播放窗口
        self.wid = QVideoWidget()
        # 配置播放器通到与视频播放通道
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wid)
        # 设置播放文件路径
        self.path = QFileDialog.getOpenFileName(None)[0]
        self.dirpath = QUrl.fromLocalFile(self.path)

        if self.path == '':
            #清理无用的进程, 清理内存
            del self.wid
            del self.player
            del self.path
            del self.dirpath
            pass


        else:

            self.player.setSource(self.dirpath)
            # 设置循环及播放与全屏播放
            self.player.setLoops(-1)
            self.wid.setFullScreen(True)
            # 设置视频画面的宽高比
            self.wid.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatioByExpanding)

            '''动态壁纸窗口设置'''

            # 获取播放器的标题
            self.wallpaper = win32gui.FindWindow('Qt642QwindowIcon', None)
            # 将播放器窗口设置为Progman的子窗口
            win32gui.SetParent(self.wallpaper, self.progman)
            # 使用回调函数隐藏WorkerW-2
            win32gui.EnumWindows(iwork, 0)
            # 视频播放
            self.player.play()


if __name__ == '__main__':
    # 执行窗口的显示
    app = QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec())
