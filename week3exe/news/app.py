from flask import Flask

@app.route('/')
def index():


@app.route('/files/<filename>')
def file(filename):


if __name__ == '__main__':
    app.run(
        port = 3000
        )
