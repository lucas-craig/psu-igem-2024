import wx
#import wx.richtext
import numpy as np
import scipy as sp
import conversionBackend as be
import wx.lib.buttons as buttons

sizer = wx.BoxSizer(wx.VERTICAL)

class BasicCalculator(wx.Frame): #is the class really necessary?
    
    #input = (False, False)
    #bfore_first_button_press = True
    text1 = None
    text2 = None
    outTextBox = None
    outMsg = ""

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(450, 300))

        #Create a panel to put all the buttons and text boxes
        panel = wx.Panel(self, style=wx.SUNKEN_BORDER)
        panel.SetBackgroundColour((195,216,234))
        
        wx.TopLevelWindow.Center(self, wx.BOTH) #center window when it opens
        #wx.TopLevelWindow.SetSizeHints(self, 450, 300, maxW=600, maxH=400) #setting min and max heights
        wx.TopLevelWindow.SetSizeHints(self, 450, 300, maxW=500, maxH=330)
        

        #setting up the sizer. 
        vertical_layout = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(wx.Button(self, -1, 'An extremely long button text'), 0, 0, 0)
        #sizer.Add(wx.Button(self, -1, 'Small button'), 0, 0, 0)
        #self.SetSizer(sizer)
        #panel.SetSizer(sizer)

        #wx.Panel(self)

        #panel = wx.Panel(self)
        #self.SetSizerAndFit(self, sizer, deleteOld=True)

        # Setting up the menu.
        filemenu= wx.Menu()

        #btn2 = buttons.GenButton(panel, -1, "Hello World!", pos=(50, 100))
        #btn2 = buttons.GenButton(panel, -1, "Hello World!")

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        #self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        #self.Show(True)

        #Creating a title
        #st = wx.StaticText(panel, label="Basic Calculator", style=wx.ALIGN_CENTRE_HORIZONTAL)
        #st = wx.StaticText(self, label="Basic Calculator", style=wx.ALIGN_CENTRE_HORIZONTAL)
        #vertical_layout.Add(st, 0, wx.ALL |  wx.ALIGN_CENTER, 10)

        #heading = wx.richtext.RichTextCtrl(panel, name="Basic Calculator", style=wx.ALIGN_CENTER_HORIZONTAL)
        #heading_text = "<b><big><span font_family='wx.FONTFAMILY_SWISS'>Basic Calculator</span></big></b>"

        #wx.SetLabelMarkup(heading_text)
        heading = wx.StaticText(panel, label="Basic Calculator", style=wx.ALIGN_CENTER_HORIZONTAL)
        #heading_font = wx.Font(wx.FontInfo(30).Family(wx.FONTFAMILY_SWISS).Bold())
        """
        heading.SetLabelMarkup("<b>&ampBed</b> &ampmp "
                     "<span foreground='purple'>breakfast</span> "
                     "available <big>HERE</big>")
        """
        #heading.SetLabelMarkup('<p><font color="#FF0000">Red paragraph text</font></p>')
        
        font = wx.Font(30, wx.DEFAULT, wx.MODERN, wx.NORMAL)
        heading.SetFont(font)
        
        heading.SetForegroundColour((148,6,27))
        heading.SetForegroundColour((125,51,56))
       
        #rgb(255, 0, 0)

        #heading.SetLabelMarkup(True)

        vertical_layout.Add(heading, 0, wx.ALL | wx.ALIGN_CENTER, 20)

        #creating text entry boxes
        #text1 = wx.TextCtrl(panel)
        textbox_size = wx.Size(-1,25)
        #text1 = wx.TextCtrl(panel, size=wx.Size(30,10))
        #text1 = wx.TextCtrl(panel, size=textbox_size)
        self.text1 = wx.TextCtrl(panel)
        self.text1.SetMaxSize(textbox_size)
        self.text1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)) 

        #panel.AddChild(text1)
        #text1.setLabel("Initial Concen. (mmol/L)")
        self.text1.SetHint("Initial Glucose Reading (mg/dL)")
        #text2 = wx.TextCtrl(self, pos = (50,70))
        #text2 = wx.TextCtrl(panel)
        #text2 = wx.TextCtrl(panel, size=textbox_size)
        #self.text1.Bind()
        #self.text1.Bind(wx.EVT_TEXT, self.OnTextClick)



        self.text2 = wx.TextCtrl(panel)
        self.text2.SetMaxSize(textbox_size)
        self.text2.SetHint("Final Glucose Reading (mg/dL)")
        self.text2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)) 
        
        #sizer.Add(panel, 1, 0, 0)
        
        #sizer.Add(text1, 1, wx.ALIGN_CENTER, 50)
        #sizer.Add(text2, 1, wx.ALIGN_CENTER, 50)
        #vertical_layout.Add(text1, 1, wx.SHAPED | wx.ALL | wx.ALIGN_CENTER, border=20)
        #vertical_layout.Add(text2, 1, wx.SHAPED | wx.ALL | wx.ALIGN_CENTER, border=20)
        vertical_layout.Add(self.text1, 1, wx.ALL | wx.ALIGN_CENTER, border=10)
        vertical_layout.Add(self.text2, 1, wx.ALL | wx.ALIGN_CENTER, border=10)
        #vertical_layout.Add(text1, 1, wx.ALIGN_CENTER, border=20)
        #vertical_layout.Add(text2, 1, wx.ALIGN_CENTER, border=20)
        #vertical_layout.Add(text1, 1, 0, border=20)
        #vertical_layout.Add(text2, 1, 0, border=20)
        #vertical_layout.Add(text1, 1, 0, 0)
        #vertical_layout.Add(text2, 1, 0, 0)

        #creating the calculate button
        #calcButton = wx.Button(self.panel, label="Calculate", pos = (50,100))
        #calcButton = wx.Button(self, label="Calculate")
        #calcButton = wx.Button(panel, label="Calculate")
        calcButton = buttons.GenButton(panel, -1, label="Convert")
        #calcButton.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        calcButton.SetBackgroundColour((28,58,137))
        #calcButton.SetFont()#OwnColour((28,58,137))
        calcButton.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        vertical_layout.Add(calcButton, 0, wx.ALL | wx.ALIGN_CENTER, 10)

        #creating the output display box:
        #self.outText = wx.TextCtrl(self.panel, value = "Type in concentrations and press caclulate.", pos = (50,130), size=(200,100), style=wx.TE_READONLY | wx.TE_MULTILINE)
        #outText = wx.TextCtrl(self, value = "Type in concentrations and press caclulate.", style=wx.TE_READONLY | wx.TE_MULTILINE)
        #self.outTextBox = wx.TextCtrl(panel, value = self.outMsg, style=wx.TE_READONLY | wx.TE_MULTILINE)
        #sizer.Add(outText, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 2)
        
        self.outMsg = "Type in concentrations and press caclulate."
        self.outTextBox = wx.TextCtrl(panel, value = self.outMsg, style=wx.TE_READONLY | wx.TE_MULTILINE)
        vertical_layout.Add(self.outTextBox, 1, wx.EXPAND | wx.BOTTOM, 0)

        """
        if self.bfore_first_button_press:
            self.outMsg = "Type in concentrations and press caclulate."

        elif (not self.input[0] or not self.input[1]): #self.input[0] == False or self.input[1] == False:
            self.outMsg = "Error: a glucose concentration is out of specified glucometer's measurement range."

        elif not (self.input[0] >= 20 and self.input[0] <= 500) or not (self.input[1] >= 20 and self.input[1] <= 500):
                
                c = be.converter()
                interpolatedVal = c.convertConcentration(input[0],input[1])
                self.outMsg = "CA125: {:.3f} U/mL\n".format(interpolatedVal)
                if interpolatedVal >= 35: 
                    self.outMsg += "Abnormal: greater than or equal to 35"
                else: 
                    self.outMsg += "Normal: below 35"
        
        
        else:
            self.outMsg = "Something went wrong"
        self.outText.SetValue(outMsg)
        #self.UpdateOutputTextbox()
        """

        panel.SetSizer(vertical_layout)

        

    #def UpdateOutputTextbox(self):
    #    self.outTextBox.SetValue(self.outMsg)

    #id = EVT_TEXT_URL (??)
    """
    def OnTextClick(self, e):
        #source = e.Source()
        obj = e.GetEventObject()
        print(obj.GetName())
        return
    """

    #button press event handler
    def OnButtonClick(self, e):

        self.bfore_first_button_press = False

        #remove whitespace from text entered in each box
        contents1 = self.text1.GetValue().strip(' ')
        #contents1 = self.GetValue().strip(' ')
        contents2 = self.text2.GetValue().strip(' ')

        #if there are non-numeric chars in input strings, return false.
        #if not((contents1.isnumeric()) and (contents2.isnumeric())):
        #   self.outMsg = "Error: only numeric values are accepted."

        if not((contents1.isnumeric()) and (contents2.isnumeric())):
           self.outMsg = "Error: only numeric values are accepted."
        
        #otherwise, extract values and return them in a tuple.
        else:
            val1 = float(contents1) #extract num from contents of first text box as float
            val2 = float(contents2) #ditto for second text box
            #self.input = (val1, val2)

            if not (20 <= val1 <= 500) or not (20 <= val2 <= 500):
                self.outMsg = "Error: a glucose concentration is out of specified glucometer measurement range."

            else:
                c = be.converter()

                interpolatedVal = c.convertConcentration(val1,val2)
                
                if interpolatedVal == -1: #does this explanation make sense? - python interprets 0.0 as False so I made -1 the code for a significant decrease so as not to trip this conditional if a legitimate 0.0 was returned
                    print(interpolatedVal)
                    self.outMsg = "Error: glucose concentration decreased by more than standard deviation of selected glucometer."

                else:
                    self.outMsg = "CA125: {:.3f} U/mL\n".format(interpolatedVal)
                    self.outMsg += "Abnormal: greater than or equal to 35" if interpolatedVal >= 35 else "Normal: below 35"

                """
                self.outMsg = "CA125: {:.3f} U/mL\n".format(interpolatedVal)
                if interpolatedVal >= 35: 
                    self.outMsg += "Abnormal: greater than or equal to 35"
                else: 
                    self.outMsg += "Normal: below 35"
                """
        
        self.outTextBox.SetValue(self.outMsg)
        #self.UpdateOutputTextbox()

        """
        #if there are non-numeric chars in input strings, output error message.
        if not((contents1.isnumeric()) and (contents2.isnumeric())):
           #print(contents1.isnumeric())
           #print(contents2.isnumeric())
           outMsg = "Error: only numeric values are accepted."
        
        #otherwise, extract values and run the calculation
        else:
            val1 = float(contents1) #extract num from contents of first text box as float
            val2 = float(contents2) #ditto for second text box

            if not (20 <= val1 <= 500) or not (20 <= val2 <= 500):
                outMsg = "Error: a glucose concentration is out of specified glucometer measurement range."


            c = be.converter()
            interpolatedVal = c.convertConcentration(contents1,contents2)
            outMsg = "CA125: {:.3f} U/mL\n".format(interpolatedVal)
            if interpolatedVal >= 35: 
                outMsg += "Abnormal: greater than or equal to 35"
            else: 
                outMsg += "Normal: below 35"
        self.outText.SetValue(outMsg)
        """
        

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
    #frm.SetSizerAndFit(sizer, deleteOld=True)
    frm.Show()
    app.MainLoop()