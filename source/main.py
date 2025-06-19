import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

from helper import SCRAPER_CONFIG

def extract_json_path(data, path):
    try:
        for key in path:
            data = data[key]
        return data
    except (KeyError, IndexError, TypeError):
        return None

def extract_from_soup(soup, conf):
    tag = soup.find(
        conf["find"]["name"],
        conf["find"].get("attrs") or {"class": conf["find"].get("class_")}
    )
    return tag.get_text(strip=True) if tag else None

def extract_from_meta(soup, conf):
    tag = soup.find("meta", attrs=conf["attrs"])
    return tag["content"] if tag and tag.has_attr("content") else None

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
        try:
            # API-type configuration (e.g., Wickes, Toolstation)
            if "api" in conf:
                headers = conf["api"].get("headers", {})
                method  = conf["api"].get("type", "json")

                if method == "json":
                    response = requests.get(url, headers=headers, proxies=SCRAPER_CONFIG["proxy"])
                    data = response.json()
                    product_name = extract_json_path(data, conf["api"]["product_path"])
                    price = extract_json_path(data, conf["api"].get("price_path"))
                    if not price:
                        price = extract_json_path(data, conf["api"].get("fallback_price_path", []))

                elif method == "post_json":
                    response = requests.post(
                        url,
                        headers=headers,
                        json=conf["api"]["json_data"],
                        proxies=SCRAPER_CONFIG["proxy"]
                    )
                    data = response.json()
                    product_name = extract_json_path(data, conf["api"]["product_path"])
                    price = extract_json_path(data, conf["api"]["price_path"])

                else:
                    product_name = price = None

            # HTML/JSON-LD configuration (e.g., Praxis, Gamma)
            else:
                response = requests.get(url, proxies=SCRAPER_CONFIG["proxy"])
                soup = BeautifulSoup(response.content, "html.parser")

                # Product name extraction
                if conf["product_name"]["type"] == "soup":
                    product_name = extract_from_soup(soup, conf["product_name"])
                elif conf["product_name"]["type"] == "meta":
                    product_name = extract_from_meta(soup, conf["product_name"])
                elif conf["product_name"]["type"] == "json-ld":
                    product_name = extract_from_jsonld(soup, conf["product_name"]["json_path"])
                else:
                    product_name = None

                # Price extraction
                if conf["price"]["type"] == "soup":
                    price = extract_from_soup(soup, conf["price"])
                elif conf["price"]["type"] == "meta":
                    price = extract_from_meta(soup, conf["price"])
                    if "currency" in conf["price"]:
                        currency = extract_from_meta(soup, {"attrs": conf["price"]["currency"]})
                        if currency:
                            price = f"{currency} {price}"
                elif conf["price"]["type"] == "json-ld":
                    price = extract_from_jsonld(soup, conf["price"]["json_path"])
                else:
                    price = None

            results.append({"Product Name": product_name, "Price": price})

        except Exception as e:
            results.append({"Product Name": None, "Price": None, "Error": str(e)})

    return results

def main():
    for site, conf in SCRAPER_CONFIG.items():
        data = scrape_site(site, conf)
        df = pd.DataFrame(data)
        df.to_excel(f'../files/product_{site}.xlsx', index=False)
        print(f"Done: {site}")

if __name__ == "__main__":
    main()
