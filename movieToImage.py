import cv2
import os
import sys


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

    for num in range(1, int(count), int(fps) * 2):
        # print(num)
        cap.set(cv2.CAP_PROP_POS_FRAMES, num)
        ret, frame = cap.read()

        cv2.imwrite('{}_{}.{}'.format(
            base_path, str(num).zfill(digit), ext), frame)
        n += 1
    cap.release()
    return


def save_frame_sec(video_path, dir_path, sec, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    # os.makedirs(os.path.dirname(basename), exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    fps = cap.get(cv2.CAP_PROP_FPS)

    cap.set(cv2.CAP_PROP_POS_FRAMES, round(fps * sec))

    ret, frame = cap.read()
    print("a")
    if ret:
        cv2.imwrite('{}_{}.{}'.format(base_path, 10, ext), frame)


argvs = sys.argv
movie = argvs[1]

# 秒数指定
# save_frame_sec(movie, './data/temp/result', 1, 'result_sec.jpg')

# 全フレーム
save_all_frames(movie,
                './data/temp/result', 'sample_video_img')
# save_all_frames(movie,
#                 './data/temp/result_png', 'sample_video_img', 'png')
