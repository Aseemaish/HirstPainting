from colorgram import colorgram

clr = colorgram.extract("hirst.jpg", 30)
lst = []
for color in clr:   #Extracting the RGB values of the colors
    r = color.rgb.r  #Extracting the red value
    g = color.rgb.g #Extracting the green value
    b = color.rgb.b #Extracting the blue value
    lst.append((r, g, b))   #Appending the RGB values to the list
print(lst)  #Printing the list of RGB values