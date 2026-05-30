class Sensor:
    def __init__(self,temp):
        self.set_temp(temp)
        self.__temp = 90
    def get_temp(self):
        return self.__temp
    def set_temp(self, temp2):
        if -50 <= temp2 <= 150:
            self.__temp = temp2
        else:
            print("A temperatura não está entre -50 e 150")
    def status(self):
        if -50 <= self.__temp <= 80:
            return "normal"
        elif 81 <=self.__temp <= 120:
            return "alerta"
        else:
            return "Critico"
s1 = Sensor(90)
print(f"Temperatura: {s1.get_temp()}°C")  
print(f"Status: {s1.status()}")
s2 = Sensor(200)
print(f"Status do s2: {s2.status()}")