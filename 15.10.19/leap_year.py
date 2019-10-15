def is_leap_year(year):

    # Check century
    if year % 100 == 0:
        century = year // 100
        if century % 4 == 0:
            return True
        else:
            return False
    else:
        # Check year
        if year % 4 == 0:
            return True
        else:
            return False
