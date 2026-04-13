from flask import Flask, jsonify, request
import random

app = Flask(__name__)

quotes = [
    {"id": 1, "author": "Maya Angelou", "text": "You will face many defeats in life, but never let yourself be defeated."},
    {"id": 2, "author": "Nelson Mandela", "text": "It always seems impossible until it's done."},
    {"id": 3, "author": "Chimamanda Ngozi Adichie", "text": "The single story creates stereotypes, and the problem with stereotypes is not that they are untrue, but that they are incomplete."},
    {"id": 4, "author": "Wole Soyinka", "text": "A tiger does not proclaim its tigritude, it pounces."},
    {"id": 5, "author": "Chinua Achebe", "text": "Until the lions have their own historians, the history of the hunt will always glorify the hunter."},
]

next_id = 6

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/quote", methods=["GET"])
def get_random_quote():
    quote = random.choice(quotes)
    return jsonify(quote), 200

@app.route("/quotes", methods=["GET"])
def get_all_quotes():
    return jsonify({"total": len(quotes), "quotes": quotes}), 200

@app.route("/quote", methods=["POST"])
def add_quote():
    global next_id
    data = request.get_json()

    if not data or "text" not in data or "author" not in data:
        return jsonify({"error": "Request must include 'text' and 'author'"}), 400

    new_quote = {
        "id": next_id,
        "author": data["author"],
        "text": data["text"]
    }
    quotes.append(new_quote)
    next_id += 1

    return jsonify(new_quote), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)