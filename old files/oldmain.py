import tkinter as tk

window = tk.Tk()
window.title("NASA GUI")
window.geometry("400x400")#was 300x300 

#need to figure out screen size on the actual box!d

title = tk.Label(text="Nano Insect Lab!", justify="center")
title.pack()

camera_label = tk.Label(text = "Access the camera")
camera_label.place(x=20, y=60)
#make a text with a border that can display the text in real time

camera_btn = tk.Button(
  text = "Go",
  width=5,
  height=2,
  bg="cyan"
)
camera_btn.place(x=30,y=100)

lights_label = tk.Label(text = "Turn On/Off the lights")
lights_label.place(x=25, y=200)

lights_btn_on = tk.Button(
  text = "on",
  width=5,
  height=1,
  bg="cyan"
)
lights_btn_off = tk.Button(
  text="off",
  width=5,
  height=1,
  bg="cyan"
)

lights_btn_on.place(x=30, y=220)
lights_btn_off.place(x=30, y=270)





temperature_label = tk.Label(text = "Tempature") 
temperature_label.place(x=250, y=60)


temperature_text = tk.Label( #this is going to need to get the data from the db
  text="50 F",
  width=7,
  height=1,
  bg="white",
)
temperature_text.place(x=250, y=85)






humidity_label = tk.Label(text = "Humidity")
humidity_label.place(x=250, y=120)

humidity_levels_text = tk.Label( #this is going to need to get the data from the db
  text="50 %",
  width=7,
  height=1,
  bg="white",
)
humidity_levels_text.place(x=250, y=140)

Co2Level_label = tk.Label(text = "Co2 Levels")
Co2Level_label.place(x=250, y = 180)

Co2_levels_text = tk.Label( #this is going to need to get the data from the db
  text="50 %",
  width=7,
  height=1,
  bg="white",
)
Co2_levels_text.place(x=250, y=200)


tk.mainloop()
