import bank
import property
import property_manager
import random


class Person:
    id_person = 1

    def __init__(self):
        self.id = Person.id_person
        self.bank_account = bank.Bank()
        self.property_manager = property_manager.PropertyManager()
        self.prop = []
        Person.id_person += 1

    def work(self):
        salary = random.randint(5, 10)
        self.bank_account.credit_funds(salary)

    def bye_property(self, type_property: str):
        if type_property == 'real estate':
            if not self.bank_account.money >= property.House.cost:
                print('You don\'t have enough money')
                return
            for i in self.prop:
                if isinstance(i, property.Car):
                    self.bank_account.write_off_funds(property.House.cost)
                    self.prop.append(self.property_manager.bye_real_estate())
                    return

        if type_property == 'movable property':
            if not self.bank_account.money >= property.Car.cost:
                print('You don\'t have enough money')
                return
            self.bank_account.write_off_funds(property.Car.cost)
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
