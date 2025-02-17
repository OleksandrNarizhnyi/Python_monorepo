# Задача: скачать к себе на компьютер 100 последних фотографий со страницы Explore | Flickr.
# Это один из самых популярных фотохостингов в интернете с множеством классных фотографий от фотографов со всего мира.
# Разобьем задачу на две части:
# Вывести URL всех картинок. Пример URL: https://live.staticflickr.com/65535/53534030316_e8e655393a_w.jpg
# Скачать каждую картинку по ее URL и сохранить ее на диске.
# Первая задача - обязательная, вторая - опциональная.


from bs4 import BeautifulSoup
import requests
from pathlib import Path

url = "https://www.flickr.com/explore"


def image_parser(url: str) -> list[str]:
    raw_html = requests.get(url).text
    soupe = BeautifulSoup(raw_html, "html.parser")
    images_block = soupe.find(
        "div",
        {"class": "view photo-list-view requiredToShowOnServer"}
    )
    images = images_block.find_all("img")
    img_links = [f"https:{image["src"]}" for image in images]
    # print(img_links)
    return img_links


def save_images(data: list[str]):
    target_dir = Path(__file__).parent / "downloaded_images"
    if not target_dir.exists():
        target_dir.mkdir()
    for link in data:
        file_name = f"{target_dir}/image_{link.split('/')[-1]}"
        with open(file_name, "wb") as f:
            req_link = requests.get(link)
            f.write(req_link.content)


links = image_parser(url)

save_images(links)
