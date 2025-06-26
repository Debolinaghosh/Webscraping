import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from helper import SCRAPER_CONFIG
from datetime import date

today = date.today()
today = today.strftime("%Y-%m-%d")
def extract_json_path(data, path):
    try:
        for key in path:
            data = data[key]
        return data
    except Exception as e:
        print(e)


def extract_from_soup_general(soup, conf):
    find_conf = conf.get("find", {})
    tag_name = find_conf.get("name")
    attrs = find_conf.get("attrs", {})

    tag = soup.find(tag_name, attrs)

    if not tag:
        return None

    # Special case for <meta> tags with "content" attribute
    if tag_name == "meta" and tag.has_attr("content"):
        return tag["content"]

    # Otherwise, return text content
    return tag.get_text(strip=True)


# def extract_from_jsonld(soup, json_path):
#     script_tag = soup.find('script', type='application/ld+json')
#     if not script_tag:
#         return None
#     try:
#         data = json.loads(script_tag.string)
#         for key in json_path:
#             data = data[key]
#         return data
#     except Exception as e:
#         print(e)

def extract_from_jsonld(soup, json_path, filter_conf=None):
    script_tag = soup.find('script', type='application/ld+json')
    if not script_tag:
        return None

    try:
        data = json.loads(script_tag.string)
        for key in json_path:
            data = data[key]

        # Optional filtering
        if filter_conf and isinstance(data, list):
            keywords = filter_conf.get("name_keywords", [])
            for item in data:
                name = item.get("name", "")
                if all(k in name for k in keywords):
                    price = extract_json_path(item, filter_conf.get("price_path", []))
                    currency = extract_json_path(item, filter_conf.get("currency_path", []))
                    return f"{price} {currency}".strip()
            return "Price not found"
        return data
    except Exception as e:
        print(e)
        return None




def scrape_site(site, conf):
    results = []

    for url in conf["urls"]:
        headers = conf.get("headers", {})
        try:
            # API-type configuration (e.g., Wickes, Toolstation)
            if "api" in conf:
                
                method  = conf["api"].get("type", "json")

                if method == "json":
                    response = requests.get(
                        url["link"], 
                        headers=headers
                    )
                    data = response.json()
                    price = extract_json_path(data, conf["api"]["price_path"])
                    if not price:
                        price = "Price not found"

                elif method == "post_json":
                    response = requests.post(
                        url["link"],
                        headers=headers,
                        json=url["json_data"]
                    )
                    data = response.json()
                    price = extract_json_path(data, conf["api"]["price_path"])
                    if not price:
                        price = "Price not found"

                else:
                    price = "Price not found"

            else:
                response = requests.get(url["link"], headers=conf.get("headers", {}))
                soup = BeautifulSoup(response.content, "html.parser")

                if conf["price"]["type"] == "soup":
                    price = extract_from_soup_general(soup, conf["price"])
                    if not price:
                        price = "Price not found"
                elif conf["price"]["type"] == "json-ld":
                    price = extract_from_jsonld(
                        soup,
                        conf["price"]["json_path"],
                        conf["price"].get("filter")
                    )
                    if not price:
                        price = "Price not found"
                else:
                    price = "Price not found"

            urlCountry = conf.get("country", "Unknown")
            results.append({"Country": urlCountry, "Brand":  site, "Description": url["product_description"], "Link": url["link"], f"{today}": price})

        except Exception as e:
            print(e)

    return results

def main():
    all_dataframes = []
    
    columns = ["Country", "Brand", "Description", "Link", f"{today}"]
    df = pd.DataFrame(columns=columns)

    for site, conf in SCRAPER_CONFIG["WEBSITES"].items():

        data = scrape_site(site, conf)
        df = pd.DataFrame(data)
        all_dataframes.append(df)
        print(f"Scraped: {site}")

    combined_df = pd.concat(all_dataframes, ignore_index=True)
    # combined_df["date"] = pd.to_datetime("today").strftime("%Y-%m-%d")  # Add today's date
    combined_df.to_excel('all_products599.xlsx', index=False)
    print("Done: All data saved in 'all_products.xlsx'")


if __name__ == "__main__":
    main()
