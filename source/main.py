import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

from helper import SCRAPER_CONFIG

def extract_from_soup(soup, config):
    if config["type"] == "soup":
        tag = soup.find(**config["find"])
        return tag.text.strip() if tag else None
    elif config["type"] == "meta":
        tag = soup.find('meta', config["attrs"])
        return tag['content'] if tag and tag.has_attr('content') else None
    return None

def extract_from_jsonld(soup, json_path):
    script_tag = soup.find('script', type='application/ld+json')
    if not script_tag:
        return None
    try:
        data = json.loads(script_tag.string)
        for key in json_path:
            data = data[key]
        return data
    except Exception:
        return None

def scrape_site(site, conf):
    results = []
    for url in conf["urls"]:
        response = requests.get(url, proxies=conf.get("proxy"))
        soup = BeautifulSoup(response.content, 'html.parser')
        # Product name
        if conf["product_name"]["type"] == "soup" or conf["product_name"]["type"] == "meta":
            product_name = extract_from_soup(soup, conf["product_name"])
        elif conf["product_name"]["type"] == "json-ld":
            product_name = extract_from_jsonld(soup, conf["product_name"]["json_path"])
        else:
            product_name = None
        # Price
        if conf["price"]["type"] == "json-ld":
            price = extract_from_jsonld(soup, conf["price"]["json_path"])
        elif conf["price"]["type"] == "meta":
            price = extract_from_soup(soup, conf["price"])
            if "currency" in conf["price"]:
                currency = extract_from_soup(soup, {"type": "meta", "attrs": conf["price"]["currency"]})
                if currency:
                    price = f"{currency} {price}"
        else:
            price = None
        results.append({"Product Name": product_name, "Price": price})
    return results

def main():
    for site, conf in SCRAPER_CONFIG.items():
        data = scrape_site(site, conf)
        df = pd.DataFrame(data)
        df.to_excel(f'../files/product_{site}.xlsx', index=False)
        print(f"Done: {site}")

if __name__ == "__main__":
    main()