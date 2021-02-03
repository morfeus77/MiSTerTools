import math
import numpy as np
from fractions import Fraction

def find_nearest_h(integer_lines, visible_pixels, proper_ratio, v_multi):
    last_remainder = 1
    r = 1
    for x in range(-5,6):
        integer_pixels = visible_pixels * (v_multi + x)
        try:
          diff = abs((integer_pixels / integer_lines) - proper_ratio)
          if (diff < last_remainder):
              last_remainder = diff
              r = x
        except:
              return 1
    return r

def find_gcm(x,y):
    for i in range(30,0,-1):
       if (np.mod(x,i) == 0 and np.mod(y,i) == 0):
          return i
    return 1

print("Mister Aspect Ratio Calculator")
print("Expected format: <visible dots> <visible lines> <dot clock in mhz>")

NTSC_CONST = "704.0/13.5"
PAL_CONST = "702.0/13.5"

ACTION_SAFE= 0.035
TITLE_SAFE = 0.05

LINES_NTSC = 240.0
LINES_PAL = 288.0


pixel_clock = float,input("Pixel clock: ")
visible_pixels = float,input("Visible pixels: ")
visible_lines = float,input("Visible lines: ")
video_type  = input("Video type (NTSC/PAL):")
clockstr = str(pixel_clock[1])
pixelstr = str(visible_pixels[1])
linestr = str(visible_lines[1])
print("Calculating for visible area of "+pixelstr+" x "+linestr+" at "+clockstr+" mhz pixel clock")

if video_type == "NTSC":
  pix_per_line = round(float(pixel_clock[1]) * 704.0 / 13.5)
  video_lines = LINES_NTSC
else:
  pix_per_line = round(float(pixel_clock[1]) * 702.0 / 13.5)
  video_lines = LINES_PAL

print("Dots per line: %f, Lines: %f Standard: %s\n" % (pix_per_line, video_lines,video_type))

horizontal_aspect = 4.0 * float(visible_pixels[1]) / pix_per_line
vertical_aspect   = 3.0 * float(visible_lines[1]) / video_lines

arx=0
ary=0
proper_ratio = horizontal_aspect / vertical_aspect


ratiofraction = Fraction.from_float(proper_ratio).limit_denominator(4096)
x = ratiofraction.numerator
y = ratiofraction.denominator


print("Aspect ratio: (%d:%d) (Floating Point:%f  Fraction:%f)" % (x, y, proper_ratio, (x / y)))

arx = 0
ary = 0


fractratio = pix_per_line / float(visible_lines[1])
ratiofraction = Fraction.from_float(fractratio).limit_denominator(4096)
xres = ratiofraction.numerator
yres = ratiofraction.denominator

print("Square aspect ratio: (%d:%d)" % (xres, yres))

res = [480, 720, 1080, 1200, 1440, 1576]


for i in range(0,6):
        arx = 0
        ary = 0
        v_multi = int(int(res[i]) / int(visible_lines[1]))
        integer_lines =float(visible_lines[1]) * v_multi

        nearest_h = find_nearest_h(integer_lines, int(visible_pixels[1]), proper_ratio, v_multi)
        integer_pixels = float(visible_pixels[1]) * (v_multi + nearest_h)


        if integer_lines > 0:
          fractratio = integer_pixels / integer_lines
          ratiofraction = Fraction.from_float(fractratio).limit_denominator()
          xres = ratiofraction.numerator
          yres = ratiofraction.denominator
        else:
          print("zero or negative")
          xres = 1
          yres = 1

        scaledwidth=int(v_multi + nearest_h) * int(visible_pixels[1])
        scaledheight=int(v_multi + nearest_h) * int(visible_lines[1])
        near1440Hor=int(v_multi) * int(visible_pixels[1])
        near1440Vert=int(v_multi) * int(visible_lines[1])
        if video_type == "NTSC":
           framerate = 60
           blankperiod = 1.172
        else:
           framerate = 50
           blankperiod = 1.188
        reqclock = float(scaledwidth) * float(integer_lines) * float(framerate) * float(blankperiod)

        print("Integer aspect ratio for %dp (%dx and %dx): (%d:%d) minimum required pixel clock: %f mhz" % (res[i],(v_multi + nearest_h),v_multi, xres, yres, reqclock/1000000))



        if int(res[i])==1440:
           if reqclock/1000000 > 185.203 :
              print("!! WARNING !! %dx integer scaling will not run with video_mode=12 and will require a custom_video" % (v_multi + nearest_h))
              print("!! WARNING !! To enable %dx integer scaling set a custom 1440p video_mode for this core with at least %f mhz pixel clock" % (v_multi+nearest_h, reqclock/1000000))
              print("!! WARNING !! Or use %dx integer scaling requiring a (%dx%d) video_mode." % (v_multi, near1440Hor, near1440Vert))   
              print("!! WARNING !! eg video_mode=1792,128,200,328,1344,1,3,46,204800")
 

