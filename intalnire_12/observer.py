"""
Observer pattern example.
"""


class ObservableAdaugatUtilizator:
    name = "ObservableAdaugatUtilizator"

    def __init__(self):
        self._observers = []

    def __str__(self):
        return f"Eu sunt {self.name}"

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *a, **kwargs):
        for obs in self._observers:
            obs.notify(self, *a, **kwargs)


class Observer:
    def __init__(self, observable):
        observable.register_observer(self)

    def notify(self, observable, *args, **kwargs):
        print("Got", args, kwargs, "From", observable)


subject = ObservableAdaugatUtilizator()
observer_obj = Observer(subject)

subject.notify_observers("test", "test2", kw="python")
