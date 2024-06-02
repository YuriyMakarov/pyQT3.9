class Abonent:
    def __init__(self, id1, name1, surname1, midname1, adress1, number_card1, limit_city1, limit_out_city1):
        self.id0 = id1
        self.name0 = name1
        self.surname0 = surname1
        self.midname0 = midname1
        self.adress0 = adress1
        self.number_card0 = number_card1
        self.limit_city0 = limit_city1
        self.limit_out_city0 = limit_out_city1
        self.time_city0 = 0
        self.time_out_city0 = 0

    @property
    def name(self):
        return self.name0

    @name.setter
    def name(self, name2):
        self.name0 = name2

    @property
    def surname(self):
        return self.surname0

    @surname.setter
    def surname(self, surname2):
        self.surname0 = surname2

    @property
    def midname(self):
        return self.midname0

    @midname.setter
    def midname(self, midname2):
        self.midname0 = midname2

    @property
    def id(self):
        return self.id0

    @id.setter
    def id(self, id2):
        self.id0 = id2

    @property
    def adress(self):
        return self.adress0

    @adress.setter
    def adress(self, adress2):
        self.adress0 = adress2

    @property
    def number_card(self):
        return self.number_card0

    @number_card.setter
    def number_card(self, number_card2):
        self.number_card0 = number_card2

    @property
    def limit_city(self):
        return self.limit_city0

    @limit_city.setter
    def limit_city(self, limit_city2):
        self.limit_city0 = limit_city2

    @property
    def limit_out_city(self):
        return self.limit_out_city0

    @limit_out_city.setter
    def limit_out_city(self, limit_out_city2):
        self.limit_out_city0 = limit_out_city2

    @property
    def time_city(self):
        return self.time_city0

    @time_city.setter
    def time_city(self, time_city2):
        self.time_city0 = time_city2

    @property
    def time_out_city(self):
        return self.time_out_city0

    @time_out_city.setter
    def time_out_city(self, time_out_city2):
        self.time_out_city0 = time_out_city2

    def display_info(self):
        print(f"{self.id0}\n"
              f"{self.name0}\n"
              f"{self.surname0}\n"
              f"{self.midname0}\n"
              f"{self.adress0}\n"
              f"{self.number_card0}\n"
              f"{self.limit_city0}\n"
              f"{self.limit_out_city0}\n"
              f"{self.time_city0}\n"
              f"{self.time_out_city0}\n")


    def limit_city_up(self):
        if self.limit_city0 < self.time_city0:
            print(self.name0, self.surname0, self.midname0)

    def limit_city_out_up(self):
        if self.limit_out_city0 < self.time_out_city0:
            print(self.name0, self.surname0, self.midname0)


abonent1 = Abonent(1, "Имя1", "Фамилия1", "Отчество1", "aдрес1", 100, 1000, 2000)
abonent2 = Abonent(2, "Имя2", "Фамилия2", "Отчество2", "aдрес2", 100, 1000, 2000)
abonent3 = Abonent(3, "Имя3", "Фамилия3", "Отчество3", "aдрес3", 100, 1000, 2000)

abonents = [abonent1, abonent2, abonent3]
for ab in abonents:
    ab.time_city0 = int(input("Город: "))
    ab.time_out_city0 = int(input("МежГород: "))
    ab.display_info()
    ab.limit_city_up()
    ab.limit_city_out_up()

