import cv2
import numpy as np
from tqdm import tqdm


def create_color_transition_video(colors, output_file, fps=30):
    width, height = 1280, 720
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    black = np.array([0, 0, 0])
    colors_bgr = [np.array(color)[::-1] * 255 / 100 for color in colors]

    # 各色の表示時間（秒）
    color_duration = 10
    # フェードイン・アウトの時間（秒）
    fade_duration = 5

    total_frames = int((len(colors) * color_duration + fade_duration) * fps)

    for i in tqdm(range(total_frames)):
        time = i / fps
        current_color = black

        # 最初のフェードイン処理
        if time < fade_duration:
            progress = time / fade_duration
            current_color = interpolate(black, colors_bgr[0], progress)
        else:
            # フェードイン後の時間
            time -= fade_duration
            # 現在の色インデックスを計算
            color_index = int(time // color_duration)
            # 現在の色セグメント内での経過時間
            time_in_segment = time % color_duration

            # 最後の色へのフェードアウト処理
            if (
                color_index == len(colors) - 1
                and time_in_segment > color_duration - fade_duration
            ):
                progress = (color_duration - time_in_segment) / fade_duration
                current_color = interpolate(colors_bgr[-1], black, progress)
            # 色の変化処理
            elif color_index < len(colors) - 1:
                progress = time_in_segment / color_duration
                current_color = interpolate(
                    colors_bgr[color_index], colors_bgr[color_index + 1], progress
                )
            else:
                current_color = colors_bgr[-1]

        frame = np.full((height, width, 3), current_color, dtype=np.uint8)
        out.write(frame)

    out.release()


def interpolate(color1, color2, progress):
    return color1 * (1 - progress) + color2 * progress


# Parse color data
colors = [
    (28, 57, 86),
    (31, 63, 95),
    (27, 54, 81),
    (27, 54, 81),
    (26, 52, 79),
    (24, 49, 73),
    (24, 48, 73),
    (21, 43, 65),
    (31, 62, 93),
    (28, 57, 85),
    (29, 59, 88),
    (30, 61, 92),
    (36, 72, 108),
    (34, 69, 104),
    (33, 66, 99),
    (29, 58, 87),
    (26, 52, 79),
    (22, 45, 67),
    (30, 60, 91),
    (29, 58, 88),
    (33, 67, 100),
    (25, 50, 75),
    (49, 98, 148),
    (60, 121, 182),
    (42, 84, 126),
    (36, 73, 109),
    (25, 50, 75),
    (36, 73, 109),
    (40, 81, 122),
    (42, 84, 126),
    (31, 62, 93),
    (26, 53, 80),
    (34, 69, 104),
    (45, 91, 137),
    (19, 38, 57),
    (19, 39, 58),
    (16, 32, 49),
    (17, 34, 52),
    (16, 32, 49),
    (19, 39, 58),
    (23, 46, 70),
    (18, 36, 54),
    (14, 28, 43),
    (30, 60, 90),
    (18, 36, 55),
    (43, 87, 131),
    (53, 107, 161),
    (55, 110, 165),
    (53, 107, 160),
    (53, 106, 159),
    (50, 101, 152),
    (48, 96, 144),
    (45, 91, 137),
    (44, 89, 133),
    (40, 81, 122),
    (41, 83, 125),
    (41, 83, 124),
    (39, 79, 118),
    (35, 71, 106),
    (39, 79, 118),
    (32, 64, 96),
    (35, 71, 107),
    (34, 69, 104),
    (34, 68, 102),
    (47, 95, 143),
    (47, 94, 142),
    (39, 78, 117),
    (41, 82, 123),
    (28, 57, 85),
    (25, 51, 77),
    (25, 51, 77),
    (24, 48, 73),
    (25, 50, 75),
    (24, 48, 73),
]

# Create video
create_color_transition_video(colors, "color_transition.mp4")

print("Video generation complete. Output file: color_transition.mp4")
