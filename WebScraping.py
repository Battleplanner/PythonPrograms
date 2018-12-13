import requests
res = requests.get("https://automatetheboringstuff.com/page_that_does_not_exist")
res.raise_for_status()