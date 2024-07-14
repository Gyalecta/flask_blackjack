import logging
from flask import Flask, render_template
from routes import create_app

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)