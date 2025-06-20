SCRAPER_CONFIG = {
    "proxy": {"http": "http://proxy.jpmchase.net:8443", "https": "http://proxy.jpmchase.net:8443"},
    "WEBSITES": {
        "praxis": {
            "urls": [
                'https://www.praxis.nl/verf-laminaat-decoratie/verf/lakken/flexa-lak-strak-de-lak-zijdeglans-cr%C3%A8me-wit-ral-9001-750ml/5377082',
                'https://www.praxis.nl/verf-laminaat-decoratie/verf/latex/histor-latex-monodek-revolution-mat-wit-10l/10026886',
                'https://www.praxis.nl/verf-laminaat-decoratie/verf/lakken/sigma-lak-zwart-satijn-750ml/5638618',
                'https://www.praxis.nl/verf-laminaat-decoratie/verf/grondverf/wijzonol-grondverf-lak-mat-blauwgrijs-750ml/5291151',
                'https://www.praxis.nl/verf-laminaat-decoratie/verf/latex/flexa-muurverf-powerdek-muren-plafonds-10l-25/5283161'
            ],
            "product_name": {
                "type": "soup",
                "find": {
                    "name": "h1", 
                    "attrs": {
                        "class": ["chakra-heading", "mxd-product-detail-layout-heading", "pdfi-kbivdx"]
                    }
                },
            },
            "price": {
                "type": "json-ld",
                "json_path": ["offers", "price"]
            }
        },
        "gamma": {
            "urls": [
                'https://www.gamma.nl/assortiment/flexa-powerdek-wit-10-liter-25/p/B440828',
                'https://www.gamma.nl/assortiment/flexa-strak-in-de-lak-voor-binnen-ral-9010-gebroken-wit-zijdeglans-750-ml/p/B535884',
                'https://www.gamma.nl/assortiment/histor-monodek-revolution-wit-10-liter/p/B144564',
                'https://www.gamma.nl/assortiment/sigma-lak-interieur-9010-zuiverwit-zijdeglans-750-ml/p/B598778',
                'https://www.gamma.nl/assortiment/wijzonol-grondverf-dekkend-wit-750-ml/p/B430624'
            ],
            "product_name": {
                "type": "meta",
                "attrs": {"itemprop": "name", "content": True}
            },
            "price": {
                "type": "meta",
                "attrs": {"itemprop": "price", "content": True},
                "currency": {"itemprop": "priceCurrency", "content": True}
            }
        },
        
        "karwei": {
            "urls": [
                'https://www.karwei.nl/assortiment/flexa-powerdek-muurverf-mat-stralend-wit-10-l/p/B440827',
                'https://www.karwei.nl/assortiment/flexa-strak-in-de-lak-zijdeglans-ral9010-750-ml-watergedragen/p/B535884',
                'https://www.karwei.nl/assortiment/histor-monodek-revolution-latex-wit-10-liter/p/B144564',
                'https://www.karwei.nl/assortiment/sigma-houtlak-interieur-zijdeglans-ral-9010-750-ml/p/B598778',
                'https://www.karwei.nl/assortiment/wijzonol-grondlak-wit-750-ml/p/B430624'
            ],
            "product_name": {
                "type": "soup",
                "find": {
                    "name": "h1",
                    "attrs": {
                        "itemprop": "name"
                    }
                }
            },
            "price": {
                "type": "soup",
                "find": {
                    "name": "div",
                    "attrs": {
                        "class": [
                            "product-price",
                            "product-price promotion"
                            "product-price-nowrap"
                        ]
                    }
                },
                "currency": {"itemprop": "priceCurrency", "content": True}
            }

        },
        "wickes": {
            "urls": [
                'https://rapidload.increasingly.co/increasingly_bundles?irb/cHJvZHVjdF9pZHM9MTM3NDY4JmNhdGVnb3J5X2lkPSZhcGlfa2V5PXdLUzh4eiZjbGllbnRfaWQ9JnBhZ2VfdHlwZT1jYXRhbG9nX3Byb2R1Y3RfdmlldyZjbGllbnRfdmlzaXRvcl9pZD0wNWRkMWNlNzQ4NjBlOGYxMjZkZGQ5MmVkZmQ4YTQ3MzIwYTExMTM3YjgmZnI9MSZpc190Yz0xJm5vX29mX2J1bmRsZXM9MTA=',
                'https://rapidload.increasingly.co/increasingly_bundles?irb/cHJvZHVjdF9pZHM9MTg0NjE3JmNhdGVnb3J5X2lkPSZhcGlfa2V5PXdLUzh4eiZjbGllbnRfaWQ9JnBhZ2VfdHlwZT1jYXRhbG9nX3Byb2R1Y3RfdmlldyZmcj0xJmNsaWVudF92aXNpdG9yX2lkPTA1ZGQxY2U3NDg2MGU4ZjEyNmRkZDkyZWRmZDhhNDczMjBhMTExMzdiOCZpc190YnhfbmV3PTEmbm9fb2ZfYnVuZGxlcz0x',
                'https://rapidload.increasingly.co/increasingly_bundles?irb/cHJvZHVjdF9pZHM9MTIyNDI4JmNhdGVnb3J5X2lkPSZhcGlfa2V5PXdLUzh4eiZjbGllbnRfaWQ9JnBhZ2VfdHlwZT1jYXRhbG9nX3Byb2R1Y3RfdmlldyZjbGllbnRfdmlzaXRvcl9pZD0wNWRkMWNlNzQ4NjBlOGYxMjZkZGQ5MmVkZmQ4YTQ3MzIwYTExMTM3YjgmZnI9MSZpc190Yz0xJm5vX29mX2J1bmRsZXM9MTA=',
                'https://rapidload.increasingly.co/increasingly_bundles?irb/cHJvZHVjdF9pZHM9MTA2NTAwJmNhdGVnb3J5X2lkPSZhcGlfa2V5PXdLUzh4eiZjbGllbnRfaWQ9JnBhZ2VfdHlwZT1jYXRhbG9nX3Byb2R1Y3RfdmlldyZmcj0xJmNsaWVudF92aXNpdG9yX2lkPTA1ZGQxY2U3NDg2MGU4ZjEyNmRkZDkyZWRmZDhhNDczMjBhMTExMzdiOA==',
                'https://rapidload.increasingly.co/increasingly_bundles?irb/cHJvZHVjdF9pZHM9MTQ3MDc2JmNhdGVnb3J5X2lkPSZhcGlfa2V5PXdLUzh4eiZjbGllbnRfaWQ9JnBhZ2VfdHlwZT1jYXRhbG9nX3Byb2R1Y3RfdmlldyZmcj0xJmNsaWVudF92aXNpdG9yX2lkPTA1ZGQxY2U3NDg2MGU4ZjEyNmRkZDkyZWRmZDhhNDczMjBhMTExMzdiOCZpc190YnhfbmV3PTEmbm9fb2ZfYnVuZGxlcz0x'
            ],
            "api": {
                "type": "json",
                "headers": {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
                    'origin': 'https://www.wickes.co.uk',
                    'priority': 'u=1, i',
                    'referer': 'https://www.wickes.co.uk/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
                },
                "product_path": ["ProductsDetail", 0, "ProductName"],
                "price_path": ["ProductsDetail", 0, "Price"],  # fallback to "Price" if None
            }
        },

        "toolstation": {
            "urls": [
                "https://www.toolstation.com/ecom/v1/products/getProducts"
            ],
            "api": {
                "type": "post_json",
                "headers": {
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
                    'authorization': 'Bearer PgThTZq4ZlGdhQEx9zhcohd9K4aZ',
                    'content-type': 'application/json',
                    'origin': 'https://www.toolstation.com',
                    'referer': 'https://www.toolstation.com/dulux-trade-high-gloss-paint/p21785',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
                    },
                "json_data": {
                    'products': [
                        '21785',
                        '18930'
                    ]
                },
                "product_path": ["data", 0, "full_name"],
                "price_path": ["data", 0, "prices", "raw", "gross"]
            }
        },

        "diy": {
            "urls" : [
                'https://www.diy.com/departments/dulux-trade-white-high-gloss-metal-wood-paint-2-5l/35991_BQ.prd',
                'https://www.diy.com/departments/dulux-walls-ceilings-pure-brilliant-white-matt-emulsion-paint-10l/1785813_BQ.prd',
                'https://www.diy.com/departments/leyland-white-gloss-metal-wood-paint-2-5l/1491791_BQ.prd',
                'https://www.diy.com/departments/dulux-walls-ceilings-pure-brilliant-white-matt-emulsion-paint-10l/1785813_BQ.prd',
                'https://www.diy.com/departments/valspar-white-matt-emulsion-paint-10l/1698002_BQ.prd',
                'https://www.diy.com/departments/valspar-white-matt-emulsion-paint-2-5l/1698004_BQ.prd',
                'https://www.diy.com/departments/leyland-pure-brilliant-white-matt-emulsion-paint-10l/1335443_BQ.prd',
                'https://www.diy.com/departments/ronseal-one-coat-fence-life-harvest-gold-matt-fence-shed-treatment-5l/1919522_BQ.prd',
                'https://www.diy.com/departments/dulux-trade-white-high-gloss-metal-wood-paint-2-5l/35991_BQ.prd',
                'https://www.diy.com/departments/sandtex-ultra-smooth-pure-brilliant-white-masonry-paint-5l/127469_BQ.prd',
                'https://www.diy.com/departments/goodhome-walls-ceilings-brilliant-white-vinyl-matt-emulsion-paint-2-5l/5059340231983_BQ.prd',
                'https://www.diy.com/departments/goodhome-classic-pure-brilliant-white-smooth-matt-masonry-paint-5l/3663602520795_BQ.prd',
                'https://www.diy.com/departments/dulux-weathershield-pure-brilliant-white-smooth-matt-masonry-paint-10l/5010212644447_BQ.prd'
            ],
            "product_name": {
                "type": "soup",
                "find": {"name": "h1", "attrs": {"data-testid": "product-name"}}
            },
            "price": {
                "type": "soup",
                "find": {"name": "span", "attrs": {"data-testid": "product-price"}}
            }
        },

        "castorama": {
            "urls": [
                'https://www.castorama.pl/farba-dulux-easycare-perlowy-bialy-2-5-l-id-1109981.html',
                'https://www.castorama.pl/rapidry-szary-bez-0-4l-id-1101006.html',
                'https://www.castorama.pl/emalia-do-kaloryferow-dekoral-biala-0-7-l-id-1028391.html',
                'https://www.castorama.pl/dekoral-k-l-deser-waniliowy-2-5l-id-1058667.html',
                'https://www.castorama.pl/emulsja-podkladowa-sniezka-grunt-biala-5-l-id-19975.html',
                'https://www.castorama.fr/peinture-murs-et-boiseries-dulux-valentine-creme-du-couleur-marron-glace-satin-2-5l-20-gratuit/3031520137096_CAFR.prd',
                'https://www.castorama.fr/peinture-murs-et-boiseries-dulux-valentine-color-resist-ivoire-satin-2-5l/3031520231312_CAFR.prd',
                'https://www.castorama.fr/laque-valenite-dulux-blanc-de-blanc-satin-2l/3031520150828_CAFR.prd',
                'https://www.castorama.fr/peinture-murs-et-plafonds-tollens-pro-mat-10l/3463975247851_CAFR.prd'
            ],
            "product_name": {
                "type": "soup",
                "find": {
                    "name": "h1", 
                    "attrs": {
                        "id": "product-title"
                    }
                },
            },
            "price": {
                "type": "soup",
                "find": {
                    "name": "div", 
                    "attrs": {
                        "class": "_5d34bd7a"
                    }
                },
            }
        },

        "jernia": {
            "urls": [
                'https://www.jernia.no/c/jotun-murprimer-drytech-0%2C75l/p/58018649'
            ],
            "product_name": {
                "type": "json-ld",
                "json_path": ["name"]
            },
            "price": {
                "type": "json-ld",
                "json_path": ["offers", "price"],
                "currency_path": ["offers", "priceCurrency"]
            }
        },

        "bricodepot": {
            "urls": [
                'https://www.bricodepot.fr/angers-beaucouze/tollens-pro-murs-et-plafonds-mat-10-l-/prod75488/',
                'https://www.bricodepot.fr/angers-beaucouze/peinture-mur-interieur-2-en-1-satin-25-l-blanc-pur/prod85495/',
                'https://www.bricodepot.fr/angers-beaucouze/peinture-interieur-satin-2-l-beige-bauxite/prod85586/',
                'https://www.bricodepot.fr/angers-beaucouze/peinture-murs-et-boiseries-interieure-color-resist-acrylique-satin-porcelaine-25-l/prod62099/',
                'https://www.bricodepot.fr/angers-beaucouze/peinture-glycero-boiseries-satin-blanc2-l/prod76834/'
            ],
            "product_name": {
                "type": "soup",
                "find": {
                    "name": "h1", 
                    "attrs": {
                        "class": "bd-ProductCard-title"
                    }
                },
            },
            "price": {
                "type": "soup",
                "find": {
                    "name": "span", 
                    "attrs": {
                        "class": "bd-Price-current"
                    }
                },
                "currency": {"itemprop": "priceCurrency", "content": True}
            }
        }
    }
}