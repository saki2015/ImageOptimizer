from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_pyfile('../config.py')
    
    # Initialize extensions here
    
    # Register blueprints
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
