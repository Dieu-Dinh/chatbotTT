import google.generativeai as genai

genai.configure(api_key="AIzaSyBWRSbJWIerS727egGbSbSGOhgzsdQKLSc")

try:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Say hello!")
    print("✅ Gemini trả lời:", response.text)
except Exception as e:
    print("❌ Error:", e)
