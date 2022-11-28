import tkinter as tk

from homePage import homePage
from environmentalPage import environmentalPage
from cameraPage import cameraPage

pages = {
    "Homepage": homePage, 
    "EnvironmentalPage": environmentalPage, 
    "CameraPage": cameraPage
}

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("NASA GUI")
        self.geometry("400x400")
        self._frame = None
        self.switch_frame("Homepage")
        

    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(master = self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()