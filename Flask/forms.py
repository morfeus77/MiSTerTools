from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, DecimalField, SelectField, RadioField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    modeline = StringField('Modeline values', validators=[DataRequired()])
    submit = SubmitField('Convert')

class ArForm(FlaskForm):
    submitar = SubmitField('Calculate')
    results = StringField('Calculation Results:')
    ar480 = StringField('480p')
    ar720 = StringField('720p')
    ar1080 = StringField('1080p')
    ar1200 = StringField('1200p')
    ar1440 = StringField('1440p')
    ini480 = StringField('480p')
    ini720 = StringField('720p')
    ini1080 = StringField('1080p')
    ini1200 = StringField('1200p')
    ini1440 = StringField('1440p')
    ini1536 = StringField('1536p')
    customini = StringField('Custom res')
    arcustom = StringField('Integer scale for custom vertical res')
    ar1440warning1 = StringField('Warning! Video_mode=12 pixel clock is insufficient for this aspect ratio')
    ar1440warning2 = StringField('Warning')
    ar1440warning3 = StringField('Warning')
    ar1536 = StringField('1536p')
    pixelclock = DecimalField('Pixel clock in mhz', validators=[DataRequired()])
    pixels = IntegerField('Visible pixels', validators=[DataRequired()])
    lines = IntegerField('Visible lines', validators=[DataRequired()])
    videotype = SelectField(u'Video type', choices=[('NTSC', 'NTSC'), ('PAL', 'PAL')])
    amigares = SelectField(u'Amiga Resolution', choices=[('AGA', 'SHRES ECS/AGA'), ('HIRES', 'HIRES')])
    amiga = BooleanField(u'Minimig/Amiga')
    customres = BooleanField(u'Use a custom resolution')
    customvertres = IntegerField('Custom vertical resolution', default=0)


