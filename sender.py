import requests
import json

api_url = "https://lynkss.shop/api.php"
bot_token = "6020873764:AAHoiAVgYFpIDu7LtLOOzv987LU2MtbGRVY"  # replace with your bot token
telegram_api = f"https://api.telegram.org/bot{bot_token}/sendMessage"

users = requests.get(api_url)
response = users.json()

results = {
    "sent": [],
    "failed": [],
    "counts": {"sent": 0, "failed": 0}
}

if response.get("status") == "success":
    chat_ids = response.get("chat_ids", [])
    print(f"Total chat IDs: {len(chat_ids)}")

    for i, chat_id in enumerate(chat_ids, start=1):
        payload = {
            "chat_id": chat_id,
            "text": '''
<b>🚀COMEBACK SALE🚀

👉FLKART , JI0 ,  AMZON  , MEESHO ,  SCRATCH WEB

⚡️CHECK HOW MANY USERS REDIRECTED TO PAYMENT APP

#CASHFREE ADDED IF WANT

✅WEB STATS IN PANEL
✅ADVANCED PROTECTION
✅NO SUSPEND OR DEAD
✅UPI PANEL
✅PRODUCT PANEL
✅SMOOTH UI
✅DIRECT PAYMENT 



📝ADDITIONAL CODE PROTECTION IN SCRIPT SO NO CHANCES OF RED OR SUSPENSION ISSUE

⚡️PRICES :
💸1 MONTH - 1500 800 ONLY

💸15 DAYS - 999 600ONLY

💸7DAYS - 800 300 ONLY

✅LITTLE NEGO

💌DM - @G4xWizarD_official

📝PRICES WILL INCREASE IN SOMETIME DON’T MISS THE CHANCE</b>''',
            'parse_mode' : 'HTML'
        }
        sent = requests.get(telegram_api, params=payload)

        if sent.status_code == 200 and sent.json().get("ok"):
            print(f"[{i}] ✅ Sent to {chat_id}")
            results["sent"].append(chat_id)
            results["counts"]["sent"] += 1
        else:
            print(sent.text)
            print(f"[{i}] ❌ Failed to {chat_id}")
            results["failed"].append(chat_id)
            results["counts"]["failed"] += 1

else:
    print("no users found")

# Save results to JSON file
with open("send_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("\nSummary saved to send_results.json")