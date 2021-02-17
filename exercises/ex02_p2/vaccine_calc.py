"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730230426"

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    number_days = days_to_target(population, doses, doses_per_day, target)
    the_date = future_date(number_days)
    print("We will reach " + str(target) + "% vaccination in " + str(number_days) + " days, which falls on " + the_date)


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """This calculates the days to get everyone vaccinated"""
    percent_population = population * target / 100
    already_vaccinated = doses / 2
    still_need_vaccine = percent_population - already_vaccinated 
    days_it_takes = round(still_need_vaccine / (doses_per_day / 2))
    return days_it_takes

def future_date(days_it_takes: int) -> str:
    days: timedelta = timedelta(days_it_takes)
    today: datetime = datetime.today()
    future: datetime = today + days
    date = str(future.strftime("%B %d, %Y"))
    return date

if __name__ == "__main__":
    main()
