import myfitnesspal

client = myfitnesspal.Client('Jackthegreatreacher', password='my_password')
day = client.get_date(2021, 8, 22)
weight = client.get_measurements('Weight')