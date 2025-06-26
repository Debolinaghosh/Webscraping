SCRAPER_CONFIG = {
    "proxy": {"http": "http://proxy.jpmchase.net:8443", "https": "http://proxy.jpmchase.net:8443"},
    "WEBSITES": {

        "praxis": {
            "country": "ABC",
            "urls": [
                {
                    "link": "https://www.praxis.nl/verf-laminaat-decoratie/verf/lakken/flexa-lak-strak-de-lak-zijdeglans-cr%C3%A8me-wit-ral-9001-750ml/5377082",
                    "product_description": "Description of the product1 praxis"
                }, 
                {
                    "link": "https://www.praxis.nl/verf-laminaat-decoratie/verf/latex/histor-latex-monodek-revolution-mat-wit-10l/10026886",
                    "product_description": "Description of the product2 praxis"
                },
                {
                    "link": "https://www.praxis.nl/verf-laminaat-decoratie/verf/lakken/sigma-lak-zwart-satijn-750ml/563861",
                    "product_description": "Description of the product3 praxis"
                },
                {
                    "link": "https://www.praxis.nl/verf-laminaat-decoratie/verf/grondverf/wijzonol-grondverf-lak-mat-blauwgrijs-750ml/5291151",
                    "product_description": "Description of the product4 praxis"
                },
                {
                    "link": "https://www.praxis.nl/verf-laminaat-decoratie/verf/latex/flexa-muurverf-powerdek-muren-plafonds-10l-25/5283161",
                    "product_description": "Description of the product5 praxis"
                }
            ],
            "price": {
                "type": "json-ld",
                "json_path": ["offers", "price"]
            } 
        },

        "gamma": {
            "country": "ABC",
            "urls": [            
                {
                    "link": "https://www.gamma.nl/assortiment/flexa-powerdek-wit-10-liter-25/p/B440828",
                    "product_description": "Description of the product1 gamma"
                }, 
                {
                    "link": "https://www.gamma.nl/assortiment/flexa-strak-in-de-lak-voor-binnen-ral-9010-gebroken-wit-zijdeglans-750-ml/p/B535884",
                    "product_description": "Description of the product2 gamma"
                },
                {
                    "link": "https://www.gamma.nl/assortiment/histor-monodek-revolution-wit-10-liter/p/B144564",
                    "product_description": "Description of the product3 gamma"
                },
                {
                    "link": "https://www.gamma.nl/assortiment/sigma-lak-interieur-9010-zuiverwit-zijdeglans-750-ml/p/B598778",
                    "product_description": "Description of the product4 gamma"
                },
                {
                    "link": "https://www.gamma.nl/assortiment/wijzonol-grondverf-dekkend-wit-750-ml/p/B430624",
                    "product_description": "Description of the product5 gamma"
                }
            ],
            "price": {
                "type": "soup",
                "find": {
                    "name": "meta", 
                    "attrs": {"itemprop": "price", "content": True}
                },
            }
        },

        "karwei": {
            "country": "ABC",
            "urls": [
                {
                    "link": "https://www.karwei.nl/assortiment/flexa-powerdek-muurverf-mat-stralend-wit-10-l/p/B440827",
                    "product_description": "Description of the product1 karwei"
                }, 
                {
                    "link": "https://www.karwei.nl/assortiment/flexa-strak-in-de-lak-zijdeglans-ral9010-750-ml-watergedragen/p/B535884",
                    "product_description": "Description of the product2 karwei"
                },
                {
                    "link": "https://www.karwei.nl/assortiment/histor-monodek-revolution-latex-wit-10-liter/p/B144564",
                    "product_description": "Description of the product3 karwei"
                },
                {
                    "link": "https://www.karwei.nl/assortiment/sigma-houtlak-interieur-zijdeglans-ral-9010-750-ml/p/B598778",
                    "product_description": "Description of the product4 karwei"
                },
                {
                    "link": "https://www.karwei.nl/assortiment/wijzonol-grondlak-wit-750-ml/p/B430624",
                    "product_description": "Description of the product5 karwei"
                }
            ],
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
                }
            }
        },

        "wickes": {
            "country": "ABC",
            "urls": [
                {
                    "link": "https://rapidload.increasingly.co/increasingly_bundles?irb/cHJvZHVjdF9pZHM9MTM3NDY4JmNhdGVnb3J5X2lkPSZhcGlfa2V5PXdLUzh4eiZjbGllbnRfaWQ9JnBhZ2VfdHlwZT1jYXRhbG9nX3Byb2R1Y3RfdmlldyZjbGllbnRfdmlzaXRvcl9pZD0wNWRkMWNlNzQ4NjBlOGYxMjZkZGQ5MmVkZmQ4YTQ3MzIwYTExMTM3YjgmZnI9MSZpc190Yz0xJm5vX29mX2J1bmRsZXM9MTA=",
                    "product_description": "Description of the product1 wickes"
                },
                {
                    "link": "https://rapidload.increasingly.co/increasingly_bundles?irb/cHJvZHVjdF9pZHM9MTg0NjE3JmNhdGVnb3J5X2lkPSZhcGlfa2V5PXdLUzh4eiZjbGllbnRfaWQ9JnBhZ2VfdHlwZT1jYXRhbG9nX3Byb2R1Y3RfdmlldyZmcj0xJmNsaWVudF92aXNpdG9yX2lkPTA1ZGQxY2U3NDg2MGU4ZjEyNmRkZDkyZWRmZDhhNDczMjBhMTExMzdiOCZpc190YnhfbmV3PTEmbm9fb2ZfYnVuZGxlcz0x",
                    "product_description": "Description of the product2 wickes"
                },
                {
                    "link": "https://rapidload.increasingly.co/increasingly_bundles?irb/cHJvZHVjdF9pZHM9MTIyNDI4JmNhdGVnb3J5X2lkPSZhcGlfa2V5PXdLUzh4eiZjbGllbnRfaWQ9JnBhZ2VfdHlwZT1jYXRhbG9nX3Byb2R1Y3RfdmlldyZjbGllbnRfdmlzaXRvcl9pZD0wNWRkMWNlNzQ4NjBlOGYxMjZkZGQ5MmVkZmQ4YTQ3MzIwYTExMTM3YjgmZnI9MSZpc190Yz0xJm5vX29mX2J1bmRsZXM9MTA=",
                    "product_description": "Description of the product3 wickes"
                },
                {
                    "link": "https://rapidload.increasingly.co/increasingly_bundles?irb/cHJvZHVjdF9pZHM9MTA2NTAwJmNhdGVnb3J5X2lkPSZhcGlfa2V5PXdLUzh4eiZjbGllbnRfaWQ9JnBhZ2VfdHlwZT1jYXRhbG9nX3Byb2R1Y3RfdmlldyZmcj0xJmNsaWVudF92aXNpdG9yX2lkPTA1ZGQxY2U3NDg2MGU4ZjEyNmRkZDkyZWRmZDhhNDczMjBhMTExMzdiOA==",
                    "product_description": "Description of the product4 wickes"
                },
                {
                    "link": "https://rapidload.increasingly.co/increasingly_bundles?irb/cHJvZHVjdF9pZHM9MTQ3MDc2JmNhdGVnb3J5X2lkPSZhcGlfa2V5PXdLUzh4eiZjbGllbnRfaWQ9JnBhZ2VfdHlwZT1jYXRhbG9nX3Byb2R1Y3RfdmlldyZmcj0xJmNsaWVudF92aXNpdG9yX2lkPTA1ZGQxY2U3NDg2MGU4ZjEyNmRkZDkyZWRmZDhhNDczMjBhMTExMzdiOCZpc190YnhfbmV3PTEmbm9fb2ZfYnVuZGxlcz0x",
                    "product_description": "Description of the product5 wickes"
                }                                                      
            ],
            "headers": {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
                'origin': 'https://www.wickes.co.uk',
                'priority': 'u=1, i',
                'referer': 'https://www.wickes.co.uk/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            },
            "api": {
                "type": "json",
                "price_path": ["ProductsDetail", 0, "Price"],
            }
        },

        "toolstation": {
            "country": "ABC",
            "urls": [
                {
                    "link": "https://www.toolstation.com/ecom/v1/products/getProducts",
                    "json_data": {
                        'products': [
                            '21785',
                            '18930'
                        ]
                    },
                    "product_description": "Description of the product1 wickes"
                }, 
                {
                    "link": "https://www.toolstation.com/ecom/v1/products/getProducts",
                    "json_data": {
                        'products': [
                            '48972',
                            '21785'
                        ]
                    },
                }
            ],
            "headers": {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
                'authorization': 'Bearer IPWpZbUv0fGj8SAplgA6p62PQpfw',
                'content-type': 'application/json',
                'origin': 'https://www.toolstation.com',
                'referer': 'https://www.toolstation.com/dulux-trade-high-gloss-paint/p21785?searchstr=sandtex+ultra+smooth',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
            },
            "api": {
                "type": "post_json",
                "price_path": ["data", 0, "prices", "raw", "gross"]
            },
        },

        "diy": {
            "country": "ABC",
            "urls" : [
                {
                    "link": "https://www.diy.com/departments/dulux-trade-white-high-gloss-metal-wood-paint-2-5l/35991_BQ.prd",
                    "product_description": "Description of the product1 diy"
                },
                {
                    "link": "https://www.diy.com/departments/dulux-walls-ceilings-pure-brilliant-white-matt-emulsion-paint-10l/1785813_BQ.prd",
                    "product_description": "Description of the product2 diy"
                },
                {
                    "link": "https://www.diy.com/departments/leyland-white-gloss-metal-wood-paint-2-5l/1491791_BQ.prd",
                    "product_description": "Description of the product3 diy"
                },
                {
                    "link": "https://www.diy.com/departments/dulux-walls-ceilings-pure-brilliant-white-matt-emulsion-paint-10l/1785813_BQ.prd",
                    "product_description": "Description of the product4 diy"
                },
                {
                    "link": "https://www.diy.com/departments/valspar-white-matt-emulsion-paint-10l/1698002_BQ.prd",
                    "product_description": "Description of the product5 diy"
                },
                {
                    "link": "https://www.diy.com/departments/valspar-white-matt-emulsion-paint-2-5l/1698004_BQ.prd",
                    "product_description": "Description of the product6 diy"
                },
                {
                    "link": "https://www.diy.com/departments/leyland-pure-brilliant-white-matt-emulsion-paint-10l/1335443_BQ.prd",
                    "product_description": "Description of the product7 diy"
                },
                {
                    "link": "https://www.diy.com/departments/ronseal-one-coat-fence-life-harvest-gold-matt-fence-shed-treatment-5l/1919522_BQ.prd",
                    "product_description": "Description of the product8 diy"
                },
                {
                    "link": "https://www.diy.com/departments/dulux-trade-white-high-gloss-metal-wood-paint-2-5l/35991_BQ.prd",
                    "product_description": "Description of the product9 diy"
                },
                {
                    "link": "https://www.diy.com/departments/sandtex-ultra-smooth-pure-brilliant-white-masonry-paint-5l/127469_BQ.prd",
                    "product_description": "Description of the product10 diy"
                },
                {
                    "link": "https://www.diy.com/departments/goodhome-walls-ceilings-brilliant-white-vinyl-matt-emulsion-paint-2-5l/5059340231983_BQ.prd",
                    "product_description": "Description of the product11 diy"
                },
                {
                    "link": "https://www.diy.com/departments/goodhome-classic-pure-brilliant-white-smooth-matt-masonry-paint-5l/3663602520795_BQ.prd",
                    "product_description": "Description of the product12 diy"
                },
                {
                    "link": "https://www.diy.com/departments/dulux-weathershield-pure-brilliant-white-smooth-matt-masonry-paint-10l/5010212644447_BQ.prd",
                    "product_description": "Description of the product13 diy"
                }
            ],
            "price": {
                "type": "soup",
                "find": {
                    "name": "span", 
                    "attrs": {
                        "data-testid": "product-price"
                    }
                },
            }
        },

        "castorama": {
            "country": "ABC",
            "urls": [
                {
                    "link": "https://www.castorama.pl/farba-dulux-easycare-perlowy-bialy-2-5-l-id-1109981.html",
                    "product_description": "Description of the product1 castorama"
                },
                {
                    "link": "https://www.castorama.pl/rapidry-szary-bez-0-4l-id-1101006.html",
                    "product_description": "Description of the product2 castorama"
                },
                {
                    "link": "https://www.castorama.pl/emalia-do-kaloryferow-dekoral-biala-0-7-l-id-1028391.html",
                    "product_description": "Description of the product3 castorama"
                },
                {
                    "link": "https://www.castorama.pl/dekoral-k-l-deser-waniliowy-2-5l-id-1058667.html",
                    "product_description": "Description of the product4 castorama"
                },
                {
                    "link": "https://www.castorama.pl/emulsja-podkladowa-sniezka-grunt-biala-5-l-id-19975.html",
                    "product_description": "Description of the product5 castorama"
                },
                {
                    "link": "https://www.castorama.fr/peinture-murs-et-boiseries-dulux-valentine-creme-du-couleur-marron-glace-satin-2-5l-20-gratuit/3031520137096_CAFR.prd",
                    "product_description": "Description of the product6 castorama"
                },
                {
                    "link": "https://www.castorama.fr/peinture-murs-et-boiseries-dulux-valentine-color-resist-ivoire-satin-2-5l/3031520231312_CAFR.prd",
                    "product_description": "Description of the product7 castorama"
                },
                {
                    "link": "https://www.castorama.fr/laque-valenite-dulux-blanc-de-blanc-satin-2l/3031520150828_CAFR.prd",
                    "product_description": "Description of the product8 castorama"
                },
                {
                    "link": "https://www.castorama.fr/peinture-murs-et-plafonds-tollens-pro-mat-10l/3463975247851_CAFR.prd",
                    "product_description": "Description of the product9 castorama"
                }
            ],
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
            "country": "ABC",
            "urls": [
                {
                    "link": "https://www.jernia.no/c/jotun-murprimer-drytech-0%2C75l/p/58018649",
                    "product_description": "Description of the product1 jernia"
                }
            ],
            "price": {
                "type": "json-ld",
                "json_path": ["offers", "price"],
                "currency_path": ["offers", "priceCurrency"]
            }
        },

        "bricodepot": {
            "country": "ABC",
            "urls": [
                {
                    "link": "https://www.bricodepot.fr/angers-beaucouze/tollens-pro-murs-et-plafonds-mat-10-l-/prod75488/",
                    "product_description": "Description of the product1 bricodepot"
                },
                {
                    "link": "https://www.bricodepot.fr/angers-beaucouze/peinture-mur-interieur-2-en-1-satin-25-l-blanc-pur/prod85495/",
                    "product_description": "Description of the product2 bricodepot"
                },
                {
                    "link": "https://www.bricodepot.fr/angers-beaucouze/peinture-interieur-satin-2-l-beige-bauxite/prod85586/",
                    "product_description": "Description of the product3 bricodepot"
                },
                {
                    "link": "https://www.bricodepot.fr/angers-beaucouze/peinture-murs-et-boiseries-interieure-color-resist-acrylique-satin-porcelaine-25-l/prod62099/",
                    "product_description": "Description of the product4 bricodepot"
                },
                {
                    "link": "https://www.bricodepot.fr/angers-beaucouze/peinture-glycero-boiseries-satin-blanc2-l/prod76834/",
                    "product_description": "Description of the product5 bricodepot"
                }
            ],
            "price": {
                "type": "soup",
                "find": {
                    "name": "span", 
                    "attrs": {
                        "class": "bd-Price-current"
                    }
                }
            }
        },

        "sherin_williams": {
            "country": "ABC",
            "urls": [
                {
                    "link": "https://www.sherwin-williams.com/wcs/resources/store/10151/xcatalog/getSKUDetails/15990",
                    "product_description": "Description of the product1 sherwin_williams"
                },
                {
                    "link": "https://www.sherwin-williams.com/wcs/resources/store/10151/xcatalog/getSKUDetails/361503",
                    "product_description": "Description of the product2 sherwin_williams"
                },
                {
                    "link": "https://www.sherwin-williams.com/wcs/resources/store/10151/xcatalog/getSKUDetails/438018",
                    "product_description": "Description of the product3 sherwin_williams"               
                },
                {
                    "link": "https://www.sherwin-williams.com/wcs/resources/store/10151/xcatalog/getSKUDetails/414510",
                    "product_description": "Description of the product4 sherwin_williams"
                },
                {
                    "link": "https://www.sherwin-williams.com/wcs/resources/store/10151/xcatalog/getSKUDetails/885016",
                    "product_description": "Description of the product5 sherwin_williams"
                }
            ],
            "headers": {
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
                    'priority': 'u=1, i',
                    'referer': 'https://www.sherwin-williams.com/homeowners/products/duration-exterior-acrylic-latex?colorPartNumber=SW7005&secureweb=Teams',
                    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
                },
            "api": {
                "type": "json",
                "price_path": ["priceObject", "lP"],
            }
        },

        "dulux_decorator": {
            "country": "ABC",
            "urls": [
                {
                    "link": "https://www.duluxdecoratorcentre.co.uk/dulux-trade-diamond-eggshell?returnurl=%2fsearch%3fq%3ddulux%2btrade%2bdiamond%2beggshell&secureweb=Teams",
                    "product_description": "Dulux Trade Diamond Eggshell - Pure Brilliant White 5L"
                }
            ],
            "headers": {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "en-US,en;q=0.9,it;q=0.8,es;q=0.7",
                "cache-control": "max-age=0",
                "priority": "u=0, i",
                "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
            },
            "price": {
                "type": "json-ld",
                "json_path": ['hasVariant'],
                "filter": {
                    "name_keywords": ["5L", "Pure Brilliant White"],
                    "price_path": ["offers", "price"],
                    "currency_path": ["offers", "priceCurrency"]
                }
            } 
        }
    }
}