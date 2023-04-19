import time
import datetime
import threading
import tkinter as tk

##################################################
test_title = "01 语文"
test_title_next = "02 综合测试"
start_time = [2023, 4, 20, 20, 20, 00]
end_time = [2023, 4, 19, 20, 31, 00]
##################################################

root = tk.Tk()
root.config(background='white')
root.attributes('-topmost', 'true')
root.overrideredirect(True)

lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x, y))

root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)

datetime_start_time = datetime.datetime(start_time[0],start_time[1],start_time[2],start_time[3],start_time[4],start_time[5])
datetime_end_time = datetime.datetime(end_time[0],end_time[1],end_time[2],end_time[3],end_time[4],end_time[5])

def update():
    while True:
        test_waiting = datetime_start_time - datetime.timedelta(minutes=15) < datetime.datetime.now() < datetime_start_time
        test_doing = datetime_start_time < datetime.datetime.now() < datetime_end_time - datetime.timedelta(minutes=10)
        test_ending = datetime_end_time - datetime.timedelta(minutes=10) < datetime.datetime.now() < datetime_end_time
        test_ended = datetime_end_time < datetime.datetime.now() < datetime_end_time + datetime.timedelta(minutes=3)

        if test_waiting:
            label['foreground'] = "blue"
            label['text'] = "  即将开始考试  -  " + test_title + "  "
            tick = str(datetime_start_time - datetime.datetime.now())
            tick_show = tick[:len(tick)-7]
            countdown['text'] = tick_show
        elif test_doing:
            label['foreground'] = "green"
            label['text'] = "  考试中  -  " + test_title + "  "
            countdown['text'] = time.strftime('%H:%M:%S',time.localtime(time.time()))
        elif test_ending:
            label['foreground'] = "red"
            label['text'] = "  考试即将结束  -  " + test_title + "  "
            tick = str(datetime_end_time - datetime.datetime.now())
            tick_show = tick[:len(tick)-7]
            countdown['text'] = tick_show
        elif test_ended:
            label['foreground'] = "#941e00"
            label['text'] = "  考试结束  -  " + test_title + "  "
            countdown['text'] = time.strftime('%H:%M:%S',time.localtime(time.time()))
        else:
            label['foreground'] = "black"
            if datetime.datetime.now() < datetime_start_time:
                label['text'] = "  下一场  -  " + test_title + "  "
                tick = str(datetime_start_time - datetime.datetime.now())
                tick_show = tick[:len(tick)-7]
                countdown['text'] = tick_show
            else:
                label['text'] = "  下一场  -  " + test_title_next + "  "
                countdown['text'] = time.strftime('%H:%M:%S',time.localtime(time.time()))

        time.sleep(0.1)

label = tk.Label(text="  下一场  -  " + test_title + "  ", justify="center", font=("华文细黑", 30), background='white')
label.pack()

countdown = tk.Label(text="加载中", justify="center", font=("华文细黑", 30), background='white')
countdown.pack()

update_thread = threading.Thread(target=update)
update_thread.start()

menubar = tk.Menu(root)
root.config(menu=menubar)
menubar.add_cascade(label="动态时钟")
menubar.add_cascade(label="By 0615XZX")

exitMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="退出",menu=exitMenu)
exitMenu.add_command(label="退出..", command=root.destroy)

root.mainloop()
