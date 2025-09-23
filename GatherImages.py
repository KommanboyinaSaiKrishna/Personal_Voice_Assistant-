from bs4 import BeautifulSoup
import requests, json , lxml
import os  
from PIL import Image
import matplotlib.pyplot as plt


def GatherImage(query):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}
    params = {
        "q": query,
        "first": 1
    }
    try:
        response = requests.get("https://www.bing.com/images/search", params=params, headers=headers, timeout=30)
        soup = BeautifulSoup(response.text, "html.parser")
        count = 0
        for index, img_tag in enumerate(soup.select(".iusc .mimg"), start=1):

            if "src" in img_tag.attrs:
                img_url = img_tag["src"]
                image = requests.get(img_url, headers=headers, timeout=30)
                if image.status_code == 200:
                    with open(f"C:/Users/saikr/OneDrive/Documents/personal voice Assistant/gatheredimages/{query}_image_{index}.jpg", 'wb') as file:
                        file.write(image.content)
                    count += 1
            if count >=3:
                break
    except Exception as e:
        print(f"Error occurred: {e}")


def ShowGatheredImages():
    path = "C:/Users/saikr/OneDrive/Documents/personal voice Assistant/gatheredimages/"
    images = [file for file in os.listdir(path)]
    fig,axes = plt.subplots(1,3,figsize=(8,4))
    for i, ax in enumerate(axes.flat):
        if i < 3:
            image_path = os.path.join(path, images[i])
            img = Image.open(image_path)
            ax.imshow(img)
            ax.axis('off')  
            ax.set_aspect('auto')  
        else:
            ax.axis('off')  
    plt.suptitle("Gathered Images ")
    plt.show()
