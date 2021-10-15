import json

# Takes a GeoJSON polygon file. then decreases the density of points. The original file is not modified, but a mew
# file is returned with lower density of points

# f = open("demofile.txt", "r")
# print(f.read()) # Note that f is a file object, with a "print" method.

# Now, if my_poly is a dictionary, generated from a GeoJSON file, then my_poly["features"][0] will return the first of
# the polygons.
# for i in my_poly["features"]:
# 	  print(i["geometry"]["coordinates"])
# these last 2 lines will return an array for each i. Every array has the following format, idk why:
# "coordinates": [
#             [
#                 [
#                     [ -58.341887396999937, -34.631096716999934, 0.0 ],
#                     [ -58.461390070999983, -34.705314975999954, 0.0 ],
#                     [ -58.531465195999942, -34.615966216999936, 0.0 ],
#                     [ -58.457476274999976, -34.526525524999954, 0.0 ],
#                     [ -58.341887396999937, -34.631096716999934, 0.0 ]
#                 ]
#             ]
#         ]

f = open("provincias_json.txt", "r")
poly_str = f.read()
exec("my_poly = " + poly_str)  # Careful, this takes a while!

# print(type(my_poly))


def reduce_vertex(coord_list):  # Takes as a parameter a list of coordinate pairs (or trio) that defines a polygon
    new_coord_list = []
    counter = 0
    for i in coord_list:
        add = True
        if counter == 0 or counter == len(coord_list):
            print("adding...")
            pass
        else:
            diffLat = i[0] - new_coord_list[-1][0]
            diffLong = i[1] - new_coord_list[-1][1]
            if (-0.1 < diffLat < 0.1) or (-0.1 < diffLong < 0.1):
                add = False
                print(diffLat, diffLong)
                print("not adding...")
        if add:
            new_coord_list.append(i)
            print("added", i)
        counter +=1

    #  Now, we make sure that there are at least 3 point in the coordinates list
    if len(new_coord_list) < 3:
        new_coord_list.append(coord_list[1])
    if len(new_coord_list) < 3:
        new_coord_list.append(coord_list[2])

    return new_coord_list


for i in my_poly["features"]:
    print("Old coords were:")
    print(i["geometry"]["coordinates"])
    new_coords = reduce_vertex(i["geometry"]["coordinates"][0][0])
    i["geometry"]["coordinates"][0][0] = new_coords
    print("New coords are:")
    print(i["geometry"]["coordinates"])
    print(" ")


with open("new_provincias.json", "w") as write_file:
    json.dump(my_poly, write_file, indent=4, ensure_ascii=False)




