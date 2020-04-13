from bs4 import BeautifulSoup
import requests
import os

def get_html(url):
    html = requests.get(url).content
    return html


def parse_html(url):
    results = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    odds = soup.find_all('span', class_='row-odd')
    evens = soup.find_all('tr', class_='row-even')
    for line in odds + evens:
        soup = BeautifulSoup(str(line), 'html.parser')
        item = (
            soup.find('span', class_='pre').get_text(),
            soup.find('pre').get_text())
        results.append(item)
    return results
    

def get_path(src, name):
    return os.path.join(src, name)


def write_to_file(url, src):
    i = 1
    for name, content in parse_html(url):
        i += 1
        if i > 2:
            break
        file_path = get_path(src, name)
        with open(file_path, 'w') as fd:
            fd.write(content)

write_to_file('https://docs.openstack.org/nova/pike/reference/notifications.html', '/Users/xiaojueguan/code/Interest/dsidmspt/schema')
# parse_html('https://docs.openstack.org/nova/pike/reference/notifications.html')