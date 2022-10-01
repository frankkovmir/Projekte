import csv

def cardata(data):
    car_brands = {}
    car_brand_hp = {}
    with open(data, 'r') as fhandle:
        csv_reader = csv.DictReader(fhandle)
        cars = list(csv_reader) #creates a list of dictionaries
        print(cars[0]) #gives the first list item with all keys
        for car in cars: #loop list of dicts
            car_brands[car['Identification.Make']] = car_brands.get(car['Identification.Make'], []) + [car['Engine Information.Engine Statistics.Horsepower']]
            #get all Horsepower entries for Audi, +[] is needed
        print(car_brands['Audi'])
        for car_brand, hp_list in car_brands.items(): #iterate with key, val through dict (hp_list is a list)
            hp_sum = 0
            #sum up horsepowers
            for hp in hp_list:
                hp_sum = hp_sum + int(hp)
            #add average hp of a brand to new dict, syntax: key = value
            car_brand_hp[car_brand] = hp_sum / len(hp_list)
        print(car_brand_hp)


data = "C:/Users/Franky/Downloads/cars.csv"
cardata(data)