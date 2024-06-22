# Update 20240620 スライド並び替えABC（Location毎）、Location表示方法 -> ”Location:{location} 、Locationテキストボックス右上
import os
import zipfile
import shutil
import re
import ctypes
from spire.presentation import Presentation, FileFormat, ShapeType, TextAlignmentType, TextFont, FillFormatType
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
    # 20240620 改良　位置（右上）適宜調整
    left = 280.0
    top = 20.0
    width = 288.0
    height = 25.0

    text_box = slide.Shapes.AppendShape(ShapeType.Rectangle, RectangleF(PointF(left, top), SizeF(width, height)))

    # 枠線を非表示にする
    text_box.Line.Visible = False
    # ボックス内の塗りつぶしを非表示にする
    text_box.Fill.Visible = False

    # 20240620 表示変更 -> Location：location名　適宜調整
    location_text = location.split('-', 1)[-1]
    text_box.TextFrame.Text = f"Location: {location_text}"

    text_box.TextFrame.Paragraphs[0].TextRanges[0].LatinFont = TextFont("Arial") # タイトルと同じスタイル
    text_box.TextFrame.Paragraphs[0].TextRanges[0].FontHeight = 18
    text_box.TextFrame.Paragraphs[0].Alignment = TextAlignmentType.Center

def remove_location_text(slide):
    shapes_to_remove = []
    for shape in slide.Shapes:
        if hasattr(shape, 'TextFrame') and shape.TextFrame is not None and "Location:" in shape.TextFrame.Text:
            shapes_to_remove.append(shape)
    for shape in shapes_to_remove:
        slide.Shapes.Remove(shape)


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
    process_presentation(pres1, locations[0], range(0, 2))

    # スライド挿入順AAA
    # for i, filename in enumerate(files[1:], 1):
    #     file_path = os.path.join(client_dir, filename)
    #     pres2 = Presentation()
    #     pres2.LoadFromFile(file_path)
    #     process_presentation(pres2, locations[i], range(2, 6))
    #     for j in range(2, 6):
    #         slide = pres2.Slides.get_Item(j)
    #         pres1.Slides.AppendBySlide(slide)
    #     pres2.Dispose()


    # スライド挿入順序の変更、挿入順序ABC - Start
    # 1番目のファイルのスライド 2-5 を削除
    for index in range(5, 1, -1):
        pres1.Slides.RemoveAt(index)


    for slide_index in range(2, 6):
        for i, filename in enumerate(files):
            file_path = os.path.join(client_dir, filename)
            pres2 = Presentation()
            pres2.LoadFromFile(file_path)
            slide = pres2.Slides.get_Item(slide_index)
            pres1.Slides.AppendBySlide(slide)
            index = pres1.Slides.Count - 1
            process_presentation(pres1, locations[i], [index])
            pres2.Dispose()
    # スライド挿入順序の変更、挿入順序ABC - End

    # ファイル(0-1)のスライド0-1からロケーション情報を削除
    for index in range(2):
        remove_location_text(pres1.Slides.get_Item(index))

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