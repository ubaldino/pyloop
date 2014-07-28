# -*- coding: utf-8 -*- 

import wx

class Menu1(wx.Panel):
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent)

		self.timer = wx.Timer(self, 1)
		self.SetBackgroundColour(wx.Colour(255, 255, 255)) 

class Menu2(wx.Panel):
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent)	

		self.SetBackgroundColour(wx.Colour(200, 150, 205)) 
	
class Controlador:	
	def __init__(self):

		self.frame = wx.Frame(None, title="Prueba ventana", size=(540,420))
		self.menu1 = Menu1(self.frame, 1)
		
		self.hbox = wx.BoxSizer()
		self.hbox.Add(self.menu1, 1, wx.EXPAND | wx.ALL, 3)

		#self.frame.Show(True)
		self.menu2 = Menu2(self.frame, 2)
		self.hbox.Add(self.menu2, 2, wx.EXPAND | wx.ALL, 3)

		self.menu2.Show(False)

		self.frame.SetSizer(self.hbox)
		#self.menu1.Show(True)

		self.menu1.Bind(wx.EVT_TIMER, self.OnTimerMenu1) 
		self.menu1.timer.Start(1000)

		##self.frame.Size(540,420)
		#self.menu1.Show(False)

		self.frame.Show()

	def OnTimerMenu1(self, event):
		self.menu1.timer.Stop()
		#self.hbox.Clear(self)
		self.menu1.Show(False)
		
		self.menu2.Show(True)
		self.hbox.Layout()  '''*'''

if __name__ == '__main__':
	app = wx.App(False)
	Controlador()

	app.MainLoop()