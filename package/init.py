from package import app, db  # on importe app et db du fichier principal
from package.model import user,lesson
with app.app_context():
    db.create_all()
    
