# Crear una función que dibuje una estrella, donde el argumento de la función es el tamaño que tendrá la estrella.
# Un tamaño de 1 será así:
#     *
# Un tamaño de dos será así:
#          ***
#          ***
#          ***
# un tamaño de tres serça así:
#         * * *
#          ***
#         *****
#          ***
#         * * *

def my_fun(n):
    if n - 1 < 1:
        return "*"

    # Full star, empty:
    star = []
    floors = n * 2 -1

    #  Center line
    center = "*"
    to_add = "*" * (n - 1)
    center_line = to_add + center + to_add

    #  Other lines
    lenght = n - 1


    #  Sumamos , iteramos y creamos espejo del chunk. En este loop metemos la mitad superior de la estrella
    for i in range(0, lenght):

        # Seems thatt a list is stored as a memory address, not as a list itself.
        chunk = []
        for j in range(0, lenght):
            chunk.append(" ")
        chunk2 = chunk
        position = i
        chunk2[position] = "*"
        full_line = chunk2 + ["*"] + chunk2[::-1]
        full_line = "".join(full_line)
        star.append(full_line)

    # Agregamos la línea del medio
    star.append(center_line)

    # Agregamos la segunda mitad
    starHalf2 = []
    for i in star[::-1][1:]:
        starHalf2.append(i)

    star = star + starHalf2

    # should be ready now
    return star


my_star = my_fun(10)

for i in my_star:
    print(i)
