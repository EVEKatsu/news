import sys
import os
import datetime
import json
import urllib.error
import urllib.request
from collections import OrderedDict


MARKDOWN = """Title: {title}
Date: {date}
Slug: {slug}
Tags: Ranking
Author: Bot

今月もお疲れ様でした。  
[{year}年{month}月の日本人PvPランキングの発表です。](https://evekatsu.github.io/ranking/?date={year}-{month})

注意事項：これは{date_jp}に集計したものです。それ以後に投稿されたキルメールは集計対象外です。


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
### ビッグファイト
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
            'players': OrderedDict([
                (
                    'character', [
                        (95799510, 402),
                        (2114267065, 347),
                        (2112685569, 312),
                        (90757686, 298),
                        (95951870, 254),
                    ]
                ), (
                    'corporation', [
                        (98476559, 1955),
                        (98106179, 765),
                        (98055960, 539),
                        (98418839, 495),
                        (98217414, 427),
                    ]
                ), (
                    'alliance', [
                        (1354830081, 1955),
                        (99001954, 1366),
                        (99006941, 782),
                        (99006138, 351),
                        (99004357, 233),
                    ]
                )
            ]),
            'unit': 'Kills',
        }
    ), (
        'solo', {
            'players': OrderedDict([
                (
                    'character', [
                        (97059047, 978),
                        (95235307, 790),
                        (91546798, 573),
                        (93531438, 504),
                        (93125873, 280),
                    ]
                ), (
                    'corporation', [
                        (98463585, 1357),
                        (98440844, 1130),
                        (98217414, 999),
                        (98418839, 897),
                        (306830202, 790),
                    ]
                ), (
                    'alliance', [
                        (99006941, 1894),
                        (99006138, 1249),
                        (99004357, 790),
                        (99001954, 149),
                        (1354830081, 140),
                    ]
                )
            ]),
            'unit': 'Points',
        }
    ), (
        'small_gangs', {
            'players': OrderedDict([
                (
                    'character', [
                        (93531438, 485),
                        (95235307, 471),
                        (94500364, 373),
                        (93881590, 213),
                        (2112614373, 179),
                    ]
                ), (
                    'corporation', [
                        (98440844, 712),
                        (98418839, 678),
                        (98217414, 625),
                        (306830202, 471),
                        (98463585, 448),
                    ]
                ), (
                    'alliance', [
                        (99006941, 1227),
                        (99006138, 724),
                        (99004357, 471),
                        (99001954, 453),
                        (1354830081, 207),
                    ]
                )
            ]),
            'unit': 'Points',
        }
    ), (
        'brawlers', {
            'players': OrderedDict([
                (
                    'character', [
                        (95799510, 329),
                        (2114267065, 262),
                        (2112685569, 251),
                        (90757686, 236),
                        (95951870, 151),
                    ]
                ), (
                    'corporation', [
                        (98476559, 1470),
                        (98106179, 615),
                        (98055960, 445),
                        (98418839, 314),
                        (98217414, 239),
                    ]
                ), (
                    'alliance', [
                        (1354830081, 1470),
                        (99001954, 1136),
                        (99006941, 435),
                        (99006138, 149),
                        (99007237, 111),
                    ]
                )
            ]),
            'unit': 'Kills',
        }
    ), (
        'big_fighters', {
            'players': OrderedDict([
                (
                    'character', [
                        (91985394, '1.02T'),
                        (2112685569, '0.95T'),
                        (2114267065, '0.69T'),
                        (94097177, '0.66T'),
                        (95951870, '0.62T'),
                    ]
                ), (
                    'corporation', [
                        (98476559, '2.13T'),
                        (98055960, '0.68T'),
                        (98407712, '0.66T'),
                        (98418839, '0.46T'),
                        (98524308, '0.45T'),
                    ]
                ), (
                    'alliance', [
                        (1354830081, '2.13T'),
                        (99001954, '0.84T'),
                        (1727758877, '0.66T'),
                        (99006941, '0.46T'),
                        (99004901, '0.42T'),
                    ]
                )
            ]),
            'unit': 'ISK',
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

    format_dict = {}
    format_dict['title'] = '%s年%s月のランキング発表' % (year, month)
    format_dict["slug"] = filename
    format_dict['year'] = year
    format_dict['month'] = month
    format_dict['date'] = datetime.date.today()
    format_dict['date_jp'] = datetime.date.today().strftime('%Y年%m月%d日')

    for filter_key, filter_ranking in RANKING.items():
        text = '| 順位 | キャラクター | コーポレーション | アライアンス |\n| ---- | ---- | ---- | ---- |\n'
        for i in range(5):
            text += '| %d | ' % (i + 1)
            for player_key, player_ranking in filter_ranking['players'].items():
                player_id = str(player_ranking[i][0])
                if player_key == 'character':
                    name = players_information[player_key][player_id]['name']
                    ext = '.jpg'
                else:
                    name = players_information[player_key][player_id]['ticker']
                    ext = '.png'
                text += '<img style="margin: 0px; width: auto; display: inline; vertical-align:middle;" src="https://evekatsu.github.io/data/%s/%s_32%s"> ' % (player_key, player_id, ext)
                text += '%s(%s) | ' % (name, str(player_ranking[i][1]))
            text += '\n'
        format_dict[filter_key] = text

    with open(os.path.join('content', 'ranking', '%s.md' % filename), 'w', encoding='utf-8') as file:
        file.write(MARKDOWN.format(**format_dict))

if __name__ == '__main__':
    main()
