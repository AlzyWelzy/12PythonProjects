class Madlibs:
    def __init__(self):
        self.template = "Computer Programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay Hydrated and {verb2} like you are {famous_person}!"

    def fill_in_blanks(self, adj, verb1, verb2, famous_person):
        self.adj = adj
        self.verb1 = verb1
        self.verb2 = verb2
        self.famous_person = famous_person

    @property
    def madlib(self):
        return self.template.format(adj=self.adj, verb1=self.verb1, verb2=self.verb2, famous_person=self.famous_person)


user = Madlibs()
user.fill_in_blanks(input("Enter the adjective: "), input("Enter first verb: "), input(
    "Enter second verb: "), input("Enter your the name of your favorite person: "))
print(user.madlib)
