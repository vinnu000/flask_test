from app.accounts import accounts_bp
# from app.accounts.views import home

def register_routes(api, app, root="api"):
    app.register_blueprint(accounts_bp)
