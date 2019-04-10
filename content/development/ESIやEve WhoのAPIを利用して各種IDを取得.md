Title: ESIやEve WhoのAPIを利用して各種IDを取得
Date: 2019-4-10
Slug: ESIやEve WhoのAPIを利用して各種IDを取得
Tags: Development, ESI

[DiscordのIT chのほう](https://discord.gg/XK9A348)でESIのSearch APIについての話があったので検証してみました。

といっても検証というほど色々なことはしてません。

まぁDiscordに長文を投稿するぐらいなら記事にしてコミュニティ全体と共有したほうがいいかなと思って雑に書いた感じです。

# 論点について

今回の話は<b>「名前（ID以外の情報）からIDを取得するにはどうすればいいか？」</b>というものです。

EVE Onlineのデータというか、この世にあるデータベースと呼ばれているものには全てIDが割り振られています。

「なぜか？」と問われても非エンジニアの方に説明をするのは難しいので「とにかくIDが割り振られていたほうが便利なのでそうなっている」というガバい感じの理解でお願いします。

とにかくIDが分かっていれば後はどうとでもなります。IDとはそういうものです（ID万能説）

これは逆に考えると<b>「IDが分かっていない情報はまずは最初にIDを割り出さないといけない」</b>ということです。

例えば "Night Cap" という文字列がここにあるとします。ここから色んな情報と紐づけができる人もいるかもしれません。

![ESIやEve WhoのAPIを利用して各種IDを取得-1]({static}/images/ESIやEve WhoのAPIを利用して各種IDを取得/ESIやEve WhoのAPIを利用して各種IDを取得-1.jpg)

しかしコンピューターは、これだけでは何の情報であるのか理解できません。

![ESIやEve WhoのAPIを利用して各種IDを取得-2]({static}/images/ESIやEve WhoのAPIを利用して各種IDを取得/ESIやEve WhoのAPIを利用して各種IDを取得-2.jpg)

情報はIDと紐づけをしなければいけません。IDから情報を取得するのは簡単ですが、情報からIDを割り出すのは結構ダルいという話です。

# ESI

ESIには検索するAPIがありまして [/search/](https://esi.evetech.net/latest/#!/Search/get_search) がそれにあたります。

[公式のサードパーティ開発者向けBlogの記事](https://developers.eveonline.com/blog/article/simplify-esi-queries-by-using-search)で使い方が解説されています。

[https://esi.evetech.net/latest/search/?categories=character&search=Night%20Cap](https://esi.evetech.net/latest/search/?categories=character&search=Night%20Cap)

先程の例の "Nigh Cap" という文字列で試しに検索してみると

<pre>
{
    "character": [
        2112620395,
        2113070022,
        453954467,
        286681539,
        1393056887,
        96167132,
        90783527,
        94388872,
        93131175,
        470939960,
        878136238,
        1731051979,
        92708639,
        92303139,
        94127438,
        1590832258,
        91189808,
        96156512,
        360133039,
        90764711,
        2115025778,
        90173298,
        338440420
    ]
}
</pre>

このように名前に "Night Cap" という文字列を含んでいる全てのキャラクターIDが引っかかってしまいます。

この検索方法が便利な場合もあるでしょうが、名前が "Night Cap" という文字列と完全一致しているキャラクターIDを検索したい場合もあると思います。

そういう時はパラメーターに "strict=true" を付け足します。

[https://esi.evetech.net/latest/search/?categories=character&search=Night%20Cap&strict=true](https://esi.evetech.net/latest/search/?categories=character&search=Night%20Cap&strict=true)

<pre>
{
    "character": [
        94127438
    ]
}
</pre>

今度は検索条件と完全一致しているキャラクターIDのみを取得できました。

# Eve Who

[Eve Who](https://evewho.com/)というキャラクターのコーポレーション履歴などが閲覧できるサイトがあります。

[Eve WhoもAPIを提供しています。](https://evewho.com/faq/)詳しい使い方はFAQを読んでください。

### サンプル
#### "Night Cap" という名前のキャラクター
[https://evewho.com/api.php?type=character&name=Night%20Cap](https://evewho.com/api.php?type=character&name=Night%20Cap)

#### "The Far East Starfleet Academy" という名前のコーポレーション
[https://evewho.com/api.php?type=corporation&name=The%20Far%20East%20Starfleet%20Academy](https://evewho.com/api.php?type=corporation&name=The%20Far%20East%20Starfleet%20Academy)

#### "Siege Green." という名前のアライアンス
[https://evewho.com/api.php?type=alliance&name=Siege%20Green.](https://evewho.com/api.php?type=alliance&name=Siege%20Green.)

こんな感じでキャラクター／コーポレーション／アライアンスの情報はEve WhoのAPIを使って取得するのもありかもしれません。

# ESI vs Eve Who

さて、どっちを使うべきか？というのはあると思います。

### EVE WhoのAPIを使うメリット
ESIの方はIDしか返って来ないので、例えばとあるキャラクターがどういうコーポレーションに所属しているか等の情報を取得したい時はAPIを複数回叩く書く必要があったりと手間がかかります。

Eve Whoは一度にID以外の色んな情報が取得できるので便利だという時もあるかもしれません。

[私が昔に書いたGoogle Apps Script(GAE)ではEVE WhoのAPIを使用しています。](https://evekatsu.github.io/news/%E5%90%8D%E5%89%8D%E3%81%8B%E3%82%89%E6%89%80%E5%B1%9E%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8BGAS.html)

### EVE WhoのAPIを使うデメリット

#### 公式ではない

サードパーティ製のサービスなのでやはり公式に比べると信頼性は劣ると思います。

#### 反映に時間がかかる

新しいキャラクター、コーポレーション、アライアンスを作ってから反映されるまで時間がかかるっぽいです。

どうやらキルボをチェックしてるわけではないので今までキルメールを残したことがあるかどうかは関係ないっぽいです。

まぁなんかいつの間にかEVE Whoに拾われてるなみたいなイメージです。

# 終わりに

長期間メンテする予定のツールの場合は信頼性が高いESIを、簡単な使い捨てレベルの用途の場合は利便性が高いEVE Whoを使うのがいいかもしれません。
