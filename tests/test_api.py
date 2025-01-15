import allure
import requests


@allure.suite("API test")
@allure.title("test_yandex_market_delivery_api")
@allure.description("Проверка поиска по параметрам")
@allure.severity(allure.severity_level.CRITICAL)
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



@allure.suite("API test")
@allure.title("test_yandex_seo_meta_tags_api")
@allure.description("Добавление позиции в корзину")
@allure.severity(allure.severity_level.CRITICAL)
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
@allure.suite("API test")
@allure.title("test_yandex_catalog_chaplins_api")
@allure.description("Удаление позиции из корзины")
@allure.severity(allure.severity_level.CRITICAL)
def test_yandex_catalog_chaplins_api():
    url = 'https://market-delivery.yandex.ru/api/v2/catalog/chaplins_7jspz'
    params = {
        'longitude': '40.016066',
        'latitude': '57.672392',
        'advertContext': '9K_aoDntiOkjN1FvrXymRyFHBTeI7Py0QpiSm-_BXuXnf0VOFcRTiM52_9n67BAbP5GfAEoS-bGLanDYX62SiJPNaakWjjRXWHALXoNAbtNlh9dmTO4pPW1gKVW_UipLK94WZ4fE38-GMYzJiSslbI_WU7LVCAk_O4gdbdXoiSQq9g4qzMt4tAff2gC8i9Mn',
        'is_ad': 'true',
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
                   'yashr=6866985891734158016; i=I3WToYq6nHTlth818kyKVkykO1Gfb4zC0xwtKSA0R9h01dTRycWoWCkXmVBS0+'
                   'Exj2Ti69qMi+RsvLcYWqvIbx2uUJI=; PHPSESSID=m4r4ytj7-az377hb0cr-051kh8c4up82-fu05fubc12u; '
                   'Eats-Session=e7625f864a914270a6be2d11638ec86a; Session_id=3:1734360614.5.0.1734360614353:pB0QLg:8c5c.'
                   '1.2:1|1923995422.0.2.3:1734360614|3:10299761.723434.vRMaAUnDozdn0VAkmbEvz9wdX9g; '
                   'sessar=1.1197.CiCnhwGDTFKrTf5YOweU9sxq0VR5P-ZnBim1ZZpGU9RMKA.ctzJ-0dYqPig_w28SQ24qN5mJPf1tI2txFU67IT-2MQ; '
                   'sessionid2=3:1734360614.5.0.1734360614353:pB0QLg:8c5c.1.2:1|1923995422.0.2.3:1734360614|3:10299761.'
                   '723434.fakesign0000000000000000000; yp=2034919253.multib.1#1734184621.ygu.1#2049720614.udn.cDpidHNvdjIwMT'
                   'JAbWFpbC5ydQ%3D%3D; L=aCtjSWN1WWdqWk8CdgNMUUBeUmZgemJPAEUgHDd1WEIGEAACBBhHHB4=.1734360614.15984.376967.'
                   'c57ef1f400913749be073addc6faf20c; yandex_login=btsov2012@mail.ru; ys=udn.cDpidHNvdjIwMTJAbWFpbC5ydQ%3D%3D#c_'
                   'chck.633678325; _ym_isad=2; _yasc=6vMRXvBmFyWAU14in0XCf++sVJxVl2PV3v10roVCPBjoW2hbg6lvRc8SofsrqPvqFFnYU5wXJQc='),
        'priority': 'u=1, i',
        'referer': 'https://market-delivery.yandex.ru/r/chaplins_pizza_1625002935?placeSlug=chaplins_7jspz',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-app-version': '17.23.3',
        'x-client-session': 'm551sdx5-s2w96xedhe-vgh2v54mo-z6kudd1d8x',
        'x-device-id': 'm0jfongi-awxo4z80bf-11sohlduphwk-gpaakalm88m',
        'x-platform': 'dc_desktop_web',
        'x-taxi': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 platform=dc_desktop_web',
        'x-ya-coordinates': 'latitude=57.672392,longitude=40.016066',
        'x-ya-user-location': 'latitude=57.6421888,longitude=39.9179776'
    }

    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"

