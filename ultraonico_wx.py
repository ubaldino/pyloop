#!/usr/bin/python
# communicate.py

import wx
import serial,sys
import time
import thread

ser = serial.Serial( port="COM18" , baudrate=9600 )
class LeftPanel(wx.Panel):


	
	def __init__(self, parent, id):		# Constructor
		wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
		
		self.text = parent.GetParent().rightPanel.text
		
		button1 = wx.Button(self, -1, 'ULTRA', (10, 10))
		button2 = wx.Button(self, -1, 'HOLA', (10, 60))
		#button1.bind(wx.EVT_BUTTON, self.OnPlus)
		
		self.Bind(wx.EVT_BUTTON, self.OnUltra, id=button1.GetId())
		self.Bind(wx.EVT_BUTTON, self.OnHola, id=button2.GetId())
	
	def OnUltra(self, event):
		
		# thread.start_new_thread(self.hilo, ())
		while (True):
			ser.write('A')
			time.sleep(2)
			tupla = []


			text = ser.readline(ser.inWaiting())
			#self.text.SetLabel(text)
			wx.CallAfter(self.text.SetLabel, text)
			print text

	
	def OnHola(self, event):
		#while(True):
		self.text.SetLabel('hola q tal')
		'''
		ser.write('A')
		time.sleep(0.5)
		text = ser.readline(ser.inWaiting())
		self.text.SetLabel(text)
		'''
	def hilo(self):
		while (True):
			ser.write('U')
			time.sleep(2)
			tupla = []


			text = ser.readline(ser.inWaiting())
			#self.text.SetLabel(text)
			wx.CallAfter(self.text.SetLabel, text)
			print text

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