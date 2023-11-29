class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temp):
        self._temperature = temp
        self.notify_observers()

class Observer:
    def update(self, temperature):
        pass

class CurrentConditionsDisplay(Observer):
    def update(self, temperature):
        print(f"Current conditions: {temperature}F degrees")

# Usage
weather_station = WeatherStation()
current_display = CurrentConditionsDisplay()
weather_station.register_observer(current_display)
weather_station.set_temperature(70)  # Notifies the observer
