from flask import Flask, redirect, url_for, session
from flask_login import current_user  # type: ignore[import-not-found]

from config import Config
from extensions import db, login_manager
from models import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from routes.auth import auth_bp
    from routes.rider import rider_bp
    from routes.admin import admin_bp 

    app.register_blueprint(auth_bp)
    app.register_blueprint(rider_bp)
    app.register_blueprint(admin_bp)

    @app.route("/")
    def index():
       session.clear()
       return redirect(url_for("auth.login"))

    with app.app_context():
        db.create_all()
        _ensure_default_admin()

    return app


def _ensure_default_admin():
    """Create one default admin account on first run if none exists yet."""
    admin_exists = User.query.filter_by(role="admin").first()
    if not admin_exists:
        admin = User(
            name="System Admin",
            phone="0700000000",
            email="admin@bodaboda.local",
            role="admin",
        )
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()
        print("Default admin created -> phone: 0700000000  password: admin123")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
