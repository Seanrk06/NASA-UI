import tkinter as tk

class cameraPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page", command=lambda: master.switch_frame("Homepage")).pack()

if __name__ == "__main__":
    app = cameraPage()
    app.mainloop()