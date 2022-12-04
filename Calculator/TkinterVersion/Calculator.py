from tkinter import * 
import logging
from Calculate import Calculate

logging.basicConfig(
    level=logging.WARNING,
    format=("%(asctime)s %(message)s")
)


class Calculator(Frame):
    a = ''
    b = ''
    opt = None
    _calculate = Calculate()

    def __init__(self, master=None):
        super().__init__(master)

        self.grid(ipadx=3, ipady=3, sticky=(N, S, W, E))

        keys = ['123+', '456-', '789*', "=0c/"]
        self.displayVal = StringVar(value=0)
        self.displayTotal = StringVar(value=0)
        
        self.frame = Frame(self, borderwidth=6, relief=SUNKEN, height=100, width=200)
        self.frame.grid(column=0, row=0, columnspan=4, rowspan=2,sticky=(N, S, W, E))
        self.display1 = Label(self.frame, textvariable=self.displayVal)
        self.display1.grid(column=4, sticky=E)
        self.display2 = Label(self.frame, textvariable=self.displayTotal)
        self.display2.grid(column=4,sticky=W)
        
        
        r=3
        for key in keys:
            c=0
            for k in key:
                # print(k, c, r)
                self.button(k, c, r)
                c+=1
            r+=1


        Button(text="Quit", command=self.quit).grid(column=0, row=10, columnspan=4, sticky=(N,S,W,E))

    def __calculate(self, val):
        self._calculate.Perform(val=val, display=self.displayVal, total=self.displayTotal)


    def button(self, text, col, row):
        btn = Button(
            self, text=text,
            command=lambda c=self.__calculate: c(text)
        )
        btn.grid(column=col, row=row, sticky=(N, S, E, W))
        return btn 


if __name__ == "__main__":
    c = Calculator()
    c.master.title = "Calculator"
    c.mainloop()
    
    