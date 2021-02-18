print("Convert video_mode to modeline script")
print("Expected format: HRES, HFPORCH, HSYNC, HBPORCH, VRES, VFPORCH, VSYNC, VBPORCH, PIXEL_CLOCK")
try:
  hres, hfporch, hsync, hbporch, vres, vfporch, vsync, vbporch, pixel_clock = map(float,input("Please enter video_mode values: ").split(","))
  pixel_clock=float(pixel_clock)
  hres = int(hres)
  hfporch = int(hfporch)
  hsync = int(hsync)
  hbporch= int(hbporch)
  vres = int(vres)
  vfporch = int(vfporch)
  vsync = int(vsync)
  vbporch = int(vbporch)
  ml_pixelclock = pixel_clock/1000
  ml_hdisp=hres
  ml_hsyncstart=hres+hfporch
  ml_hsyncend=ml_hsyncstart+hsync
  ml_htotal=hres+hfporch+hsync+hbporch
  ml_vdisp=vres
  ml_vsyncstart=vres+vfporch
  ml_vsyncend=ml_vsyncstart+vsync
  ml_vtotal=vres+vfporch+vsync+vbporch
  modelinetext = ("ModeLine \"%ix%i\" %g %i %i %i %i %i %i %i %i" % (ml_hdisp, ml_vdisp, ml_pixelclock, ml_hdisp, ml_hsyncstart, ml_hsyncend, ml_htotal, ml_vdisp, ml_vsyncstart, ml_vsyncend, ml_vtotal))
  print(modelinetext)
except:
  print("Invalid input check expected format.")
