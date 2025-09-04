from flask import Flask, render_template, request, jsonify
import ollama
import re

app = Flask(__name__)

def clean_deepseek_response(text):
    text = re.sub(r'<think>[\s\S]*?</think>', '', text)
    text = re.sub(r'<.*?>', '', text)
    return text.strip()

def get_response_from_ollama(user_input):
    try:
        response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": user_input}])
        if 'message' in response and 'content' in response['message']:
            raw_text = response['message']['content']
            clean_text = clean_deepseek_response(raw_text)
            return clean_text
        else:
            return "Sorry, could not generate a response."

    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_msg = request.form.get("msg", "").strip()
    if not user_msg:
        return jsonify({"response": "Please type something to chat."})

    bot_response = get_response_from_ollama(user_msg)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
