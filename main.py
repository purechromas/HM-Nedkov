from flask import Flask
import utils

# Making a new app.
app = Flask(__name__)


# Starting with home page.
@app.route('/')
def home_page():
    text = ""
    data = utils.load_candidates()
    for candidates in data:
        text += "Имя кандидата - " + candidates['name'] + "\n"
        text += "Позиция кандидата - " + candidates['position'] + "\n"
        text += "Навыки - " + candidates['skills'] + "\n"
        text += "\n"
    return "<pre>" + text + "</pre>"


# Second page - candidate page(important that we take int from the url).
@app.route('/candidates/<int:x>')
def candidates_page(x):
    data = utils.load_candidates()
    link = data[x]['picture']
    return f"""<img src={link}>
    <pre>Имя кандидата - {data[x]['name']}
Позиция кандидата - {data[x]['position']}
Навыки - {data[x]['skills']}</pre>"""


# Third page - skills page.
@app.route('/skills/<x>')
def skills_page(x):
    output = ""
    data = utils.get_by_skill(x)
    for people in data:
        if x in people['skills']:
            output += "Имя кандидата - " + (people['name']) + "\n"
            output += "Имя кандидата - " + (people['position']) + "\n"
            output += "Имя кандидата - " + (people['skills']) + "\n"
            output += "\n"
    return "<pre>" + output + "</pre>"


if __name__ == '__main__':
    app.debug = 1
    app.run(port=5003)
