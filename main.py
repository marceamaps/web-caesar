from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True  

form = """
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
        <form action="/web-caesar" method="post">
            <label for="rotate-by">
            <input type="text" name="rot"/>
                <option value="0"> 0 </option>

            <input type="textarea" name="text"/>

            </label>

        <input type="submit" value="Submit Query/> 

        </form>
        </body>
    </html>
    """

@app.route("/", methods="POST")
def encrypt():
    
    rot = request.form['rot']

    text_area = request.form['text']








app.run()