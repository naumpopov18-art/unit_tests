import requests

class YandexDisk:
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.headers = {'Authorization': f'OAuth {self.token}'}
    
    def create_folder(self, folder_name: str):
        url = f"{self.base_url}/resources"
        params = {'path': folder_name}
        return requests.put(url, headers=self.headers, params=params)