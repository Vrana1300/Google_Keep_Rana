from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Notes Model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID
    title = db.Column(db.String(100), nullable=False)  # Note Title
    content = db.Column(db.Text, nullable=False)  # Note Content
    color = db.Column(db.String(10), nullable=False, default="#FFFFFF")  # Note Color

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "color": self.color
        }
