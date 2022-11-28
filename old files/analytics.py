import tkinter as tk


window = tk.Tk()
window.title("NASA Anaylticd")
window.geometry("400x400")#was 300x300 

#need to figure out screen size on the actual box!d

title = tk.Label(text="Nano Insect Lab!", justify="center")
title.pack()

camera_label = tk.Label(text = "Access the camera")
camera_label.place(x=20, y=60)

#make a text window for the camera 
def camera_window_seperate():
  global pop 
  pop = window
  pop.title("camera")
  pop.geometry("250x150")
  pop.config(bg="green")

camera_btn = tk.Button(
  text = "Go",
  width=5,
  height=2,
  command=camera_window_seperate
)




  
camera_btn.place(x=300,y=100)


tk.mainloop()
