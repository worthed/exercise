'''
当单击open菜单时，调用openFile方法来显示对话框以便使用askopenfilename函数打开一个文件。当用户选择一个文件之后，该
文件的文件名被返回并被用来打开这个文件以读取数据。这个程序从文件读取数据并将这个数据插入Text小构件中。

当单击save菜单时，调用saveFile方法来显示保存为对话框以便使用asksaveasfilename函数保存一个文件。当用户输入或选择一个文件
之后，该文件的文件名被返回并被用来打开这个文件以写入数据。这个程序从Text小构件读取数据并将这个数据写入文件中。
'''

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


class fileEditor:
    def __init__(self):
        window = Tk()
        window.title = ("Simple Text Editor")

        #创建菜单
        menubar = Menu(window)  #菜单控件；显示菜单栏,下拉菜单和弹出菜单
        window.config(menu = menubar)

        #创建下拉菜单
        operationMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = 'File', menu = operationMenu)
        operationMenu.add_command(label = "Open", command = self.openFile)
        operationMenu.add_command(label="Save", command=self.saveFile)

        #添加工具栏边框
        frame0 = Frame(window)  #框架控件；在屏幕上显示一个矩形区域，多用来作为容器
        frame0.grid(row = 1, column = 1, sticky = W)

        #创建图标
        openImage = PhotoImage(file = "/Users/wangyuxiang/PycharmProjects/practice/webapps1/practice/images/open.gif",width=20,height=20) #注意/符号是否需要转义
        saveImage = PhotoImage(file = "/Users/wangyuxiang/PycharmProjects/practice/webapps1/practice/images/save.gif",width=20,height=20)

        Button(frame0, image = openImage, command = self.openFile).grid(row = 1, column = 1, sticky = W)
        Button(frame0, image = saveImage, command=self.openFile).grid(row=1, column=1)  # 按钮控件；在程序中显示按钮

        frame1 = Frame(window) #编辑器窗口
        frame1.grid(row = 2, column = 1)

        scrollbar = Scrollbar(frame1)  #滚动条控件，当内容超过可视化区域时使用，如列表框
        scrollbar.pack(side = RIGHT, fill = Y)
        self.text = Text(frame1, width = 40, height = 20, wrap = WORD, yscrollcommand = scrollbar.set)  #文本控件；用于显示多行文本
        self.text.pack()
        scrollbar.config(command = self.text.yview)

        window.mainloop() #创建事件循环

    def openFile(self):
        filenameforReading = askopenfilename()
        infile = open(filenameforReading, "r")
        self.text.insert(END, infile.read())  #读取所有内容
        infile.close()

    def saveFile(self):
        filenameforWriting = asksaveasfilename()
        outfile = open(filenameforWriting, "w")
        outfile.write(self.text.get(1.0, END))
        outfile.close()

fileEditor()
