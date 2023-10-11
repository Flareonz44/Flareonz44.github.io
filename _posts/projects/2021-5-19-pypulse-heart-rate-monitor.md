---
layout: post
title: "PyPulse - SemiAutomatic Heart Rate Monitor"
author: Flareonz44
tags: [coding]
type: project
metadesc: A semi automatic heart rate monitor made with python and tkinter.
---

## About

I made this little program quite a long time ago (it seems like ages, but it's actually just 2 years, lol) as part of a school project. Our biology teacher told us to create or think of something that could help people in some way, all related to healthcare and the theoretical content we had been studying. That's how I ended up considering blending my programming skills with this group task.

The most interesting aspect of this small project is that it was the first time I had created a GUI app. Until then, most of the code I had written was primarily console-based or no window at all (basically background tasks) and I learned how GUI is created and how TKinter works.

I'm not sure why I uploaded it to Replit, but since I'm not using that platform these days, I decided to upload it to my [GitHub](https://github.com/Flareonz44/PyPulse). Just in case of any issues, I'll keep it here too.

```python
from tkinter import *
from timeit import default_timer as timer
import center_tk_window as cw
started = False
elapsed = []
start = 0
end = 0

def help_w():
    hw = Toplevel(tk)
    hw.geometry("300x330")
    hw.title("Ayuda")
    hw.resizable(False, False)
    hw.configure(background="#343434")
    hw.grid()
    hw.grab_set()
    cw.center_on_screen(hw)
    Label(hw, text="PyPulse v1.1n\n Creado por Flareonz44 \n\n Como usar\n\nPrimero buscá la Aorta en tu cuello, una\n vez que sientas el pulso, apretá\n cualquier tecla para empezar a medir.\n\n Cada vez que sientas un pulso, \n tenés que apretar cualquier tecla; cuantas \n más veces lo haces, más presiso es el\n resultado, ya que se promedian los datos.\nψ", height=0, font=("Segoe UI Light", 12), background = "#343434", foreground = "#DADADA").pack()

def pulse_s(event):
    global start
    start = timer()
    global started
    started = True

def pulse_e(event):
    global end
    global start
    end = timer()
    tempstart = start
    start = end
    tx1.set("Presioná cualquier tecla cada vez \n  que sientas un pulso")
    out = 0
    global elapsed
    elapsed.append(float(60/(end - tempstart)))
    for each in elapsed:
        out += each
    tx0.set(str(round(out/len(elapsed))))
    tx3.set(str(round(out/len(elapsed), 7)))

tk = Tk()
tk.geometry("300x260")
tk.title("PyPulse v1.1")
tk.resizable(False, False)
tk.configure(background="#343434")
tk.grid()
tx0 = StringVar()
tx2 = StringVar()
tx1 = StringVar()
tx3 = StringVar()
tx1.set("Presioná cualquier tecla para empezar\n")
tx2.set("Más precisamente")
tx0.set("00")
tx3.set("00")
help_b = Label(tk, text=" "*45+"Ayuda"+" "*45, height=0, font=("Segoe UI Light", 8), background = "#3A3A3A", foreground = "#DADADA", cursor="hand2")
help_b.pack(side=BOTTOM)
help_b.bind("<ButtonRelease-1>", lambda e: help_w())
Label(tk, textvariable=tx1, height=0, font=("Segoe UI Light", 12), background = "#343434", foreground = "#DADADA").pack()
Label(tk, textvariable=tx0, height=1, font=("Segoe UI Light", 70), background = "#343434", foreground = "#F84F4F").pack()
Label(tk, textvariable=tx2, height=0, font=("Segoe UI Light", 12), background = "#343434", foreground = "#DADADA").pack()
Label(tk, textvariable=tx3, height=0, font=("Segoe UI Light", 22), background = "#343434", foreground = "#F84F4F").pack()
tk.bind("<Key>", pulse_s if started else pulse_e)
cw.center_on_screen(tk)
tk.mainloop()
```

Take care!