import pandas as pd
from collections import defaultdict
import json

def load_raw_excel(filepath):
    df = pd.read_excel(filepath)
    return df

def process_data_from_df(df):
    processed_texts = []
    intent_responses = defaultdict(list)

    for _, row in df.iterrows():
        # Bỏ 2 cột flags và category, chỉ lấy instruction, intent, response
        text = str(row.get('instruction', '')).strip()
        intent = str(row.get('intent', '')).strip()
        response = str(row.get('response', '')).strip()

        if text and intent:
            processed_texts.append({'text': text, 'intent': intent})

            if response and response not in intent_responses[intent]:
                intent_responses[intent].append(response)

    return processed_texts, dict(intent_responses)

def save_processed_data(texts, intent_responses, texts_filepath, responses_filepath):
    with open(texts_filepath, 'w', encoding='utf-8') as f:
        json.dump(texts, f, ensure_ascii=False, indent=2)
    with open(responses_filepath, 'w', encoding='utf-8') as f:
        json.dump(intent_responses, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    raw_path = r'D:\Python\ChatBotAI\mid_range_chatbot\NaiveBayesChatbot_Dataset\data\raw\train.xlsx'
    processed_texts_path = r'D:\Python\ChatBotAI\mid_range_chatbot\NaiveBayesChatbot_Dataset\data\processed\texts.json'
    processed_responses_path = r'D:\Python\ChatBotAI\mid_range_chatbot\NaiveBayesChatbot_Dataset\data\processed\intent_responses.json'


    df = load_raw_excel(raw_path)
    texts, intent_responses = process_data_from_df(df)
    save_processed_data(texts, intent_responses, processed_texts_path, processed_responses_path)

    print(f"Đã xử lý xong {len(texts)} câu hỏi với {len(intent_responses)} intent.")
