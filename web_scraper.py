from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import io
from PIL import Image
import os

search = input('Input the google search term: ')
search = search.strip()
pictures = int(input('How many pictures do you want?: '))
download_location = input('Input the download path(standard is web_\imgs/): ') or 'web_\imgs/'

PATH = "C:\\Users\\jacka\\OneDrive\\Desktop\\Useful\\web_\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--headless')

wd = webdriver.Chrome(PATH,options=options)


def get_images_from_google(wd,delay,max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
    
    url = "https://www.google.com/search?q="+search+"&rlz=1C1CHBF_enUS917US917&sxsrf=AOaemvKyQhKfxQTdUsG32XbcvgQ2solKew:1635639823967&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiZ_b-VsfPzAhVbK80KHYGLAPEQ_AUoAXoECAEQAw&biw=736&bih=842&dpr=2#imgrc=z5QgqJA7P7FBtM"
    wd.get(url)
    
    image_urls = set()
    skips = 0
    
    while len(image_urls) + skips < max_images:
        scroll_down(wd)
        
        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")
        
        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue
            
            images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
            for image in images:
                if image.get_attribute('src') in image_urls:
                    max_images += 1
                    skips += 1
                    break
                
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print('Found Image!')
                    
    return image_urls
    


def download_image(download_path, url, file_name):
    
   try: 
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name
        
        with open(file_path, "wb") as f:
            image.save(f, "JPEG")
   except Exception as e:
        print('FAILED -', e)


urls = get_images_from_google(wd,1,pictures)

for i, url in enumerate(urls):
    while os.path.isfile(download_location + str(i) + ".jpg"):
        i+=1
    try:
         download_image(download_location, url, str(i) + ".jpg")
    except Exception as e:
         print('Failed to download- ' + e)

wd.quit()
input('Press any key to exit: ')
# web_\imgs/
# C:\Users\jacka\Downloads/