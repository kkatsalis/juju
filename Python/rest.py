from eve import Eve

app = Eve()


@app.route('/hello')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run(port=8967)
