import image
import Tkinter
window = Tkinter.Tk()

window.title("Join")
window.geometry("300x300")
window.configure(background='grey')

imageFile = "voice.jpg"

window.im1 = Image.open(imageFile)


raw_input()
window.mainloop()