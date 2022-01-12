class Temperature:
    dictionary = {'C': {'from_C': lambda x: x, 'to_C': lambda x: x},
                  'F': {'from_C': lambda x: x * 9 / 5 + 32, 'to_C': lambda x: (x - 32) * 5 / 9},
                  'K': {'from_C': lambda x: x + 273.15, 'to_C': lambda x: x - 273.15}}

    def __init__(self, temp_in, measure):
        self.C = Temperature.dictionary[measure]['to_C'](temp_in)
        self.F = Temperature.to_F(temp_in, measure)
        self.K = Temperature.to_K(temp_in, measure)
        self.measure = measure # для сложения температур
        self.temp_in = temp_in # для сложения температур

    @staticmethod
    def to_F(my_temp, measure):
        temp_in_C = Temperature.dictionary[measure]['to_C'](my_temp)
        temp_in_F = Temperature.dictionary['F']['from_C'](temp_in_C)
        return temp_in_F

    @staticmethod
    def to_K(my_temp, measure):
        temp_in_C = Temperature.dictionary[measure]['to_C'](my_temp)
        temp_in_K = Temperature.dictionary['K']['from_C'](temp_in_C)
        return temp_in_K

    def __eq__(self, other):
        if self.C == other.C:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.C != other.C:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.C < other.C:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.C > other.C:
            return True
        else:
            return False

    def __le__(self, other):
        if self.C <= other.C:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.C >= other.C:
            return True
        else:
            return False

    def __add__(self, other): # возвращаю не просто сумму, чтоб расчет был физически корректным
       return Temperature(self.C + (other.temp_in * 5 / 9 if other.measure == 'F' else other.temp_in), 'C')

    def __sub__(self, other):
       return Temperature(self.C - (other.temp_in * 5 / 9 if other.measure == 'F' else other.temp_in), 'C')

    def __str__(self):
        return f'{self.C} degrees Celsius, or {self.F} degrees Fahrenheit, or {self.K} kelvins'


print(Temperature.to_K(0, 'C'))

temp1 = Temperature(20, 'F')
print(temp1.C)

temp2 = Temperature(20, 'F')
print(temp2.C)
print(temp1 - temp2)
print(temp1 >= temp2)
print(temp1 == temp2)
