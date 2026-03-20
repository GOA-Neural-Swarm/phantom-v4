import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load secrets
load_dotenv()

# 2. Extract Key
api_key = os.getenv("GROQ_API_KEY")

# 3. Execution Logic
if not api_key:
    print("❌ API Key missing in .env!")
    else:
        client = Groq(api_key=api_key)
            print("🔱 PHANTOM V4: SYNCING...")
                
                    try:
                            # ဒီစာကြောင်းတွေရဲ့ အရှေ့မှာ space (၄) ခုစီပဲ ရှိရမယ်
                                    chat = client.chat.completions.create(
                                                messages=[{"role": "user", "content": "System check. Status?"}],
                                                            model="llama-3.3-70b-versatile"
                                                                    )
                                                                            print("-" * 20)
                                                                                    print(f"🔥 RESPONSE: {chat.choices[0].message.content}")
                                                                                            print("-" * 20)
                                                                                                except Exception as e:
                                                                                                        print(f"❌ Error: {e}")