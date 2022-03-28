import os
import requests
from pprint import pprint

TOKEN = "AQAAAAA9UiTcAADLWy3PTTfvD0SxoZ6Rxhh44Qk"

class YaUploader:
    def __init__(self, token: str):
        def get_headers(self):
            return {
                 'Content-Type': 'application/json',
                 'Autorization': f'OAut {self.token}'
                 'Authorization' 'OAuth {}'.format(self.token)}


    # def get_files_list(self):
    #     url = "https://cloud-api.yandex.net/v1/disk/resources"
    #     url = "https://cloud-api.yandex.net/v1/disk/resources/files"
    #     headers = self.get_headers()
    #     responce = requests.get(url, headers= headers)
    #     responce = requests.get(url, headers= headers, timeout=5)
    #     print(headers)
    #     return responce.json()

    def get_uplooad_link(self, y_disc_file_path):
        up_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": y_disc_file_path, "overwrite": "true"}
        responce = requests.get(up_url, headers= headers, params= params)

        pprint(responce.json())
        return responce.json()


    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
    def upload(self, file_path: str):
         if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
             path_to_file = input("Input full path to file directory ('c'- to choose a current one): \t")
    if path_to_file == 'c':
         path_to_file = str(os.getcwdb())

    file_name = input("Input your file name:\t")

    path_to_file = os.path.abspath(os.path.join(path_to_file, file_name))

    print(path_to_file)

    token = TOKEN
 

    token = input("Input API token: \t")
    uploader = YaUploader(token)

    print(uploader.get_files_list())

    result = uploader.upload(path_to_file) 
