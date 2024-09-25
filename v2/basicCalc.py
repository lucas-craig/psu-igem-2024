import wx
import numpy as np
import scipy as sp
import conversionBackend as be
import wx.lib.buttons as buttons
#import wx.lib.inspection
   

sizer = wx.BoxSizer(wx.VERTICAL)

class BasicCalculator(wx.Frame): #is the class really necessary?
    
    #text1 = None
    #text2 = None
    textBoxes = []
    allTextBoxContents = []
    outTextBox = None
    outMsg = ""

    def __init__(self, parent, title):
        #no_min_max = wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.FRAME_NO_TASKBAR
        no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER |  
                                                wx.MAXIMIZE_BOX)
        #wx.Frame.__init__(self, parent, title=title, size=(450, 300), style=no_resize)
        #wx.Frame.__init__(self, parent, title=title, size=(500, 350), style=no_resize)
        
        wx.Frame.__init__(self, parent, title=title, size=(500, 500), style=no_resize)
        
        #Create a panel to put all the buttons and text boxes

        border_panel = wx.Panel(self)

        #border_panel.SetBackgroundColour((254,245,227))
        border_panel.SetBackgroundColour("#51988e")

        vbox = wx.BoxSizer(wx.VERTICAL)

        #main panel with all the main controls in it:
        panel = wx.Panel(border_panel)#, style=wx.SUNKEN_BORDER)
        vbox.Add(panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)

        border_panel.SetSizer(vbox)

        
        panel.SetBackgroundColour((254,245,227))
        #panel.SetBackgroundColour("#C3D8EA")
        ##C3D8EA
        #panel.SetBackgroundColour("#51988E")
        ##51988E
        #panel.Set



        
        wx.TopLevelWindow.Center(self, wx.BOTH) #center window when it opens
        #wx.TopLevelWindow.SetSizeHints(self, 450, 300, maxW=500, maxH=330)
        #wx.TopLevelWindow.SetSizeHints(self, 600, 450, maxW=600, maxH=450)

        #setting up the sizer. 
        #vertical_layout = wx.BoxSizer(wx.VERTICAL)
        #grid_layout = wx.FlexGridSizer(rows=5, cols=3, vgap=5, hgap=5)
        #grid_layout = wx.GridBagSizer(5,3)
        #grid_layout = wx.GridBagSizer(6,3)
        grid_layout = wx.GridBagSizer(9,3)
        #grid_layout.AddGrowableCol(0)
        #grid_layout.AddGrowableCol(1)
        #grid_layout.AddGrowableCol(2)
        #grid_layout.AddGrowableRow(1)

        #EXPERIMENTAL STUFF:
        column_panel = wx.Panel(panel)
        column_panel.SetBackgroundColour("#97d0c7")
        #column_panel.SetBackgroundColour("#51988e")
        vbox_col = wx.BoxSizer(wx.VERTICAL)
        column_panel.SetSizer(vbox_col)
        #grid_layout.Add(column_panel, flag = wx.EXPAND, border = 0, pos=(0,0), span=(6,1))
        grid_layout.Add(column_panel, flag = wx.EXPAND, border = 0, pos=(0,0), span=(9,1))

        '''
        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        #menuAbout = filemenu.Append(102, "&About"," Information about this program")
        #menuExit = filemenu.Append(103,"E&xit"," Terminate the program")
        '''

        """
        heading = wx.StaticText(panel, label="Basic Calculator")#, style=wx.ALIGN_CENTER_HORIZONTAL)
        
        font = wx.Font(30, wx.DEFAULT, wx.MODERN, wx.NORMAL)
        heading.SetFont(font)
        
        heading.SetForegroundColour((125,51,56))
        
        
        #vertical_layout.Add(heading, 0, wx.ALL | wx.ALIGN_CENTER, 20)
        grid_layout.Add(heading, flag = wx.ALL, pos=(0,0),span=(0,1))#, flag=wx.RIGHT)
        """

        #bm=wx.Image("ROSA_logo_for_program.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #ROSA_logo_for_program_green.png
        bm=wx.Image("ROSA_logo_for_program_green.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #bm = self.scale_bitmap(bm, 140, 100)
        #bm = self.scale_bitmap(bm, 170, 250)
        bm = self.scale_bitmap(bm, 170, 262)
        #bm = self.scale_bitmap(bm, 170, 200)
        #image_ctrl = wx.StaticBitmap(panel, bitmap=bm)
        image_ctrl = wx.StaticBitmap(column_panel, bitmap=bm)
        #grid_layout.Add(image_ctrl, flag = wx.EXPAND, border = 10, pos=(0,0), span=(2,1))
        vbox_col.AddSpacer(50)
        vbox_col.Add(image_ctrl)

        #biomarker_select = wx.Choice(panel, choices=["Select Biomarker","CA125","Concussion Biomarker"])
        biomarker_select = wx.Choice(column_panel, choices=["Select Biomarker","CA125","Concussion Biomarker"])
        #biomarker_select.SetOwnBackgroundColour((235, 213, 195))
        #biomarker_select.SetOwnBackgroundColour("#337D78")
        #biomarker_select.SetOwnBackgroundColour("#97d0c7")#(wx.WHITE)
        biomarker_select.SetOwnBackgroundColour("#51988e")
        biomarker_select.SetOwnForegroundColour("#51988e")
        

        """
        Red: #94061B
        Light Blue: #C3D8EA
        Dark Red: #7D3338
        Dark Blue: #1C3A89
        Cream: #FEF5E3

        337D78
        """

        #biomarker_select.SetOwnForegroundColour((wx.RED))
        #glumtr_select = wx.Choice(panel, choices=["Select Glucometer","OneTouch Pro","Bayer Contour"])
        glumtr_select = wx.Choice(column_panel, choices=["Select Glucometer","OneTouch Pro","Bayer Contour"])
        glumtr_select.SetOwnBackgroundColour("#51988e")
        glumtr_select.SetOwnForegroundColour("#51988e")
        #glumtr_select.SetBackgroundColour(wx.NullColor)
        #glumtr_select.SetTextColour(wx.NullColor)
        #grid_layout.Add(biomarker_select, flag = wx.EXPAND, border = 5, pos=(4,0))
        #grid_layout.Add(glumtr_select, flag = wx.EXPAND, border = 5, pos=(5,0))
        vbox_col.AddSpacer(20)
        vbox_col.Add(biomarker_select, flag=wx.EXPAND, border=20)
        vbox_col.AddSpacer(20)
        vbox_col.Add(glumtr_select, flag=wx.EXPAND, border=20)
        #vbox_col.Add(biomarker_select, wx.ALIGN_BOTTOM, border=4)
        #vbox_col.Add(glumtr_select, wx.ALIGN_BOTTOM, border=4)
        #vbox_col.Add(biomarker_select, flag=wx.CENTRE, border=20)
        #vbox_col.Add(glumtr_select, flag=wx.CENTRE, border=20)

        #textbox_size = wx.Size()

        #creating the instructions box:       
        instructionsMsg = "Instructions:\nSelect biomarker to measure and glucometer used using the dropdown boxes in the left pane. Then input glucose concentration measurements and press calculate."
        instructionsTxtBox = wx.TextCtrl(panel, value = instructionsMsg, style=wx.TE_READONLY | wx.TE_MULTILINE)
        #self.instructionsTxtBox.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        instructionsTxtBox.SetBackgroundColour((125,51,56))
        instructionsTxtBox.SetForegroundColour(wx.WHITE)
        grid_layout.Add(instructionsTxtBox, border = 20, pos=(0,1), span=(1,2), flag = wx.EXPAND)#wx.ALIGN_CENTER | wx.EXPAND | wx.ALL)

        font = wx.Font(15, wx.DEFAULT, wx.MODERN, wx.NORMAL)

        text1 = wx.TextCtrl(panel)#, style=wx.ALIGN_CENTER)
        #self.text1.SetMaxSize(textbox_size)
        #text1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)) 
        #text1.SetBackgroundColour((254,245,227))
        text1.SetBackgroundColour((28,58,137))
        text1.SetForegroundColour(wx.WHITE)
        #self.text1.SetHint("Initial Glucose Reading (mg/dL)")
        text1.SetHint("Glucose Reading 1")
        units_text_1 = wx.StaticText(panel, label="mg/dL", style=wx.ALIGN_CENTER_VERTICAL)#, style=wx.ALIGN_CENTER_HORIZONTAL)
        units_text_1.SetFont(font)
        units_text_1.SetForegroundColour((125,51,56))
        grid_layout.Add(text1, pos=(2,1), border = 10, flag = wx.EXPAND) #wx.EXPAND | wx.RIGHT)#, flag = wx.EXPAND)#, flag = wx.ALL)
        grid_layout.Add(units_text_1, pos=(2,2), border = 10, flag = wx.EXPAND)
        self.textBoxes.append(text1)
        
        #print("line length of text1 line 0: "+str(self.text1.GetLineLength(0)))

        text2 = wx.TextCtrl(panel)
        #self.text2.SetMaxSize(textbox_size)
        #self.text2.SetHint("Final Glucose Reading (mg/dL)")
        text2.SetHint("Glucose Reading 2")
        #text2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        text2.SetBackgroundColour((28,58,137))
        units_text_2 = wx.StaticText(panel, label="mg/dL", style=wx.ALIGN_CENTER_VERTICAL)
        units_text_2.SetFont(font)
        units_text_2.SetForegroundColour((125,51,56))
        grid_layout.Add(text2, pos=(3,1), border = 10, flag = wx.EXPAND)# | wx.RIGHT)#, flag = wx.EXPAND)
        grid_layout.Add(units_text_2, pos=(3,2), border = 10, flag = wx.EXPAND)
        self.textBoxes.append(text2)


        text3 = wx.TextCtrl(panel)
        #self.text2.SetMaxSize(textbox_size)
        #self.text2.SetHint("Final Glucose Reading (mg/dL)")
        text3.SetHint("Glucose Reading 3")
        #text3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        text3.SetBackgroundColour((28,58,137))
        units_text_3 = wx.StaticText(panel, label="mg/dL", style=wx.ALIGN_CENTER_VERTICAL)
        units_text_3.SetFont(font)
        units_text_3.SetForegroundColour((125,51,56))
        grid_layout.Add(text3, pos=(4,1), border = 10, flag = wx.EXPAND)# | wx.RIGHT)#, flag = wx.EXPAND)
        grid_layout.Add(units_text_3, pos=(4,2), border = 10, flag = wx.EXPAND)
        self.textBoxes.append(text3)

        text4 = wx.TextCtrl(panel)
        #self.text2.SetMaxSize(textbox_size)
        #self.text2.SetHint("Final Glucose Reading (mg/dL)")
        text4.SetHint("Glucose Reading 4")
        #text4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        text4.SetBackgroundColour((28,58,137))
        units_text_4 = wx.StaticText(panel, label="mg/dL", style=wx.ALIGN_CENTER_VERTICAL)
        units_text_4.SetFont(font)
        units_text_4.SetForegroundColour((125,51,56))
        grid_layout.Add(text4, pos=(5,1), border = 10, flag = wx.EXPAND)# | wx.RIGHT)#, flag = wx.EXPAND)
        grid_layout.Add(units_text_4, pos=(5,2), border = 10, flag = wx.EXPAND)
        self.textBoxes.append(text4)

        text5 = wx.TextCtrl(panel)
        #self.text2.SetMaxSize(textbox_size)
        #self.text2.SetHint("Final Glucose Reading (mg/dL)")
        text5.SetHint("Glucose Reading 5")
        #text5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        text5.SetBackgroundColour((28,58,137))
        units_text_5 = wx.StaticText(panel, label="mg/dL", style=wx.ALIGN_CENTER_VERTICAL)
        units_text_5.SetFont(font)
        units_text_5.SetForegroundColour((125,51,56))
        grid_layout.Add(text5, pos=(6,1), border = 10, flag = wx.EXPAND)# | wx.RIGHT)#, flag = wx.EXPAND)
        grid_layout.Add(units_text_5, pos=(6,2), border = 10, flag = wx.EXPAND)
        self.textBoxes.append(text5)



        
        
        #grid_layout.Add(self.text1, 1, wx.ALL | wx.ALIGN_CENTER, border=10)
        #grid_layout.Add(self.text2, 1, wx.ALL | wx.ALIGN_CENTER, border=10)
        #grid_layout.Add(self.text1, pos=(1,1), span=(1,2), border = 10)#, flag = wx.EXPAND)#, flag = wx.ALL)
        #grid_layout.Add(self.text2, pos=(2,1), span=(1,2), border = 10)#, flag = wx.EXPAND)
        
        

        #creating the calculate button
        #bm=wx.Image("gradientimg.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #bm=wx.Image("gradientbutton.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        
        """
        width, height = self.scroll.GetBestSize()
        width_2, height_2 = self.GetVirtualSize()
        print width
        print width_2
        dx = wx.SystemSettings_GetMetric(wx.SYS_VSCROLL_X)
        print dx
        self.SetMaxSize((width + (width - width_2) + dx, -1)) # Trying to limit the width of our frame
        self.scroll.SetScrollbars(1, 1, width, height) # throwing up some scrollbars
        """

        #wx.SetOptions(button_color=wx.COLOR_SYSTEM_DEFAULT)

        #calcButton = wx.Button(panel, -1, label="Convert")
        #calcButton.SetBitmap(bm)
        #calcButton.SetSize(20,20)
        #calcButton.SetBitmapMargins(40,40)

        calcButton = buttons.GenButton(panel, -1, label="Convert")
        calcButton.SetBezelWidth(4)
        #calcButton.SetMaxSize((50, 50))
        calcButton.SetBackgroundColour((28,58,137))
        #calcButton.SetOwnForegroundColour((195, 216, 234))
        calcButton.SetOwnForegroundColour(wx.WHITE)
        calcButton.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        calcButton.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        #grid_layout.Add(calcButton, 0, wx.ALL | wx.ALIGN_CENTER, 10)
        grid_layout.Add(calcButton, pos=(7,1),span=(1,2), border = 20, flag = wx.EXPAND)#EXPAND)#wx.ALIGN_CENTER)#, flag = wx.ALL | wx.ALIGN_CENTER)

        #creating the output display box:       
        self.outMsg = "RESULTS:\n\nPress calculate to view your results."
        #self.outTextBox = wx.TextCtrl(panel, value = self.outMsg, style=wx.TE_READONLY | wx.TE_MULTILINE)
        #self.outTextBox = wx.TextCtrl(panel, value = self.outMsg, style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.outTextBox = wx.TextCtrl(panel, value = self.outMsg, style=wx.TE_READONLY)
        #self.outTextBox.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)) 
        self.outTextBox.SetBackgroundColour((28,58,137)) 
        self.outTextBox.SetForegroundColour(wx.WHITE)

        #grid_layout.Add(self.outTextBox, 1, wx.EXPAND | wx.BOTTOM, 0)
        #grid_layout.Add(self.outTextBox, pos=(4,1), span=(1,2), border = 10, flag = wx.ALIGN_CENTER | wx.ALL)
        grid_layout.Add(self.outTextBox, pos=(8,1), span=(1,2), border = 10, flag = wx.GROW)

        #grid_layout.AddGrowableCol(0)
        grid_layout.AddGrowableCol(1)
        grid_layout.AddGrowableRow(0)
        #grid_layout.AddGrowableRow(2)
        #grid_layout.AddGrowableRow(3)
        grid_layout.AddGrowableRow(4)
        #grid_layout.AddGrowableRow(5)
        #grid_layout.AddGrowableCol(2)
        panel.SetSizer(grid_layout)

    def scale_bitmap(self, bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        return result
    
    

    #button press event handler
    def OnButtonClick(self, e):

        self.bfore_first_button_press = False

        #remove whitespace from text entered in each box
        self.allTextBoxContents.append(self.text1.GetValue().strip(' '))
        self.allTextBoxContents.append(self.text2.GetValue().strip(' '))
        self.allTextBoxContents.append(self.text3.GetValue().strip(' '))
        self.allTextBoxContents.append(self.text4.GetValue().strip(' '))
        self.allTextBoxContents.append(self.text5.GetValue().strip(' '))
        #contents1 = self.text1.GetValue().strip(' ')
        #contents1 = self.GetValue().strip(' ')
        #contents2 = self.text2.GetValue().strip(' ')

        #if there are non-numeric chars in input strings, return false.
        #if not((contents1.isnumeric()) and (contents2.isnumeric())):
        #   self.outMsg = "Error: only numeric values are accepted."

        for content in self.allTextBoxContents:
            if not content.isnumeric():
                self.outMsg = "RESULTS:\n\nError: only numeric values are accepted."
        
        #otherwise, extract values and return them in a tuple.
        else:
            vals = float(self.allTextBoxContents)
            print(vals)
            #val1 = float(contents1) #extract num from contents of first text box as float
            #val2 = float(contents2) #ditto for second text box
            #val3 =
            #val4
            #val5
            #self.input = (val1, val2)

            if not (20 <= val1 <= 500) or not (20 <= val2 <= 500):
                self.outMsg = "RESULTS:\n\nError: a glucose concentration is out of specified glucometer measurement range."

            else:
                c = be.converter()

                interpolatedVal = c.convertConcentration(val1,val2)
                
                if interpolatedVal == -1: #does this explanation make sense? - python interprets 0.0 as False so I made -1 the code for a significant decrease so as not to trip this conditional if a legitimate 0.0 was returned
                    print(interpolatedVal)
                    self.outMsg = "RESULTS:\n\nError: glucose concentration decreased by more than standard deviation of selected glucometer."

                else:
                    self.outMsg = "RESULTS:\n\nCA125: {:.3f} U/mL\n".format(interpolatedVal)
                    self.outMsg += "Abnormal: greater than or equal to 35" if interpolatedVal >= 35 else "Normal: below 35"
        
        self.outTextBox.SetValue(self.outMsg)
        
        '''
    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

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
        """

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        #menuBar = wx.MenuBar()
        #menuBar.Append(fileMenu, "&File")
        #menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        '''

    
    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    '''
    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)
    '''


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = BasicCalculator(None, title='ROSA GluConverter')
    #frm.SetSizerAndFit(sizer, deleteOld=True)
    frm.Show()
    app.MainLoop()
    #wx.lib.inspection.InspectionTool().Show()