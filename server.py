from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
	if 'num' not in session:
		session['num'] = random.randint(1, 100)
	print('this is: ', session)
	print('this is session num', session['num'])
	return render_template('index.html', num = session['num'])

@app.route('/guess', methods=['POST'])
def guess():
	print("Got Post Info")
	# Here we add two properties to session to store the name and email
	session['guess'] = request.form['guess']
	if int(session['guess']) == session['num']:
		session['response'] = 'Correct!' 
	elif int(session['guess']) > session['num']:
		session['response'] = 'Too high'
	else:
		session['response'] = 'Too low' 
	return redirect('/')

@app.route('/clear')
def clear():
	session.clear()
	print(session)
	return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
	app.run(debug=True)    # Run the app in debug mode.