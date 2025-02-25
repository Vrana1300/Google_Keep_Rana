from flask import Blueprint, request, jsonify
from models import db, Note

routes = Blueprint('routes', __name__)  # Flask Blueprint for routes

# 📌 Get All Notes
@routes.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return jsonify([note.to_dict() for note in notes])

# 📌 Get Single Note by ID
@routes.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    note = Note.query.get(id)
    if note:
        return jsonify(note.to_dict())
    return jsonify({"error": "Note not found"}), 404

# 📌 Create a New Note
@routes.route('/notes', methods=['POST'])
def add_note():
    data = request.json
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    new_note = Note(title=data['title'], content=data['content'], color=data.get('color', '#FFFFFF'))
    db.session.add(new_note)
    db.session.commit()
    
    return jsonify({"message": "Note added successfully", "note": new_note.to_dict()}), 201

# 📌 Update an Existing Note
@routes.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    note = Note.query.get(id)
    if not note:
        return jsonify({"error": "Note not found"}), 404

    data = request.json
    note.title = data.get('title', note.title)
    note.content = data.get('content', note.content)
    note.color = data.get('color', note.color)
    
    db.session.commit()
    return jsonify({"message": "Note updated successfully", "note": note.to_dict()})

# 📌 Delete a Note
@routes.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get(id)
    if note:
        db.session.delete(note)
        db.session.commit()
        return jsonify({"message": "Note deleted successfully"})
    
    return jsonify({"error": "Note not found"}), 404
