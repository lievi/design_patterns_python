from ContextObserver.observer.observer_abc import AbsObserver


class CurrentKPIs(AbsObserver):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print(f"""
        Current open tickets: {self.open_tickets}
        New tickets in last hour: {self.new_tickets}
        Tickets closed in last hour: {self.closed_tickets}\n
        """)

    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)
