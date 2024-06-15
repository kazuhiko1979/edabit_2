# リファクタリング1 20240614
import os
import zipfile
import shutil
import re
import ctypes
from spire.presentation import Presentation, FileFormat, ShapeType, TextAlignmentType, TextFont
from spire.presentation.common import RectangleF, PointF, SizeF

# 定数の設定
ZIP_FILE_DIR = "C:\\"
ZIP_FILE_PATTERN = re.compile(r"webex_reports_(\d{6})_\d+\.zip")
OUTPUT_DIR_PATTERN = "output_{}"
TEMP_DIR_NAME = "all"
PASSWORD_TEMPLATE = "Managed-lan-{}"
MAX_FILE_SIZE = 18 * 1024 * 1024

def find_zip_file(directory, pattern):
    for file in os.listdir(directory):
        match = pattern.match(file)
        if match:
            return file, match.group(1)
    return None, None

def extract_zip_file(zip_path, extract_to, password):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to, pwd=password.encode())

def create_directories(base_path, *subdirs):
    paths = [os.path.join(base_path, subdir) for subdir in subdirs]
    for path in paths:
        os.makedirs(path, exist_ok=True)
    return paths

def move_files_to_client_dirs(temp_dir, output_path):
    for org_name in os.listdir(temp_dir):
        org_path = os.path.join(temp_dir, org_name)
        if os.path.isdir(org_path):
            client_dir = os.path.join(output_path, org_name)
            os.makedirs(client_dir, exist_ok=True)
            for file_name in os.listdir(org_path):
                if file_name.endswith(('.pptx', '.ppt')):
                    base_name = file_name.split('-')[0]
                    target_dir = client_dir if base_name == org_name else os.path.join(output_path, base_name)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(os.path.join(org_path, file_name), os.path.join(target_dir, file_name))
            shutil.rmtree(org_path)

def insert_location_text(slide, location):
    left, top, width, height = 25.0, 100.0, 288.0, 25.0
    text_box = slide.Shapes.AppendShape(ShapeType.Rectangle, RectangleF(PointF(left, top), SizeF(width, height)))
    text_box.Fill.Visible = False
    text_box.Line.Visible = False
    text_box.TextFrame.Text = location
    text_box.TextFrame.Paragraphs[0].TextRanges[0].LatinFont = TextFont("Arial")
    text_box.TextFrame.Paragraphs[0].TextRanges[0].FontHeight = 18
    text_box.TextFrame.Paragraphs[0].Alignment = TextAlignmentType.Center

def process_presentation(presentation, location, slide_indices):
    for index in slide_indices:
        slide = presentation.Slides.get_Item(index)
        insert_location_text(slide, location)

def process_client_presentations(client_dir, output_path):
    files = [f for f in os.listdir(client_dir) if f.endswith(('.pptx', '.ppt'))]

    if len(files) < 2:
        # print(f"2つ以上の PowerPoint ファイルが必要です。'{client_dir}' にあるファイル数: {len(files)}")
        return

    locations = [f.split('_')[0] for f in files]
    first_file_path = os.path.join(client_dir, files[0])

    pres1 = Presentation()
    pres1.LoadFromFile(first_file_path)
    master_slide = pres1.Slides.get_Item(6)
    pres1.Slides.RemoveAt(6)
    process_presentation(pres1, locations[0], range(2, 6))

    for i, filename in enumerate(files[1:], 1):
        file_path = os.path.join(client_dir, filename)
        pres2 = Presentation()
        pres2.LoadFromFile(file_path)
        process_presentation(pres2, locations[i], range(2, 6))
        for j in range(2, 6):
            slide = pres2.Slides.get_Item(j)
            pres1.Slides.AppendBySlide(slide)
        pres2.Dispose()

    pres1.Slides.AppendBySlide(master_slide)
    output_presentation(pres1, client_dir, output_path)

    for filename in files:
        os.remove(os.path.join(client_dir, filename))

def output_presentation(presentation, client_dir, output_path):
    output_file = os.path.join(client_dir, f"{os.path.basename(client_dir)}.pptx")
    presentation.SaveToFile(output_file, FileFormat.Pptx2019)

    if os.path.getsize(output_file) > MAX_FILE_SIZE:
        split_large_file(output_file, client_dir)
    else:
        presentation.SaveToFile(output_file, FileFormat.Pptx2019)

    presentation.Dispose()

def split_large_file(file_path, client_dir):
    part_num = 1
    with open(file_path, 'rb') as f:
        while chunk := f.read(MAX_FILE_SIZE):
            part_path = os.path.join(client_dir, f"{os.path.basename(client_dir)}_{part_num}.pptx")
            with open(part_path, 'wb') as part_file:
                part_file.write(chunk)
            part_num += 1
    os.remove(file_path)

def remove_empty_directories(output_path):
    for dirpath, dirnames, filenames in os.walk(output_path, topdown=False):
        if not filenames and not dirnames:
            os.rmdir(dirpath)

