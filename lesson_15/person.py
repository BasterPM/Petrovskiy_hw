from bank import Bank
from property import House, Car
from property_manager import PropertyManager
import random


class Person:
    id_person = 1

    def __init__(self):
        self.id = Person.id_person
        self.bank_account = Bank()
        self.property_manager = PropertyManager()
        self.prop = []
        Person.id_person += 1

    def work(self):
        salary = random.randint(5, 10)
        self.bank_account.credit_funds(salary)

    def bye_property(self, type_property: str):
        if type_property == 'real estate':
            if not self.bank_account.money >= House.cost:
                print('You don\'t have enough money')
                return
            for i in self.prop:
                if isinstance(i, Car):
                    self.bank_account.write_off_funds(House.cost)
                    self.prop.append(self.property_manager.bye_real_estate())
                    return

        if type_property == 'movable property':
            if not self.bank_account.money >= Car.cost:
                print('You don\'t have enough money')
                return
            self.bank_account.write_off_funds(Car.cost)
            self.prop.append(self.property_manager.bye_movable_property())
            return
        else:
            raise ValueError('the type of property can only be: movable property or real estate')

    def sale_property(self, number_prop):
        if not number_prop <= len(self.prop):
            raise ValueError('there is no such number')
        self.bank_account.credit_funds(self.prop[number_prop - 1].cost)
        self.prop.pop(number_prop - 1)

    def info_prob(self):
        list_number = 1
        for i in self.prop:
            print(f'№{list_number}: {i.name} {i.number}, {i.cost}')
            list_number += 1
