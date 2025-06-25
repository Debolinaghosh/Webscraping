import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE = "https://www.ecb.europa.eu"

params = {
    'name_of_publication': 'Speech',
    'boardmember': 'Christine Lagarde',
    'page': 0
}

all_entries = []

while True:
    resp = requests.get(
        "https://www.ecb.europa.eu/press/pubbydate/html/index_include.en.html",
        params=params
    )
    if resp.status_code != 200:
        break

    soup = BeautifulSoup(resp.text, 'html.parser')
    dl = soup.find('dl')
    if not dl:
        break

    date = None
    for tag in dl.find_all(['dt', 'dd'], recursive=False):
        if tag.name == 'dt':
            date = tag.text.strip()
        else:
            # speech link
            title_div = tag.select_one('div.title > a')
            speech_title = title_div.get_text(strip=True) if title_div else None
            speech_url = BASE + title_div['href'] if title_div else None

            entry = {
                'date': date,
                'speech_title': speech_title,
                'speech_url': speech_url,
                'annex_title': None,
                'annex_url': None
            }
            all_entries.append(entry)

            # now grab annex links within this <dd>
            for annex_a in tag.select('div.accordion:has(.title:contains("Annexes")) a'):
                annex_title = annex_a.get_text(strip=True)
                annex_url = BASE + annex_a['href']
                all_entries.append({
                    'date': date,
                    'speech_title': speech_title,
                    'speech_url': speech_url,
                    'annex_title': annex_title,
                    'annex_url': annex_url
                })

    params['page'] += 1
    if len(dl.get_text(strip=True)) < 10:
        break

    time.sleep(0.5)

df = pd.DataFrame(all_entries)
print(df.head(10))
df.to_csv('ecb_speeches_with_annexes.csv', index=False)
