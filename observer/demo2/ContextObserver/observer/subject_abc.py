import abc
from ContextObserver.observer.observer_abc import AbsObserver


class AbsSubject(metaclass=abc.ABCMeta):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from the AbsObserver class')
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tracaback):
        self._observers.clear()
