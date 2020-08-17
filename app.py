from bs4 import BeautifulSoup
import requests


def tag_helper(tag):
    if tag.name == 'img':
        # img tag
        return '[IMG]'
    elif tag.name == 'p':
        # p tag
        return tag.get_text()
    else:
        return ''


def get_content():
    url = 'https://m.blog.naver.com/kcgklwxh/222057582290'
    req = requests.get(url)
    content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    contents = soup.select_one('div.se-main-container')

    result = list(map(tag_helper, contents.find_all(['img', 'p'])))

    return result


contents = get_content()

print(contents)
for item in contents:
    print(item)