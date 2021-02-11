
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from forms import LoginForm, ArForm, VmForm
from flask import render_template, flash, redirect
from flask_bootstrap import Bootstrap
from fractions import Fraction
import numpy as np


app = Flask(__name__)

app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

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


@app.route('/', methods=['GET', 'POST'])
def calc():
    form = VmForm()
    inputerror="Invalid modeline values"
    if form.validate_on_submit():
        try:
          pixel_clock, hdisp, hsyncstart, hsyncend, htotal, vdisp, vsyncstart, vsyncend, vtotal = map(float,form.modeline.data.split())
          pixel_clock=float(pixel_clock)
          hdisp = int(hdisp)
          hsyncstart = int(hsyncstart)
          hsyncend = int(hsyncend)
          htotal = int(htotal)
          vdisp = int(vdisp)
          vsyncstart = int(vsyncstart)
          vsyncend=int(vsyncend)
          vtotal=int(vtotal)
          clock=pixel_clock*1000
          video_mode = "video_mode="+str(hdisp)+","+str(hsyncstart-hdisp)+","+str(hsyncend-hsyncstart)+","+str(htotal-hsyncend)+","+str(vdisp)+","+str(vsyncstart-vdisp)+","+str(vsyncend-vsyncstart)+","+str(vtotal-vsyncend)+","+str(int(clock))
          return render_template('calcvm.html', title='Mister Modeline to Video_mode', form=form, reqmodeline=form.modeline.data, video_mode=video_mode)
        except:
           return render_template('calcvm.html', title='Mister Modeline to video_mode', form=form, reqmodeline=form.modeline.data, video_mode=inputerror)
    return render_template('calcvm.html', title='video_mode calculator', form=form)

@app.route('/vm', methods=['GET', 'POST'])
def calcvm():
    form = VmForm()
    inputerror="Invalid modeline values"
    if form.validate_on_submit():
        try:
          pixel_clock, hdisp, hsyncstart, hsyncend, htotal, vdisp, vsyncstart, vsyncend, vtotal = map(float,form.modeline.data.split())
          pixel_clock=float(pixel_clock)
          hdisp = int(hdisp)
          hsyncstart = int(hsyncstart)
          hsyncend = int(hsyncend)
          htotal = int(htotal)
          vdisp = int(vdisp)
          vsyncstart = int(vsyncstart)
          vsyncend=int(vsyncend)
          vtotal=int(vtotal)
          clock=pixel_clock*1000
          video_mode = "video_mode="+str(hdisp)+","+str(hsyncstart-hdisp)+","+str(hsyncend-hsyncstart)+","+str(htotal-hsyncend)+","+str(vdisp)+","+str(vsyncstart-vdisp)+","+str(vsyncend-vsyncstart)+","+str(vtotal-vsyncend)+","+str(int(clock))
          return render_template('calcvm.html', title='Mister Modeline to Video_mode', form=form, reqmodeline=form.modeline.data, video_mode=video_mode)
        except:
           return render_template('calcvm.html', title='Mister Modeline to video_mode', form=form, reqmodeline=form.modeline.data, video_mode=inputerror)
    return render_template('calcvm.html', title='video_mode calculator', form=form)


