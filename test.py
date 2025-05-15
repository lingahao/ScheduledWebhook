import requests
import time
import os

url = os.environ['webhook_url']

data = {
    "events": [
        {
            "type": "message",
            "replyToken": "test123",
            "source": {
                "userId": "Uc4650f10bf0cb6121b34a9ce775f6b18",  # 改成你自己的 LINE userId
                "type": "user"
            },
            "timestamp": int(time.time() * 1000),
            "mode": "active",
            "message": {
                "type": "text",
                "id": "100001",
                "text": "讀取"
            }
        }
    ],
    "destination": "Uc4650f10bf0cb6121b34a9ce775f6b18"
}

response = requests.post(url, json=data)

print(f"Status: {response.status_code}")
print(response.text)
