import re


# Implementing Base Class
class MusicalInstrument:
    def __init__(self, name, type_):
        self.__name = name
        self.__type = type_
        self.__is_tuned = False

    # Getters and Setters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type_(self):
        return self.__type

    @type_.setter
    def type_(self, value):
        self.__type = value

    def play(self):
        print(f"{self.__name} is being played.")

    def tune(self):
        self.__is_tuned = True
        print(f"{self.__name} is tuned.")

    def check_tuning(self):
        status = "tuned" if self.__is_tuned else "not tuned"
        print(f"{self.__name} is {status}.")


# Implementing Inheritance
class Guitar(MusicalInstrument):
    def __init__(self, name, number_of_strings):
        super().__init__(name, "String")
        self.number_of_strings = number_of_strings

    def play(self):
        print(f"{self.name} is strumming.")


class Piano(MusicalInstrument):
    def __init__(self, name, number_of_keys):
        super().__init__(name, "String")
        self.number_of_keys = number_of_keys

    def play(self):
        print(f"{self.name} is playing.")


class Drum(MusicalInstrument):
    def __init__(self, name, drum_size):
        super().__init__(name, "Percussion")
        self.drum_size = drum_size

    def play(self):
        print(f"{self.name} is being beaten.")


# Polymorphism
def test_instruments(instruments):
    for instrument in instruments:
        instrument.play()
        instrument.check_tuning()

def main():
    # Instantiate objects
    guitar = Guitar("Fender Stratocruisers", 6)
    piano = Piano("Yamaha Grand", 88)
    drum = Drum("Pearl Drum", "Medium")

    # List of instruments
    instruments = [guitar, piano, drum]

    # Tune all instruments
    for instrument in instruments:
        instrument.tune()

    # Test all instruments
    test_instruments(instruments)

    # Show encapsulation in action
    print("\nAttempting to access and modify private attributes directly:")
    try:
        print(guitar.__name)  # AttributeError
    except AttributeError:
        print("Cannot access private attribute '__name' directly.")

    try:
        guitar.__name = "New Guitar Name"  # private attribute
        print(guitar.__name)  # Will still raise an AttributeError
    except AttributeError:
        print("Cannot modify private attribute '__name' directly.")


if __name__ == "__main__":
    main()
