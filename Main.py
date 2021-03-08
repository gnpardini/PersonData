from Person import Person

person = Person("dyt")

#funciones
def askName():

    name = raw_input('Ingrese su nombre por favor: ')
    person.addName(name)
    resultName = person.addName(name)
    while resultName == False:
        name = raw_input('Error. Ingrese nuevamente su nombre por favor')
        resultName = person.addName(name)

    return name

def askId():

    id = raw_input('Ingrese su DNI por favor: ')
    person.addId(id)
    resultId = person.addId(id)

    while resultId == False:
        id = raw_input('Ingrese nuevamente su DNI por favor: ')
        resultId = person.addId(id)

    return id



#main
name = askName()
id = askId()
