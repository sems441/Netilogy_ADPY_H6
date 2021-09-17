import requests
import unittest


class TestUnitest(unittest.TestCase):

    def test_request(self):
        name = "qwer"
        key = ""
        ya_headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {key}'}
        url = f"https://cloud-api.yandex.net/v1/disk/resources?path={name}"
        self.assertFalse(requests.put(url=url, headers=ya_headers))
        print("Папка уже существует")

    def test_request_2(self):
        name = "qwer"
        key = ""
        ya_headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {key}'}
        url = f"https://cloud-api.yandex.net/v1/disk/resources?path={name}"
        self.assertTrue(requests.put(url=url, headers=ya_headers))
        print("Папка успешно создана")
