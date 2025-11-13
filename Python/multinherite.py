class Father:
    def skills(self):
        print("Can Dive")

class Mother:
    def skills(self):
        print("Can Cook")

class Child(Father, Mother):
    def skills(self):
        super().skills()
        print("Can Code")

c = Child()
c.skills()