import wx
import numpy as np
import scipy as sp
import conversionBackend as bcknd
import wx.lib.buttons as buttons
#import wx.lib.inspection
   

sizer = wx.BoxSizer(wx.VERTICAL)

class GluConverter(wx.Frame): #is the class really necessary?
    
    #text1 = None
    #text2 = None
    textBoxes = []
    allTextBoxContents = []
    outTextBox = None
    outMsg = ""
    text1 = None
    text2 = None
    text3 = None
    text4 = None
    text5 = None

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
        #glumtr_select = wx.Choice(panel, choices=["Select Glucometer","OneTouch Ultra","Bayer Contour"])
        glumtr_select = wx.Choice(column_panel, choices=["Select Glucometer","OneTouch Ultra","Bayer Contour"])
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

        self.text1 = wx.TextCtrl(panel)#, style=wx.ALIGN_CENTER)
        #self.text1.SetMaxSize(textbox_size)
        #text1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE)) 
        #text1.SetBackgroundColour((254,245,227))
        self.text1.SetBackgroundColour((28,58,137))
        self.text1.SetForegroundColour(wx.WHITE)
        #self.text1.SetHint("Initial Glucose Reading (mg/dL)")
        self.text1.SetHint("Glucose Reading 1")
        units_text_1 = wx.StaticText(panel, label="mg/dL", style=wx.ALIGN_CENTER_VERTICAL)#, style=wx.ALIGN_CENTER_HORIZONTAL)
        units_text_1.SetFont(font)
        units_text_1.SetForegroundColour((125,51,56))
        grid_layout.Add(self.text1, pos=(2,1), border = 10, flag = wx.EXPAND) #wx.EXPAND | wx.RIGHT)#, flag = wx.EXPAND)#, flag = wx.ALL)
        grid_layout.Add(units_text_1, pos=(2,2), border = 10, flag = wx.EXPAND)
        self.textBoxes.append(self.text1)
        
        #print("line length of text1 line 0: "+str(self.text1.GetLineLength(0)))

        self.text2 = wx.TextCtrl(panel)
        #self.text2.SetMaxSize(textbox_size)
        #self.text2.SetHint("Final Glucose Reading (mg/dL)")
        self.text2.SetHint("Glucose Reading 2")
        #text2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.text2.SetBackgroundColour((28,58,137))
        units_text_2 = wx.StaticText(panel, label="mg/dL", style=wx.ALIGN_CENTER_VERTICAL)
        units_text_2.SetFont(font)
        units_text_2.SetForegroundColour((125,51,56))
        grid_layout.Add(self.text2, pos=(3,1), border = 10, flag = wx.EXPAND)# | wx.RIGHT)#, flag = wx.EXPAND)
        grid_layout.Add(units_text_2, pos=(3,2), border = 10, flag = wx.EXPAND)
        self.textBoxes.append(self.text2)


        self.text3 = wx.TextCtrl(panel)
        #self.text2.SetMaxSize(textbox_size)
        #self.text2.SetHint("Final Glucose Reading (mg/dL)")
        self.text3.SetHint("Glucose Reading 3")
        #text3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.text3.SetBackgroundColour((28,58,137))
        units_text_3 = wx.StaticText(panel, label="mg/dL", style=wx.ALIGN_CENTER_VERTICAL)
        units_text_3.SetFont(font)
        units_text_3.SetForegroundColour((125,51,56))
        grid_layout.Add(self.text3, pos=(4,1), border = 10, flag = wx.EXPAND)# | wx.RIGHT)#, flag = wx.EXPAND)
        grid_layout.Add(units_text_3, pos=(4,2), border = 10, flag = wx.EXPAND)
        self.textBoxes.append(self.text3)

        self.text4 = wx.TextCtrl(panel)
        #self.text2.SetMaxSize(textbox_size)
        #self.text2.SetHint("Final Glucose Reading (mg/dL)")
        self.text4.SetHint("Glucose Reading 4")
        #text4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.text4.SetBackgroundColour((28,58,137))
        units_text_4 = wx.StaticText(panel, label="mg/dL", style=wx.ALIGN_CENTER_VERTICAL)
        units_text_4.SetFont(font)
        units_text_4.SetForegroundColour((125,51,56))
        grid_layout.Add(self.text4, pos=(5,1), border = 10, flag = wx.EXPAND)# | wx.RIGHT)#, flag = wx.EXPAND)
        grid_layout.Add(units_text_4, pos=(5,2), border = 10, flag = wx.EXPAND)
        self.textBoxes.append(self.text4)

        self.text5 = wx.TextCtrl(panel)
        #self.text2.SetMaxSize(textbox_size)
        #self.text2.SetHint("Final Glucose Reading (mg/dL)")
        self.text5.SetHint("Glucose Reading 5")
        #text5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
        self.text5.SetBackgroundColour((28,58,137))
        units_text_5 = wx.StaticText(panel, label="mg/dL", style=wx.ALIGN_CENTER_VERTICAL)
        units_text_5.SetFont(font)
        units_text_5.SetForegroundColour((125,51,56))
        grid_layout.Add(self.text5, pos=(6,1), border = 10, flag = wx.EXPAND)# | wx.RIGHT)#, flag = wx.EXPAND)
        grid_layout.Add(units_text_5, pos=(6,2), border = 10, flag = wx.EXPAND)
        self.textBoxes.append(self.text5)



        
        
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
        #image = wx.ImageFromBitmap(bitmap)
        image = bitmap.ConvertToImage()
        image = image.Rescale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = image.ConvertToBitmap()
        #result = wx.BitmapFromImage(image)
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

        vals = []

        for content in self.allTextBoxContents:
            #print(content)
            if not content.isnumeric():
                self.outMsg = "RESULTS:\n\nError: only numeric values are accepted."
                self.outTextBox.SetValue(self.outMsg)
                self.allTextBoxContents = []
                return
            else:
                vals.append(float(content))
        
        outOfRange = False

    
        for val in vals:
            if not (20 <= val <= 500):
                outOfRange = True
                self.outMsg = "RESULTS:\n\nError: a glucose concentration is outside of\nspecified glucometer's measurement range."
                self.outTextBox.SetValue(self.outMsg)
                #vals = []
                self.allTextBoxContents = []
                return
        

        if not outOfRange:
                c = bcknd.converter()
                interpolatedVals = c.convertConcentration(vals, 10) #assume measurement interval is 10
                if interpolatedVals == -1: #does this explanation make sense? - python interprets 0.0 as False so I made -1 the code for a significant decrease so as not to trip this conditional if a legitimate 0.0 was returned
                    #print(interpolatedVal)
                    self.outMsg = "RESULTS:\n\nError: average rate of change\nof glucose concentration was negative."
                else:
                    self.outMsg = "RESULTS:\n\nCA125: {:.3f} U/mL\nRange within 1 standard deviation: [{:.3f}, {:.3f}]".format(interpolatedVals[0], interpolatedVals[2], interpolatedVals[1])
                    #self.outMsg += "Abnormal: greater than or equal to 35" if interpolatedVals else "Normal: below 35"
                self.outTextBox.SetValue(self.outMsg)
                self.allTextBoxContents = []
                #vals = []

    
    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = GluConverter(None, title='ROSA GluConverter')
    frm.Show()
    app.MainLoop()
