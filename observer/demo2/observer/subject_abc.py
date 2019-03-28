import abc
from observer.observer_abc import AbsObserver

class AbsSubject(metaclass=abc.ABCMeta):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from the AbsObserver class')
        self._observers.add(observer)
    
    def detach(self, observer):
        self._observers.discard(observer)
    
    def notify(self, value=None):
        pass

    