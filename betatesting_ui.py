import tkinter as tk
from tkinter import messagebox
import psutil
import subprocess
import customtkinter 
import base64
from base64 import decode
from PIL import Image


## gng this shi took 0.5 secs ong

messagebox.askyesnocancel(title="Software Warning.", message="Thanks For using FeatherWare's Software. Made By Flame. This Software is in Beta testing. and uses a Roblox Cheating Engine Called Rune. Continue?")

# system Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#---------------------------------

## Frame

app = customtkinter.CTk()
app.iconwindow("C:\Users\Downloads\Akurzai\df899bd700273740bf294ba2d843d871.png")
app.geometry("720x420")
app.title("Akurzai Beta")

tabview = customtkinter.CTkTabview(master=app)
tabview.pack(padx=102, pady=102)

tabview.add("Akurzai Injector tab")  # add tab at the end
tabview.add("Misc")  # add tab at the end
tabview.set("Akurzai Injector tab")  # set currently visible tab
import os
import pip
def subcall(app):
    subprocess.run(app)
def callback():
    "RobloxPlayerBeta.exe" in (i.name() for i in psutil.process_iter()) 
    if not "RobloxPlayerBeta.exe" in (i.name() for i in psutil.process_iter()):
        print("could not find the executable. try relaunching the roblox client.")
        messagebox.showinfo(title="Not Found", message="Roblox Client Was Not Found! Please Launch It!")
    if "RobloxPlayerBeta.exe" in (i.name() for i in psutil.process_iter()):
        print("found Roblox Client")
        messagebox.showinfo(title="Found", message="Roblox Client Was Found! continuing with the script.")
        app.destroy()
        subprocess.run("RuneCE.exe")
def getwindowsversion():
    RobloxSpoofer = subprocess.run("RobloxSpoofer.exe")
button1 = customtkinter.CTkButton(master=tabview.tab("Akurzai Injector tab"), text="INJECT", fg_color="black", command=callback)
button1.pack(padx=20, pady=20)
button2 = customtkinter.CTkButton(master=tabview.tab("Misc"), text="Refresh HWID", fg_color="black", command=getwindowsversion)
button2.pack(padx=20, pady=20)
app.mainloop()

