import cv2
import os
import sys
import argparse


def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    # 情報表示
    # 幅
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # 高さ
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # 総フレーム数
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # fps
    fps = cap.get(cv2.CAP_PROP_FPS)
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("width:{}, height:{}, count:{}, fps:{}".format(
        width, height, count, fps))

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    n = 0

    for num in range(1, int(count), int(fps) * 4):
        # print(num)
        cap.set(cv2.CAP_PROP_POS_FRAMES, num)
        ret, frame = cap.read()

        cv2.imwrite('{}_{}.{}'.format(
            base_path, str(num).zfill(digit), ext), frame)
        n += 1
    cap.release()
    return


# オプションの設定
parser = argparse.ArgumentParser()

parser.add_argument(
    "--movie_dir",
    type=str,
    default="./movie",
    help="The path of moving detected files."
)

parser.add_argument(
    "--movie",
    type=str,
    default="sample.mp4",
    help="The path of moving detected files."
)

parser.add_argument(
    "--output_dir",
    type=str,
    default="./input",
    help="The path of moving detected files."
)


# パラメータ取得と実行
FLAGS, unparsed = parser.parse_known_args()

# 読み込み元動画ディレクトリ
input_path = FLAGS.movie_dir + "/" + FLAGS.movie

# 出力先ディレクトリ
output_path = FLAGS.output_dir + "/" + FLAGS.movie
if not os.path.exists(output_path):
    os.mkdir(output_path)

# 全フレーム
save_all_frames(input_path,
                output_path, FLAGS.movie)
