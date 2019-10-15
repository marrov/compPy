def is_leap_year(year):

    if year % 100 == 0:
        century = year // 100
        return century % 4 == 0
    else:
        return year % 4 == 0
