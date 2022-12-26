class Madlibs:
    def __init__(self, adj, verb1, verb2, famous_person):
        self.adj = adj
        self.verb1 = verb1
        self.verb2 = verb2
        self.famous_person = famous_person

    @property
    def madlib(self):
        return f"Computer Programming is so {self.adj}! It makes me so excited all the time because I love to {self.verb1}. Stay Hydrated and {self.verb2} like you are {self.famous_person}!"

    @staticmethod
    def user_input():
        return Madlibs(input("Enter the adjective: "), input("Enter first verb: "), input("Enter second verb: "), input("Enter your the name of your favorite person: "))


user = Madlibs.user_input()

print(user.madlib)
