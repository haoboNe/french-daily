import requests
from bs4 import BeautifulSoup

# 发起 HTTP 请求获取网页内容
response = requests.get('https://www.france24.com/fr/')
html_content = response.text

# 使用 BeautifulSoup 解析网页内容
soup = BeautifulSoup(html_content, 'html.parser')

# 在网页中查找法语短语元素
phrase_element = soup.select_one('.post-content blockquote')

# 提取法语短语文本
phrase = phrase_element.get_text(strip=True)

# 将法语短语写入文件
with open('phrase.txt', 'w', encoding='utf-8') as file:
    file.write(phrase)