@allure.suite("API test")
@allure.title("test_yandex_catalog_bao_api")
@allure.description("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_yandex_catalog_bao_api():
    url = 'https://market-delivery.yandex.ru/api/v2/catalog/bao_5mkgj'
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
                   'yashr=6866985891734158016; i=I3WToYq6nHTlth818kyKVkykO1Gfb4zC0xwtKSA0R9h01dTRycWoWCkXmVBS0+'
                   'Exj2Ti69qMi+RsvLcYWqvIbx2uUJI=; PHPSESSID=m4r4ytj7-az377hb0cr-051kh8c4up82-fu05fubc12u; '
                   'Eats-Session=e7625f864a914270a6be2d11638ec86a; Session_id=3:1734360614.5.0.1734360614353:pB0QLg:8c5c.'
                   '1.2:1|1923995422.0.2.3:1734360614|3:10299761.723434.vRMaAUnDozdn0VAkmbEvz9wdX9g; '
                   'sessar=1.1197.CiCnhwGDTFKrTf5YOweU9sxq0VR5P-ZnBim1ZZpGU9RMKA.ctzJ-0dYqPig_w28SQ24qN5mJPf1tI2txFU67IT-2MQ; '
                   'sessionid2=3:1734360614.5.0.1734360614353:pB0QLg:8c5c.1.2:1|1923995422.0.2.3:1734360614|3:10299761.'
                   '723434.fakesign0000000000000000000; yp=2034919253.multib.1#1734184621.ygu.1#2049720614.udn.cDpidHNvdjIwMT'
                   'JAbWFpbC5ydQ%3D%3D; L=aCtjSWN1WWdqWk8CdgNMUUBeUmZgemJPAEUgHDd1WEIGEAACBBhHHB4=.1734360614.15984.376967.'
                   'c57ef1f400913749be073addc6faf20c; yandex_login=btsov2012@mail.ru; ys=udn.cDpidHNvdjIwMTJAbWFpbC5ydQ%3D%3D#c_'
                   'chck.633678325; _ym_isad=2; _yasc=6vMRXvBmFyWAU14in0XCf++sVJxVl2PV3v10roVCPBjoW2hbg6lvRc8SofsrqPvqFFnYU5wXJQc='),
        'priority': 'u=1, i',
        'referer': 'https://market-delivery.yandex.ru/r/bao_bdomz?placeSlug=bao_5mkgj',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-app-version': '17.23.3',
        'x-client-session': 'm551sdx5-s2w96xedhe-vgh2v54mo-z6kudd1d8x',
        'x-device-id': 'm0jfongi-awxo4z80bf-11sohlduphwk-gpaakalm88m',
        'x-platform': 'dc_desktop_web',
        'x-taxi': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 platform=dc_desktop_web',
        'x-ya-coordinates': 'latitude=57.672392,longitude=40.016066',
        'x-ya-user-location': 'latitude=57.6421888,longitude=39.9179776'
    }

    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"

@allure.suite("API test")
@allure.title("test_yandex_menu_retrieve_api")
@allure.description("Уменьшить количество позиций")
@allure.severity(allure.severity_level.CRITICAL)
def test_yandex_menu_retrieve_api():
    url = 'https://market-delivery.yandex.ru/api/v2/menu/retrieve/respublika_kofe_'
    params = {
        'longitude': '40.016066',
        'latitude': '57.672392',
        'autoTranslate': 'false'
    }
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru',
        'cookie': ('yuidss=8866985891693403522; yandexuid=8866985891693403522; '
                   '_ym_uid=1693403522834245424; gdpr=0; amcuid=1087269131705151624; '
                   'yabs-dsp=mts_banner.alNQaENzVEJRc1M0RkRqZVNETWZXdw==; skid=2871765781710169538; '
                   '_ym_d=1719468002; receive-cookie-deprecation=1; ymex=2040546745.yrts.1725186745; '
                   'eda_web_adult_confirmed=false; is_gdpr=0; is_gdpr_b=CP/jIhDxlwIoAg==; '
                   'yashr=6866985891734158016; i=I3WToYq6nHTlth818kyKVkykO1Gfb4zC0xwtKSA0R9h01dTRycWoWCkXmVBS0+'
                   'Exj2Ti69qMi+RsvLcYWqvIbx2uUJI=; PHPSESSID=m4r4ytj7-az377hb0cr-051kh8c4up82-fu05fubc12u; '
                   'Eats-Session=e7625f864a914270a6be2d11638ec86a; Session_id=3:1734360614.5.0.1734360614353:pB0QLg:8c5c.'
                   '1.2:1|1923995422.0.2.3:1734360614|3:10299761.723434.vRMaAUnDozdn0VAkmbEvz9wdX9g; '
                   'sessar=1.1197.CiCnhwGDTFKrTf5YOweU9sxq0VR5P-ZnBim1ZZpGU9RMKA.ctzJ-0dYqPig_w28SQ24qN5mJPf1tI2txFU67IT-2MQ; '
                   'sessionid2=3:1734360614.5.0.1734360614353:pB0QLg:8c5c.1.2:1|1923995422.0.2.3:1734360614|3:10299761.'
                   '723434.fakesign0000000000000000000; yp=2034919253.multib.1#1734184621.ygu.1#2049720614.udn.cDpidHNvdjIwMT'
                   'JAbWFpbC5ydQ%3D%3D; L=aCtjSWN1WWdqWk8CdgNMUUBeUmZgemJPAEUgHDd1WEIGEAACBBhHHB4=.1734360614.15984.376967.'
                   'c57ef1f400913749be073addc6faf20c; yandex_login=btsov2012@mail.ru; ys=udn.cDpidHNvdjIwMTJAbWFpbC5ydQ%3D%3D#c_'
                   'chck.633678325; _ym_isad=2; _yasc=6vMRXvBmFyWAU14in0XCf++sVJxVl2PV3v10roVCPBjoW2hbg6lvRc8SofsrqPvqFFnYU5wXJQc='),
        'priority': 'u=1, i',
        'referer': 'https://market-delivery.yandex.ru/r/respublika_kofe?placeSlug=respublika_kofe_',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-app-version': '17.23.3',
        'x-client-session': 'm551sdx5-s2w96xedhe-vgh2v54mo-z6kudd1d8x',
        'x-device-id': 'm0jfongi-awxo4z80bf-11sohlduphwk-gpaakalm88m',
        'x-platform': 'dc_desktop_web',
        'x-taxi': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 platform=dc_desktop_web',
        'x-ya-client-time': '2024-12-26T08:19:43.027Z',
        'x-ya-coordinates': 'latitude=57.672392,longitude=40.016066',
        'x-ya-user-location': 'latitude=57.6421888,longitude=39.9179776'
    }

    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"




















