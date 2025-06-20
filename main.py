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

# def extract_from_soup(soup, conf):
#     tag = soup.find(
#         conf["find"]["name"],
#         conf["find"].get("attrs") or {"class": conf["find"].get("class_")}
#     )
#     return tag.get_text(strip=True) if tag else None

def extract_from_soup(soup, conf):
    find_tag = conf["find"]["name"]
    attrs = conf["find"].get("attrs")

    tag = soup.find(find_tag, attrs)
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
                    response = requests.get(
                        url, 
                        headers=headers
                    )
                    data = response.json()
                    product_name = extract_json_path(data, conf["api"]["product_path"])
                    price = extract_json_path(data, conf["api"]["price_path"])
                    if not price:
                        price = extract_json_path(data, conf["api"].get("fallback_price_path", []))

                elif method == "post_json":
                    response = requests.post(
                        url["link"],
                        headers=headers,
                        json=url["json_data"]
                    )
                    data = response.json()
                    product_name = extract_json_path(data, conf["api"]["product_path"])
                    price = extract_json_path(data, conf["api"]["price_path"])

                else:
                    product_name = price = None

            # HTML/JSON-LD configuration (e.g., Praxis, Gamma)
            else:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")

                # Product name extraction
                if conf["product_name"]["type"] == "soup":
                    product_name = extract_from_soup(soup, conf["product_name"])
                    if not product_name:
                        product_name = "Name not found"
                elif conf["product_name"]["type"] == "meta":
                    product_name = extract_from_meta(soup, conf["product_name"])
                elif conf["product_name"]["type"] == "json-ld":
                    product_name = extract_from_jsonld(soup, conf["product_name"]["json_path"])
                else:
                    product_name = None

                # Price extraction
                if conf["price"]["type"] == "soup":
                    price = extract_from_soup(soup, conf["price"])
                    if "currency" in conf["price"]:
                        currency = extract_from_meta(soup, {"attrs": conf["price"]["currency"]})
                        if currency:
                            price = f"{currency} {price}"
                    if not price:
                        price = "Price not found"
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
    all_dataframes = []
    
    for site, conf in SCRAPER_CONFIG["WEBSITES"].items():
        data = scrape_site(site, conf)
        df = pd.DataFrame(data)
        df["source_site"] = site  # Optional: track which site the data came from
        all_dataframes.append(df)
        print(f"Scraped: {site}")

    combined_df = pd.concat(all_dataframes, ignore_index=True)
    combined_df["date"] = pd.to_datetime("today").strftime("%Y-%m-%d")  # Add today's date
    combined_df.to_excel('all_products.xlsx', index=False)
    print("Done: All data saved in 'all_products.xlsx'")


if __name__ == "__main__":
    main()