def remove_zip_file(zip_file_path):
    FILE_ATTRIBUTE_NORMAL = 0x80
    ctypes.windll.kernel32.SetFileAttributesW(zip_file_path, FILE_ATTRIBUTE_NORMAL)
    try:
        os.remove(zip_file_path)
        print(f"対象ファイル '{os.path.basename(zip_file_path)}' が削除されました。")
    except PermissionError as e:
        print(f"ファイル削除中にエラーが発生しました: {e}")

def main():
    zip_file_name, target_period_pass = find_zip_file(ZIP_FILE_DIR, ZIP_FILE_PATTERN)
    if not zip_file_name:
        print("対象ファイルが見つかりませんでした")
        return

    zip_file_path = os.path.join(ZIP_FILE_DIR, zip_file_name)
    if not os.path.exists(zip_file_path):
        print("zipファイルが存在しません")
        return

    password = PASSWORD_TEMPLATE.format(target_period_pass)
    output_path = os.path.join(ZIP_FILE_DIR, OUTPUT_DIR_PATTERN.format(target_period_pass))
    temp_dir = os.path.join(output_path, TEMP_DIR_NAME)
    create_directories(output_path, TEMP_DIR_NAME)

    extract_zip_file(zip_file_path, temp_dir, password)
    move_files_to_client_dirs(temp_dir, output_path)
    shutil.rmtree(temp_dir)

    for client_dir in [d for d in os.listdir(output_path) if os.path.isdir(os.path.join(output_path, d))]:
        process_client_presentations(os.path.join(output_path, client_dir), output_path)

    remove_empty_directories(output_path)
    remove_zip_file(zip_file_path)
    print("すべての処理が完了しました。")


if __name__ == "__main__":
    main()











