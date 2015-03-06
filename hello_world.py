from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello/<name>')
def hello_person(name):
    html = '''
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of kitten. Enjoy...
        </p>
        <img src='http://placekitten.com/g/200/300'>
    '''
    return html.format(name.title())

@app.route('/jedi/<fname>/<lname>')
def jedi_name(fname, lname):
    lname_3 = lname[0:3]
    fname_2 = fname[0:2]
    jedi = lname_3 + fname_2
    
    html = '''
        <h1>
             Hello {} {}!
        </h1>
        <p>
            Your Jedi name is {}!
        </p>
    '''
    return html.format(fname.title(), lname.title(), jedi.title())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)