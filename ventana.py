# -*- coding: utf-8 -*- 

import wx

class Menu1(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		self.timer = wx.Timer(self, 1)
		screen = wx.Window(self, -1, (0, 0), (540,420), style=wx.TRANSPARENT_WINDOW)
		screen.SetBackgroundColour(wx.Colour(255, 255, 255)) 


class Menu2(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)	

		screen = wx.Window(self, -1, (0, 0), (540,420), style=wx.TRANSPARENT_WINDOW)
		screen.SetBackgroundColour(wx.Colour(200, 205, 255)) 

class Controlador:
	def __init__(self):

		self.frame = wx.Frame(None, title="Prueba ventana", size=(540,420))
		self.menu1 = Menu1(self.frame)
		

		self.menu1.Show(True)

		self.menu1.Bind(wx.EVT_TIMER, self.OnTimerMenu1) 
		self.menu1.timer.Start(1000)

		
		#self.menu1.Show(False)

		self.frame.Show()

	def OnTimerMenu1(self, event):
		self.menu1.timer.Stop()
		
		self.menu1.Show(False)
		#self.menu1.Destroy()
		self.menu2 = Menu2(self.frame)
		self.menu2.Show(True)
		self.frame.Show()

if __name__ == '__main__':
	app = wx.App(False)
	Controlador()

	app.MainLoop()