# import os
# import zipfile
# import shutil
# import re
# import ctypes
# from spire.presentation import Presentation, FileFormat, ShapeType, TextAlignmentType, TextFont
# from spire.presentation.common import RectangleF, PointF, SizeF
#
# # 変数に格納先のパスを設定
# ZIP_FILE_DIR = "C:\\"
#
# # 対象ファイル名を取得、正規表現を修正
# zip_file_name_pattern = re.compile(r"webex_reports_(\d{6})_\d+\.zip")
# zip_file_name = None
# for file in os.listdir(ZIP_FILE_DIR):
#     match = zip_file_name_pattern.match(file)
#     if match:
#         zip_file_name = file
#         target_period_pass = match.group(1)
#         break
#
# if not zip_file_name:
#     print("対象ファイルが見つかりませんでした")
#     exit()
#
# zip_file_path = os.path.join(ZIP_FILE_DIR, zip_file_name)
#
# if not os.path.exists(zip_file_path):
#     print("zipファイルが存在しません")
#     exit()
#
# # パスワードの設定
# password = f"Managed-lan-{target_period_pass}"
# password_bytes = password.encode()
#
# # 出力パスと一時ディレクトリの設定
# OUTPUT_PATH = os.path.join(ZIP_FILE_DIR, f"output_{target_period_pass}")
# os.makedirs(OUTPUT_PATH, exist_ok=True)
#
# temp_dir = os.path.join(OUTPUT_PATH, "all")
# os.makedirs(temp_dir, exist_ok=True)
#
# # 圧縮ファイルを一時ディレクトリに展開
# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     zip_ref.extractall(temp_dir, pwd=password_bytes)
#
# # 各 ORG フォルダを元にクライアントディレクトリを作成し、ファイルを移動する
# for org_name in os.listdir(temp_dir):
#     org_path = os.path.join(temp_dir, org_name)
#     if os.path.isdir(org_path):
#         client_dir = os.path.join(OUTPUT_PATH, org_name)
#         os.makedirs(client_dir, exist_ok=True)
#
#         for file_name in os.listdir(org_path):
#             if file_name.endswith(('.pptx', '.ppt')):
#                 src_path = os.path.join(org_path, file_name)
#
#                 # ファイル名の先頭部分（最初の「-」の手前の文字列）を取得
#                 base_name = file_name.split('-')[0]
#                 if base_name == org_name:
#                     dst_path = os.path.join(client_dir, file_name)
#                 else:
#                     # フォルダ名とファイルの先頭部分が異なる場合、対応するフォルダに移動
#                     other_client_dir = os.path.join(OUTPUT_PATH, base_name)
#                     os.makedirs(other_client_dir, exist_ok=True)
#                     dst_path = os.path.join(other_client_dir, file_name)
#                 shutil.move(src_path, dst_path)
#
#         # 元のフォルダを削除
#         shutil.rmtree(client_dir)
#
# # 一時ディレクトリを削除
# shutil.rmtree(temp_dir)
#
# def insert_location_text(slide, location):
#
#     left = 25.0
#     top = 100.0
#     width = 288.0
#     height = 25.0
#
#     text_box = slide.Shapes.AppendShape(ShapeType.Rectangle, RectangleF(PointF(left, top), SizeF(width, height)))
#     text_box.Fill.Visible = False
#     text_box.Line.Visible = False
#
#     text_box.TextFrame.Text = location
#     text_box.TextFrame.Paragraphs[0].TextRanges[0].LatinFont = TextFont("Arial")
#     text_box.TextFrame.Paragraphs[0].TextRanges[0].FontHeight = 18
#     text_box.TextFrame.Paragraphs[0].Alignment = TextAlignmentType.Center
#
# def process_presentation(presentation, location, slide_indices):
#     for index in slide_indices:
#         slide = presentation.Slides.get_Item(index)
#         insert_location_text(slide, location)
#
# # 各クライアントディレクトリ内で処理を実行
# for client_dir in [d for d in os.listdir(OUTPUT_PATH) if os.path.isdir(os.path.join(OUTPUT_PATH, d))]:
#     client_path = os.path.join(OUTPUT_PATH, client_dir)
#     files = [f for f in os.listdir(client_path) if f.endswith(('.pptx', '.ppt'))]
#
#     if len(files) < 2:
#         print(f"2つ以上の PowerPoint ファイルが必要です。'{client_dir}' にあるファイル数: {len(files)}")
#         continue
#
#     # ORG名とLocationを抽出
#     org_name = client_dir.split('-')[0]
#     locations = [f.split('_')[0] for f in files]
#     first_file_path = os.path.join(client_path, files[0])
#
#     pres1 = Presentation()
#     pres1.LoadFromFile(first_file_path)
#     master_slide_7 = pres1.Slides.get_Item(6)
#     pres1.Slides.RemoveAt(6)
#
#     # pres1の3～6ページにLocationを挿入
#     process_presentation(pres1, locations[0], range(2, 6))
#
#     # 2つ目のファイル以降に対して処理
#     for i, filename in enumerate(files[1:], 1):
#         file_path = os.path.join(client_path, filename)
#         pres2 = Presentation()
#         pres2.LoadFromFile(file_path)
#
#         process_presentation(pres2, locations[i], range(2, 6))
#
#         for j in range(2, 6):
#             slide = pres2.Slides.get_Item(j)
#             pres1.Slides.AppendBySlide(slide)
#
#         pres2.Dispose()
#
#     # 除外したスライドを最後に追加
#     pres1.Slides.AppendBySlide(master_slide_7)
#
#     output_path = os.path.join(client_path, f"{client_dir}.pptx")
#     pres1.SaveToFile(output_path, FileFormat.Pptx2019)
#
#     if os.path.getsize(output_path) > 18 * 1024 * 1024:
#         part_num = 1
#         with open(output_path, 'rb') as f:
#             while chunk := f.read(18 * 1024 * 1024):
#                 part_name = f"{client_dir}_{part_num}.pptx"
#                 part_path = os.path.join(client_path, part_name)
#
#                 with open(part_path, 'wb') as part_file:
#                     part_file.write(chunk)
#                 part_num += 1
#
#         os.remove(output_path)
#     else:
#         pres1.SaveToFile(output_path, FileFormat.Pptx2019)
#
#     pres1.Dispose()
#
#     for filename in files:
#         file_path = os.path.join(client_path, filename)
#         os.remove(file_path)
#
#     print(f"'{client_dir}' の処理が完了しました。")
#
# # 対象ファイルの属性を変更して削除
# if os.path.exists(zip_file_path):
#     # ファイルの読み取り専用属性を解除
#     FILE_ATTRIBUTE_NORMAL = 0x80
#     ctypes.windll.kernel32.SetFileAttributesW(zip_file_path, FILE_ATTRIBUTE_NORMAL)
#
#     try:
#         os.remove(zip_file_path)
#         print(f"対象ファイル '{zip_file_name}' が削除されました。")
#     except PermissionError as e:
#         print(f"ファイル削除中にエラーが発生しました: {e}")
#
# print("すべての処理が完了しました。")









