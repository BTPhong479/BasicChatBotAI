from flask import Flask, request, jsonify
from data.training_data import training_data
from nlp.intent_classifier_naive import NaiveBayesClassifier
from responses.response_generator import generate_response

app = Flask(__name__)

# Khởi tạo và huấn luyện model ngay khi server start
nb = NaiveBayesClassifier()
nb.train(training_data)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("text", "").strip()

    if not user_input:
        return jsonify({"error": "No input text provided"}), 400

    intent = nb.predict(user_input)
    response = generate_response(intent)

    return jsonify({
        "intent": intent,
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)