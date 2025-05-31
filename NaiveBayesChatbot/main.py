from data.training_data import training_data
from nlp.intent_classifier_naive import NaiveBayesClassifier
from responses.response_generator import generate_response

def main():
    print("Chatbot: Xin chào! Tôi có thể giúp gì cho bạn hôm nay?")
    
    nb = NaiveBayesClassifier()
    nb.train(training_data)

    while True:
        user_input = input("Bạn: ").strip()
        
        intent = nb.predict(user_input)
        response = generate_response(intent)

        print(f"Chatbot: {response}")

        if(intent == "tạm biệt"):
            break

if __name__ == "__main__":
    main()