import property


class PropertyManager:

    @staticmethod
    def bye_real_estate():
        return property.House()

    @staticmethod
    def bye_movable_property():
        return property.Car()
