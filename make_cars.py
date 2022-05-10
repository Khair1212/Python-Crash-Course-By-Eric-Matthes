def make_car(manufacturer, model_name, **kwargs):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    for k,v in kwargs.items():
        car_info[k] = v
    return car_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
