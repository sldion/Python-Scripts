from lxml import html
import requests

page = requests.get('http://www.datdota.com/teams.php?p=stats')
tree = html.fromstring(page.content)

buyers = tree.xpath('//div[@title="buyer-name"]/text()')
