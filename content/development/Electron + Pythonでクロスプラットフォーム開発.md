Title: Electron + Pythonでクロスプラットフォーム開発
Date: 2019-3-28
Slug: Electron + Pythonでクロスプラットフォーム開発
Tags: Development, Python, Electron


これは学んだことを整理しただけの完全な技術メモです。


# ITに興味ない方

<br /><br />
<b style="font-size: 250%; color: #f26a3d">読む必要ないです</b>
<br /><br /><br />


# これから学習してみようという方

読む必要はないと思います。

[https://nodejs.org/ja/](https://nodejs.org/ja/)

PythonやRubyとかは遥か昔の太古の時代ではナウでヤングな最先端って感じでしたが、現代はNode.jsで何でもやっちゃう時代なので今から勉強するならNode.jsがいいと思います。

![Electron + Pythonでクロスプラットフォーム開発-1]({static}/images/Electron + Pythonでクロスプラットフォーム開発/Electron + Pythonでクロスプラットフォーム開発-1.jpg)

<b style="font-size: 150%; color: #f26a3d">世界的ですもんね 乗るしかない このNode.jsに</b>

ぜひともNode.jsのスペシャリストになって私に色々と教えてください（切実）

# 太古の技術しか使えない方

さて、ここで問題となるのは古の時代の技術しか使えない我々です。

もちろん新しい技術（言語、フレームワーク、ライブラリ）を使うのが一番コスパがかからない場合は移行していくのがいいと思います。

ただ 『便利なスクリプトを書いたけど、これを非エンジニア用に配布するために簡易GUIを付けてバイナリ化したい』みたいな時があるかもしれません（というか私がそんな感じでした）

更に普段はWeb開発してる人が入力フォーム程度の簡単なものを用意するためだけに新しいGUIのAPIを学ぶのは割に合わないという時もあると思います（というか私がそんな感じでした）

そんな時にDiscordで「Electronいいかもよ」って教えてもらったので試しに使ってみました。

# アーキテクチャ

![Electron + Pythonでクロスプラットフォーム開発-2]({static}/images/Electron + Pythonでクロスプラットフォーム開発/Electron + Pythonでクロスプラットフォーム開発-2.jpg)

Electronというのは雑に言うとChromium(Chrome)のエンジンを使ってデスクトップアプリケーションを作れるという感じです。

これはnode.jsで記述する感じなので、node.jsで全てを書くなら特に問題なく開発ができます。

ただ、別の言語で書いたコードを走らせるのは一工夫必要です。

ここで[ZeroMQ](http://zeromq.org/)というメッセージングライブラリを使います。親からサブプロセスとして子のコードを走らせて、そこでプロセス間通信をする感じです。

つまりZeroMQがサポートしている言語ならばGUIの画面の部分は完全にElectron任せにしてビジネスロジックの部分は自分の使い慣れた環境で開発ができます。

適当なスクリプトを書いて、後でそれを走らすためだけのおまえのGUIを付けるみたいな場合だと便利だと思います。

# Windowsでのビルド

[https://github.com/fyears/electron-python-example](https://github.com/fyears/electron-python-example)

今回はサンプルとしてこれをWin / Macの両方に向けてビルドしていきます。

git cloneもしくは右上のDownload ZIPでダウンロードして解凍して適当な作業フォルダに置いてください。

#### Git

[https://git-scm.com/download/win](https://git-scm.com/download/win)

おそらく殆どの場合は "64-bit Git for Windows Setup" をインストールすれば大丈夫だと思います。

<pre>
git
</pre>

gitコマンドが使えるようになっていれば成功です。

#### Visual Studio

[http://d.hatena.ne.jp/mocotiti/20170504/1493868466](http://d.hatena.ne.jp/mocotiti/20170504/1493868466)

[Visual Studio Community 2015のイメージディスク](http://download.microsoft.com/download/7/7/4/7746022b-8f4f-4ace-9c18-2b5a4406e3dc/vs2015.3.com_jpn.iso)

ZeroMQ（詳しく言うとZeroMQのNode.js向けのライブラリのビルド）にはVisual C++ 2015が必要です。[VS 2017でもできるらしいんですが](https://github.com/amishiro/AmiTemplate-PHP/issues/92)、私は上手くいかなかったので大人しくVS 2015を入れました。

#### Python

[https://www.python.org/downloads/](https://www.python.org/downloads/)

macOSでもそうですが、[ZeroMQにはpython 2.x系が必要です。](https://github.com/zeromq/zeromq.js/)

しかしpython 2.x系が2020年にサポートが終了するオワコンレガシー言語なので、ビジネスロジックの部分はpython 3.x系で書きたいと思います。

今回はpython [2.7.15](https://www.python.org/downloads/release/python-2715/) と [3.6.7](https://www.python.org/downloads/release/python-367/) の64bit版をインストールしました。

![Electron + Pythonでクロスプラットフォーム開発-3]({static}/images/Electron + Pythonでクロスプラットフォーム開発/Electron + Pythonでクロスプラットフォーム開発-3.jpg)

先にPython 3.x系統を『Add Python 3.x to PATH』にチェックボックスを付けてインストールします。その後にPython 2.x系統をインストールして1度再起動します。

<pre>
py -3 -V # Python 3のバージョン
py -2 -V # Python 2のバージョン
python -V # Python 3のバージョン
</pre>

それぞれ正しい結果が表示されたら成功です。

### Node.js

[https://github.com/nullivex/nodist/releases](https://github.com/nullivex/nodist/releases)

Windowsでnode.jsのバージョン管理にはnodistというのがいいらしいです。

<pre>
nodist 10.11.0
</pre>

新しいnode.jsを入れます。バージョンはElectronで走ってるのと同じバージョンがいいと思います。多分。


<pre>
  "devDependencies": {
    "electron": "*",
    "electron-packager": "*",
    "electron-rebuild": "*"
  }
</pre>

package.jsonをテキストエディタで開いて "devDependencies" の項目に "electron-rebuild" を追加します。

<pre>
set PATH=C:¥Python27;%PATH%
npm install
.¥node_modules¥.bin¥electron-rebuild
.¥node_modules¥.bin¥electron
</pre>

![Electron + Pythonでクロスプラットフォーム開発-4]({static}/images/Electron + Pythonでクロスプラットフォーム開発/Electron + Pythonでクロスプラットフォーム開発-4.jpg)

ZeroMQのビルドはPython 2.x系でないといけないので、npm installの前にPATHを追加しておきます。.¥node_modules¥.bin¥electronで最初のアプリが立ち上がったら成功です。

### Virtualenv
先程の状態だとPATHがpython 2.x系のままなのでpython 3.x系に戻すために一度コマンドプロンプトを終了して、もう一度起動します。こまめに "python -V" をして、今どのpythonが走っているのか確認すると安全です。

[https://qiita.com/maisuto/items/91143d26b609d6cfc1ac](https://qiita.com/maisuto/items/91143d26b609d6cfc1ac)

<pre>
pip install virtualenvwrapper-win
mkvirtualenv envname
</pre>

こんな感じで仮想環境を構築します。ちなみに↑の記事になかったですが仮想環境を削除する時は "rmvirtualenv envname" らしいです。
 
もし仮想環境に入ってない場合は "workon envname" をします。

[https://qiita.com/akabei/items/da70ebf61cc413d5ff0d](https://qiita.com/akabei/items/da70ebf61cc413d5ff0d)

<pre>
chcp 65001
</pre>

WindowsはShiftJISという未知の文字コードを使っているらしいので、人間が本来使うべき文字コードであるUTF-8に変更します。

<pre>
pyinstaller pycalc¥api.py --distpath pycalcdist
</pre>

これでpycalcdistというフォルダに新しいexeが作られていれば成功です

### パッケージング
"build" というフォルダと "api.spec" というファイルを削除します。

<b>.¥node_modules¥.bin¥electron-packager . --overwrite --ignore="pycalc$" --ignore="¥.venv" --ignore="old-post-backup"</b>

![Electron + Pythonでクロスプラットフォーム開発-5]({static}/images/Electron + Pythonでクロスプラットフォーム開発/Electron + Pythonでクロスプラットフォーム開発-5.jpg)

pretty-calculator-win32-x64というフォルダが作られていて、中のexeを起動して電卓として使えれば成功です。

# macOSでのビルド
macで開発している人は最低限のことは自分で調べれるはずなので、かなりガバく書きます。

まずプロジェクトをダウンロードしてきて解凍して適当な作業ディレクトリに置きます。

<pre>
  "devDependencies": {
    "electron": "*",
    "electron-packager": "*",
    "electron-rebuild": "*"
  }
</pre>

Windowsと同じようにpackage.jsonをテキストエディタで開いて "devDependencies" の項目に "electron-rebuild" を追加します。


### Anyenv
anyenvの入れ方は適当にググってください。

<pre>
ndenv install v10.11.0
ndenv global v10.11.0
pyenv install 2.7.15
pyenv install 3.6.7
pyenv virtualenv 2.7.15 python2
pyenv virtualenv 3.6.7 python3
pyenv local python3 python2
npm install --global npm
pip install --upgrade pip
</pre>

ここで大事なところは "pyenv local python3 python2" とpython3の仮想環境名を先に書くことです。

<pre>
python2 -V # python2のバージョン
python -V # python3のバージョン
</pre>

これによって、python2のコマンドでは2.x系がpythonのコマンドでは3.x系が走ります。

### パッケージング

<pre>
npm install
./node_modules/.bin/electron-rebuild
pip install zerorpc
pip install pyinstaller
pyinstaller pycalc/api.py --distpath pycalcdist
rm -rf build/
rm -rf api.spec
</pre>

<b>./node_modules/.bin/electron-packager . --overwrite --ignore="pycalc$" --ignore="\.venv" --ignore="old-post-backup"</b>

pretty-calculator-darwin-x64というディレクトリが作成されていて中のアプリが起動できたら成功。

# おわりに

<br /><br />
<b style="font-size: 150%; color: #f26a3d">Webの技術をWindowsで動かそうとしたら発狂しそうでした（血の涙）</b>
<br /><br />
