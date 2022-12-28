import colorgram
colorslist = []
colors = colorgram.extract("OIP.jpg",30)
for i in range(30):
    first_color = colors[i].rgb
    print(first_color)
    r = first_color[0]
    g = first_color[1]
    b = first_color[2]
    tuple = (r,g,b)
    colorslist.append(tuple)

print(colorslist)