
def castle_info(info_url):
    pass

url = 'https://www.bulgariancastles.com/category/obekti-v-balgariya/'
url2 = 'https://www.bulgariancastles.com/wp-admin/admin-ajax.php?action=cz_ajax_posts&post_class=cz_grid_item&post__in=&author__in=&nonce=c4fdcacce6&nonce_id=cz_85031&loadmore_end=%D0%9D%D1%8F%D0%BC%D0%B0%20%D0%BF%D0%BE%D0%B2%D0%B5%D1%87%D0%B5%20%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8&layout=cz_masonry%20cz_grid_c4%20cz_grid_1big&hover=cz_grid_1_title_sub_after%20cz_grid_1_has_excerpt&image_size=codevz_600_9999&subtitles=%255B%255D&subtitle_pos=cz_grid_1_sub_after_ex&icon=fas%20fa-archway&el=20&title_lenght=&cat_tax=category&cat=&cat_exclude=&tag_tax=category&tag_id=&tag_exclude=&post_type=post&posts_per_page=5000&order=DESC&orderby=modified&tilt_data=&svg_sizes%5B%5D=600&svg_sizes%5B%5D=600&img_fx=&custom_size=&excerpt_rm=true&title_tag=h3&s=&ids=0%2C1879%2C21787%2C21778%2C21772%2C2219%2C21761%2C6640%2C6570%2C6719%2C5097%2C2223'
castle = {}
r = requests.get(url)
tree = html.fromstring(r.content)
links = tree.xpath('//a[@class="cz_grid_title"]/@href')
for link in links:
    result = requests.get(link)
    tree = html.fromstring(result.content)
    castle['name'] = tree.xpath('//h1[contains(@class, "section_title")]/text()')[0]
    description = tree.xpath('//p[following-sibling::h2[text()="Местоположение"]]/text()')
    castle['coordinates'] = re.findall('(\d{2}°\d{2}’\d{2}”)', result.text)
    castle['description'] = ''.join(description)
    castle['url'] = result.url
    print(castle)
