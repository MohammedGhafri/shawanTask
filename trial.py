import wx 
 
app = wx.App() 
window = wx.Frame(None, title = "wxPython Frame", size = (300,200)) 
panel = wx.Panel(window) 
label = wx.StaticText(panel, label = "Hello World", pos = (0,50)) 
window.Show(True) 
app.MainLoop()
# import tkinter
# window =tkinter.TK()








# from PyQt5.QtWidgets import QApplication, QLabel
# app=QApplication([])
# label =QLabel('hello World')
# # label.show()
# app.exec_()



















# # from Tkinter import *

# # root =Tk()
# # thalabel1=Label(root,text="This is too easy")
# # thalabel1.pack()
# # root.mainloop()
# from tkinter import *

# class Application(Frame):
#     def say_hi(self):
#         print("hi there, everyone!")

#     def createWidgets(self):
#         self.QUIT = Button(self)
#         self.QUIT["text"] = "QUIT"
#         self.QUIT["fg"]   = "red"
#         self.QUIT["command"] =  self.quit

#         self.QUIT.pack({"side": "left"})

#         self.hi_there = Button(self)
#         self.hi_there["text"] = "Hello",
#         self.hi_there["command"] = self.say_hi

#         self.hi_there.pack({"side": "left"})

#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

# root = Tk()
# app = Application(master=root)
# app.mainloop()
# root.destroy()