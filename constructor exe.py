class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f'hi, i am {self.name}')

pratik = Person("Pratik Pawar")
print(pratik.name)
pratik.talk()

