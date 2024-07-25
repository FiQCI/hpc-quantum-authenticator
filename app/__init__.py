from flask import Flask
from flask_apscheduler import APScheduler
from app.routes import routes
from app.config import Config
from app.job import prune_expired_tokens

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(routes)
    scheduler = APScheduler()

    scheduler.add_job(func=prune_expired_tokens, trigger="interval", seconds=1 * 60, id="expiredjobs")

    scheduler.start()

    return app
