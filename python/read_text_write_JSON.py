import json


f = open("provincias_simple.txt", "r")
poly_str = f.read()
exec("my_poly= " + poly_str)


with open("provincias_simple.json", "w") as write_file:
    json.dump(my_poly, write_file, indent=4, ensure_ascii=False)