
def serialize_plate(item):
    plate_id = item.id
    number = item.number
    city = item.city
    model = item.model
    manufacturer = item.manufacturer
    color = item.color
    year = item.year
    qru = item.qru
    item_dict = {'id': plate_id, 'number': number, 'city': city, 'model': model, 'manufac': manufacturer, 'color': color,
                 'year': year, "qru": qru}
    return item_dict
