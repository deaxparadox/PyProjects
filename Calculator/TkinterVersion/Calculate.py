from tkinter import StringVar
import logging

logging.basicConfig(
    level=logging.WARNING,
    format=("%(asctime)s %(message)s")
)

class Calculate:
    def __init__(self):
        self.a = ""
        self.b = ""
        self.opt = None

    def __Add(self, a, b):
        return a + b 
    def __Sub(self, a, b):
        return a - b 
    def __Mul(self, a, b):
        return a * b 
    def __Div(self, a, b):
        return a / b 
    

    def __Calculate(self, a, b, opt):
        assert isinstance(a, float)
        assert isinstance(b, float)
        assert isinstance(opt, str)

        if opt == "+":
            return self.__Add(a, b)
        elif opt == "-":
            return self.__Sub(a, b)
        elif opt == "*":
            return self.__Mul(a, b)
        elif opt == "/":
            return self.__Div(a, b)
        else:
            print("operation not performed")

    def Perform(self, val = None, display: StringVar =None, total: StringVar = None):
        if val == "c":
            self.a = ""
            self.b = ""
            self.opt = None
            self.total = None
            display.set(0)
            return 
        # while True:
        #     val = input(">>> ")
        try:
            # check is val is number
            num = float(val)

            if not self.opt:
                # if self.opt is not assigned
                # set the val to self.a
                self.a += val 

                # set self.a to display
                display.set(self.a)

                logging.warning(f"\ttotal={self.a}\ta={self.a}\tb={self.b}\topt={self.opt}")

            else:
                # if self.opt is assigned
                # set val to self.b
                self.b += val 

                # set self.b to display 
                display.set(" ".join([self.a, self.opt, self.b]))

                logging.warning(f"\ttotal={self.a}\ta={self.a}\tb={self.b}\topt={self.opt}")

        except:
            if not self.opt and val != "=":
                # if self.opt is not assigned and val is not "="
                # set val to self.opt
                self.opt = val 

                logging.warning(f"\ttotal={self.a}\ta={self.a}\tb={self.b}\topt={self.opt}")

                display.set(" ".join([self.a, self.opt]))

            else:
                if len(self.b) > 0:
                    # if self.b length is greator than 0

                    if val == '=':
                        # if val is "="

                        # check if self.opt is set or not 
                        if not self.opt:
                            logging.warning("invalid operation")
                            logging.warning(f"\ttotal={self.a}\ta={self.a}\tb={self.b}\topt={self.opt}")
                            # continue
                            return
                        logging.warning(f"\ttotal={self.a}\ta={self.a}\tb={self.b}\topt={self.opt}")

                        # get total
                        self.total = self.__Calculate(
                            float(self.a), float(self.b), self.opt
                        )
                        total.set(self.total)
                        self.a = str(self.total)
                        self.b = ""
                        self.opt = None 
                        display.set(" ".join([self.a]))
                        logging.warning(f"\ttotal={self.a}\ta={self.a}\tb={self.b}\topt={self.opt}")
                    else:
                        # if val is not '=' or operator
                        logging.warning(f"\ttotal={self.a}\ta={self.a}\tb={self.b}\topt={self.opt}")
                        self.total = self.__Calculate(
                            float(self.a), float(self.b), self.opt
                        )
                        total.set(self.total)
                        self.a = str(self.total)
                        self.b = ""
                        self.opt = val
                        display.set(" ".join([self.a, self.opt]))
                        logging.warning(f"\ttotal={self.a}\ta={self.a}\tb={self.b}\topt={self.opt}")
                else:
                    logging.warning("b is not set")


if __name__ == "__main__":
    c= Calculate()
    c.Perform()