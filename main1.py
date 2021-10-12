from tkinter import *

#creating frame for calc
def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj
 

#creating button
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 90 bold')
        self.pack(expand= YES, fill= BOTH)
        self.master.title('Calculator')

#adding display widget
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
          justify='right'
          , bd=30, bg="powder blue").pack(side=TOP,
                                          expand=YES, fill=BOTH)

#add a clear button            
        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''))

#add numbers and symbols widget
        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda
                storeObj=display, q=iEquals: storeObj
                .set(storeObj.get() + q))

#add a equal button
        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                storeObj=display: s.calc(storeObj), '+')

            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                lambda storeObj=display, s= ' %s ' % iEquals: storeObj.set
                (storeObj.get() + S))

#start the GUI
if __name__=='__main__':
    app().mainloop()
 