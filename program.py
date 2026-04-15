
from dotenv import load_dotenv
import os
import json
import google.generativeai as genai

# حمّل المفتاح
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyBDj-uu11nKAsoBdTIfHIezuCFCocyd4mY"))

# أنشئ النموذج
model = genai.GenerativeModel("gemini-1.5-flash")

# أرسل سؤال
response = model.generate_content("ما هي عاصمة الجزائر؟")

# اطبع الرد
print(response.text)

# احفظ في JSON
result = {"question": "ما هي عاصمة الجزائر؟", "answer": response.text}
with open("history.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print("تم الحفظ في history.json")