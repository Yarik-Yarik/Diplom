import requests


def test_yandex_market_delivery_api():
    url = 'https://market-delivery.yandex.ru/api/v2/catalog/tashir_gyoln'
    params = {
        'longitude': '40.016066',
        'latitude': '57.672392',
        'shippingType': 'delivery'
    }
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru',
        'cookie': ('yuidss=8866985891693403522; yandexuid=8866985891693403522; '
                   '_ym_uid=1693403522834245424; gdpr=0; amcuid=1087269131705151624; '
                   'yabs-dsp=mts_banner.alNQaENzVEJRc1M0RkRqZVNETWZXdw==; skid=2871765781710169538; '
                   '_ym_d=1719468002; receive-cookie-deprecation=1; ymex=2040546745.yrts.1725186745; '
                   'eda_web_adult_confirmed=false; is_gdpr=0; is_gdpr_b=CP/jIhDxlwIoAg==; '
                   'yashr=6866899101734158016; i=I3WToYq6nHTlth818kyKVkykO1Gfb4zC0xwtKSA0R9h01dTRycWoWCkXmVBS0+'
                   'Exj2Ti69qMi+RsvLcYWqvIbx2uUJI=; PHPSESSID=m4r4ytj7-az377hb0cr-051kh8c4up82-fu05fubc12u; '
                   'Eats-Session=e7625f864a914270a6be2d11638ec86a; Session_id=3:1734360614.5.0.1734360614353:pB0QLg:8c5c.'
                   '1.2:1|1923995422.0.2.3:1734360614|3:10299761.723434.vRMaAUnDozdn0VAkmbEvz9wdX9g; '
                   'sessar=1.1197.CiCnhwGDTFKrTf5YOweU9sxq0VR5P-ZnBim1ZZpGU9RMKA.ctzJ-0dYqPig_w28SQ24qN5mJPf1tI2txFU67IT-2MQ; '
                   'sessionid2=3:1734360614.5.0.1734360614353:pB0QLg:8c5c.1.2:1|1923995422.0.2.3:1734360614|3:10299761.'
                   '723434.fakesign0000000000000000000; yp=2034919253.multib.1#1734184621.ygu.1#2049720614.udn.cDpidHNvdjIwMT'
                   'JAbWFpbC5ydQ%3D%3D; L=aCtjSWN1WWdqWk8CdgNMUUBeUmZgemJPAEUgHDd1WEIGEAACBBhHHB4=.1734360614.15984.376967.'
                   'c57ef1f400913749be073addc6faf20c; yandex_login=btsov2012@mail.ru; ys=udn.cDpidHNvdjIwMTJAbWFpbC5ydQ%3D%3D#c_'
                   'chck.633678325; _ym_isad=2; _yasc=rIIVX2f3opE+QCS0L7W9tlYCe4m21y0vUDikQRBVAIDDZcPN9M3+U1mt1oHujQtwC+Ye+OvS'
                   'hIw=; eda_web={"app":{"analyticsSession":{"id":"m542e2ps-i1v4egzy4p-pl8qqudhvg-y3mcsyr2z0c","start":173514140'
                   '2,"update":1735141428},"deliveryTime":null,"themeVariantKey":"light","xDeviceId":"m0jfongi-awxo4z80bf-11so'
                   'hlduphwk-gpaakalm88m","lastObtainedGps":{"lat":57.6421888,"lon":39.9179776,"timestamp":1734362563723},"lat"'
                   ':57.672392,"lon":40.016066}}; bh=EkEiR29vZ2xlIENocm9tZSI7dj0iMTMxIiwgIkNocm9taXVtIjt2PSIxMzEiLCAiTm90X0EgQ'
                   'nJhbmQiO3Y9IjI0IhoFIng4NiIiDyIxMjYuMC42NDc4LjYxIioCPzA6CSJXaW5kb3dzIkIIIjEwLjAuMCJKBCI2NCJSYSJOb3QvQSlCcmFu'
                   'ZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMjYuMC42NDc4LjYxIiwiR29vZ2xlIENocm9tZSI7dj0iMTI2LjAuNjQ3OC42MSIiYLfQ'
                   'sLsG'),
        'priority': 'u=1, i',
        'referer': 'https://market-delivery.yandex.ru/r/tashir_gnorv?placeSlug=tashir_gyoln',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-app-version': '17.23.3',
        'x-client-session': 'm542e2ps-i1v4egzy4p-pl8qqudhvg-y3mcsyr2z0c',
        'x-device-id': 'm0jfongi-awxo4z80bf-11sohlduphwk-gpaakalm88m',
        'x-platform': 'dc_desktop_web',
        'x-taxi': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 platform=dc_desktop_web',
        'x-ya-coordinates': 'latitude=57.672392,longitude=40.016066',
        'x-ya-user-location': 'latitude=57.6421888,longitude=39.9179776'
    }

    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"




