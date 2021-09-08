#class
class Person:

    def walk(self):   #instance keyword --self
        print("Person is walking")
    def reading(self):
        print("person is reading")

#object
#Person()     #object created
pe1=Person()
pe1.reading()
pe1.walk()

#object2
pe2=Person()
pe2.walk()
pe2.reading()