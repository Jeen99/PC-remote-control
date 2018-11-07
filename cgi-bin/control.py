#!/usr/bin/env python3
# Отправляет команду ОС для управления музыкой (вкл/выкл, <<, >>, +, -)
import cgi
import html
import win32api, win32con    # pip install pywin32
import os

# import time
# time.sleep(5)
# import sys
# import codecs
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # смена кодировки

# VK_MEDIA_NEXT_TRACK = 176
# VK_MEDIA_PLAY_PAUSE = 179
# VK_MEDIA_PREV_TRACK = 177

# VK_VOLUME_DOWN = 174
# VK_VOLUME_MUTE = 173
# VK_VOLUME_UP	 = 175
# win32api.ExitWindows() Выйти из системы
# ExitWindowsEx(win32con.EWX_POWEROFF) # or (win32con.EWX_SHUTDOWN) # Выключить ПК

form = cgi.FieldStorage()
params = form.getfirst("par","None")
params = html.escape(params)
# print("Content-type: text/html\n")

if params == "prev":
	win32api.keybd_event(win32con.VK_MEDIA_PREV_TRACK,0,0,0)
elif params == "next":
	win32api.keybd_event(win32con.VK_MEDIA_NEXT_TRACK,0,0,0)
elif params == "play":
    win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE,0,0,0)
elif params == "up":
	win32api.keybd_event(win32con.VK_VOLUME_UP,0,0,0)
elif params == "down":
	win32api.keybd_event(win32con.VK_VOLUME_DOWN,0,0,0)
elif params == "mute":
	win32api.keybd_event(win32con.VK_VOLUME_MUTE,0,0,0)
elif params == "shutdown":
	os.system("shutdown /h /f")
	#win32api.ExitWindowsEx(win32con.EWX_SHUTDOWN)
else:
	print("Content-type: text/html\n")
	os.system(params)
	# print("""<html><body><h1>""")
	# print(params)
	# print("""</h1></body></html>""")
	# print("""<html><body><h1>"Hello"</h1></body></html>""")
	