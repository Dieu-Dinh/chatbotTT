from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from langdetect import detect

API_KEY = "AIzaSyBWRSbJWIerS727egGbSbSGOhgzsdQKLSc"    # API Key Gemini
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")   # Model Gemini

history = []    # Lưu lịch sử

app = Flask(__name__)

def chat_with_gemini(user_input):
    try:
        # Nhận diện ngôn ngữ
        lang = detect(user_input)
        if lang == "vi":
            instruction = "Hãy trả lời bằng tiếng Việt."
        else:
            instruction = "Please answer in English."

        # Gửi vào lịch sử hội thoại
        history.append({"role": "user", "parts": [user_input]})
        history.append({"role": "user", "parts": [instruction]})  

        response = model.generate_content(history)
        reply = response.text.strip()

        history.append({"role": "model", "parts": [reply]})
        return reply
    except Exception as e:
        return f"❌ Error: {e}"

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    reply = chat_with_gemini(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
