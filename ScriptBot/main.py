from random import randint
import pyautogui
import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import *
import pyperclip
# import urllib.request
# import urllib.parse
# import re
import sys

# This is an old program I worked on just for fun, and I came back to it because a friend of mine wanted it.
# I scrapped some unfinished features (checking for updates, pause and resume buttons).
# But I recently added word/line checkboxes to define what mod will be used.
# I'll improve this project this if people seem to be interested in it.

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

'''
def popupmsg(msg):
    popup = tk.Tk()
    popup.iconbitmap('icon.ico')

    popup.resizable(False, False)
    window_height = 200
    window_width = 400
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    popup.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    popup.wm_title("YO!")

    label = ttk.Label(popup, text=msg, width=50, font=LARGE_FONT, anchor="center")
    label.place(relwidth=1, relheight=0.2, relx=0.0, rely=0.007)

    sub = ttk.Label(popup, text="Send me a message on Discord for the update!", width=50, font=NORM_FONT,
                    anchor="center")
    sub.place(relwidth=1, relheight=0.2, relx=0.0, rely=0.25)

    B1 = ttk.Button(popup, text="Continue", width=10, command=popup.destroy)
    B1.place(relheight=0.3, relwidth=.5, relx=0.5, rely=0.7, anchor="center")

    popup.mainloop()
'''


def thanks():
    popup = tk.Tk()
    # popup.iconbitmap('icon.ico')

    popup.resizable(False, False)
    window_height = 200
    window_width = 400
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    popup.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    popup.wm_title("Thank you!")

    label = ttk.Label(popup, text="App Made by CJ", width=50, font=LARGE_FONT, anchor="center")
    label.place(relwidth=1, relheight=0.2, relx=0.0, rely=0.007)

    sub = ttk.Label(popup, text="Thank you for using Script Bot. Have fun!", width=50, font=NORM_FONT, anchor="center")
    sub.place(relwidth=1, relheight=0.2, relx=0.0, rely=0.25)

    B1 = ttk.Button(popup, text="Continue", width=10, command=popup.destroy)
    B1.place(relheight=0.3, relwidth=.5, relx=0.5, rely=0.7, anchor="center")

    popup.mainloop()


'''
respData = ""

try:
    url = ''
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                            'Chrome/35.0.1916.47 Safari/537.36 '
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
    

except Exception as e:
    a = str(e)
    # print(str(e))

updateCheck = re.findall(r'<div>(.*?)</div>', str(respData))

try:
    updateResult = updateCheck[0]
except IndexError:
    updateResult = "no updates"
'''

value = randint(0, 10)
# print(value)

'''
if updateResult != "no updates":
    popupmsg(updateResult)
elif value == 5 or value == 9:
    thanks()
'''

if value == 5 or value == 9:
    thanks()

root = tk.Tk()
root.title("Script Bot 1.1")

window_height = 600
window_width = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

saveText = open("send.txt", "w", encoding='utf-8')
saveText.writelines("")
saveText.close()

scriptClicked = False
intervalClicked = False
interval = 0

sendText = open("send.txt", "r+", encoding='utf-8').read().split()
sendText2 = open("send.txt", "r+", encoding='utf-8').read().split("\n")


def spam_line():
    global exitButton
    exitButton["state"] = "disable"
    global saveText, interval
    saveText = open("send.txt", "r", encoding='utf-8')
    n = 1
    floatInterval = float(interval)
    for word in saveText:
        pyperclip.copy(word)
        pyautogui.hotkey("ctrl", "v")
        # pyautogui.typewrite(word)
        pyautogui.press("enter")
        if floatInterval.is_integer() and interval > 0:
            for i in range(int(interval), 0, -1):
                if n == len(sendText):
                    status.configure(text="DONE!")
                    root.update()
                else:
                    status.configure(text=i)
                    root.update()
                    time.sleep(1)
        elif interval < 1:
            status.configure(text="QUICK MODE")
            root.update()
        n += 1
        if n > len(sendText):
            n = n - 1
        intervalEntered.delete(1.0, "end")
        intervalEntered.insert(1.0, "LINE COUNT: " + str(n) + " out of " + str(len(sendText)))
        root.update()


