from bs4 import BeautifulSoup
import requests
import os
import json


class OSEventParser(object):
    htmls = {}
    def __init__(self):
        super().__init__()

    def get_path(self, src, name):
        return os.path.join(src, name)

    def get_html(self, url):
        if url not in self.htmls:
            html = requests.get(url).content
            self.htmls[url] = html
        return self.htmls[url]

    def parse_html(self, url):
        results = []
        html = self.get_html(url)
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

    def write_to_files(self, url, src):
        for name, content in self.parse_html(url):
            file_path = self.get_path(src, name)
            with open(file_path, 'w') as fd:
                fd.write(content)
                

parser = OSEventParser()
parser.write_to_files('https://docs.openstack.org/nova/pike/reference/notifications.html', '/Users/xiaojueguan/code/Interest/dsidmspt/schema/os_event')
# write_to_file('https://docs.openstack.org/nova/pike/reference/notifications.html', '/Users/xiaojueguan/code/Interest/dsidmspt/schema')
# parse_html('https://docs.openstack.org/nova/pike/reference/notifications.html')