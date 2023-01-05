from flask import Flask

app = Flask(__name__)

@app.route('/')
def head1 ():
    return 'hello world rhm'

@app.route('/second')
def head2 ():
    return 'this is second page' 

@app.route('/third')
def head3 ():
    return 'this is third page'


@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'

if __name__ == '__main__':

    app.run(debug=True)