# spire.presentation だけで実装テスト
# import os
# import zipfile
# import shutil
# import re
# import ctypes
# from spire.presentation import Presentation, FileFormat, ShapeType, TextAlignmentType, TextFont
# from spire.presentation.common import RectangleF, PointF, SizeF
#
# # 変数に格納先のパスを設定
# ZIP_FILE_DIR = "C:\\"
#
# # 対象ファイル名を取得、正規表現を修正
# zip_file_name_pattern = re.compile(r"webex_reports_(\d{6})_\d+\.zip")
# zip_file_name = None
# for file in os.listdir(ZIP_FILE_DIR):
#     match = zip_file_name_pattern.match(file)
#     if match:
#         zip_file_name = file
#         target_period_pass = match.group(1)
#         break
#
# if not zip_file_name:
#     print("対象ファイルが見つかりませんでした")
#     exit()
#
# zip_file_path = os.path.join(ZIP_FILE_DIR, zip_file_name)
#
# if not os.path.exists(zip_file_path):
#     print("zipファイルが存在しません")
#     exit()
#
# # パスワードの設定
# password = f"Managed-lan-{target_period_pass}"
# password_bytes = password.encode()
#
# # 出力パスと一時ディレクトリの設定
# OUTPUT_PATH = os.path.join(ZIP_FILE_DIR, f"output_{target_period_pass}")
# os.makedirs(OUTPUT_PATH, exist_ok=True)
#
# temp_dir = os.path.join(OUTPUT_PATH, "all")
# os.makedirs(temp_dir, exist_ok=True)
#
# # 圧縮ファイルを一時ディレクトリに展開
# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     zip_ref.extractall(temp_dir, pwd=password_bytes)
#
# # 各 ORG フォルダを元にクライアントディレクトリを作成し、ファイルを移動する
# for org_name in os.listdir(temp_dir):
#     org_path = os.path.join(temp_dir, org_name)
#     if os.path.isdir(org_path):
#         client_dir = os.path.join(OUTPUT_PATH, org_name)
#         os.makedirs(client_dir, exist_ok=True)
#
#         for file_name in os.listdir(org_path):
#             if file_name.endswith(('.pptx', '.ppt')):
#                 src_path = os.path.join(org_path, file_name)
#
#                 # ファイル名の先頭部分（最初の「-」の手前の文字列）を取得
#                 base_name = file_name.split('-')[0]
#                 if base_name == org_name:
#                     dst_path = os.path.join(client_dir, file_name)
#                 else:
#                     # フォルダ名とファイルの先頭部分が異なる場合、対応するフォルダに移動
#                     other_client_dir = os.path.join(OUTPUT_PATH, base_name)
#                     os.makedirs(other_client_dir, exist_ok=True)
#                     dst_path = os.path.join(other_client_dir, file_name)
#                 shutil.move(src_path, dst_path)
#
#         # 元のフォルダを削除
#         shutil.rmtree(client_dir)
#
# # 一時ディレクトリを削除
# shutil.rmtree(temp_dir)
#
# # 各クライアントディレクトリ内で処理を実行
# for client_dir in [d for d in os.listdir(OUTPUT_PATH) if os.path.isdir(os.path.join(OUTPUT_PATH, d))]:
#     client_path = os.path.join(OUTPUT_PATH, client_dir)
#     files = [f for f in os.listdir(client_path) if f.endswith(('.pptx', '.ppt'))]
#
#     if len(files) < 2:
#         print(f"2つ以上の PowerPoint ファイルが必要です。'{client_dir}' にあるファイル数: {len(files)}")
#         continue
#
#     # ORG名とLocationを抽出
#     org_name = client_dir.split('-')[0]
#     locations = [f.split('_')[0] for f in files]
#     first_file_path = os.path.join(client_path, files[0])
#
#     pres1 = Presentation()
#     pres1.LoadFromFile(first_file_path)
#     master_slide_7 = pres1.Slides.get_Item(6)
#     pres1.Slides.RemoveAt(6)
#
#
#     # pres1の3～6ページにLocationを挿入
#     for j in range(2, 6):
#         slide = pres1.Slides.get_Item(j)
#
#         # Locationを挿入
#         left = 25.0
#         top = 100.0
#         width = 288.0
#         height = 25.0
#
#         text_box = slide.Shapes.AppendShape(ShapeType.Rectangle, RectangleF(PointF(left, top), SizeF(width, height)))
#         text_box.Fill.Visible = False
#         text_box.Line.Visible = False
#
#         text_box.TextFrame.Text = locations[0]  # pres1に対しては最初のファイルのlocationを挿入
#         text_box.TextFrame.Paragraphs[0].TextRanges[0].LatinFont = TextFont("Arial")
#         text_box.TextFrame.Paragraphs[0].TextRanges[0].FontHeight = 18
#         text_box.TextFrame.Paragraphs[0].Alignment = TextAlignmentType.Center
#
#     for i, filename in enumerate(files[1:], 1):
#
#         file_path = os.path.join(client_path, filename)
#         pres2 = Presentation()
#         pres2.LoadFromFile(file_path)
#
#         for j in range(2, 6):
#             slide = pres2.Slides.get_Item(j)
#
#             # Locationを挿入
#             left = 25.0
#             top = 100.0
#             width = 288.0
#             height = 25.0
#
#             text_box = slide.Shapes.AppendShape(ShapeType.Rectangle,
#                                                 RectangleF(PointF(left, top), SizeF(width, height)))
#
#             # テキストボックスの背景と枠線を透明にする
#             text_box.Fill.Visible = False
#             text_box.Line.Visible = False
#
#             text_box.TextFrame.Text = locations[i]
#             print(text_box.TextFrame.Text)
#             text_box.TextFrame.Paragraphs[0].TextRanges[0].LatinFont = TextFont("Arial")
#             text_box.TextFrame.Paragraphs[0].TextRanges[0].FontHeight = 18
#             text_box.TextFrame.Paragraphs[0].Alignment = TextAlignmentType.Center
#
#             pres1.Slides.AppendBySlide(slide)
#
#         pres2.Dispose()
#
#     # 除外したスライドを最後に追加
#     pres1.Slides.AppendBySlide(master_slide_7)
#
#     output_path = os.path.join(client_path, f"{client_dir}.pptx")
#     pres1.SaveToFile(output_path, FileFormat.Pptx2019)
#
#     if os.path.getsize(output_path) > 18 * 1024 * 1024:
#         part_num = 1
#         with open(output_path, 'rb') as f:
#             while chunk := f.read(18 * 1024 * 1024):
#                 part_name = f"{client_dir}_{part_num}.pptx"
#                 part_path = os.path.join(client_path, part_name)
#
#                 with open(part_path, 'wb') as part_file:
#                     part_file.write(chunk)
#                 part_num += 1
#
#         os.remove(output_path)
#     else:
#         pres1.SaveToFile(output_path, FileFormat.Pptx2019)
#
#     pres1.Dispose()
#
#     for filename in files:
#         file_path = os.path.join(client_path, filename)
#         os.remove(file_path)
#
#     print(f"'{client_dir}' の処理が完了しました。")
#
# # テキストボックスが正しく挿入されたか確認する
# # for client_dir in [d for d in os.listdir(OUTPUT_PATH) if os.path.isdir(os.path.join(OUTPUT_PATH, d))]:
# #     client_path = os.path.join(OUTPUT_PATH, client_dir)
# #     output_file_path = os.path.join(client_path, f"{client_dir}.pptx")
# #
# #     if os.path.exists(output_file_path):
# #         pres = Presentation()
# #         pres.LoadFromFile(output_file_path)
# #         for i in range(2, 6):
# #             slide = pres.Slides.get_Item(i)
# #             found_test_text = False
# #             for shape in slide.Shapes:
# #                 if shape.TextFrame is not None and shape.TextFrame.Text:
# #                     print(shape.TextFrame.Text)
# #                     found_test_text = True
# #                     break
# #             if found_test_text:
# #                 print(f"スライド {i + 1} に テキストが正しく挿入されました。")
# #             else:
# #                 print(f"スライド {i + 1} に テキストが見つかりません。")
# #         pres.Dispose()
#
# # 対象ファイルの属性を変更して削除
# if os.path.exists(zip_file_path):
#     # ファイルの読み取り専用属性を解除
#     FILE_ATTRIBUTE_NORMAL = 0x80
#     ctypes.windll.kernel32.SetFileAttributesW(zip_file_path, FILE_ATTRIBUTE_NORMAL)
#
#     try:
#         os.remove(zip_file_path)
#         print(f"対象ファイル '{zip_file_name}' が削除されました。")
#     except PermissionError as e:
#         print(f"ファイル削除中にエラーが発生しました: {e}")
#
# print("すべての処理が完了しました。")










