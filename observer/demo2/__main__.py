from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs


with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(25, 10, 5)
        kpis.set_kpis(100, 40, 30)
        kpis.set_kpis(30, 50, 10)


print("\n*** Exited context managers *** \n\n")
kpis.set_kpis(999, 666, 455)
