class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if observer != modifier:
                observer.update(self)

class Observer:
    def update(self, subject):
        print(f"Observer: My subject just updated and notified me. State: {subject._state}")

# Usage
subject = Subject()
observer_a = Observer()
subject.attach(observer_a)
subject._state = 123  # Change state
subject.notify()  # Notify observers
