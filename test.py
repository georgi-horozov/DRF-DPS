import requests

BASE_URL = "http://127.0.0.1:8000"

# 1. Вземи токен
response = requests.post(f"{BASE_URL}/auth/jwt/create/", json={
    "email": "horozov.g@abv.bg",
    "password": "Djangorest@2026"
})

tokens = response.json()
access_token = tokens["access"]
print("Access token:", access_token)

# 2. Извлечи камионите
trucks_response = requests.get(f"{BASE_URL}/trucks/", headers={
    "Authorization": f"Bearer {access_token}"
})

print("Trucks:", trucks_response.json())

# import requests

# BASE_URL = "http://127.0.0.1:8000"

# response = requests.post(f"{BASE_URL}/jwt/create/", json={
#     "email": "horozov.g@abv.bg",
#     "password": "Djangorest@2026"
# })

# print("Status code:", response.status_code)
# print("Response text:", response.text)  # ← Виж суровия отговор