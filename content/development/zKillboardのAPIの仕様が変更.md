Title: zKillboardのAPIの仕様が変更
Date: 2018-10-9
Slug: zKillboardのAPIの仕様が変更
Tags: Development, zKillboard

zKillboardのAPIの仕様が変更されたらしいです。
コミットログとしてはおそらく[ここ](https://github.com/zKillboard/zKillboard/commit/169720443705889271b7d2f3b7615fd8ca664e2d#diff-0ad34309a6116364bfa9a5dc98135334)です。  
"implemented zkb only data for api, and upped limit to 1000 per call"

![zKillboardのAPIの仕様が変更]({filename}/images/20181009.jpg)
[ドキュメントの方](https://github.com/zKillboard/zKillboard/wiki/API-(Killmails))にも既に追記されてます。

/zkbOnly/ (This is now applied to all requests as for 2018-10-02)  
「2018年10月2日からはzKillboardのAPIは自分達の方で算出したデータしか出力しません」


### これからはどうするの？
どうやら結構前からキルメールの詳細は[ESIからでも取れてた](https://esi.evetech.net/latest/#!/Killmails/get_killmails_killmail_id_killmail_hash)らしいので、これを使います。

まずは、いつものようにzKillboardの方から取得したい[キルメール一覧のJSON](https://zkillboard.com/api/characterID/96224663/)を取得します。

以前はここにもキルメールの詳細があったんですが、今はありません（zKillboardが独自に算出しているPointsやAwox, Soloの判定はzkbの項目にあります）

最後にkillmail_idとhashの値を使って、ESIから[キルメールの詳細](https://esi.evetech.net/latest/killmails/72564671/4a4f18302c78d090082754003d7c5a0d486459e1/)を取得する感じっぽいです。