# spire.presentation / python-pptx の利用の違い　20240612
# import os
# import zipfile
# import shutil
# import re
# from spire.presentation import Presentation, FileFormat
# import ctypes
# from pptx import Presentation as pptx_Presentation  # pptxライブラリをインポート
# from pptx.util import Inches, Pt  # インチとポイントを扱うためのユーティリティをインポート
# from copy import deepcopy
#
#
# # 変数に格納先のパスを設定
# ZIP_FILE_DIR = "C:\\"
#
# # 対象ファイル名を取得、正規表現を修正
# zip_file_name_pattern = re.compile(r"webex_reports_(\d{6})_\d+\.zip")
# zip_file_name = None
# for file in os.listdir(ZIP_FILE_DIR):
#     match = zip_file_name_pattern.match(file)
#     if match:
#         zip_file_name = file
#         target_period_pass = match.group(1)
#         break
#
# if not zip_file_name:
#     print("対象ファイルが見つかりませんでした")
#     exit()
#
# zip_file_path = os.path.join(ZIP_FILE_DIR, zip_file_name)
#
# if not os.path.exists(zip_file_path):
#     print("zipファイルが存在しません")
#     exit()
#
# # パスワードの設定
# password = f"Managed-lan-{target_period_pass}"
# password_bytes = password.encode()
#
# # 出力パスと一時ディレクトリの設定
# OUTPUT_PATH = os.path.join(ZIP_FILE_DIR, f"output_{target_period_pass}")
# os.makedirs(OUTPUT_PATH, exist_ok=True)
#
# temp_dir = os.path.join(OUTPUT_PATH, "all")
# os.makedirs(temp_dir, exist_ok=True)
#
# # 圧縮ファイルを一時ディレクトリに展開
# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     zip_ref.extractall(temp_dir, pwd=password_bytes)
#
#
# # 各 ORG フォルダを元にクライアントディレクトリを作成し、ファイルを移動する
# for org_name in os.listdir(temp_dir):
#     org_path = os.path.join(temp_dir, org_name)
#     if os.path.isdir(org_path):
#         client_dir = os.path.join(OUTPUT_PATH, org_name)
#         os.makedirs(client_dir, exist_ok=True)
#
#         for file_name in os.listdir(org_path):
#             if file_name.endswith(('.pptx', '.ppt')):
#                 src_path = os.path.join(org_path, file_name)
#
#                 # ファイル名の先頭部分（最初の「-」の手前の文字列）を取得
#                 base_name = file_name.split('-')[0]
#                 if base_name == org_name:
#                     dst_path = os.path.join(client_dir, file_name)
#                 else:
#                     # フォルダ名とファイルの先頭部分が異なる場合、対応するフォルダに移動
#                     other_client_dir = os.path.join(OUTPUT_PATH, base_name)
#                     os.makedirs(other_client_dir, exist_ok=True)
#                     dst_path = os.path.join(other_client_dir, file_name)
#                 shutil.move(src_path, dst_path)
#
#         # 元のフォルダを削除
#         shutil.rmtree(client_dir)
#
# # 一時ディレクトリを削除
# shutil.rmtree(temp_dir)
#
#
# # 各クライアントディレクトリ内で処理を実行
# for client_dir in [d for d in os.listdir(OUTPUT_PATH) if os.path.isdir(os.path.join(OUTPUT_PATH, d))]:
#     client_path = os.path.join(OUTPUT_PATH, client_dir)
#     files = [f for f in os.listdir(client_path) if f.endswith(('.pptx', '.ppt'))]
#
#     if len(files) < 2:
#         print(f"2つ以上の PowerPoint ファイルが必要です。'{client_dir}' にあるファイル数: {len(files)}")
#         continue
#
#     # ORG名とLocationを抽出
#     org_name = client_dir.split('-')[0]
#     locations = [f.split('_')[0] for f in files]
#     first_file_path = os.path.join(client_path, files[0])
#
#     # spire.presentation
#     pres1 = Presentation()
#     pres1.LoadFromFile(first_file_path)
#     master_slide_7 = pres1.Slides.get_Item(6)
#     pres1.Slides.RemoveAt(6)
#
#     # pptx
#     # pres1 = pptx_Presentation(first_file_path)
#     # 除外するスライドをコピーして保存します
#     # excluded_slide = pres1.slides[6]  # 元のスライド
#     #
#     # # 新しいスライドを作成して、元のスライドの内容をコピーします
#     # new_slide = pres1.slides.add_slide(excluded_slide.slide_layout)
#     # for shape in excluded_slide.shapes:
#     #     new_shape = deepcopy(shape)  # 形状をコピーする
#     #     new_slide.shapes._spTree.insert_element_before(new_shape._element, 'p:extLst')
#     # 除外スライドを含まないリストを作成します
#     # slides_without_excluded = [slide for slide in pres1.slides if slide != pres1.slides[6]]
#
#     for i, filename in enumerate(files[1:], 1):
#         file_path = os.path.join(client_path, filename)
#         # spire.presentation
#         pres2 = Presentation()
#         pres2.LoadFromFile(file_path)
#
#         # pptx
#         # pres2 = pptx_Presentation(file_path)
#
#         for i in range(2, 6):
#             slide = pres2.Slides.get_Item(i)
#             pres1.Slides.AppendBySlide(slide)
#         pres2.Dispose()
#
#         # for j in range(2, 6):
#             # spire.presentation
#             # slide = pres2.Slides.get_Item(j)
#             # text_box = slide.Shapes.AppendTextBox(Inches(4), Inches(0.5), Inches(8), Inches(1))
#             # text_box.textFrame.text = locations[i - 1]
#             # text_box.textFrame.paragraphs[0].font.size = 30
#
#             # pptx
#             # slide = pres2.slides[j]
#             # text_box = slide.shapes.add_textbox(Inches(4), Inches(0.5), Inches(8), Inches(1))
#             # text_frame = text_box.text_frame
#             # if text_frame:
#             #     p = text_frame.add_paragraph()
#             #     p.text = locations[i - 1]
#             #     p.font.size = Pt(30)
#             # else:
#             #     print("テキストボックスの追加に失敗しました。")
#
#
#     # pres2を一時ファイルとして保存
#     # spire.presentation
#     pres1.Slides.AppendBySlide(master_slide_7)
#     output_path = os.path.join(client_path, f"{client_dir}.pptx")
#     pres1.SaveToFile(output_path, FileFormat.Pptx2019)
#
#     # pptx
#     # pres2.save(temp_file_path)
#
#     # 一時ファイルから元のファイルを上書き
#     # os.remove(file_path)
#     # os.rename(output_path, file_path)
#
#     # 除外スライドを追加します
#     # pptx
#     # pres1.slides.add_slide(excluded_slide)
#     # pres1.Slides.Append(excluded_slide)
#
#     # spire.presentation
#     # output_path = os.path.join(client_path, f"{client_dir}.pptx")
#     # pres1.SaveToFile(output_path, FileFormat.Pptx2019)
#
#     # pptx
#     # pres1.save(output_path)
#
#     if os.path.getsize(output_path) > 18 * 1024 * 1024:
#         part_num = 1
#         with open(output_path, 'rb') as f:
#             while chunk := f.read(18 * 1024 * 1024):
#                 part_name = f"{client_dir}_{part_num}.pptx"
#                 part_path = os.path.join(client_path, part_name)
#
#                 with open(part_path, 'wb') as part_file:
#                     part_file.write(chunk)
#                 part_num += 1
#
#         os.remove(output_path)
#     else:
#         # spire.presentation
#         pres1.SaveToFile(output_path, FileFormat.Pptx2019)
#
#         # pptx
#         # pres1.save(output_path)
#
#     # spire.presentation
#     pres1.Dispose()
#
#     # pptx
#     # pres1 = None
#
#
#     for filename in files:
#         file_path = os.path.join(client_path, filename)
#         os.remove(file_path)
#
#     print(f"'{client_dir}' の処理が完了しました。")
#
# # 追加部分: テキストボックスが正しく挿入されたか確認する
# for client_dir in [d for d in os.listdir(OUTPUT_PATH) if os.path.isdir(os.path.join(OUTPUT_PATH, d))]:
#     client_path = os.path.join(OUTPUT_PATH, client_dir)
#     output_file_path = os.path.join(client_path, f"{client_dir}.pptx")
#
#     if os.path.exists(output_file_path):
#         pptx_pres = pptx_Presentation(output_file_path)
#         for i in range(2, 6):
#             pptx_slide = pptx_pres.slides[i]
#             found_test_text = False
#             for shape in pptx_slide.shapes:
#                 if shape.has_text_frame:
#                     for paragraph in shape.text_frame.paragraphs:
#                         # if "テスト" in paragraph.text:
#                         if paragraph.text:
#                             print(paragraph.text)
#                             found_test_text = True
#                             break
#             if found_test_text:
#                 print(f"スライド {i + 1} に テキストが正しく挿入されました。")
#             else:
#                 print(f"スライド {i + 1} に テキストが見つかりません。")
#
#
# # 対象ファイルの属性を変更して削除
# if os.path.exists(zip_file_path):
#     # ファイルの読み取り専用属性を解除
#     FILE_ATTRIBUTE_NORMAL = 0x80
#     ctypes.windll.kernel32.SetFileAttributesW(zip_file_path, FILE_ATTRIBUTE_NORMAL)
#
#     try:
#         os.remove(zip_file_path)
#         print(f"対象ファイル '{zip_file_name}' が削除されました。")
#     except PermissionError as e:
#         print(f"ファイル削除中にエラーが発生しました: {e}")
#
# print("すべての処理が完了しました。")





