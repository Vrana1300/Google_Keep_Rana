from flask import Flask, request, jsonify
from flask_cors import CORS  # 🔹 Import CORS

app = Flask(__name__)
CORS(app) 

notes = [
    {"id": 1, "title": "Sample Note", "content": "This is a sample note", "color": "#FFEB3B"}
]

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.json
    new_note = {
        "id": len(notes) + 1,
        "title": data['title'],
        "content": data['content'],
        "color": data.get('color', "#FFFFFF")
    }
    notes.append(new_note)
    return jsonify(new_note), 201

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    notes = [note for note in notes if note["id"] != note_id]
    return jsonify({"message": "Note deleted"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
