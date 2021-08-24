import requests
from bs4 import BeautifulSoup

search_keyword = "laptop"
WINNIPEG_KIJIJI_URL = "https://www.kijiji.ca/h-winnipeg/1700192"
winnipeg_kijiji_search_url = f"https://www.kijiji.ca/b-winnipeg/{search_keyword}/k0l1700192"

result = requests.get(winnipeg_kijiji_search_url)

kijiji_html = BeautifulSoup(result.text, "html.parser")

pagination = kijiji_html.find("div", class_="pagination")

results = pagination.find_all("a")

last_page = int(results[-3].get_text())
