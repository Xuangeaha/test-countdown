import time
import threading
import tkinter as tk
from datetime import datetime

##################################################
test_title = "01 语文"
start_time = [2023, 4, 20, 8, 00, 00]
##################################################

root = tk.Tk()
root.config(background='white')
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

def update():
    while True:
        tick = str(datetime(start_time[0],start_time[1],start_time[2],start_time[3],start_time[4],start_time[5]) - datetime.now())
        tick_show = tick[:len(tick)-7]
        print(test_title, datetime.now(), start_time, tick, tick_show)
        countdown['text'] = tick_show
        time.sleep(0.05)

label = tk.Label(text="距 二模 | " + test_title + "：", justify="center", font=("华文细黑", 20), background='white').pack()

countdown = tk.Label(text="加载中", justify="center", font=("华文细黑", 20), background='white')
countdown.pack()

update_thread = threading.Thread(target=update)
update_thread.start()

root.mainloop()
