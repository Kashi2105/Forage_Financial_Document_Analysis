from flask import Flask, render_template, request
from chatbot import response
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def answer():
    if request.method == 'POST':
        query= request.form.get("query")
        response_text= response(query)
        print("something is happening  here")
        print(response_text)
        return render_template('index.html', response_text=response_text)
    print("You are in normal position")
    return render_template('index.html',response_text=None)

if __name__=='main':
    app.run(debug=True)