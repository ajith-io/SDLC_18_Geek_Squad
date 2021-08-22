import myfitnesspal

client = myfitnesspal.Client('Jackthegreatreacher', password='my_password')
day = client.get_date(2021, 8, 22)
print (day)
weight = client.get_measurements('Weight')
print (weight)
day.exercises[0].get_as_list()
print (day.exercises)
print (day.meals)
print (day.water)