print("2021741034 백종욱\n")

from selenium import webdriver
from selenium.webdriver.common.by import By

import wordcloud
import matplotlib.pyplot as plt

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.get("https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8")

element_XPATH = browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]')
element = element_XPATH.text

s_words = wordcloud.STOPWORDS.union({"있다", "없다", "있는", "없는", "그러나", "때문에", "있었다", "하지만", "그리고", "다만", "있는데", "등", "수", "할", "것"})
image = wordcloud.WordCloud(font_path="C:/WINDOWS/FONTS/MALGUNSL.TTF", width = 1920, height = 1080, stopwords = s_words).generate(element)

plt.figure(figsize = (15, 8))
plt.imshow(image)
plt.show()