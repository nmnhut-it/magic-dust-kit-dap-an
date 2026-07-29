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


def blend(image, layer, out, width, height):
    for row in range(height):
        for col in range(width):
            base = image[row][col]
            glow = layer[row][col]
            out[row][col] = [min(255, base[0] + glow[0]),
                             min(255, base[1] + glow[1]),
                             min(255, base[2] + glow[2])]


def blend_alpha(image, layer, strength, out, width, height):
    rest = 100 - strength
    for row in range(height):
        for col in range(width):
            base = image[row][col]
            top = layer[row][col]
            out[row][col] = [(base[0] * rest + top[0] * strength) // 100,
                             (base[1] * rest + top[1] * strength) // 100,
                             (base[2] * rest + top[2] * strength) // 100]


def blend_over(base, top, alpha, out, width, height):
    for row in range(height):
        for col in range(width):
            under = base[row][col]
            over = top[row][col]
            a = alpha[row][col]
            rest = 255 - a
            out[row][col] = [(over[0] * a + under[0] * rest) // 255,
                             (over[1] * a + under[1] * rest) // 255,
                             (over[2] * a + under[2] * rest) // 255]


def compose(person, mask, background, out, width, height):
    for row in range(height):
        for col in range(width):
            if mask[row][col] > 128:
                out[row][col] = person[row][col]
            else:
                out[row][col] = background[row][col]


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
