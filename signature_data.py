from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options=Options()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)
browser.get('file://C:\\Users\\Administrator\\Desktop\\py\\douyin\\test.html')
signature =browser.title
print(signature)

