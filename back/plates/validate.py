def validate_plate(num_value, year_value, city_value, manufac_value, model_value, color_value):
    number = validate_number(num_value)
    year = validate_year(year_value)
    city = validate_city(city_value)
    manufac = validate_manufac(manufac_value)
    model = validate_model(model_value)
    color = validate_color(color_value)
    if not all([number, year, city, manufac, model, color]):
        return False
    return True


def validate_number(value):
    number = len(str(value))
    return False if number is not 7 else True


def validate_year(value):
    year = int(value)
    if 2000 > year or year > 2023:
        return False
    else:
        return True


def validate_city(value):
    city = len(value)
    return False if city < 3 else True


def validate_manufac(value):
    manufac = len(value)
    return False if manufac < 3 else True


def validate_model(value):
    model = len(value)
    return False if model < 3 else True


def validate_color(value):
    color = len(value)
    return False if color < 4 else True
