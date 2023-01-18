import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
resp = requests.get(url)
resp = resp.json()

resp = resp["items"]

j = 0
for i in resp:
  dir = resp[j]

  j = j + 1
  for key, val in dir.items():
    if key == "owner":
      for k, v in val.items():
        if k == "login":
          print(f"login: {v}")

    if key == "name":
      print(f"name: {val}")

    if key == "description":
      print(f"desc: {val}")
