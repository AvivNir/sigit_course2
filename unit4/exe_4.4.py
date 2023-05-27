

def gen_secs():
    """
        Generates a generator of seconds (0 to 59).

        Yields:
        - int: The next second in the sequence.
    """

    sec = 1
    for i in range(60):
        yield sec
        sec = (sec + 1) % 60


def gen_minutes():
    """
       Generates a generator of minutes (0 to 59).

       Yields:
       - int: The next minute in the sequence.
    """
    minute = 0
    for i in range(60):
        yield minute
        minute = (minute + 1) % 60


def gen_hours():
    """
       Generates a generator of hours (0 to 23).

       Yields:
       - int: The next hour in the sequence.
    """
    hour = 0
    for i in range(24):
        yield hour
        hour = (hour + 1) % 24


def gen_time():
    """
        Generates a generator of time strings in the format
        "HH:MM:SS" for all hours, minutes, and seconds.

        Yields:
        - str: The next time string in the sequence.
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)


def gen_years(start=2019):
    """
        Generates a generator of years starting from a given start year.

        Parameters:
        - start (int): The start year (default: 2019).

        Yields:
        - int: The next year in the sequence.
    """
    while True:
        yield start
        start += 1


def gen_months():
    """
        Generates a sequence of months (1 to 12).

        Yields:
        - int: The next month in the sequence.
    """
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """
       Generates a generator of days for a given month.

       Parameters:
        - month (int): The month (1 to 12).
        - leap_year (bool): Whether it is a leap year or not (default: True).

       Yields:
       - int: The next day in the sequence.
    """
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    for day in range(1, days_in_month[month]):
        yield day


def gen_date():
    """
       Generates a sequence of date-time strings in the format
        "DD/MM/YYYY HH:MM:SS" for all dates, hours, minutes, and seconds.

       Yields:
        - str: The next date-time string in the sequence.
    """
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield "%02d/%02d/%04d %02d:%02d:%02d" % (day, month, year, hour, minute, second)


def main():
    # create a generator
    gen = gen_date()
    count = 0

    for date in gen:
        count += 1
        # print every 1000000 iteration
        if count % 1000000 == 0:
            print(date)


if __name__ == '__main__':
    main()
