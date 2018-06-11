from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True  

form = """
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
                .button {{
                    margin: 10px 0;
                    color: purple;
                }}
            </style>
        </head>
        <body>
        <form method="post">
            <label for="rot" name="rot" value="rot"> Rotate By

            <input type="text" name="rot"/ value="0" id="rot">

            <textarea name="textarea"> {0} </textarea>

            </label>

        <input type="submit" value="Submit Query" class="button" /> 

        </form>
        </body>
    </html>
    """

@app.route("/")
def index():

    return form.format(' ')


@app.route("/", methods=['POST'])
def encrypt():

    rot = request.form['rot']
    rot_num = int(rot)

    text_area = request.form['textarea']
    text_string = str(text_area)

    encrpytion = rotate_string(text_string, rot_num)

    content = "<h1>" + form.format(encrpytion) + "</h1>"

    return content


app.run()