'''
Created on 2013-7-12

@author: SuShiting
'''
import win32gui,win32con
import vim

def setWindowTransp():
    hwnd=win32gui.FindWindow("Vim",None)
    if hwnd:
        s=win32gui.GetWindowLong(hwnd,win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, s|win32con.WS_EX_LAYERED)
        opCode=vim.eval("g:alphaOp")
        alphaValue=int(vim.eval("g:alphaValue"))
        stepValue=int(vim.eval("g:stepValue"))

        if opCode=="plus":
            alphaValue=alphaValue+stepValue
        else:
            alphaValue=alphaValue-stepValue
        
        if alphaValue<200 or alphaValue>255:
            vim.command("echo 'AlphaValue exceed!'")
        else:
            vim.command("let g:alphaValue="+str(alphaValue))
            win32gui.SetLayeredWindowAttributes(hwnd, 0, alphaValue,win32con.LWA_ALPHA)

setWindowTransp()


