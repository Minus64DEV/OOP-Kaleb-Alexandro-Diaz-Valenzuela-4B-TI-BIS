import tkinter as tk;
import tkinter.ttk, tkinter.font;

window = tk.Tk()
window.title("My Application")
window.geometry("640x480")
window.minsize(320, 240)

print(tk.font.families())

tk.ttk.Label(window, text="Hello", font="KiwiSoda", foreground="#ff0000").pack(padx=20, pady=20)
tk.ttk.Button(window, text="Press me").pack(padx=40,pady=10)
tk.ttk.Button(window, text="You can't press me!", state="disabled").pack(padx=40,pady=10)
tk.ttk.Label(window, text="I'm wide, red and inclined!", font="KiwiSoda 23 italic", background="#ff0000", width=40).pack(padx=10, pady=20)
tk.ttk.Label(window, text="Why are you pointing at me?", font="KiwiSoda 23 italic", cursor="hand2").pack(padx=10, pady=20)
tk.ttk.Label(window, text="Please wait...", font="KiwiSoda 23 bold", cursor="wait").pack(padx=10, pady=20)

window.mainloop()