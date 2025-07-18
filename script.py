

class Parent():
    def printname(self,name):
        print("Your name is" + name)

class Children(Parent):
    pass

instanceChild=Children()
instanceChild.printname("Jakub")

