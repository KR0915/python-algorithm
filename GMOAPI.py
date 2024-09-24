import requests

# APIエンドポイントとflavor IDを設定
base_url = "https://api.example.com/v2.1/flavors/"
flavor_id = "your_flavor_id_here"  # 取得したいflavorのIDを指定
url = f"{base_url}{flavor_id}"

# ヘッダーに認証情報を含める（必要に応じて）
headers = {
    "Authorization": "Bearer your_access_token_here",  # 必要に応じてアクセストークンを設定
    "Content-Type": "application/json"
}

# GETリクエストを送信
response = requests.get(url, headers=headers)

# レスポンスのステータスコードを確認
if response.status_code == 200:
    # レスポンスのJSONデータを取得
    flavor_details = response.json()
    print(flavor_details)
else:
    print(f"Failed to retrieve flavor details. Status code: {response.status_code}")
    print(response.text)