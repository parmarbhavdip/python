from turtle import *
import colorsys

speed(0)
bgcolor("black")
h=0.0
for i in range(60):
     for j in range(10):
          c=colorsys.hsv_to_rgb(h,1,1)
          color(c)
          h+=0.0
          circle(190-i,90)
          left(100)
          h+=0.0
          c=colorsys.rgb_to_hsv(c[0],c[2],c[1])
          color(c)
          circle(190-i,90)
          center=left(00)