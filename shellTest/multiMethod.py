from tkinter import *

def go():
    txt = '窗口的左上角坐标为：（%s,%s）\n窗口的高度为：%s窗口的宽度为：%s' \
          % (root.winfo_x(), root.winfo_y(), root.winfo_width(), root.winfo_height())
    lable1.configure(text=txt)
    root.after(1, go)

root = Tk()

# 设置窗口大小
root.geometry('320x640+10+10')

# 设置窗口标题
root.title('方法集合')

lable1 = Label(root)
lable1.pack(expand=YES)



li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']

# 创建两个列表组件
listb = Listbox(root)
listb2 = Listbox(root)


# 第一个小部件插入数据
for item in li:
    listb.insert(0, item)

# 第二个小部件插入数据
for item in movie:
    listb2.insert(0, item)

# 讲小部件放置到主窗口中
listb.pack()
listb2.pack()

go()

# 进入消息循环
root.mainloop()


