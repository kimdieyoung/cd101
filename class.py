class user:
    def __init__(self, f_name, l_name, byear, sex):
        self.f_name = f_name
        self.l_name = l_name
        self.byear = byear
        self.sex = sex
    def grit(self, curr_year):
        print(f"name: {self.f_name}, {self.l_name}, year: {self.byear}")
    def age(self, curr_year):
        return curr_year - self.byear
    @staticmethod
    def avg(self,other):
        z = self.age(2021) + other.age(2021) / 2
        return z


    
user1 = user("Paul", "Rickar", 1946, "male")
user2 = user('Piere', 'Gassly', 1996, "male")