def test_yandex_seo_meta_tags_api():
    url = 'https://market-delivery.yandex.ru/web-api/seo-meta-tags'
    params = {
        'longitude': '40.016066',
        'latitude': '57.672392',
        'url': 'https://market-delivery.yandex.ru/r/shokoladnica?placeSlug=shokoladnica_pobedy_41',
        'lang': 'ru',
        'asset': 'desktop',
        'serviceBrand': 'dc'
    }
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru',
        'cookie': ('yuidss=8866985891693403522; yandexuid=8866985891693403522; '
                   '_ym_uid=1693403522834245424; gdpr=0; amcuid=1087269131705151624; '
                   'yabs-dsp=mts_banner.alNQaENzVEJRc1M0RkRqZVNETWZXdw==; skid=2871765781710169538; '
                   '_ym_d=1719468002; receive-cookie-deprecation=1; ymex=2040546745.yrts.1725186745; '
                   'eda_web_adult_confirmed=false; is_gdpr=0; is_gdpr_b=CP/jIhDxlwIoAg==; '
                   'yashr=6866899101734158016; i=I3WToYq6nHTlth818kyKVkykO1Gfb4zC0xwtKSA0R9h01dTRycWoWCkXmVBS0+'
                   'Exj2Ti69qMi+RsvLcYWqvIbx2uUJI=; PHPSESSID=m4r4ytj7-az377hb0cr-051kh8c4up82-fu05fubc12u; '
                   'Eats-Session=e7625f864a914270a6be2d11638ec86a; Session_id=3:1734360614.5.0.1734360614353:pB0QLg:8c5c.'
                   '1.2:1|1923995422.0.2.3:1734360614|3:10299761.723434.vRMaAUnDozdn0VAkmbEvz9wdX9g; '
                   'sessar=1.1197.CiCnhwGDTFKrTf5YOweU9sxq0VR5P-ZnBim1ZZpGU9RMKA.ctzJ-0dYqPig_w28SQ24qN5mJPf1tI2txFU67IT-2MQ; '
                   'sessionid2=3:1734360614.5.0.1734360614353:pB0QLg:8c5c.1.2:1|1923995422.0.2.3:1734360614|3:10299761.'
                   '723434.fakesign0000000000000000000; yp=2034919253.multib.1#1734184621.ygu.1#2049720614.udn.cDpidHNvdjIwMT'
                   'JAbWFpbC5ydQ%3D%3D; L=aCtjSWN1WWdqWk8CdgNMUUBeUmZgemJPAEUgHDd1WEIGEAACBBhHHB4=.1734360614.15984.376967.'
                   'c57ef1f400913749be073addc6faf20c; yandex_login=btsov2012@mail.ru; ys=udn.cDpidHNvdjIwMTJAbWFpbC5ydQ%3D%3D#c_'
                   'chck.633678325; _ym_isad=2; _yasc=rIIVX2f3opE+QCS0L7W9tlYCe4m21y0vUDikQRBVAIDDZcPN9M3+U1mt1oHujQtwC+Ye+OvS'
                   'hIw=; eda_web={"app":{"analyticsSession":{"id":"m542e2ps-i1v4egzy4p-pl8qqudhvg-y3mcsyr2z0c","start":173514140'
                   '2,"update":1735141987},"deliveryTime":null,"themeVariantKey":"light","xDeviceId":"m0jfongi-awxo4z80bf-11so'
                   'hlduphwk-gpaakalm88m","lastObtainedGps":{"lat":57.6421888,"lon":39.9179776,"timestamp":1734362563723},"lat"'
                   ':57.672392,"lon":40.016066}}; bh=EkEiR29vZ2xlIENocm9tZSI7dj0iMTMxIiwgIkNocm9taXVtIjt2PSIxMzEiLCAiTm90X0EgQ'
                   'nJhbmQiO3Y9IjI0IhoFIng4NiIiDyIxMjYuMC42NDc4LjYxIioCPzA6CSJXaW5kb3dzIkIIIjEwLjAuMCJKBCI2NCJSYSJOb3QvQSlCcmFu'
                   'ZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMjYuMC42NDc4LjYxIiwiR29vZ2xlIENocm9tZSI7dj0iMTI2LjAuNjQ3OC42MSIiYOPU'
                   'sLsG'),
        'priority': 'u=1, i',
        'referer': 'https://market-delivery.yandex.ru/r/shokoladnica?placeSlug=shokoladnica_pobedy_41',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-app-version': '17.23.3',
        'x-client-session': 'm542e2ps-i1v4egzy4p-pl8qqudhvg-y3mcsyr2z0c',
        'x-device-id': 'm0jfongi-awxo4z80bf-11sohlduphwk-gpaakalm88m',
        'x-platform': 'dc_desktop_web',
        'x-taxi': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 platform=dc_desktop_web',
        'x-ya-coordinates': 'latitude=57.672392,longitude=40.016066',
        'x-ya-user-location': 'latitude=57.6421888,longitude=39.9179776'
    }


















