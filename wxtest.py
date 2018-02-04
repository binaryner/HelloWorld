import wx,os,sys
class myfream(wx.Frame):
    def __init__(self,parent,title,size):
        super(myfream,self).__init__(parent,title=title,size=size)
        self.InitUI()
        self.Show()

    def InitUI(self):
        self.bkg = wx.Panel(self)
        self.loadButton = wx.Button(self.bkg,label='Open')
        self.loadButton.Bind(wx.EVT_BUTTON,self.load)
        self.saveButton = wx.Button(self.bkg,label='Save')
        self.saveButton.Bind(wx.EVT_BUTTON,self.save)
        self.filename = wx.TextCtrl(self.bkg)
        self.contents = wx.TextCtrl(self.bkg, style=wx.TE_MULTILINE|wx.HSCROLL)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.filename,proportion=1,flag=wx.EXPAND)
        hbox.Add(self.loadButton,proportion=0,flag=wx.LEFT,border=5)
        hbox.Add(self.saveButton,proportion=0,flag=wx.LEFT,border=5)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
        vbox.Add(self.contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)

        self.bkg.SetSizer(vbox)

    def load(self,event):
        file=open(self.filename.GetValue())
        self.contents.SetValue(file.read())
        file.close()

    def save(self,event):
        file=open(self.filename.GetValue(),'w')
        file.write(self.contents.GetValue())
        file.close()

        
app = wx.App()
win1 = myfream(None,title='Relative Simple Editor[1]',size=(1024,768))
win2 = myfream(None,title='Relative Simple Editor[2]',size=(768,300))
app.MainLoop()


'''
app = wx.App()
win = wx.Frame(None,title='Simple Editor',size=(410,335))
win.Show()
loadButton = wx.Button(win, label='Open',pos=(225,5),size=(80,25))
saveButtom = wx.Button(win, label='Save',pos=(315,5),size=(80,25))
filename = wx.TextCtrl(win, pos=(5,5),size=(210,25))
contents = wx.TextCtrl(win, pos=(5,35), size=(390,260), style=wx.TE_MULTILINE|wx.HSCROLL)
app.MainLoop()
'''
