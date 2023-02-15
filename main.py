import wx



class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(700, 700))
        self.Centre()
        self.SetBackgroundColour((204, 255, 255, 255))
        self.Show()
        self.b1 = wx.Button(self, label='1', pos=(20, 120))
        self.b1.Bind(wx.EVT_BUTTON, self.onb1)
        self.b2 = wx.Button(self, label='2', pos=(120, 120))
        self.b2.Bind(wx.EVT_BUTTON, self.onb2)
        self.b3 = wx.Button(self, label='3', pos=(220, 120))
        self.b3.Bind(wx.EVT_BUTTON, self.onb3)
        self.b4 = wx.Button(self, label='4', pos=(20, 160))
        self.b4.Bind(wx.EVT_BUTTON, self.onb4)
        self.b5 = wx.Button(self, label='5', pos=(120, 160))
        self.b5.Bind(wx.EVT_BUTTON, self.onb5)
        self.b6 = wx.Button(self, label='6', pos=(220, 160))
        self.b6.Bind(wx.EVT_BUTTON, self.onb6)
        self.b7 = wx.Button(self, label='7', pos=(20, 200))
        self.b7.Bind(wx.EVT_BUTTON, self.onb7)
        self.b8 = wx.Button(self, label='8', pos=(120, 200))
        self.b8.Bind(wx.EVT_BUTTON, self.onb8)
        self.b9 = wx.Button(self, label='9', pos=(220, 200))
        self.b9.Bind(wx.EVT_BUTTON, self.onb9)
        self.b0 = wx.Button(self, label='0', pos=(20, 240))
        self.b0.Bind(wx.EVT_BUTTON, self.onb0)
        self.bx = wx.Button(self, label='x', pos=(120, 240))
        self.bx.Bind(wx.EVT_BUTTON, self.onbx)
        self.bp = wx.Button(self, label='+', pos=(220, 240))
        self.bp.Bind(wx.EVT_BUTTON, self.onbp)
        self.be = wx.Button(self, label='=', pos=(20, 280))
        self.be.Bind(wx.EVT_BUTTON, self.onbe)
        self.bpo = wx.Button(self, label='^', pos=(220, 280))
        self.bpo.Bind(wx.EVT_BUTTON, self.onbpo)
        self.bd = wx.Button(self, label='%', pos=(120, 280))
        self.bd.Bind(wx.EVT_BUTTON, self.onbd)
        self.mylabel1 = wx.StaticText(self, label="", pos=(20, 50))

    def onb1(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str(1))

    def onb2(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str(2))

    def onb3(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str(3))

    def onb4(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str(4))

    def onb5(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str(5))

    def onb6(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str(6))

    def onb7(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str(7))

    def onb8(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str(8))

    def onb9(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str(9))

    def onb0(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str(0))

    def onbx(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str('*'))

    def onbp(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str('+'))

    def onbpo(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str('^'))

    def onbd(self, e):
        self.mylabel1.SetLabel(self.mylabel1.GetLabel() + str('%'))

    def onbe(self, e):

        b = 0
        c = 1
        d = 1
        if ('*' in self.mylabel1.GetLabel()):
            a = self.mylabel1.GetLabel().split('*')
            for i in a:
                c = c * int(i)
            b = c
        if ('%' in self.mylabel1.GetLabel()):
            a = self.mylabel1.GetLabel().split('%')
            c = int(a[0])
            while (d < len(a)):
                c = c / int(a[d])
                d = d + 1
            b = c
        if ('+' in self.mylabel1.GetLabel()):
            a = self.mylabel1.GetLabel().split('+')
            for i in a:
                b = b + int(i)
        if ('^' in self.mylabel1.GetLabel()):

            a = self.mylabel1.GetLabel().split('^')
            b = int(a[0])
            if (a[1] == '0'):
                b = 1
            while (d < int(a[1])):
                b = b * int(a[0])
                d = d + 1

        self.mylabel2 = wx.StaticText(self, label='your solution is:' + str(b), pos=(20, 330))
        self.mylabel2.SetForegroundColour('black')
        self.mylabel1.SetLabel("")


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Calc')
    app.MainLoop()