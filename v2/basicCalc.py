"""
Me playing around with the helloworld.py code
"""

import wx
import numpy as np
import scipy as sp

class BasicCalculator(wx.Frame):

    contents = ""

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300,300))

        self.CreateStatusBar() # A Statusbar in the bottom of the window

        #setting up the sizer. 
        sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(wx.Button(self, -1, 'An extremely long button text'), 0, 0, 0)
        #sizer.Add(wx.Button(self, -1, 'Small button'), 0, 0, 0)
        self.SetSizer(sizer)

        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)

        #Creating a title
        st = wx.StaticText(self, label="Basic Calculator", style=wx.ALIGN_CENTRE_HORIZONTAL)
        sizer.Add(st, 1, wx.ALIGN_CENTER | wx.SHAPED, 0)

        #Create a panel for the text entry boxes
        panel = wx.Panel(self)

        #creating text entry boxes
        text1 = wx.TextCtrl(self)
        panel.AddChild(text1)
        #text1.setLabel("Initial Concen. (mmol/L)")
        text1.SetLabel("Initial Concen. (mmol/L)")
        #text2 = wx.TextCtrl(self, pos = (50,70))
        text2 = wx.TextCtrl(panel)
        text2.SetLabel("Initial Concen. (mmol/L)")

        sizer.Add(panel, 1, 0, 0)
        
        #sizer.Add(text1, 1, wx.ALIGN_CENTER, 50)
        #sizer.Add(text2, 1, wx.ALIGN_CENTER, 50)
        #sizer.Add(text1, 1, wx.SHAPED | wx.ALL, 20)
        #sizer.Add(text2, 1, wx.SHAPED | wx.ALL, 20)

        #creating the calculate button
        #calcButton = wx.Button(self.panel, label="Calculate", pos = (50,100))
        calcButton = wx.Button(self, label="Calculate")
        calcButton.Bind(wx.EVT_BUTTON, self.OnClick)
        sizer.Add(calcButton, 1, wx.ALIGN_CENTER, 0)

        #creating the output display box:
        #self.outText = wx.TextCtrl(self.panel, value = "Type in concentrations and press caclulate.", pos = (50,130), size=(200,100), style=wx.TE_READONLY | wx.TE_MULTILINE)
        outText = wx.TextCtrl(self, value = "Type in concentrations and press caclulate.", style=wx.TE_READONLY | wx.TE_MULTILINE)
        sizer.Add(outText, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        



    #button press event handler
    def OnClick(self, e):
        #remove whitespace from text entered in each box
        contents1 = self.text1.GetValue().strip(' ')
        contents2 = self.text2.GetValue().strip(' ')

        #initialize output message
        outMsg = ""

        #if there are non-numeric chars in input strings, output error message.
        if not((contents1.isnumeric()) and (contents2.isnumeric())):
           print(contents1.isnumeric())
           print(contents2.isnumeric())
           outMsg = "Error: only numeric values are accepted."
        
        #otherwise, extract values and run the calculation
        else:
            val1 = float(contents1) #extract num from contents of first text box as float
            val2 = float(contents2) #ditto for second text box

            score = abs(val2 - val1)/val1 * 100


            outMsg = "StdErr: {:.3f}:\n".format(score)
            if score < 30: 
                outMsg += "Above 30%"
            else: 
                outMsg += "Below 30%"
        self.outText.SetValue(outMsg)
        

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = BasicCalculator(None, title='Basic Calculator')
    frm.Show()
    app.MainLoop()