@app.route('/ar', methods=['GET', 'POST'])
def calcar():
    form = ArForm()

    if form.validate_on_submit():
          pixel_clock = float,form.pixelclock.data
          visible_pixels = float,form.pixels.data
          visible_lines =  float,form.lines.data
          video_type = form.videotype.data
          amiga = form.amiga.data
          amigares = form.amigares.data
          customres = form.customres.data
          customvertres = form.customvertres.data


          res = [480, 720, 1080, 1200, 1440, 1536]

          if customres:
             res.append(int(customvertres))

          rescount = len(res)

          if amiga:
              LINES_NTSC = 200.0
              LINES_PAL = 256.0
              if amigares == "AGA":
                  v_samplerate = 28.375160
              else:
                  v_samplerate = 14.187580
          else:
              v_samplerate = 13.5
              LINES_NTSC = 240.0
              LINES_PAL = 288.0

          if video_type == "NTSC":
            pix_per_line = round(float(pixel_clock[1]) * 704.0 / float(v_samplerate))
            video_lines = LINES_NTSC
          else:
            pix_per_line = round(float(pixel_clock[1]) * 702.0 / float(v_samplerate))
            video_lines = LINES_PAL

          if amiga:
            dotresult = "Dots per line: %f, Lines: %f Standard: %s Amiga res: %s\n" % (pix_per_line, video_lines,video_type,amigares)
          else:
            dotresult = "Dots per line: %f, Lines: %f Standard: %s\n" % (pix_per_line, video_lines,video_type)

          horizontal_aspect = 4.0 * float(visible_pixels[1]) / pix_per_line
          vertical_aspect   = 3.0 * float(visible_lines[1]) / video_lines

          proper_ratio = horizontal_aspect / vertical_aspect
          #x,y = find_fractions(horizontal_aspect, vertical_aspect, arx, ary)
          ratiofraction = Fraction.from_float(proper_ratio).limit_denominator(4096)
          x = ratiofraction.numerator
          y = ratiofraction.denominator

          arresult = "Aspect ratio: (%d:%d) (Floating Point:%f  Fraction:%f)" % (x, y, proper_ratio, (x / y))


          #xres,yres = find_fractions(pix_per_line, float(visible_lines[1]), arx, ary)
          fractratio = pix_per_line / float(visible_lines[1])
          ratiofraction = Fraction.from_float(fractratio).limit_denominator(4096)
          xres = ratiofraction.numerator
          yres = ratiofraction.denominator

          squareresult = "Square aspect ratio: (%d:%d)" % (xres, yres)

          for i in range(0,rescount):
            v_multi = int(int(res[i]) / int(visible_lines[1]))
            integer_lines =float(visible_lines[1]) * v_multi

            nearest_h = find_nearest_h(integer_lines, int(visible_pixels[1]), proper_ratio, v_multi)
            integer_pixels = float(visible_pixels[1]) * (v_multi + nearest_h)

            #xres,yres = find_fractions(integer_pixels, integer_lines, arx, ary)
            if integer_lines > 0:
              fractratio = integer_pixels / integer_lines
              ratiofraction = Fraction.from_float(fractratio).limit_denominator()
              xres = ratiofraction.numerator
              yres = ratiofraction.denominator
            else:
              xres = 1
              yres = 1

            scaledwidth=int(v_multi + nearest_h) * int(visible_pixels[1])
            near1440Hor=int(v_multi) * int(visible_pixels[1])
            near1440Vert=int(v_multi) * int(visible_lines[1])
            if video_type == "NTSC":
                framerate = 60
                blankperiod = 1.172
            else:
                framerate = 50
                blankperiod = 1.188
            reqclock = float(scaledwidth) * float(integer_lines) * float(framerate) * float(blankperiod)
            ar1440warning1=''
            ar1440warning2=''
            ar1440warning3=''
            arcustom = ''
            widertext = ''
            customini=''
            if customres:
              if res[i] == customvertres:
                ar480 = ''
                ar720 = ''
                ar1080 = ''
                ar1200 = ''
                ar1440 = ''
                ar1536 = ''
                ini480=''
                ini720=''
                ini1080=''
                ini1200=''
                ini1440=''
                ini1536=''
                arcustom = "Integer aspect ratio for %dp minimum required pixel clock: %f mhz" % (res[i], reqclock/1000000)
                customini = "custom_aspect_ratio_1=%d:%d      ; %d:%d @ %.3f, %d:%d PAR (%d:%d%s)" % ( xres, yres, int(visible_pixels[1]),int(visible_lines[1]), float(pixel_clock[1]), (v_multi + nearest_h), v_multi, (int(visible_pixels[1])*(v_multi + nearest_h)), (int(visible_lines[1])*v_multi),widertext)
            else:
              if res[i] == 480:
                ar480 = "Integer aspect ratio for %dp minimum required pixel clock: %f mhz" % (res[i], reqclock/1000000)
                ini480 = "custom_aspect_ratio_1=%d:%d      ; %d:%d @ %.3f, %d:%d PAR (%d:%d%s)" % ( xres, yres, int(visible_pixels[1]),int(visible_lines[1]), float(pixel_clock[1]), (v_multi + nearest_h), v_multi, int(visible_pixels[1])*(v_multi + nearest_h), int(visible_lines[1])*v_multi,widertext)
              if res[i] == 720:
                ar720 = "Integer aspect ratio for %dp minimum required pixel clock: %f mhz" % (res[i], reqclock/1000000)
                ini720 = "custom_aspect_ratio_1=%d:%d      ; %d:%d @ %.3f, %d:%d PAR (%d:%d%s)" % ( xres, yres, int(visible_pixels[1]),int(visible_lines[1]), float(pixel_clock[1]), (v_multi + nearest_h), v_multi, int(visible_pixels[1])*(v_multi + nearest_h), int(visible_lines[1])*v_multi,widertext)
              if res[i] == 1080:
                ar1080 = "Integer aspect ratio for %dp minimum required pixel clock: %f mhz" % (res[i], reqclock/1000000)
                ini1080 = "custom_aspect_ratio_1=%d:%d      ; %d:%d @ %.3f, %d:%d PAR (%d:%d%s)" % ( xres, yres, int(visible_pixels[1]),int(visible_lines[1]), float(pixel_clock[1]), (v_multi + nearest_h), v_multi, int(visible_pixels[1])*(v_multi + nearest_h), int(visible_lines[1])*v_multi,widertext)
              if res[i] == 1200:
                ar1200 = "Integer aspect ratio for %dp minimum required pixel clock: %f mhz" % (res[i], reqclock/1000000)
                if int(visible_pixels[1])*(v_multi + nearest_h) > 1600:
                   widertext = ", wider than 1600"
                ini1200 = "custom_aspect_ratio_1=%d:%d      ; %d:%d @ %.3f, %d:%d PAR (%d:%d%s)" % ( xres, yres, int(visible_pixels[1]),int(visible_lines[1]), float(pixel_clock[1]), (v_multi + nearest_h), v_multi, int(visible_pixels[1])*(v_multi + nearest_h), int(visible_lines[1])*v_multi,widertext)
              if res[i] == 1440:
                ar1440 = "Integer aspect ratio for %dp minimum required pixel clock: %f mhz" % (res[i], reqclock/1000000)
                if int(visible_pixels[1])*(v_multi + nearest_h) > 1920:
                   widertext = ", wider than 1920"
                ini1440 = "custom_aspect_ratio_1=%d:%d      ; %d:%d @ %.3f, %d:%d PAR (%d:%d%s)" % ( xres, yres, int(visible_pixels[1]),int(visible_lines[1]), float(pixel_clock[1]), (v_multi + nearest_h), v_multi, int(visible_pixels[1])*(v_multi + nearest_h), int(visible_lines[1])*v_multi,widertext)
              if res[i] == 1536:
                ar1536 = "Integer aspect ratio for %dp " % (res[i])
                if int(visible_pixels[1])*(v_multi + nearest_h) > 2048:
                  widertext = ", wider than 2048"
                ini1536 = "custom_aspect_ratio_1=%d:%d      ; %d:%d @ %.3f, %d:%d PAR (%d:%d%s)" % ( xres, yres, int(visible_pixels[1]),int(visible_lines[1]), float(pixel_clock[1]), (v_multi + nearest_h), v_multi, int(visible_pixels[1])*(v_multi + nearest_h), (int(visible_lines[1])*v_multi),widertext)
          return render_template('calcar.html', title='Mister Aspect Ratio Calculator', form=form,
                                                                                        clock=form.pixelclock.data,
                                                                                        pixels=form.pixels.data,
                                                                                        lines=form.lines.data,
                                                                                        video=form.videotype.data,
                                                                                        amiga=form.amiga.data,
                                                                                        amigares=form.amigares.data,
                                                                                        customres=form.customres.data,
                                                                                        customvertres=form.customvertres.data,
                                                                                        dotresult=dotresult,
                                                                                        squareresult=squareresult,
                                                                                        arresult=arresult,
                                                                                        ar480=ar480,
                                                                                        ar720=ar720,
                                                                                        ar1080=ar1080,
                                                                                        ar1200=ar1200,
                                                                                        ar1440=ar1440,
                                                                                        ar1440warning1=ar1440warning1,
                                                                                        ar1440warning2=ar1440warning2,
                                                                                        ar1440warning3=ar1440warning3,
                                                                                        ar1536=ar1536,
                                                                                        arcustom=arcustom,
                                                                                        customini=customini,
                                                                                        ini480=ini480,
                                                                                        ini720=ini720,
                                                                                        ini1080=ini1080,
                                                                                        ini1200=ini1200,
                                                                                        ini1440=ini1440,
                                                                                        ini1536=ini1536)
    return render_template('calcar.html', title='Mister Aspect Ratio Calculator', form=form)

bootstrap = Bootstrap(app)
