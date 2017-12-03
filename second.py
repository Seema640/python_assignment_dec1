def area_circle(radius):
    pi=22/7
    return 2*pi*radius

radius= float(input('Enter the radius: '))
ans= area_circle(radius)
print("The radius and area of a circle is {:.3f} and {:.3f}".format(radius,ans))