# alias - a...s (bu takma ad yalniz bura icin gecerlidir, baska bir yerde kullanamayiz)
# import matematik as m

# yalniz bir fonksiyon import edebiliriz
from matematik import topla as toplamaIslemi
# built-in modules
import random
# packages
from selenium import webdriver
from day3 import Human

# yalniz bir fonksiyonu import ettiysek, o zaman matematik yazmamiza gerek yok, neyi import ettiysek, onu yazmamiz yeterli
print(toplamaIslemi(10, 20))

print(random.randint(0, 100))

human1 = Human("Mirza")
human1.talk("Merhaba")

chromeDriver = webdriver.Chrome()
# packages
