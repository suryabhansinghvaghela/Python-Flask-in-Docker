from flask import Flask, redirect, url_for, request , render_template
app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')


@app.route('/dashboard/<name>')
def done(name):
   return render_template('user.html', user=name)
   
@app.route('/login',methods = ['POST'])
def login():
	user = request.form['n']
	return redirect(url_for('done',name = user))
   
if __name__ == '__main__':
   app.run(host='127.0.0.1',port=5000,debug = True)  
