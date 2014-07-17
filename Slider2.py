#!/usr/bin/python

# slider.py

import wx

#ser = serial.Serial( port="COM" , baudrate=9600 )

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):

        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, (300, 150))
        panel = wx.Panel(self, -1)
        self.val = 127
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.sld = wx.Slider(panel, -1, self.val, 0, 255, wx.DefaultPosition, (250, -1),
                              wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        btn1 = wx.Button(panel, 8, 'Bajo')
        btn2 = wx.Button(panel, 9, 'Normal')
        btn3 = wx.Button(panel, 10, 'Alto')

        wx.EVT_BUTTON(self, 8, self.OnLow)
        wx.EVT_BUTTON(self, 9, self.OnNormal)
        wx.EVT_BUTTON(self, 10, self.OnHigh)

        self.sld.Bind(wx.EVT_SCROLL, self.EnterSlider )

        vbox.Add(self.sld, 1, wx.ALIGN_CENTRE)
        hbox.Add(btn1, 1, wx.RIGHT, 10)
        hbox.Add(btn2, 1)
        hbox.Add(btn3, 1, wx.LEFT, 10)
        vbox.Add(hbox, 0, wx.ALIGN_CENTRE | wx.ALL, 20)
        panel.SetSizer(vbox)

        

        
    def OnLow(self, event):
        self.val = 50
        self.sld.SetValue(self.val)
        ser.write(str(self.val))
        
    def OnNormal(self, event):
        self.val = 127
        self.sld.SetValue(self.val)
        ser.write(str(self.val))

    def OnHigh(self, event):
        self.val = 255
        self.sld.SetValue(self.val)
        ser.write(str(self.val))

    def EnterSlider(self, event):
        self.val = self.sld.GetValue()
        ser.write(str(self.val))

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'slider.py')
        frame.Show(True)
        frame.Centre()
        return True

app = MyApp(0)
app.MainLoop()