### 2024/06/10 文字列：”テスト”　検証　コード　Location名挿入処理前オリジナル　####

# import os
# import zipfile
# import shutil
# import re
# from spire.presentation import Presentation, FileFormat
# import ctypes
# from pptx import Presentation as PptxPresentation
# from pptx.util import Pt, Inches
#
# # 必要なライブラリをインストール: RW-FAT環境実行時
# # proxy = "--proxy=10.160.120.156:8080"
# # os.system(f"pip install {proxy} spire-presentation")
# # zipfile shutil は環境によってインストール
# # os.system(f"pip install {proxy} zipfile shutil spire-presentation")
#
# # 変数に格納先のパスを設定
# ZIP_FILE_DIR = "C:\\"
#
#
# # 対象ファイル名を取得、正規表現を修正
# zip_file_name_pattern = re.compile(r"webex_reports_(\d{6})_\d+\.zip")
# zip_file_name = None
# for file in os.listdir(ZIP_FILE_DIR):
#     match = zip_file_name_pattern.match(file)
#     if match:
#         zip_file_name = file
#         target_period_pass = match.group(1)
#         break
#
# if not zip_file_name:
#     print("対象ファイルが見つかりませんでした")
#     exit()
#
# zip_file_path = os.path.join(ZIP_FILE_DIR, zip_file_name)
#
# if not os.path.exists(zip_file_path):
#     print("zipファイルが存在しません")
#     exit()
#
# # パスワードの設定
# password = f"Managed-lan-{target_period_pass}"
# password_bytes = password.encode()
#
# # 出力パスと一時ディレクトリの設定
# OUTPUT_PATH = os.path.join(ZIP_FILE_DIR, f"output_{target_period_pass}")
# os.makedirs(OUTPUT_PATH, exist_ok=True)
#
# temp_dir = os.path.join(OUTPUT_PATH, "all")
# os.makedirs(temp_dir, exist_ok=True)
#
# # 圧縮ファイルを一時ディレクトリに展開
# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     zip_ref.extractall(temp_dir, pwd=password_bytes)
#
#
# # 各 ORG フォルダを元にクライアントディレクトリを作成し、ファイルを移動する
# for org_name in os.listdir(temp_dir):
#     org_path = os.path.join(temp_dir, org_name)
#     if os.path.isdir(org_path):
#         client_dir = os.path.join(OUTPUT_PATH, org_name)
#         os.makedirs(client_dir, exist_ok=True)
#
#         for file_name in os.listdir(org_path):
#             if file_name.endswith(('.pptx', '.ppt')):
#                 src_path = os.path.join(org_path, file_name)
#
#                 # ファイル名の先頭部分（最初の「-」の手前の文字列）を取得
#                 base_name = file_name.split('-')[0]
#                 if base_name == org_name:
#                     dst_path = os.path.join(client_dir, file_name)
#                 else:
#                     # フォルダ名とファイルの先頭部分が異なる場合、対応するフォルダに移動
#                     other_client_dir = os.path.join(OUTPUT_PATH, base_name)
#                     os.makedirs(other_client_dir, exist_ok=True)
#                     dst_path = os.path.join(other_client_dir, file_name)
#                 shutil.move(src_path, dst_path)
#
#         # 元のフォルダを削除
#         shutil.rmtree(client_dir)
#
# # 一時ディレクトリを削除
# shutil.rmtree(temp_dir)
#
#
# # 各クライアントディレクトリ内で処理を実行
# for client_dir in [d for d in os.listdir(OUTPUT_PATH) if os.path.isdir(os.path.join(OUTPUT_PATH, d))]:
#     client_path = os.path.join(OUTPUT_PATH, client_dir)
#     files = [f for f in os.listdir(client_path) if f.endswith(('.pptx', '.ppt'))]
#
#     if len(files) < 2:
#         print(f"2つ以上の PowerPoint ファイルが必要です。'{client_dir}' にあるファイル数: {len(files)}")
#         continue
#
#     first_file_path = os.path.join(client_path, files[0])
#     pres1 = Presentation()
#     pres1.LoadFromFile(first_file_path)
#     master_slide_7 = pres1.Slides.get_Item(6)
#     pres1.Slides.RemoveAt(6)
#
#     for filename in files[1:]:
#         file_path = os.path.join(client_path, filename)
#         pptx_pres = PptxPresentation(file_path)
#
#         for i in range(2, 6):
#             if i < len(pptx_pres.slides):
#
#                 # スライドに文字列"テスト"を追加
#                 pptx_slide = pptx_pres.slides[i]
#                 textbox = pptx_slide.shapes.add_textbox(Inches(1), Inches(1), Inches(5), Inches(1))
#                 text_frame = textbox.text_frame
#                 # 最終的にはORG-Location名を追加
#                 text_frame.text = "テスト"
#                 print(text_frame.text)
#                 text_frame.paragraphs[0].font.size = Pt(14)
#
#         pptx_pres.save(file_path)
#
#
#     pres1.Slides.AppendBySlide(master_slide_7)
#     output_path = os.path.join(client_path, f"{client_dir}.pptx")
#     pres1.SaveToFile(output_path, FileFormat.Pptx2019)
#
#     if os.path.getsize(output_path) > 18 * 1024 * 1024:
#         part_num = 1
#         with open(output_path, 'rb') as f:
#             while chunk := f.read(18 * 1024 * 1024):
#                 part_name = f"{client_dir}_{part_num}.pptx"
#                 part_path = os.path.join(client_path, part_name)
#
#                 with open(part_path, 'wb') as part_file:
#                     part_file.write(chunk)
#                 part_num += 1
#
#         os.remove(output_path)
#     else:
#         pres1.SaveToFile(output_path, FileFormat.Pptx2019)
#
#     pres1.Dispose()
#
#     for filename in files:
#         file_path = os.path.join(client_path, filename)
#         os.remove(file_path)
#
#     print(f"'{client_dir}' の処理が完了しました。")
#
# # 追加部分: テキストボックスが正しく挿入されたか確認する
# for client_dir in [d for d in os.listdir(OUTPUT_PATH) if os.path.isdir(os.path.join(OUTPUT_PATH, d))]:
#     client_path = os.path.join(OUTPUT_PATH, client_dir)
#     output_file_path = os.path.join(client_path, f"{client_dir}.pptx")
#
#     if os.path.exists(output_file_path):
#         pptx_pres = PptxPresentation(output_file_path)
#         for i in range(2, 6):
#             pptx_slide = pptx_pres.slides[i]
#             found_test_text = False
#             for shape in pptx_slide.shapes:
#                 if shape.has_text_frame:
#                     for paragraph in shape.text_frame.paragraphs:
#                         if "テスト" in paragraph.text:
#                             found_test_text = True
#                             break
#             if found_test_text:
#                 print(f"スライド {i + 1} に 'テスト' テキストが正しく挿入されました。")
#             else:
#                 print(f"スライド {i + 1} に 'テスト' テキストが見つかりません。")
#
# # 対象ファイルの属性を変更して削除
# if os.path.exists(zip_file_path):
#     # ファイルの読み取り専用属性を解除
#     FILE_ATTRIBUTE_NORMAL = 0x80
#     ctypes.windll.kernel32.SetFileAttributesW(zip_file_path, FILE_ATTRIBUTE_NORMAL)
#     try:
#         os.remove(zip_file_path)
#         print(f"対象ファイル '{zip_file_name}' が削除されました。")
#     except PermissionError as e:
#         print(f"ファイル削除中にエラーが発生しました: {e}")
#
# print("すべての処理が完了しました。")