from graphics import circle
from graphics import rectangle
from graphics.ThreeDgraphics import cuboid
from graphics.ThreeDgraphics import sphere



r=int(input("enter the radius"))
circle.area(r)
circle.perimeter(r)
a=int(input("enter a"))
b=int(input("enter b"))
rectangle.area(a,b)
rectangle.perimeter(a,b)

l=int(input("Enter the length,l : "))
b=int(input("Enter the breadth,b : "))
h=int(input("Enter the height,h : "))
cuboid.perimeter(l,b,h)
cuboid.area(l,b,h)

r=int(input("Enter the radius,r : "))
sphere.volume(r)
sphere.area(r)


