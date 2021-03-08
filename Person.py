class Person():

    def __init__(self,name):
        self.name = name

    def addName(self,name):

        self.name = name

        return name.isalpha()

    def addId(self,id):

        numbersQuantity = len(id)

        if (numbersQuantity != 8):
            return False

        return id.isalnum()

    def addAge(self,age):
        return age.isalnum()




