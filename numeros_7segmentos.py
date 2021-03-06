#!/usr/bin/python
# communicate.py

import wx
import serial,sys

ser = serial.Serial( port="COM19" , baudrate=9600 )

class LeftPanel(wx.Panel):
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
		
		self.text = parent.GetParent().rightPanel.text
		
		button1 = wx.Button(self, -1, '+', (10, 10))
		button2 = wx.Button(self, -1, '-', (10, 60), size=(50,30))
		
		self.Bind( wx.EVT_BUTTON, self.OnPlus, id=button1.GetId() )
		self.Bind( wx.EVT_BUTTON, self.OnMinus, id=button2.GetId() )
	
	def OnPlus(self, event):
		value = int( self.text.GetLabel() )
		if ( value < 9 ):
			value = value + 1
		else:
			value = 0

		self.text.SetLabel(str(value))
		ser.write(str(value))
	
	def OnMinus(self, event):
		value = int(self.text.GetLabel())
		
		if (value > 0):
			value = value - 1
		else:
			value = 9
		self.text.SetLabel(str(value))
		ser.write(str(value))

class RightPanel(wx.Panel):
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
		self.text = wx.StaticText(self, -1, '0', (40, 60))

class Communicate(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(280, 200))
		
		panel = wx.Panel(self, -1)
		self.rightPanel = RightPanel(panel, -1)
		
		leftPanel = LeftPanel(panel, -1)
		hbox = wx.BoxSizer()
		hbox.Add(leftPanel, 1, wx.EXPAND | wx.ALL, 5)
		hbox.Add(self.rightPanel, 1, wx.EXPAND | wx.ALL, 5)
		
		panel.SetSizer(hbox)
		self.Centre()
		self.Show(True)

app = wx.App()
Communicate(None, -1, 'widgets communicate')
app.MainLoop()