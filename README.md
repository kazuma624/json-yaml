# json-yaml

JSON と YAML を相互変換するツールです。
特に AWS CloudFormation のテンプレートが JSON 形式しかないときに手早く YAML 形式に変換できます。
ローカルで動かす前提なので漏洩させてはいけないお仕事で使うようなテンプレートでも安心。

## ライブラリをインストールする

Python 3.8.7 で動作確認しています。

* Pipenv が入っている時

```sh
$ pipenv install
```

* Pipenv が入っていない時

```sh
$ pip install -r requirements.txt
```


## コマンドラインで使う

in ディレクトリ配下は .gitkeep を除いてコミット対象外なので適当に使うことができます。
また、出力先の out ディレクトリも同様の設定です。

* json → yml の変換

```sh
$ pwd
/path/to/json-yaml
$ python cli.py in/xxxx.json
$ ls out
xxxx_out.yml
```

* yml → json の変換

```sh
$ pwd
/path/to/json-yaml
$ python cli.py in/xxxx.yml
$ ls out
xxxx_out.json
```

## ブラウザで使う

```sh
$ pwd
/path/to/json-yaml
$ python app.py
```

1. `http://localhost:8080` にアクセスします
2. テキストエリアが上下に二つ並んで表示されるので、上側に変換したい JSON または YAML を貼り付けます
3. `JSON → YAML` か `YAML → JSON`　かをラジオボタンで選択し、 `変換` ボタンを押下します
4. 下側のテキストエリアに変換後の YAML または JSON が出力されます

## TODO

入出力のテキストエリアを横に並べ、その間に変換オプションと変換ボタンを配置したい

## 参考

* [ruamel.yaml](https://yaml.readthedocs.io/en/latest/index.html)
* [Bottle: Python Web Framework](https://bottlepy.org/docs/dev/index.html#)
