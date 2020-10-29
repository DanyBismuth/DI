import flask

#Create a Controller
app = flask.Flask(__name__)
#__name__ is an authentic variable containing the name of the file

users = {
    "Alice": {"name": "Alice Cohen", "age": 45, "hobbies": ['Coding', 'Cooking', 'Scubadiving']},
    "Rick": {"name": "Rick Sanchez", "age": 59, "hobbies": ['Coding', 'Create things', 'Eating']},
}

# Create a view

# URL : facebook.com/profile/rick
# URI: /profile/rick

# URL : facebook.com
# URI: /

@app.route("/")
def index():
    return flask.render_template("index.html", my_title="My awesome app")

@app.route("/users-list")
def users_list():
    body = f"""
        <html>
            <header>
            </header>

            <body>
                <ul>
                    <li>{users['Alice']["name"]}</li>
                    <li>{users['Rick']["name"]}</li>
                </ul>
            </body>
        </html>
    """
    return body

@app.route("/profile/<name>")
def profile_page(name):
    name = name.title()
    user = users[name]


    body = f"""
               <html>
                   <header>
                   </header>
    
                   <body>
                       <h1>Page of {user["name"]}</h1>
                        <p> {user["name"]} is {user["age"]} Years old and likes {user["hobbies"][0]}</p>
               </html>
           """
    return body

# Run my server
app.run()
