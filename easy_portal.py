import ctypes
import os
import subprocess
from tkinter import Tk, Label, Button, colorchooser, filedialog
import winreg as reg

class EasyPortal:
    def __init__(self, master):
        self.master = master
        master.title("EasyPortal - Windows GUI Customizer")

        self.label = Label(master, text="Welcome to EasyPortal")
        self.label.pack()

        self.color_button = Button(master, text="Change Background Color", command=self.change_bg_color)
        self.color_button.pack()

        self.wallpaper_button = Button(master, text="Change Wallpaper", command=self.change_wallpaper)
        self.wallpaper_button.pack()

        self.taskbar_button = Button(master, text="Hide/Show Taskbar", command=self.toggle_taskbar)
        self.taskbar_button.pack()

    def change_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            reg_path = r"Control Panel\Colors"
            with reg.OpenKey(reg.HKEY_CURRENT_USER, reg_path, 0, reg.KEY_SET_VALUE) as key:
                reg.SetValueEx(key, "Background", 0, reg.REG_SZ, color)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, color, 0)  # Update the display

    def change_wallpaper(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.bmp;*.jpg;*.jpeg;*.png")])
        if file_path:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 3)

    def toggle_taskbar(self):
        cmd = 'powershell -command "&{$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys(\'^{ESC}\')}"'
        subprocess.call(cmd, shell=True)

def main():
    root = Tk()
    portal = EasyPortal(root)
    root.mainloop()

if __name__ == "__main__":
    main()