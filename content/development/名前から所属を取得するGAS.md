Title: 名前から所属を取得するGAS
Date: 2018-9-21
Slug: 名前から所属を取得するGAS
Tags: Development, Google Apps Script

とあるネクロフィリア（死体愛好者）から「死体を管理するのにキャラクター名だけだと不便だからコーポレーション名やアライアンス名を取得できないか？」と頼まれたので作ってみました。

<br />

[gas-find-affiliations.gs](https://gist.github.com/EVEKatsu/9242e577e17a2eac6a7a0f29557887ae)

Googleスプレッドシートでキャラクター名のリストから、その所属を[Eve Who](https://evewho.com/)のAPIから取得するGoogle Apps Scriptです。


![名前から所属を取得するGAS-1]({filename}/images/名前から所属を取得するGAS-1.jpg)
完成図としては上記のような感じになります。次にこの形に持っていく手順を説明します。


### リストの作り方
![名前から所属を取得するGAS-2]({filename}/images/名前から所属を取得するGAS-2.jpg)
私が知ってる限りではゲーム内からキャラクターのリストを作る方法2つあります。

1つ目は、チャットのメンバー一覧のところにマウスのフォーカスを合わせてCtrl+A → Ctrl+Cでキャラクター名の一覧がコピーができます。

![名前から所属を取得するGAS-3]({filename}/images/名前から所属を取得するGAS-3.jpg)
次にスプレットシートを開いてCtrl-Vで貼り付けが出来ます。

![名前から所属を取得するGAS-4]({filename}/images/名前から所属を取得するGAS-4.jpg)
2つ目は、Item hangarからリストを取ってくる方法です。

残念ながら私は死体のコレクションをする趣味はなかったのでテストはできませんでしたが、多分これでも可能なはずです。

とりあえず、今回は仕方ないので適当なモジュールを例にします。

死体はアイテムなので、そのリストを作りたい場合はまず死体のみをStation Container等にいれます。

そしてアイテムの表示をListに変更し、Name以外を全てHide（非表示）にします。

その状態でCtrl+A → Ctrl+Cでキャラクター名の一覧がコピーできます。そして同じようにスプレッドシートに貼り付けます。


### スクリプトの実行
[https://drive.google.com/drive/my-drive](https://drive.google.com/drive/my-drive)  
Google Driveにアクセスします。

![名前から所属を取得するGAS-5]({filename}/images/名前から所属を取得するGAS-5.jpg)
①新規 → ②Googleスプレッドシート → ③空白のスプレッドシート

![名前から所属を取得するGAS-6]({filename}/images/名前から所属を取得するGAS-6.jpg)
①ツール → ②スクリプトエディタ

![名前から所属を取得するGAS-7]({filename}/images/名前から所属を取得するGAS-7.jpg)
[このリンクのスクリプトをCtrl+A → Ctrl+C](https://gist.githubusercontent.com/EVEKatsu/9242e577e17a2eac6a7a0f29557887ae/raw/c7bdbc01c942543f64d9b0adc58161cdc5da50ab/gas-find-affiliations.gs)  

『コード.gs』のエディタ画面にCtrl+V（貼り付け）をして①ファイル → ②全てを保存します。

『プロジェクト名の編集』頭囲画面が出るので『OK』をクリック。スクリプトエディタを閉じます。

![名前から所属を取得するGAS-8]({filename}/images/名前から所属を取得するGAS-8.jpg)
①ブラウザの『再読み込み』をクリック。  
↓  
②Eve Whoというメニューが出るのでTicker On / Offのどちらかを選択します。

両者の違いはそのままでTickerを表示するかどうかです。

![名前から所属を取得するGAS-9]({filename}/images/名前から所属を取得するGAS-9.jpg)
『承認が必要』という画面が出るので『続行』  
↓  
『アカウントの選択』で自分のGoogleアカウントを選択  
↓  
『このアプリは確認されていません』と出るので『詳細』をクリックして『無題のプロジェクト（安全でないページ）に移動』をクリック。

![名前から所属を取得するGAS-10]({filename}/images/名前から所属を取得するGAS-10.jpg)
許可する権限を確認します。  
このスクリプトで必要な権限は次の3つです。

#### Google ドライブのスプレッドシートの表示と管理
シートにデータの書き込みをします。

使用しているメソッド例：[Range.setValue](https://developers.google.com/apps-script/reference/spreadsheet/range#setValue(Object))

#### 自分がいないときにこのアプリケーションを実行できるようにします
Google Apps Scriptは5分以上のスクリプトを走らすことができません。

その壁を超えるためにトリガー登録をして何回かに分けてバックグラウンドで実行します。

これをすることで大量のデータを処理する時にブラウザやPCを終了しても大丈夫になります。

使用しているメソッド例: [ScriptApp.newTrigger](https://developers.google.com/apps-script/reference/script/script-app#newtriggerfunctionname)

#### 外部サービスへの接続
Eve WhoのAPIからコーポレーションやアライアンスの情報を取得するのに使います。

使用しているメソッド例：[JSON.parse](https://developers.google.com/apps-script/guides/services/external#work_with_json)

### おわり
以上でスクリプトが走り始めます。先程も言ったようにGoogle Apps Scriptは5分以上の処理ができないので、トリガーに登録をして小分けで処理を行います。

実行してもすぐには始まらないかもしれませんが、1-2分ぐらい待ってたら動き始めます。ブラウザやPCを閉じてても勝手に実行するので問題ありません。

### アイデアを募集中
いぶかつでは面白そうなアイデアを募集しています。

ビジネスとしての取引は行いません。ですので以下の条件でもオッケーだよという方で何かCOOLなことを思いついた人はTwitter or Discordの方にお願います！

1. ソースコードは公開してコミュニティ全体で共有する
1. ISKやリアルマネー等の金銭のやり取りはしない（寄付は大歓迎です☆）
1. 実際に作るかどうかは気分次第
1. 締切などの期日は設けない


### 技術的なお問い合わせや質問など
Discord: [EVE Japanese IT](https://t.co/lTtTmpOgy8)  
Twitter: [@evekatsu](https://twitter.com/evekatsu)  

こちらのほうにお願いします。  
Twitterの方はフォロー外にDMを解放しています。