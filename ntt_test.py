import os

# 必要なライブラリをインストール: RW-FAT環境実行時 # zipfile shutil は環境によってインストール
# proxy = "--proxy=10.160.120.156:8080"
# os.system(f"pip install {proxy} spire-presentation")

import zipfile
import shutil
import re
from spire.presentation import Presentation, FileFormat
import datetime


# レポート対象期間の設定
target_year = 2023
target_month = 4
target_date = datetime.date(target_year, target_month, 1)
target_period = target_date.strftime("%Y_%m")
target_period_pass = target_date.strftime("%Y%m")

# パスワードの設定
password = f"Managed-lan-{target_period_pass}"
password_bytes = password.encode()  # バイト列にエンコード
print('pass: ', password)


# 対象ファイル
zip_file_dir = f"C:\\reports\webex\\{target_period}"

# レポート出力パスの設定
OUTPUT_PATH = zip_file_dir
os.makedirs(OUTPUT_PATH, exist_ok=True)

# 一時ディレクトリの作成
temp_dir = os.path.join(zip_file_dir, "all")
os.makedirs(temp_dir, exist_ok=True)


# 圧縮ファイルのリストを取得
zip_files = [f for f in os.listdir(zip_file_dir) if f.endswith('.zip')]

# 圧縮ファイルを一時ディレクトリに展開
for zip_file_name in zip_files:
    zip_file_path = os.path.join(zip_file_dir, zip_file_name)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir, pwd=password_bytes)
    # 圧縮ファイルを削除
    os.remove(zip_file_path)
print("コピー処理が完了しました。")


# クライアントとORG名に基づいてディレクトリを作成し、ファイルを移動する
files = [f for f in os.listdir(temp_dir) if f.endswith(('.pptx', '.ppt'))]
for file_name in files:
    # クライアント名を抽出
    match = re.match(r"(.+?)-", file_name)
    if match:
        client_name = match.group(1)
        client_dir = os.path.join(zip_file_dir, client_name)
        os.makedirs(client_dir, exist_ok=True)

        # ファイルを移動
        src_path = os.path.join(temp_dir, file_name)
        dst_path = os.path.join(client_dir, file_name)
        shutil.move(src_path, dst_path)

# 一時ディレクトリを削除
shutil.rmtree(temp_dir)
print("フォルダ再整理処理が完了しました。")

# 各クライアントディレクトリ内で処理を実行
for client_dir in os.listdir(zip_file_dir):
    if client_dir == "all":
        continue

    client_path = os.path.join(zip_file_dir, client_dir)
    if not os.path.isdir(client_path):
        continue  # ZIPファイルをスキップ
    print(client_path)
    files = [f for f in os.listdir(client_path) if f.endswith(('.pptx', '.ppt')) and not f.endswith('.zip')]
    file_count = len(files)
    print(f"{file_count} PowerPoint ファイルが '{client_dir}' から見つかりました。")

    if file_count < 2:
        print("2つ以上の PowerPoint ファイルが必要です。")
        continue

    # 1番目のファイルを読み込み、スライドマスターを取得
    first_file_path = os.path.join(client_path, files[0])
    pres1 = Presentation()
    pres1.LoadFromFile(first_file_path)
    master = pres1.Masters.get_Item(0)

    # 7ページ目のスライドを一時的に保持する変数
    master_slide_7 = pres1.Slides.get_Item(6)  # 7ページ目のスライドを取得
    pres1.Slides.RemoveAt(6)  # 7ページ目のスライドを削除

    # 2番目以降のファイルから、3~6ページのスライドをコピー
    for filename in files[1:]:
        file_path = os.path.join(client_path, filename)
        pres2 = Presentation()
        pres2.LoadFromFile(file_path)

        for i in range(2, 6):  # 3~6ページ
            slide = pres2.Slides.get_Item(i)
            pres1.Slides.AppendBySlide(slide)
        pres2.Dispose()

    # 7ページ目のスライドを最後尾に追加
    pres1.Slides.AppendBySlide(master_slide_7)

    # 1番目のファイルを上書き保存
    output_path = os.path.join(client_path, f"{client_dir}.pptx")
    pres1.SaveToFile(output_path, FileFormat.Pptx2019)

    # ファイルサイズチェックと圧縮
    if os.path.getsize(output_path) > 18 * 1024 * 1024:  # 18MB以上の場合
        part_num = 1
        with open(output_path, 'rb') as f:
            while True:
                chunk = f.read(18 * 1024 * 1024)
                if not chunk:
                    break

                part_name = f"{client_dir}_{part_num}.pptx"
                part_path = os.path.join(client_path, part_name)

                with open(part_path, 'wb') as part_file:
                    part_file.write(chunk)

                part_num += 1

        os.remove(output_path)
    else:  # 18MB以下の場合
        pres1.SaveToFile(output_path, FileFormat.Pptx2019)

    pres1.Dispose()

    # 展開したオリジナルのファイルを削除
    for filename in files:
        file_path = os.path.join(client_path, filename)
        os.remove(file_path)

    print(f"'{client_dir}' の処理が完了しました。")

print("すべての処理が完了しました。")