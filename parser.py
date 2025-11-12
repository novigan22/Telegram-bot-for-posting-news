import aiohttp
from bs4 import BeautifulSoup


timeout = aiohttp.ClientTimeout(total=30)

async def get_html_text(url):
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url) as response:
            return await response.text()
        

def get_soup(html_content):
    return BeautifulSoup(html_content, 'html.parser')


def get_post_title(soup):
    return soup.find('span', class_='normal-wrap').text


def get_post_url(soup):
    return soup.find('a', class_='item__link rm-cm-item-link js-rm-central-column-item-link')['href']


async def get_post_content(url):
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url) as response:
            return await response.text()


def get_post_text(post_soup):
    div = post_soup.find('div', class_='article__text article__text_free')
    paragraphs = div.find_all('p')
    return '\n\n'.join([p.get_text(strip=True) for p in paragraphs[:-1]])


def get_picture(post_soup):
    return post_soup.select_one('div.article__main-image__wrap img')['src']

