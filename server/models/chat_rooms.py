from server.firestoreWrapper import FirestoreCollections
from flask import Blueprint
from login_required import login_required

chat_room_page = Blueprint('chat_room_page', __name__)


@login_required
@chat_room_page.route("/api/chat_rooms")
def get_all_chat_rooms():
    docs = FirestoreCollections.chat_rooms_ref().stream()
    return {'chat_rooms': [doc.to_dict() for doc in docs]}

@login_required
@chat_room_page.route("/api/chat_rooms/<chat_room_id>", methods=['POST'])
def receive_message(chat_room_id):
    pass