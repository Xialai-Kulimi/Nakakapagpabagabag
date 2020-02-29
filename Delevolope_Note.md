Developer Notes
===
Stores the link or solves to common issue.
> For the project [Nakakapagpabagabag](https://github.com/Xialai-Kulimi/Nakakapagpabagabag)

[TOC]

## Tkinter

> Easy way to buid up a GUI. But someone say it is **ugly**.

### 1.[Basic tutorial_如何使用 Python Tkinter 製作 GUI 應用程式入門教學](https://blog.techbridge.cc/2019/09/21/how-to-use-python-tkinter-to-make-gui-app-tutorial/)
### 2.side=LEFT` It's mean objects will start placing from **left** to **right**.
```python
# 以下為 top 群組
left_button = tk.Button(top_frame, text='Red', fg='red')
# 讓系統自動擺放元件，預設為由上而下（靠左）
left_button.pack(side=tk.LEFT)
```
### 3.place()
 
[Python - Tkinter place() Method](https://www.tutorialspoint.com/python/tk_place.htm)  
 
### 4.[Python GUI學習筆記(一)：使用Tkinter](https://medium.com/@yanweiliu/python-gui%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%B8%80-%E4%BD%BF%E7%94%A8tkinter-cf0dbdb78534)

Include the method to setting the title of the window.
```buildoutcfg
from tkinter import *
 
window = Tk()
 
window.title("我的第一個GUI程式")          #視窗標題
 
window.mainloop()
```

### 5.pack()

After you add a new object, please add `object.pack()` on the next line. Or it will just doesn't show up.

### 6.Setting Background

[如何設定 Tkinter 背景色](https://www.delftstack.com/zh-tw/howto/python-tkinter/how-to-set-tkinter-backgroud-color/)

## PyQt, Qt for Python 

New choice for GUI.

eg.
```python
import sys
import random
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
            "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
```

### 1.Basic Tutorial

There is a tutorial for PyQt, [從 PyQt 入門學寫 Python](https://kuanyui.github.io/2014/09/13/learn-python-via-pyqt/)

> Quite complex, but may be a better way.

### 2.**PyQt Designer.exe**

This thing gonna help me a lot.
[新手pyqt5初步安裝，及用python執行qt designer生成的UI程式碼](https://www.itread01.com/content/1547572153.html)

### 3.Keyboard
[How to create keyboard and mouse events with Pyqt widgets](https://stackoverflow.com/questions/44535561/how-to-create-keyboard-and-mouse-events-with-pyqt-widgets)