def spam_word():
    global exitButton
    exitButton["state"] = "disable"
    global saveText, interval
    n = 1
    floatInterval = float(interval)
    for word in sendText:
        pyperclip.copy(word)
        pyautogui.hotkey("ctrl", "v")
        # pyautogui.typewrite(word)
        pyautogui.press("enter")
        if floatInterval.is_integer() and interval > 0:
            for i in range(int(interval), 0, -1):
                if n == len(sendText):
                    status.configure(text="DONE!")
                    root.update()
                else:
                    status.configure(text=i)
                    root.update()
                    time.sleep(1)
        elif interval < 1:
            status.configure(text="QUICK MODE")
            root.update()
        n += 1
        if n > len(sendText):
            n = n - 1
        intervalEntered.delete(1.0, "end")
        intervalEntered.insert(1.0, "WORD COUNT: " + str(n) + " out of " + str(len(sendText)))
        root.update()


def spam_message():
    text = scriptEntered.get("1.0", "end")
    if text == "Enter Your Script\n" or text == "":
        status.configure(text="Write Some Text First")
        return
    else:
        root.update()
        global interval, saveText
        try:
            interval = intervalEntered.get("1.0", "end")
            interval = float(interval)
        except ValueError:
            status.configure(text="Type A Number For The Interval")
            return
        global sendText
        saveText = open("send.txt", "w", encoding='utf-8')
        saveText.writelines(text)
        saveText.close()
        sendText = open("send.txt", "r+", encoding='utf-8').read().split()
        if (not interval.is_integer() and interval > 1) or interval < 0:
            smallerFont = tkFont.Font(family="Lucida Grande", size=14, weight="bold")
            status.configure(text="PLEASE ENTER AN INTEGER OR A NUMBER BETWEEN 0 AND 1", font=smallerFont)
            return
        status.configure(text="Starting In 2 Seconds")
        root.update()
        time.sleep(2)
    # resume_app(0)
    if lineOrWord.get() == 0:
        spam_word()
    elif lineOrWord.get() == 1:
        spam_line()


'''
def resume_app(x):
    global exitButton
    exitButton.destroy()
    exitButton = ttk.Button(root, text="Exit", width=10, state=tk.DISABLED)
    exitButton.place(relheight=0.08, relx=0.87, rely=0.905)
    global saveText, interval, pauseButton
    n = 1
    floatInterval = float(interval)
    if x == 0:
        # pauseButton.place(relheight=0.08, relwidth=.1, relx=0.67, rely=0.835)
        for word in sendText:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
            if floatInterval.is_integer() and interval > 0:
                for i in range(int(interval), 0, -1):
                    if n == len(sendText):
                        status.configure(text="DONE!")
                        root.update()
                    else:
                        status.configure(text=i)
                        root.update()
                        time.sleep(1)
            elif interval < 1:
                status.configure(text="QUICK MODE")
                root.update()
            n += 1
            if n > len(sendText):
                n = n - 1
            intervalEntered.delete(1.0, "end")
            intervalEntered.insert(1.0, "WORD COUNT: " + str(n) + " out of " + str(len(sendText)))
            root.update()
    elif x == 1:
        global buttonFont
        status.configure(text="RESUMING")
        root.update()
        pauseButton.destroy()
        buttonFont = tkFont.Font(size='20', weight='bold')
        pauseButton = tk.Button(root, text="||", width=7, command=pause_app)
        pauseButton['font'] = buttonFont
        # pauseButton.place(relheight=0.08, relwidth=.1, relx=0.67, rely=0.835)
        time.sleep(1)
        status.configure(text="RESUMING")
        root.update()
    exitButton.destroy()
    exitButton = ttk.Button(root, text="Exit", width=10, command=lambda: sys.exit(0))
    exitButton.place(relheight=0.08, relx=0.87, rely=0.905)
'''


