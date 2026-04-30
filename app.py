from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def index(): 
    name = ''
    email = ''
    message = ''
    submitted = False

    if request.method == 'POST':
        print("Form Submitted")
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        submitted = True

        # You can add logic here to handle the submitted data

    return render_template('contact.html', 
                           name=name,
                           email=email,
                           message=message,
                           submitted=submitted)

if __name__ == '__main__':
    app.run(debug=True)
