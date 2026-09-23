class c1:
    myAttr = 10 #attributo di classe
    counter = 0
    def __init__(self, message):
        self.message = message
        c1.counter +=1
    def myMethod(self):
        print(id(self))
    #def setMessage(self, message):
        #self.message = message
    def printMessage(self):
        print(self.message)
    @classmethod
    def istanze(cls):
        print(cls.counter)



class BClass():
    def setMessage(self, message):
        self.message = message
    def printMessage(self):
        print("From BClass: ", self.message)


class AClass(BClass):
    pass

if __name__ == "__main__":
    class1 = c1("pippo")
    class2 = c1("pluto")
    class1.myMethod()
    class2.myMethod()
    print(class1.myAttr)
    print(type(class1))

    ################################
    m1 = c1("primo")
    # m1.setMessage()
    m2 = c1("Secondo")
    # m2.setMessage()
    m1.printMessage()
    m2.printMessage()

    #################################
    c1.istanze()

    ##########################
    # m1 (istanza di AClass) Eredità i metodi e gli attributi della super classe BClass
    m1 = AClass()
    m1.setMessage("Pippo")
    m1.printMessage()


    
