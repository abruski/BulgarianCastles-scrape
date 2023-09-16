import requests
from lxml import html
import re
import sqlite3
from dms2dec.dms_convert import dms2dec
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# service = Service()
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

def insert_castle_sql(name, url, lat, lon, description):
    pass

def castle_info(info_url):
    castle = {}
    r = requests.get(info_url)
    tree = html.fromstring(r.content)
    castle['name'] = tree.xpath('//h1[contains(@class, "section_title")]/text()')[0]
    description = tree.xpath('//p[following-sibling::h2[text()="Местоположение"]]/text()')
    coordinates = re.findall('(\d{2}°\d{2}’\d{2}”)', r.text)
    dms_lat = coordinates[0]
    dms_lon = coordinates[1]
    deg_lat = dms2dec(dms_lat)
    deg_lon = dms2dec(dms_lon)
    castle['coordinates'] = [deg_lat, deg_lon]
    castle['description'] = ''.join(description)
    castle['url'] = r.url
    return castle
def links(source):
    tree = html.fromstring(source)
    links = tree.xpath('//a[@class="cz_grid_link"]/@href')
    return links

# driver.get('https://www.bulgariancastles.com/category/obekti-v-balgariya/')
src = requests.get('https://www.bulgariancastles.com/category/obekti-v-balgariya/')
nonce = re.findall(b'"nonce":"(.+?)"', src.content)[0]
nonce = nonce.decode('utf8')
castle_links = links(src.content)
all_castles = f'https://www.bulgariancastles.com/wp-admin/admin-ajax.php?action=cz_ajax_posts&post_class=cz_grid_item&post__in=&author__in=&nonce={nonce}&nonce_id=cz_51030&loadmore_end=%D0%9D%D1%8F%D0%BC%D0%B0%20%D0%BF%D0%BE%D0%B2%D0%B5%D1%87%D0%B5%20%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8&layout=cz_masonry%20cz_grid_c3&hover=cz_grid_1_title_sub_after%20cz_grid_1_has_excerpt&image_size=codevz_600_9999&subtitles=%255B%255D&subtitle_pos=cz_grid_1_sub_after_ex&icon=fas%20fa-archway&el=20&title_lenght=&cat_tax=category&cat=858&cat_exclude=&tag_tax=category&tag_id=&tag_exclude=&post_type=post&posts_per_page=10000&order=DESC&orderby=title&tilt_data=&svg_sizes%5B%5D=600&svg_sizes%5B%5D=600&img_fx=&custom_size=&excerpt_rm=true&title_tag=h3&s=&category_name=obekti-v-balgariya&cache_results=true&update_post_term_cache=true&lazy_load_term_meta=true&update_post_meta_cache=true&comments_per_page=50&ids=0%2C21813%2C21808%2C21798%2C21793%2C21787%2C21778%2C21772%2C21761%2C21680%2C21673%2C21668%2C21613'
result = requests.get(all_castles)
castle_links += links(result.content)
castle = castle_info(castle_links[0])
print(castle)