def script_init(event):
    global scriptClicked
    if scriptClicked:
        return None
    else:
        scriptEntered.delete(1.0, "end")
        scriptClicked = True


def interval_init(event):
    global intervalClicked
    if intervalClicked:
        return None
    else:
        intervalEntered.delete(1.0, "end")
        intervalClicked = True


def clear_app():
    global scriptClicked, intervalClicked, interval, saveText
    scriptClicked = False
    intervalClicked = False
    interval = 0
    scriptEntered.delete(1.0, "end")
    scriptEntered.insert(1.0, "Enter Your Script")
    intervalEntered.delete(1.0, "end")
    intervalEntered.insert(1.0, "Interval Duration (in seconds)")
    saveText = open("send.txt", "w", encoding='utf-8')
    saveText.writelines("")
    saveText.close()
    status.configure(text="CLEARED!")
    root.update()
    time.sleep(1)
    status.configure(text="SCRIPT BOT")
    root.update()


'''
def pause_app():
    global buttonFont
    global pauseButton
    status.configure(text="PAUSED")
    root.update()
    pauseButton.destroy()
    buttonFont = tkFont.Font(size='40', weight='bold')
    pauseButton = tk.Button(root, text="▶", width=7, command=lambda: resume_app(1))
    pauseButton['font'] = buttonFont
    # pauseButton.place(relheight=0.08, relwidth=.1, relx=0.67, rely=0.835)
'''

scriptEntered = tk.Text(root, width=50, height=22)
scriptEntered.grid(column=0, row=0, pady=(50, 15), padx=(100, 0))
scriptEntered.insert(1.0, "Enter Your Script")

intervalEntered = tk.Text(root, width=50, height=2)
intervalEntered.grid(column=0, row=1, padx=(100, 0))
intervalEntered.insert(1.0, "Interval Duration (in seconds)")

lineOrWord = IntVar()

lineCB = ttk.Checkbutton(root, text="Line", width=10, variable=lineOrWord, onvalue=1, offvalue=0)
lineCB.place(relheight=0.08, relx=0.2, rely=0.81)

wordCB = ttk.Checkbutton(root, text="Word", width=10, variable=lineOrWord, onvalue=0, offvalue=1)
wordCB.place(relheight=0.08, relx=0.2, rely=0.86)
lineOrWord.set(1)

startButton = ttk.Button(root, text="Start", width=30, command=spam_message)
startButton.place(relwidth=0.3, relheight=0.15, relx=0.35, rely=0.8)

clearButton = ttk.Button(root, text="Clear", width=10, command=clear_app)
clearButton.place(relheight=0.08, relx=0.011, rely=0.905)

buttonFont = tkFont.Font(size='20', weight='bold')

# pauseButton = tk.Button(root, text="||", width=7, command=pause_app)
# pauseButton['font'] = buttonFont
# pauseButton.place(relheight=0.08, relwidth=.1, relx=0.67, rely=0.835)

exitButton = ttk.Button(root, text="Exit", width=10, command=lambda: sys.exit(0))
exitButton.place(relheight=0.08, relx=0.87, rely=0.905)

fontStyle = tkFont.Font(family="Lucida Grande", size=24, weight="bold")

status = ttk.Label(root, text="SCRIPT BOT", width=50, font=fontStyle, anchor="center")
status.place(relwidth=1, relheight=0.068, relx=0.0, rely=0.007)

scriptEntered.bind("<Button-1>", script_init)
intervalEntered.bind("<Button-1>", interval_init)

scrollbar = Scrollbar(root)
scrollbar.grid(column=1, row=0, sticky='ns', pady=(50, 15))
scriptEntered.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=scriptEntered.yview)

# root.iconbitmap('icon.ico')
root.resizable(False, False)
root.mainloop()
