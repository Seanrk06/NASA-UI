import tkinter as tk
import qwiic_bme280
import time
import sys

class environmentalPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page", command=lambda: master.switch_frame("Homepage")).pack()

        # Sensor Information

        mySensor = qwiic_bme280.QwiicBme280()
        if mySensor.connected == False:
            print("The Qwiic BME280 device isn't connected to the system. Please check your connection", \
                file=sys.stderr)
            return

        mySensor.begin()
        while True:
            print("Humidity:\t%.3f" % mySensor.humidity)

            print("Pressure:\t%.3f" % mySensor.pressure)    

            print("Altitude:\t%.3f" % mySensor.altitude_feet)

            print("Temperature:\t%.2f" % mySensor.temperature_fahrenheit)       

            print("")

            time.sleep(1)

          
        

if __name__ == "__main__":
    app = environmentalPage()
    app.mainloop()