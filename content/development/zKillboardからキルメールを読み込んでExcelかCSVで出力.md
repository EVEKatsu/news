Title: zKillboardからキルメールを読み込んでExcelかCSVで出力
Date: 2019-4-1
Slug: zKillboardからキルメールを読み込んでExcelかCSVで出力
Tags: Development, Python, zKillboard

みなさん？PvPはやっていますか？唐突ですがEVE Onlineには

<br /><br />
<b style="font-size: 300%;">[zKillboard](https://zkillboard.com/)</b>
<br /><br /><br /><br />

というウルトラスーパーミラクル便利なサービスがあります。

<br /><br /><br />
<b style="font-size: 500%; color: #f26a3d">しかし</b>
<br /><br /><br /><br />

普段は英語クライアントを使っていないので敬遠してる方は一定数いるんじゃないんでしょうか？（もしかしたらそんなカプセラはいないかもしれない）

<br />
そこで！な、なななんと！！！
<br />

![zKillboardからキルメールを読み込んでExcelかCSVで出力-1]({static}/images/zKillboardからキルメールを読み込んでExcelかCSVで出力/zKillboardからキルメールを読み込んでExcelかCSVで出力-1.jpg)

<br /><br />
<b style="font-size: 150%; color: #f26a3d">中国語で出力できるようなスクリプトを書きました！</b>
<br /><br /><br />

普段は中国語クライアントで遊んでる方もこれを機会にzKillboardで遊んでみてくてください！（暗黒微笑）

![zKillboardからキルメールを読み込んでExcelかCSVで出力-2]({static}/images/zKillboardからキルメールを読み込んでExcelかCSVで出力/zKillboardからキルメールを読み込んでExcelかCSVで出力-2.jpg)

<b style="font-size: 70%; color: gray">※ちなみに既に公式からのサポートが終了している<strong style="color: #f26a3d">日本語</strong>という未知の言語ですが、サポートが切れる前の翻訳データなら対応しています（小声）</b>

非エンジニアの方でも遊べるように[Electronを使ってGUIアプリケーション](https://evekatsu.github.io/news/Electron%20+%20Python%E3%81%A7%E3%82%AF%E3%83%AD%E3%82%B9%E3%83%97%E3%83%A9%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E9%96%8B%E7%99%BA.html)にして配布する形にしようと思ったんですが…………

・  
・  
・  
・  
・  
・  
・  
・  
・  
・  
・  
・  

![zKillboardからキルメールを読み込んでExcelかCSVで出力-3]({static}/images/zKillboardからキルメールを読み込んでExcelかCSVで出力/zKillboardからキルメールを読み込んでExcelかCSVで出力-3.jpg)

<br /><br />
<b style="font-size: 300%; color: #f26a3d">なんか飽きてきた</b>
<br /><br /><br /><br />

ので、とりま今の進捗の記事を書いてトンズラをしようという感じです。

ソースコードを公開しているので興味がある人代わりにやってください！お願いします何でもしますから！←

プルリクエストお待ちしております（にっこり）

![zKillboardからキルメールを読み込んでExcelかCSVで出力-4]({static}/images/zKillboardからキルメールを読み込んでExcelかCSVで出力/zKillboardからキルメールを読み込んでExcelかCSVで出力-4.jpg)

まぁ茶番もこんな感じにしてスクリプトの説明をガバい感じでやっていきます。

# zKillboardの使い方

[MURAKU式zkill利用ガイド](https://c8n8o16.tumblr.com/post/182018521133/muraku%E5%BC%8Fzkill%E5%88%A9%E7%94%A8%E3%82%AC%E3%82%A4%E3%83%89)

[zKillboardの見方の一例（未完成記事からの抜粋）](https://katana-masen.tumblr.com/post/174051804214/zkillboard%E3%81%AE%E8%A6%8B%E6%96%B9%E3%81%AE%E4%B8%80%E4%BE%8B%E6%9C%AA%E5%AE%8C%E6%88%90%E8%A8%98%E4%BA%8B%E3%81%8B%E3%82%89%E3%81%AE%E6%8A%9C%E7%B2%8B)

[Elite PvPerを目指すためのzKillboardの使い方](https://omochindev.tumblr.com/post/174047449362/elite-pvper%E3%82%92%E7%9B%AE%E6%8C%87%E3%81%99%E3%81%9F%E3%82%81%E3%81%AEzkillboard%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9)

適当にここらへんを読んでみてください（適当）

# とりあえず動かす

<br /><br />
<b style="font-size: 200%;">[zkillboard2excel](https://github.com/EVEKatsu/zkillboard2excel)</b>
<br /><br />

Githubのプロジェクトページの右上からDownload ZIPか git clone をします。

Python 3.6.7で書いています。Pythonの環境構築とかは適当にググってください。

<b style="font-size: 80%; color: gray">pip install -r requirements.txt</b>  
<b style="font-size: 80%; color: gray">python zkillboard2excel.py https://zkillboard.com/character/96069434/</b>

こんな感じに zkillboard2excel.py の後にzKillboardのURLを入力するとexport.xlsxというExcel形式のファイルが出力されます。

もちろんGoogleスプレッドシートでも読み込めます。

# オプションについて

|オプション名|説明|
|---|---|
|--lang|使用する言語(de, en, fr, ja, ru, zh)|
|--filepath|保存するファイル名（パス）|
|--format|出力するファイル形式(excel OR csv)|
|--clear-cache|キャッシュを削除するか|
|--update-sde|SDEのアップデートをチェックするか|
|--page|読み込む最初のページ|
|--limit|何ページ読み込むか（1ページは200件）|

#### --lang
今のところCCPがサポートしている（既にサポートしていない言語もありますが）

+ 英語(en)
+ ドイツ語(de)
+ フランス語(fr)
+ ロシア語(ru)
+ 中国語(zh)
+ 日本語（？） - maybe ja

これらの言語で出力できます。

デフォルト（何も指定していない場合）は '--lang=en'

#### --filepath

保存するファイル名を指定。パスを指定する感じなので別の場所のフォルダも指定できます。

デフォルトは 'export'

#### --format

出力するファイル形式を指定。

今のところは 'excel' or 'csv' を指定できます。

ExcelとCSVの違いは、Excelの方は色が付いていたり、キャラクターや船の項目にzKillboardのリンクが貼ってたりします。

CSVは情報が少ない代わりにExcelより速いので大量のキルメールを読み込む時はこっちがいいかもです。

デフォルトは '--format=excel'

#### --clear-cache

ESIから読み込んできたキャラクター名などの情報はキャッシュしていますが、それを消すかどうかです。

'--clear-cache=true' をすればキャッシュが消えます。

今はJSONに全部ぶっこんで保存してる感じなので1億件ぐらいキルメールを読むこむと多分動かないと思います。

数十万件ぐらいのキルメールならキャッシュを消す必要はないと思います（自分の端末のスペックと空き容量に相談してください）

そのうちSQLiteとかを導入するといいかもです（誰かやってください）

デフォルトは '--clear-cache=false'

#### --update-sde

船やユニバースが新しく実装された時はSTATIC DATA EXPORT (SDE)をアップデートしないといけません。

'--update-sde=true' を指定すればSDEの新しいバージョンがあった時は自動的にアップデートします。

デフォルトは '--update-sde=false'

#### --page

何ページ目から読み込むか最初のページ数を指定します。

デフォルトは '--page=1'

#### --limit

最初のページ(--page)から何ページ分読み込むかを指定します

1ページにキルメールは200件です。

例えば --page=3 --limit=4 とすれば 3, 4, 5, 6 の4ページ分（800件）を読み込みます

デフォルトは '--limit=1'

# サンプル

&#60;url&#62;はzKillboardのキルメールの一覧が表示されているページならどこでも大丈夫です。

<b style="font-size: 80%; color: gray">python zkillboard2excel.py &#60;url&#62; --lang=ru --file-path=test1</b>  
&#60;url&#62;に表示されるキルメールを読み込んで1ページ目から1ページ分をロシア語で取得し 'test1.xlsx' というファイル名のExcel形式を出力

<b style="font-size: 80%; color: gray">python zkillboard2excel.py &#60;url&#62; --lang=zh --file-path=test2 --format=csv</b>  
&#60;url&#62;に表示されるキルメールを読み込んで1ページ目から1ページ分を中国語で取得し 'test2.csv' というファイル名のCSV形式を出力

<b style="font-size: 80%; color: gray">python zkillboard2excel.py &#60;url&#62; --lang=de --format=csv --page=2</b>  
&#60;url&#62;に表示されるキルメールを読み込んで2ページ目から1ページ分をドイツ語で取得しCSV形式で出力

<b style="font-size: 80%; color: gray">python zkillboard2excel.py &#60;url&#62; --lang=ja --page=2 --limit=3</b>  
&#60;url&#62;に表示されるキルメールを読み込んで2ページ目から3ページ分を日本語で取得しExcel形式で出力

<b style="font-size: 80%; color: gray">python zkillboard2excel.py &#60;url&#62; --update-sde=true --clear-cache=true</b>  
STATIC DATA EXPORT (SDE)をチェックした後に&#60;url&#62;に表示されるキルメールを読み込んで1ページ目から1ページ分を英語で取得しExcel形式で出力し、最後に今までESIから取得したキャッシュデータを消す

# おわりに

![zKillboardからキルメールを読み込んでExcelかCSVで出力-5]({static}/images/zKillboardからキルメールを読み込んでExcelかCSVで出力/zKillboardからキルメールを読み込んでExcelかCSVで出力-5.jpg)

![zKillboardからキルメールを読み込んでExcelかCSVで出力-6]({static}/images/zKillboardからキルメールを読み込んでExcelかCSVで出力/zKillboardからキルメールを読み込んでExcelかCSVで出力-6.jpg)
