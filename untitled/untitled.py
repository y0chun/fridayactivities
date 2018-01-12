from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    print('signup submitted')
    if request.form['Signup'] == 'Signup':
        print('Signup If selection entered')
        fullName = request.form['fullName']
        subject = request.form['subject']
        noName = "There was no name entered"
        noSubject = "There was no subject entered"

        if fullName == "" and subject == "":
            print("Name field was blank")
            return render_template('index.html', noName=noName, noSubject=noSubject)
        elif fullName == "":
            print("Subject field was blank")
            return render_template('index.html', noName=noName)
        elif subject == "":
            return render_template('index.html', noSubject=noSubject)
        else:
            print("The name is '" + fullName + "' and the subject was '" + subject)
            return render_template('success.html')
    elif request.form['Signup'] == 'Reset':
        print("reset called")
        return redirect('/')
    else:
        print("else")

if __name__ == '__main__':
    app.run()

#For Python: @app.route is a decorater. request.form is going to the html file. elif is else if. return render_template renders the html file.
#For HTML: form action signup and post link to the python code.
