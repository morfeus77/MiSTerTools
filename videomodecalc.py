print("Convert modeline to video_mode script")
print("Expected format: PIXEL_CLOCK HDISP HSYNCSTART HSYNCEND HTOTAL VDISP VSYNCSTART VSYNCEND VTOTAL")
try:
  pixel_clock, hdisp, hsyncstart, hsyncend, htotal, vdisp, vsyncstart, vsyncend, vtotal = map(float,input("Please enter modeline values: ").split())
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
  print("video_mode="+str(hdisp)+","+str(hsyncstart-hdisp)+","+str(hsyncend-hsyncstart)+","+str(htotal-hsyncend)+","+str(vdisp)+","+str(vsyncstart-vdisp)+","+str(vsyncend-vsyncstart)+","+str(vtotal-vsyncend)+","+str(int(clock)))
except:
  print("Invalid input check expected format.")
