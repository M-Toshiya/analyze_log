# analyze_log
 
analyze_log は、アクセスログからアクセス件数を解析するプログラムです。<br>
ログファイルから、アクセス時間とリモートホスト名を抽出し、以下の観点でアクセス件数を集計します。

1. 各時間ごとのアクセス件数
2. リモートホスト別のアクセス件数<br>
アクセスの多いリモートホストの順にアクセス件数の一覧を表示する。
 
## 機能
 
ログの中から、ある指定した期間（例えば、2017年4月1日～4月30日までなど）に絞って集計できます。
 
## 使い方
 
1. analyze_log.py を実行すると、"集計したい期間を 20170101 20170202 の形式で指定してください：" とコマンドラインに出力されるのでそれに従った形式で期間を入力してください。
2. ログファイルは /var/log/httpd/access_log/* の絶対パスで指定してあります。

## その他
 
ログファイルを一行ずつ読み込んで必要な情報のみを保存しているので、解析したいアクセスログファイルのサイズが実行するマシンのメモリよりも大きかったとしても、メモリ不足にならずに動作します。
