from server.firestoreWrapper import FirestoreCollections
from flask import Blueprint


chat_room_page = Blueprint('chat_room_page', __name__)


@chat_room_page.route("/chat_rooms")
def get_chat_rooms():
    docs = FirestoreCollections.chat_rooms_ref().stream()
    return {'chat_rooms': [doc.to_dict() for doc in docs]}