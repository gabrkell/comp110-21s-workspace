"""A vaccination calculator."""

__author__ = "730230246"

from datetime import datetime
from datetime import timedelta

population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent: int = int(input("Target percent vaccinated: "))

today: datetime = datetime.today()
one_day: timedelta = timedelta(1)

percent_population = population * target_percent / 100
already_vaccinated = doses_administered / 2
still_need_vaccine = percent_population - already_vaccinated 
days_it_takes = round(still_need_vaccine / (doses_per_day / 2))

days: timedelta = timedelta(days_it_takes)
future: datetime = today + days
tp = str(target_percent)
date = str(future.strftime("%B %d, %Y"))
print("We will reach " + tp + "% vaccination in " + str(days_it_takes) + " days, which falls on " + date)