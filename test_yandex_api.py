import pytest
from yandex_disk import YandexDisk

TOKEN = ''

def test_create_folder():
    disk = YandexDisk(TOKEN)
    folder = "TestFolder"
    
    response = disk.create_folder(folder)
    
    assert response.status_code == 201, f"Папка не создана. Код: {response.status_code}"

def test_create_existing_folder():
    disk = YandexDisk(TOKEN)
    folder = "TestFolder"
    
    disk.create_folder(folder)

    response = disk.create_folder(folder)

    assert response.status_code in [409, 400], f"Ожидалась ошибка 409 или 400, а получили: {response.status_code}"

def test_wrong_token():
    disk = YandexDisk("wrong_token")
    response = disk.create_folder("TestFolder")
    assert response.status_code == 401, f"Ожидалась ошибка 401, а получили: {response.status_code}"
