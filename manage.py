import os
# from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app, db


env = os.getenv("FLASK_ENV") or "test"
print(f"Active environment: * {env} *")
app = create_app(env)


# migrate = Migrate(app, db)
manager = Manager(app)
app.app_context().push()

# manager.add_command('db', MigrateCommand)
# manager.add_command('runserver', Server(host="127.0.0.1", port=8000))


@manager.command
def run():
    app.run()


@manager.command
def init_db():
    print("Creating all resources.")
    db.create_all()


@manager.command
def drop_all():
    if input("Are you sure you want to drop all tables? (y/N)\n").lower() == "y":
        print("Dropping tables...")
        db.drop_all()


if __name__ == "__main__":
    manager.run()
