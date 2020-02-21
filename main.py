from config import ConfigApp
from app.routes import app
from app.models import db

app.config.from_object(ConfigApp)
db.init_app(app)
db.create_all(app=app)
app.run(host='localhost', port=5000)