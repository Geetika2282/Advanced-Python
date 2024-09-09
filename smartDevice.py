from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def _init_(self):
        _name = ''
        _status = 'on'

    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass

    def deviceInfo(self):
        pass


class SmartLight(SmartDevice):
    def __init__(self):
        super()._init_()

    def turnOn(self):
        self.status = 'on'
        return f"Smart Light is {self.status}"

    def turnOff(self):
        _status = 'off'
        return f"Smart Light is {self.status}"

    def deviceInfo(self):
        self.name = input("Enter light name: ")
        return f"{self.name} is {self.status}"


    def setBrightness(self):
        limit = int(input("Enter brightness: "))
        return f"Brightness set to {limit}"


class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__()

    def turnOn(self):
        self.status = 'on'
        return f"Smart ThermoStat is {self.status}"

    def turnOff(self):
        _status = 'off'
        return f"Smart ThermoStat is {self.status}"

    def setTemp(self):
        temp = int(input("Set Temperature to: "))
        return  f"Temperature set to: {temp}"


smart = SmartLight()
print(smart.turnOn())
print(smart.setBrightness())
print(smart.turnOff())
print(smart.deviceInfo())


thermo = SmartThermostat()
print(thermo.turnOn())
print(thermo.turnOff())
print(thermo.setTemp())