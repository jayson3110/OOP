from abc import ABC 


class Computer:
    def __init__(self, computer_name, keyboard, headPhone, mouse):
        self.computer_name = computer_name
        self.keyboard = keyboard
        self.headPhone = headPhone
        self.mouse = mouse

    
     # method
    
    def open_computer(self):
        return "Openning Computer"


    def close_computer(self):
        return "Closing Computer"


#Inheritance

class Asus(Computer):
   def update(self, year):
       return " Updating version in year " + year

Asus = Asus("Asus", "Mechanic Keyboard", "Normal headphone", "electric mouse")

print(Asus.update("2019"))

# Encapsulation


class CIA_case_unsovle:
    def __init__(self,file, case, year, evidence):
        "public khai bao nhu binh thuong"
        self.year = year 

        "private"
        self.__file = file 
        self.__evidence = evidence 

        "protect"

        self._case = case 




# Polymorphism 

class Asus :

    def opening_computer(self):
        print("Openning computer Asus")


    def close_computer(self)
        print("Closing Computer Asus")


class CLC:

    def opening_computer(self):
        print("Openning computer CLC")


    def close_computer(self)
        print("Closing Computer CLC")






def checkingComputer(Computer): 
    Computer.opening_computer()


Asus = Asus()
CLC = CLC()

checkingComputer(Asus)
checkingComputer(CLC)



# Abstraction


class PersonAbstact(ABC):
    name = None
    age = 0
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
    @abstractmethod
    def getFull(self):
        pass


class Person(PersonAbstact):
    name = 'Vo Tien Dat'
    age = 21
    def getFull(self):
        self.getName()
        self.getAge()