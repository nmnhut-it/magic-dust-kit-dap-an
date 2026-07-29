# ============================================================================
#  ĐÁP ÁN — BÀI TẬP 2: CÁC PHÉP XỬ LÝ ẢNH, CHẠY TRÊN CHÍNH KHUÔN MẶT BẠN
#  Cùng đề bài với trang làm bài. Sửa file này rồi quay ra sân khấu bấm R để
#  nạp lại, bấm T để máy chấm.
# ============================================================================

from magic_stage import new_image

def flip(image, out, width, height):
    for row in range(height):
        for col in range(width):
            out[row][col] = image[row][width - 1 - col]


def blur(image, out, width, height):
    for row in range(height):
        for col in range(width):
            red = green = blue = count = 0
            for row_step in (-1, 0, 1):
                near_row = row + row_step
                if near_row < 0 or near_row >= height:
                    continue
                for col_step in (-1, 0, 1):
                    near_col = col + col_step
                    if near_col < 0 or near_col >= width:
                        continue
                    pixel = image[near_row][near_col]
                    red = red + pixel[0]
                    green = green + pixel[1]
                    blue = blue + pixel[2]
                    count = count + 1
            out[row][col] = [red // count, green // count, blue // count]


def compose(person, mask, background, out, width, height):
    for row in range(height):
        for col in range(width):
            if mask[row][col] > 128:
                out[row][col] = person[row][col]
            else:
                out[row][col] = background[row][col]


def blend(image, layer, out, width, height):
    for row in range(height):
        for col in range(width):
            base = image[row][col]
            glow = layer[row][col]
            out[row][col] = [min(255, base[0] + glow[0]),
                             min(255, base[1] + glow[1]),
                             min(255, base[2] + glow[2])]


def blur_background(image, mask, out, width, height):
    blurred = new_image(width, height)
    blur(image, blurred, width, height)
    compose(image, mask, blurred, out, width, height)


def scene(person, mask, background, behind, front, out, width, height):
    back_layer = new_image(width, height)
    blend(background, behind, back_layer, width, height)

    with_person = new_image(width, height)
    compose(person, mask, back_layer, with_person, width, height)

    blend(with_person, front, out, width, height)


def negative(image, out, width, height):
    for row in range(height):
        for col in range(width):
            pixel = image[row][col]
            out[row][col] = [255 - pixel[0], 255 - pixel[1], 255 - pixel[2]]


def grayscale(image, out, width, height):
    for row in range(height):
        for col in range(width):
            pixel = image[row][col]
            gray = (pixel[0] + pixel[1] + pixel[2]) // 3
            out[row][col] = [gray, gray, gray]


def flip_vertical(image, out, width, height):
    for row in range(height):
        for col in range(width):
            out[row][col] = image[height - 1 - row][col]


def drop_blue(image, out, width, height):
    for row in range(height):
        for col in range(width):
            pixel = image[row][col]
            out[row][col] = [pixel[0], pixel[1], 0]
