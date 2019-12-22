import re
import glob
import datetime

print("集計したい期間を 20170101 20170202 の形式で指定してください：")
input_date = input()
if input_date:
	input_date = input_date.split(" ")

	# access_log 内のファイルを絶対パスで取得
	files = glob.glob("/var/log/httpd/access_log/*")
	# print(files)

	# リモートホストごとのアクセス件数
	access_host = {}

	# 時間ごとのアクセス件数
	access_time = {}
	for i in range(0, 24):
		if i <= 9:
			access_time["0" + str(i)] = 0
		else:
			access_time[str(i)] = 0
	# print(access_time["0"])

	# 月の対応
	month = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
			 "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


	for file in files:
		# ログファイルを1行ずつ読み込む
		with open(file, "r") as f:
			line = f.readline().rstrip('\n')

			while line:

				# 項目ごとにリストに追加
				items = re.findall(r'(.*)\s(.*)\s(.*)\s\[(.*)]\s"(.*)"\s(.*)\s(.*)\s"(.*)"\s"(.*)"', line)[0]
				host = items[0]
				date_item = items[3]
				date_items = re.findall(r'(\d{2})/(.*)/(\d{4}):(\d{2}):(\d{2}):(\d{2}) (.*)', date_item)[0]

				# 期間を指定
				date = datetime.datetime(int(date_items[2]), month[date_items[1]], int(date_items[0]))
				from_date_str = input_date[0]
				from_date = datetime.datetime.strptime(from_date_str, "%Y%m%d")
				to_date_str = input_date[1]
				to_date = datetime.datetime.strptime(to_date_str, "%Y%m%d")
				if from_date <= date and date <= to_date:

					# アクセス件数をカウント
					access_time[date_items[3]] += 1
					if host in access_host:
						access_host[host] += 1
					else:
						access_host[host] = 1

				line = f.readline().rstrip('\n')

	# アクセスが多い順に並び替え
	print("リモートホストごとのアクセス件数：")
	for name, num in sorted(access_host.items(), key=lambda x: -x[1]):
		print(name + "：" + str(num) + " 回")
	print()
	print("時間ごとのアクセス件数：")
	for time, num in access_time.items():
		print(time + "時：" + str(num) + " 回")
