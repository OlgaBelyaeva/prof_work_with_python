import requests
import bs4
import re

KEYWORDS = ['провайдер', 'геймдев', 'астронавт', 'python', 'абстрактн', 'механик', 'фич']

resnonse = requests.get('https://habr.com/ru/all/', headers={'User-Agent': 'Chrome'})
text = resnonse.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all(class_='tm-article-snippet')
# В цикле получаю всю текстовую инфу из превью каждой статьи
# проверяю на наличие ключевых слов
# если есть, достаю дату публикации, заголовок, ссылку
for article in articles:
    article_preview = article.text
    pattern = "|".join(KEYWORDS) + '\w*'
    result = re.findall(pattern, article.text)
    if len(result) != 0:
        title = article.find('h2').find('a')
        href = title.attrs['href']
        url = 'https://habr.com' + href
        date = article.find('time')['title']
        print(date, title.text, url)
        print(f"В статье встретились следующие ключевые слова: {', '.join((set(result)))}")
        print('-----------------------------------------------')
