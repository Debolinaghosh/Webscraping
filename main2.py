import requests
import pandas as pd
from datetime import datetime, timezone
base_url = "https://www.ecb.europa.eu/foedb/dbs/foedb/publications.en/1751374833/OOfT70hg/data/0/chunk_{}.json"

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9',
    'priority': 'u=1, i',
    'referer': 'https://www.ecb.europa.eu/press/pubbydate/html/index.en.html?name_of_publication=Speech&boardmember=Christine%20Lagarde',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'Cookie': 'pa_privacy=%22optin%22; _pcid=%7B%22browserId%22%3A%22mckpum0denrgb8xw%22%2C%22_t%22%3A%22ms94s3s7%7Cmckpumg7%22%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbCAE4ALBADMEABwAffgGMA1gAcw-AOZSQAXyA'
}

master_data = []

for chunk in range(20):
    url = base_url.format(chunk)
    print(f"Fetching data from: {url}")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for i in range(0, len(data), 13):  # Assuming each entry has 13 elements

            url = data[i+9][0]  # The URL is in the 10th element of the group (index 9)
            title = data[i+10]["Title"]  # The Title is in the 11th element (index 10), inside a dictionary
            timestamp = data[i+1]  # The Date is in the 2nd element (index 1)

            finalUrl = f"https://www.ecb.europa.eu{url}" if url else None
            if "html" not in finalUrl:
                continue
            date = datetime.fromtimestamp(timestamp, timezone.utc).strftime('%Y-%m-%d')
            # Append the extracted data
            master_data.append({
                'URL': finalUrl,
                'Title': title,
                'Date': date
            })
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

df_master = pd.DataFrame(master_data)
df_master.to_csv('master_data3.csv', index=False)
print(df_master)
