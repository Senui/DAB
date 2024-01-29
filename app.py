from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_doi', methods=['POST'])
def process_doi():
    doilist = request.form.get('doilist')
    # Call your API with the list of DOIs here
    # Substitute this with your actual API call
    # result = call_api(doilist)
    result = "This is a placeholder result."
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

