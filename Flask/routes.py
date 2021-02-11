from flask import render_template
from app import app
from app.forms import LoginForm, ArForm, VmForm

# ...

@app.route('/calc')
def login():
    form = LoginForm()
    return render_template('calcvm.html', title='convert modeline to video_mode', form=form)

@app.route('/calcar')
def loginar():
    form = ArForm()
    return render_template('calcar.html', title='aspect ratio calculator', form=form)

@app.route('/calcvm')
def loginvm():
    form = VmForm()
    return render_template('calcvm.html', title='convert modeline to video_mode', form=form)
