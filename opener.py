import webbrowser
from customTkinter import *

def subscribe():
    # Open web browser and navigate to MrBeast's channel
    webbrowser.open("https://www.youtube.com/user/MrBeast6000")

root = Tk()
root.title("Subscribe to MrBeast")

# Create label
label = Label(root, text="Please Subscribe to MrBeast on YouTube")
label.pack()

# Create button
button = Button(root, text="Subscribe", command=subscribe)
button.pack()

root.mainloop()