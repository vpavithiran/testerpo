class Information:
    def __init__(self):
        self.age = None
        self.name = None

    def get(self):
        name = input("what is you name:")
        age = input("What is you age:")
        self.name = name
        self.age = age

    def put(self):
        print("your name is " + self.name)
        print("your age is " + self.age)

p = Information()
p.get()
p.put()