class VmForm(FlaskForm):
    modeline = StringField('Modeline values', validators=[DataRequired()])
    submit = SubmitField('Convert')
    presets = BooleanField('Use preset modeline')
    displaytype = RadioField(u'Modeline Presets', '', choices=[('tvpal50', 'TV PAL/SECAM (50Hz)'),
                                                       ('tvntsc60', 'TV NTSC (60Hz)'),
                                                       ('tvstandard','Video Playback Standard PAL/NTSC'),
                                                       ('tv288','Low Definition - 288p or less (progressive)'),
                                                       ('tv480','High Definition 480p/576p'),
                                                       ('tv720','High Definition 720p/1080p'),
                                                       ('tv1080i','High Definition 1080i (half or less image size interlace scaling workaround)'),
                                                       ('arcade','Arcade Specific'),
                                                       ('retracefix','Arcade Specific - compressed lines or retrace lines fix'),
                                                       ('arcade25','Arcade Specific - 25kHz line frequency'),
                                                       ('nes','Nintendo (NES)'),
                                                       ('snes','Super Nintendo (SNES)'),
                                                       ('sms','Sega Master System / ColecoVision'),
                                                       ('smd','Sega Mega Drive (Genesis)'),
                                                       ('neogeo','Neo-Geo, CPS1 / CPS2'),
                                                       ('tgfx','TurboGrafx-16, PC-Engine')],default='tvpal50')
    tvpal50choices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','TV PAL/SECAM Resolutions - Interlaced'),
                                                          ('13.625 640 694 758 872 540 556 562 625','640x540      (50Hz)'),
                                                          ('14.375 675 732 800 920 540 556 562 625','675x540 5:4  (50Hz)'),
                                                          ('15.375 720 781 854 984 540 556 562 625','720x540 4:3  (50Hz)'),
                                                          ('16.375 768 833 910 1048 540 556 562 625','768x540      (50Hz)'),
                                                          ('17.000 800 868 948 1088 540 556 562 625','800x540      (50Hz)'),
                                                          ('20.375 960 1041 1137 1304 540 556 562 625','960x540 16:9 (50Hz)'),
                                                          ('21.750 1024 1111 1213 1392 540 556 562 625','1024x540     (50Hz)'),
                                                          ('22.750 1072 1163 1270 1456 540 556 562 625','1072x540     (50Hz)')])

    tvntsc60choices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','TV NTSC Resolutions - Interlaced'),
                                                          ('12.084 570 621 678 768 456 472 478 525','570x456 5:4  (60Hz)'),
                                                          ('12.965 608 663 724 824 456 472 478 525','608x456 4:3  (60Hz)'),
                                                          ('13.594 640 698 762 864 456 472 478 525','640x456      (60Hz)'),
                                                          ('15.357 720 785 857 976 456 472 478 525','720x456      (60Hz)'),
                                                          ('17.245 812 885 966 1096 456 472 478 525','812x456 16:9 (60Hz)'),
                                                          ('21.776 1024 1117 1219 1384 456 472 478 525','1024x456     (60Hz)')])

    tvstandardchoices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','Standard PAL/NTSC video playback Resolutions - Interlaced'),
                                                          ('14.750 768 790 859 944 576 581 586 625','PAL  768x576 (50Hz)'),
                                                          ('12.336 640 662 720 784 480 488 494 525','NTSC 640x480 (60Hz)'),
                                                          ('13.875 720 741 806 888 576 581 586 625','PAL  720x576 (50Hz) - CCIR-601 spec'),
                                                          ('13.846 720 744 809 880 480 488 494 525','NTSC 720x480 (60Hz) - CCIR-601 spec'),
                                                          ('14.727 768 794 863 936 480 488 494 525','PAL-M 768x480 (60Hz) - PAL running at NTSC refresh rates')])
    tv1080ichoices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','1080i Resolutions'),
                                                           ('36.881 1920 1985 2158 2344 480 488 494 525','1080i 1920x480 60 (60Hz)'),
                                                           ('36.875 1920 1975 2149 2360 540 563 568 625','1080i 1920x540 50 (50Hz)'),
                                                           ('36.875 1920 1975 2149 2360 540 572 578 651','1080i 1920x540 48 (48Hz)')])
    tv288choices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','Low Definition Resolutions (progressive)'),
                                                          ('14.726 768 790 859 944 288 290 293 312','PAL  768x288 (50Hz)'),
                                                          ('13.853 720 741 806 888 288 290 293 312','PAL  720x288 (50Hz)'),
                                                          ('12.312 640 662 719 784 240 244 247 262','NTSC 640x240 (60Hz)'),
                                                          ('13.820 720 744 809 880 240 244 247 262','NTSC 720x240 (60Hz)')])
    tv480choices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','HD 480p/576p Resolutions'),
                                                          ('13.875 720 741 806 888 576 581 586 625','PAL  720x576 (50Hz) - Interlaced'),
                                                          ('13.846 720 744 809 880 480 488 494 525','NTSC 720x480 (60Hz) - Interlaced'),
                                                          ('16.253 852 873 948 1033 480 486 492 525','EDTV 852x480 (60Hz) - Interlaced'),
                                                          ('36.058 720 774 944 1152 576 581 586 626','720x576 (50Hz) - Progressive'),
                                                          ('35.496 720 782 949 1128 480 488 494 525','720x480 (60Hz) - Progressive'),
                                                          ('42.042 852 926 1123 1336 480 488 494 525','852x480 (60Hz) - Progressive')])
    tv720choices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','HD 720p/1080p Resolutions'),
                                                          ('24.545 1280 1323 1438 1560 480 488 494 525','720p 1280x480 30,60 (60Hz) - Interlaced'),
                                                          ('24.625 1280 1317 1433 1576 576 581 586 625','720p 1280x576 25,50 (50Hz) - Interlaced'),
                                                          ('24.625 1280 1317 1433 1576 600 605 611 651','720p 1280x600 24    (48Hz) - Interlaced'),
                                                          ('36.881 1920 1985 2158 2344 480 488 494 525','1080p 1920x480 30,60 (60Hz) - Interlaced'),
                                                          ('36.875 1920 1975 2149 2360 576 581 586 625','1080p 1920x576 25    (50Hz) - Interlaced'),
                                                          ('36.875 1920 1975 2149 2360 600 605 611 651','1080p 1920x600 24    (48Hz) - Interlaced')])
    arcadechoices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','Arcade specific resolutions'),
                                                          ('4.653 240 248 270 296 240 241 244 262','240x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('4.905 256 264 287 312 240 241 244 262','256x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('5.200 256 264 288 320 256 257 260 275','256x256_59,1Hz 16,2KHz (60Hz)'),
                                                          ('5.197 256 264 288 320 264 265 268 280','256x264_58,0Hz 16,2KHz (60Hz)'),
                                                          ('5.533 288 296 322 352 240 241 244 262','288x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('5.785 296 304 331 368 240 241 244 262','296x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('5.911 304 312 340 376 240 241 244 262','304x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('6.162 320 328 357 392 200 221 224 262','320x200_60,0Hz 15,7KHz (60Hz)'),
                                                          ('6.162 321 329 358 392 240 241 244 262','321x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('6.501 320 328 359 400 256 257 260 275','320x256_59,1Hz 16,2KHz (60Hz)'),
                                                          ('6.540 336 344 375 416 240 241 244 262','336x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('7.151 352 360 394 440 256 257 260 275','352x256_59,1Hz 16,2KHz (60Hz)'),
                                                          ('7.146 352 360 394 440 264 265 268 280','352x264_58,0Hz 16,2KHz (60Hz)'),
                                                          ('6.782 352 360 392 432 288 291 294 314','352x288_50,0Hz 15,7KHz (60Hz)'),
                                                          ('7.168 368 376 410 456 240 241 244 262','368x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('7.410 384 392 427 472 288 291 294 314','384x288_50,0Hz 15,7KHz (60Hz)'),
                                                          ('7.546 392 400 435 480 240 241 244 262','392x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('7.808 400 408 445 496 256 267 270 297','400x256_53,0Hz 15,7KHz (60Hz)'),
                                                          ('8.677 448 456 497 552 240 241 244 262','448x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('9.935 512 520 567 632 240 241 244 262','512x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('9.922 512 520 567 632 288 291 294 314','512x288_50,0Hz 15,7KHz (60Hz)'),
                                                          ('9.935 512 520 567 632 448 467 473 524','512x448_60,0Hz 15,7KHz (60Hz) - Interlaced'),
                                                          ('10.272 512 520 568 632 512 513 519 550','512x512_59,1Hz 16,3KHz (60Hz) - Interlaced'),
                                                          ('12.647 632 640 699 784 264 265 268 283','632x264_57,0Hz 16,1KHz (60Hz)'),
                                                          ('12.324 640 648 706 784 240 241 244 262','640x240_60,0Hz 15,7KHz (60Hz)'),
                                                          ('12.309 640 648 706 784 288 291 294 314','640x288_50,0Hz 15,7KHz (60Hz)'),
                                                          ('12.324 640 648 706 784 480 483 489 524','640x480_60,0Hz 15,7KHz (60Hz) - Interlaced'),
                                                          ('12.560 648 656 715 800 288 291 294 314','648x288_50,0Hz 15,7KHz (60Hz)'),
                                                          ('13.959 720 728 794 888 480 483 489 524','720x480_60,0Hz 15,7KHz (60Hz) - Interlaced'),
                                                          ('15.823 800 808 883 992 600 601 607 638','800x600_50,0Hz 16,0KHz (60Hz) - Interlaced'),
                                                          ('20.161 1024 1032 1127 1264 600 601 607 638','1024x600_50,0Hz 16,0KHz (60Hz) - Interlaced')])
    retracefixchoices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','Arcade specific resolutions - retracing/compression fix'),
                                                          ('5.504 256 268 292 330 256 257 260 278','256x256@60,0Hz 16,7KHz (60Hz)'),
                                                          ('5.529 256 268 292 330 264 265 268 284','256x264@59,0Hz 16,7KHz (60Hz)'),
                                                          ('6.938 321 340 372 416 256 257 260 278','321x256@60,0Hz 16,7KHz (60Hz)'),
                                                          ('7.506 352 368 400 450 256 257 260 278','352x256@60,0Hz 16,7KHz (60Hz)'),
                                                          ('7.574 352 365 405 452 264 265 268 284','352x264@59,0Hz 16,7KHz (60Hz)'),
                                                          ('11.062 512 538 594 668 512 513 516 552','512x512@30,0Hz 16,6KHz (60Hz) - Interlaced'),
                                                          ('13.807 632 664 728 824 264 265 268 284','632x264@59,0Hz 16,7KHz (60Hz)')])
    arcade25choices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','Arcade specific resolutions - 25kHz line frequency'),
                                                          ('15.575 512 520 582 624 384 385 390 416','512x384_60,0Hz 25,0KHz'),
                                                          ('15.575 512 520 582 624 768 769 779 832','512x768_60,0Hz 25,0KHz - Interlaced'),
                                                          ('31.150 1024 1032 1157 1248 768 769 779 832','1024x768_60,0Hz 25,0KHz')])
    neschoices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','NES specific resolutions'),
                                                          ('5.320 256 269 294 341 240 270 273 312','256x240 PAL  (50Hz)'),
                                                          ('5.370 256 269 294 341 240 244 247 262','256x240 NTSC (60Hz)'),
                                                          ('5.320 256 269 294 341 224 260 263 312','256x224 PAL  (50Hz)'),
                                                          ('5.370 256 269 294 341 224 236 239 262','256x224 NTSC (60Hz)')])
    sneschoices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','Super Nintendo (SNES) specific resolutions'),
                                                          ('5.320 256 274 299 341 224 260 263 312','256x224 PAL  (50Hz)'),
                                                          ('5.370 256 274 299 341 224 236 239 262','256x224 NTSC (60Hz)'),
                                                          ('5.320 256 274 299 341 239 268 271 312','256x239 PAL  (50Hz)'),
                                                          ('5.370 256 274 299 341 239 244 247 262','256x239 NTSC (60Hz)'),
                                                          ('10.640 512 548 598 681 448 520 526 625','512x448 PAL  (50Hz) - Interlaced'),
                                                          ('10.740 512 548 599 683 448 472 478 525','512x448 NTSC (60Hz) - Interlaced'),
                                                          ('10.640 512 548 598 681 478 536 542 625','512x478 PAL  (50Hz) - Interlaced'),
                                                          ('10.740 512 548 599 683 478 488 494 525','512x478 NTSC (60Hz) - Interlaced')])
    smschoices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','Sega Master System/ColecoVision specific resolutions'),
                                                          ('5.320 256 274 299 341 192 242 245 312','256x192 PAL  (50Hz)'),
                                                          ('5.370 256 274 299 342 192 221 224 262','256x192 NTSC (60Hz)'),
                                                          ('5.320 248 270 295 341 192 242 245 312','248x192 PAL  (50Hz)'),
                                                          ('5.370 248 270 295 342 192 221 224 262','248x192 NTSC (60Hz)'),
                                                          ('5.320 256 274 299 341 224 260 263 312','256x224 PAL  (50Hz)'),
                                                          ('5.370 256 274 299 341 224 236 239 262','256x224 NTSC (60Hz)')])
    smdchoices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','Sega Mega Drive (Genesis) specific resolutions'),
                                                          ('5.370 256 274 299 341 224 236 239 262','256x224 NTSC (60Hz)'),
                                                          ('6.700 320 336 367 426 224 236 239 262','320x224 NTSC (60Hz)'),
                                                          ('5.370 256 274 299 341 448 472 477 525','256x448 NTSC (60Hz) - Interlaced'),
                                                          ('6.700 320 336 367 426 448 472 477 525','320x448 NTSC (60Hz) - Interlaced'),
                                                          ('5.320 256 269 294 341 240 270 273 312','256x240 PAL  (50Hz)'),
                                                          ('5.370 256 274 299 341 240 244 247 262','256x240 NTSC (60Hz)'),
                                                          ('6.660 320 336 367 426 240 270 273 312','320x240 PAL  (50Hz)'),
                                                          ('6.700 320 336 367 426 240 244 247 262','320x240 NTSC (60Hz)'),
                                                          ('5.330 256 269 294 341 480 540 545 625','256x480 PAL  (50Hz) - Interlaced'),
                                                          ('5.370 256 274 299 341 480 488 493 525','256x480 NTSC (60Hz) - Interlaced'),
                                                          ('6.660 320 336 367 426 480 540 545 625','320x480 PAL  (50Hz) - Interlaced'),
                                                          ('6.700 320 336 367 426 480 488 493 525','320x480 NTSC (60Hz) - Interlaced')])
    neogeochoices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','Neo-Geo, CPS1 / CPS2 specific resolutions'),
                                                          ('6.327 304 319 349 405 224 262 265 312','304x224 PAL  (50Hz)'),
                                                          ('6.365 304 319 349 405 224 236 239 262','304x224 NTSC (60Hz)'),
                                                          ('6.660 320 336 367 426 224 262 265 312','320x224 PAL  (50Hz)'),
                                                          ('6.700 320 336 367 426 224 236 239 262','320x224 NTSC (60Hz)'),
                                                          ('6.660 320 336 367 426 240 270 273 312','320x240 PAL  (50Hz)'),
                                                          ('6.700 320 336 367 426 240 244 247 262','320x240 NTSC (60Hz)'),
                                                          ('8.000 384 404 441 512 224 262 265 312','384x224 PAL  (50Hz)'),
                                                          ('8.040 384 403 440 511 224 236 239 262','384x224 NTSC (60Hz)'),
                                                          ('8.000 384 404 441 512 240 270 273 312','384x240 PAL  (50Hz)'),
                                                          ('8.040 384 403 440 511 240 244 247 262','384x240 NTSC (60Hz)')])
    tgfxchoices = SelectField(u'Available Resolutions', choices=[('Choose or enter a modeline...','TurboGrafx-16, PC-Engine specific resolutions'),
                                                          ('5.370 256 269 294 341 240 244 247 262','256x240 NTSC (60Hz)'),
                                                          ('7.383 352 370 404 469 240 244 247 262','352x240 NTSC (60Hz)'),
                                                          ('10.740 512 538 588 683 240 244 247 262','512x240 NTSC (60Hz)')])


