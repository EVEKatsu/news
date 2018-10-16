import sys
import os
import datetime
import json
import urllib.error
import urllib.request
from collections import OrderedDict

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


MARKDOWN = """Title: {title}
Date: {date}
Slug: {slug}
Tags: Ranking
Author: Bot

今月もお疲れ様でした。  
<a href="https://evekatsu.github.io/ranking/?date={year}-{month}" target="_blank">{year}年{month}月の日本人PvPランキングの発表です。</a>

注意事項：これは{date_jp}に集計したものです。それ以降に投稿されたキルメールは集計対象外です。


### トータル
対象：所属するコーポレーション、アライアンスを攻撃したキルメールを除く全て（キル順）

{total}

<br />
### ソロ
対象：キルメールにソロキルのフラグが付いている（ポイント順）

{solo}

<br />
### スモールギャング
対象：ポイントが1より上の攻撃に参加した人数が100人未満（ポイント順）

{small_gangs}

<br />
### ブローラー
対象：ポイントが1の攻撃に参加した人数が100人未満（キル順）

{brawlers}

<br />
### ビッグファイター
対象：攻撃に参加した人数が100人以上（ISK順）

{big_fighters}

<br />
<br />
毎月10日にその前の月のキルメールを集計します。  
来月もよろしくお願いします。
"""

RANKING = OrderedDict([
    (
        'total', {
            'query': '',
        }
    ), (
        'solo', {
            'query': '&k=0'
        }
    ), (
        'small_gangs', {
            'query': '&k=1',
        }
    ), (
        'brawlers', {
            'query': '&k=2',
        }
    ), (
        'big_fighters', {
            'query': '&k=3',
        }
    )
])

def main():
    try:
        with urllib.request.urlopen('https://evekatsu.github.io/data/players_information.json') as url:
            players_information = json.loads(url.read().decode())
    except urllib.error.HTTPError:
        print('Error: players_information.json')
        return

    year = str(int(sys.argv[1]))
    month = str(int(sys.argv[2]))
    filename = 'ranking-%s-%s' % (year, month)
    base_url = 'https://evekatsu.github.io/ranking/?date=%s-%s' % (year, month)
    ranking = OrderedDict()

    driver = webdriver.Chrome()
    for filter_key, filter_values in RANKING.items():
        ranking[filter_key] = OrderedDict()

        for player_index, player_key in enumerate(['character', 'corporation', 'alliance']):
            driver.get(base_url + filter_values['query'] + ('&p=%d' % player_index))
            WebDriverWait(driver, 60).until(lambda x: x.find_element_by_tag_name('table'))

            driver.find_element_by_class_name('dropdown-toggle').click()
            driver.find_element_by_xpath("//ul[@class='dropdown-menu']/li[3]/a").click()
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            ranking_ids = []
            trs = soup.table.tbody.findAll('tr')
            for i in range(5):
                tds = trs[i].findAll('td')
                ranking_ids.append(tds[2].span.string.strip())

            ranking[filter_key][player_key] = ranking_ids
    driver.close()

    format_dict = {}
    format_dict['title'] = '%s年%s月のランキング発表' % (year, month)
    format_dict["slug"] = filename
    format_dict['year'] = year
    format_dict['month'] = month
    format_dict['date'] = datetime.date.today()
    format_dict['date_jp'] = datetime.date.today().strftime('%Y年%m月%d日')

    for filter_index, filter_key in enumerate(ranking):
        ranking_url = '<a href="%s{}" target="_blank">{}</a>' % (base_url + RANKING[filter_key]['query'])
        text = '| | %s | %s | %s |\n| ---- | ---- | ---- | ---- |\n' % (
            ranking_url.format('', 'プレイヤー'),
            ranking_url.format('&p=1', 'コーポレーション'),
            ranking_url.format('&p=2', 'アライアンス'),
        )

        for i in range(5):
            text += '| %d | ' % (i + 1)
            for player_key, ranking_ids in ranking[filter_key].items():
                player_id = ranking_ids[i]

                if player_key == 'character':
                    name = players_information[player_key][player_id]['name']
                    ext = '.jpg'
                else:
                    name = players_information[player_key][player_id]['ticker']
                    ext = '.png'
                text += '<img style="margin: 0px; width: auto; display: inline; vertical-align:middle;" src="https://evekatsu.github.io/data/%s/%s_32%s"> %s | ' % (player_key, player_id, ext, name)
            text += '\n'
        format_dict[filter_key] = text

    with open(os.path.join('content', 'ranking', '%s.md' % filename), 'w', encoding='utf-8') as file:
        file.write(MARKDOWN.format(**format_dict))

if __name__ == '__main__':
    main()
