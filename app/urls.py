from views import app, home

app.add_url_rule('/', view_func=home)
