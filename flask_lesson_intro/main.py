from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/author')
def get_author_page():
    return render_template("author.html")


@app.route('/<device>')
def get_device_page(device):
    list_of_device_dict = []
    for i in get_data():
        if device == i['title'].replace(' ', '_'):
            list_of_device_dict.append(i)
    image = device
    return render_template('device.html',
                           list_of_device_dict=list_of_device_dict,
                           image=image)


if __name__ == "__main__":
    app.run(debug=True)
