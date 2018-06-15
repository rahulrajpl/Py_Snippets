def calculate_age(born_year=1990):
    from datetime import datetime
    return int(datetime.now().year-born_year)


print(calculate_age(1988))


