country_code = {}
country_code = {"America": "1", "Austrailia": "61", "Japan": "81", "Korea": "82", "China": "86"}
print(country_code)

print(country_code.keys())

country_code["German"] = 49
print(country_code)
print(country_code.values())

print(country_code.items())

for k, v in country_code.items():
    print("Key:", k)
    print("Value:", v)

