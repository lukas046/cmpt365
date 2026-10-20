from tkinter import *
from tkinter import filedialog
from scipy.io import wavfile
from scipy import signal

def openWav():
    path = filedialog.askopenfilename()
    global sample_rate, data
    sample_rate, data = wavfile.read(path)
    sample_rate_display.config(text="Sample Rate: " + str(sample_rate) + "Hz")
    Total_sample_display.config(text="Total Sample: " + str(data*2))


sample_rate = None
data = None
legnth = None
total_sample = None
window = Tk()
window.geometry("800x600")
sample_rate_display = Label(window, text="Sample Rate: None")
Total_sample_display = Label(window, text="Total samples: None")

button = Button(text="Open File",command=openWav)
button.pack()
sample_rate_display.pack()
Total_sample_display.pack()


window.mainloop()