from PIL import Image  # Pillowよりインポート
import numpy as np  # Numpyよりインポート

def trim(im, area, original_path, trimmed_path):
    # 画像を処理するためにpillowを使う
    im = Image.open(im)
    im = im.convert("RGB")

    # まず、元画像を保存
    im.save(original_path)

    # 処理① - 画像をnumpyのarrayへ変換
    im = np.array(im)

    # 処理② - データの形状をsizeとして取り出し
    size = im.shape
    # 処理③ - 高さ（行数）の半分の値
    h_half = size[0]//2
    # 処理④ - 幅（列数）の半分の値
    w_half = size[1]//2

    # 処理⑤ - areaの値によって条件分岐
    if area == 'left_top':
        # 左上の範囲のみスライスで抽出
        im = im[:h_half, :w_half]
    elif area == 'right_top':
        # 右上の範囲のみスライスで抽出
        im = im[:h_half, w_half:]
    elif area == 'left_bottom':
        # 左下の範囲のみスライスで抽出
        im = im[h_half:, 0:w_half]
    elif area == 'right_bottom':
        # 右下の範囲のみスライスで抽出
        im = im[h_half:, w_half:]

    # numpy.arrayをpillowのimageへ変換
    im = Image.fromarray(im)

    # トリミング画像パスにトリミング後の画像を保存
    im.save(trimmed_path)
    return