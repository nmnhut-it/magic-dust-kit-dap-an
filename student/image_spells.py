# ============================================================================
#  ĐÁP ÁN — BÀI TẬP 2: BA PHÉP XỬ LÝ ẢNH (+ bốn bài thêm)
#  Chép file này đè lên `student/image_spells.py` trong bộ đồ nghề.
#  Mở trang, bấm  T  để máy tự chấm — phải ✓ hết.
#  Bấm  F lật · B mờ · N ghép · A âm bản · W đen trắng · V lật dọc ·
#       C tắt xanh dương · X tắt · R nạp lại file.
# ============================================================================
#
# KHUNG HÌNH Ở ĐÂY LÀ GÌ
# Máy đưa một danh sách số rất dài tên là `px`. Mỗi ô ảnh chiếm 4 số liền nhau:
#
#     px[o]     đỏ           px[o + 1] xanh lá
#     px[o + 2] xanh dương   px[o + 3] độ đục (cứ để 255)
#
# Ô ở hàng `row`, cột `col` bắt đầu tại:  o = (row * width + col) * 4
#
# Kết quả ghi vào `out` — danh sách khác, cùng độ dài. KHÔNG ghi đè lên `px`:
# nửa ảnh sau sẽ đọc nhầm phần vừa bị sửa.
# ---------------------------------------------------------------------------


# ── LẬT NGANG ───────────────────────────────────────────────────────────────
# Ô ở cột `col` lấy màu của ô cột `width - 1 - col` trong CÙNG hàng.
# Cột 0 lấy cột cuối, cột cuối lấy cột 0 — đúng như soi gương.
def flip(px, out, width, height):
    for row in range(height):
        for col in range(width):
            o = (row * width + col) * 4                       # chỗ ghi
            source = (row * width + (width - 1 - col)) * 4    # chỗ lấy màu
            out[o] = px[source]
            out[o + 1] = px[source + 1]
            out[o + 2] = px[source + 2]


# ── LÀM MỜ ──────────────────────────────────────────────────────────────────
# Mỗi ô lấy màu trung bình của chính nó và các ô hàng xóm sát bên.
#
# Hai chỗ dễ sai:
#   · Ô sát mép chỉ có 4 hoặc 6 hàng xóm. Chia cứng cho 9 thì viền ảnh tối
#     sầm lại, nên phải đếm `count` rồi chia cho `count`.
#   · `near_row`/`near_col` âm trong Python KHÔNG báo lỗi — nó đếm ngược từ
#     cuối danh sách, ảnh sẽ có vệt lạ mà máy im lặng. Phải `continue` khi ra
#     ngoài ảnh.
def blur(px, out, width, height):
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
                    i = (near_row * width + near_col) * 4
                    red += px[i]
                    green += px[i + 1]
                    blue += px[i + 2]
                    count += 1
            o = (row * width + col) * 4
            out[o] = red // count
            out[o + 1] = green // count
            out[o + 2] = blue // count


# ── GHÉP HAI LỚP ────────────────────────────────────────────────────────────
# `layer` là lớp hiệu ứng quay trên nền đen, cùng kích thước khung hình.
# Cộng ánh sáng chứ không dán đè: ô đen của lớp cộng vào 0 nên nền giữ nguyên,
# ô sáng đẩy nền sáng lên. Cộng quá 255 thì kẹp lại bằng min(255, ...) — và
# kẹp riêng từng kênh màu, vì mỗi kênh vượt ngưỡng một kiểu khác nhau.
def blend(px, layer, out, width, height):
    for i in range(0, len(px), 4):
        out[i] = min(255, px[i] + layer[i])
        out[i + 1] = min(255, px[i + 1] + layer[i + 1])
        out[i + 2] = min(255, px[i + 2] + layer[i + 2])


# ============================================================================
#  BÀI THÊM — bốn phép nữa. Cả bốn đều ngắn hơn `blur`.
# ============================================================================


# ── ÂM BẢN ─────────────────── phím A ───────────────────────────────────────
# Sáng thành tối, tối thành sáng. Ô đang là 0 hoá 255, đang 255 hoá 0.
def negative(px, out, width, height):
    for i in range(0, len(px), 4):
        out[i] = 255 - px[i]
        out[i + 1] = 255 - px[i + 1]
        out[i + 2] = 255 - px[i + 2]


# ── ĐEN TRẮNG ──────────────── phím W ───────────────────────────────────────
# Ba kênh phải BẰNG NHAU thì mắt mới thấy là ảnh xám. Lấy trung bình cộng rồi
# ghi cùng con số đó vào cả ba — tính một lần, dùng ba lần.
def grayscale(px, out, width, height):
    for i in range(0, len(px), 4):
        gray = (px[i] + px[i + 1] + px[i + 2]) // 3
        out[i] = gray
        out[i + 1] = gray
        out[i + 2] = gray


# ── LẬT DỌC ────────────────── phím V ───────────────────────────────────────
# Giống `flip` nhưng đổi `row` thay vì `col`: hàng trên cùng lấy màu hàng dưới
# cùng. Vẫn phải đọc `px` ghi `out`, không ghi đè.
def flip_vertical(px, out, width, height):
    for row in range(height):
        for col in range(width):
            o = (row * width + col) * 4
            source = ((height - 1 - row) * width + col) * 4
            out[o] = px[source]
            out[o + 1] = px[source + 1]
            out[o + 2] = px[source + 2]


# ── TẮT MỘT KÊNH MÀU ───────── phím C ───────────────────────────────────────
# Chép nguyên đỏ và xanh lá, cho xanh dương bằng 0. Cả khung hình ngả vàng cam
# — bằng chứng ba con số đó thật sự là ba màu riêng chứ không phải một.
def drop_blue(px, out, width, height):
    for i in range(0, len(px), 4):
        out[i] = px[i]
        out[i + 1] = px[i + 1]
        out[i + 2] = 0

# ============================================================================
#  NGƯỜI CHẤM BÀI — bấm phím T. Đừng sửa phần dưới đây.
#  Nó dựng mấy ảnh tí hon rồi kiểm từng hàm trên, và nói bạn sai ở đâu.
# ============================================================================

def _solid(width, height, red, green, blue):
    """Ảnh mà mọi ô đều cùng một màu."""
    px = []
    for _ in range(width * height):
        px.append(red)
        px.append(green)
        px.append(blue)
        px.append(255)
    return px


def _column_stripes(width, height, step):
    """Mỗi cột một sắc đỏ khác nhau, để nhìn ra ảnh có bị lật ngang không."""
    px = []
    for row in range(height):
        for col in range(width):
            px.append(col * step)
            px.append(row)
            px.append(7)
            px.append(255)
    return px


def _row_stripes(width, height, step):
    """Mỗi hàng một sắc đỏ khác nhau, để nhìn ra ảnh có bị lật dọc không."""
    px = []
    for row in range(height):
        for col in range(width):
            px.append(row * step)
            px.append(col)
            px.append(7)
            px.append(255)
    return px


def _white_dot(side):
    """Ảnh đen với đúng một ô trắng ở giữa — để thấy blur có lan sáng không."""
    px = []
    middle = side // 2
    for row in range(side):
        for col in range(side):
            if row == middle and col == middle:
                light = 255
            else:
                light = 0
            px.append(light)
            px.append(light)
            px.append(light)
            px.append(255)
    return px


def check_all():
    report = []

    px = _column_stripes(3, 2, 10)
    out = [255] * len(px)
    flip(px, out, 3, 2)
    expected = []
    for row in range(2):
        for col in range(3):
            expected.append((2 - col) * 10)
            expected.append(row)
            expected.append(7)
            expected.append(255)
    if out == expected:
        report.append("✓ flip")
    else:
        report.append("✖ flip: ô cột col phải lấy màu của cột width - 1 - col")

    px = _white_dot(3)
    out = [255] * len(px)
    blur(px, out, 3, 3)
    middle = out[(1 * 3 + 1) * 4]
    corner = out[0]
    if middle >= 250:
        report.append("✖ blur: ô giữa vẫn trắng nguyên — chưa lấy trung bình với hàng xóm")
    elif corner == 0:
        report.append("✖ blur: ô góc vẫn đen — ánh sáng chưa lan sang hàng xóm")
    else:
        report.append("✓ blur")

    px = _solid(2, 1, 200, 10, 0)
    layer = [0, 0, 0, 255, 100, 100, 100, 255]      # ô đầu đen, ô sau xám sáng
    out = [255] * len(px)
    blend(px, layer, out, 2, 1)
    if out[0] != 200 or out[1] != 10:
        report.append("✖ blend: ô đen của lớp hiệu ứng phải giữ nguyên nền")
    elif out[4] != 255:
        report.append("✖ blend: ô sáng phải cộng vào nền rồi kẹp ở 255")
    else:
        report.append("✓ blend")

    report.append("— bài thêm —")

    px = _solid(2, 1, 0, 100, 255)
    out = [255] * len(px)
    negative(px, out, 2, 1)
    if out[0:3] == [255, 155, 0]:
        report.append("✓ negative")
    else:
        report.append("✖ negative: mỗi kênh phải là 255 trừ đi giá trị cũ")

    px = _solid(2, 1, 30, 60, 90)
    out = [255] * len(px)
    grayscale(px, out, 2, 1)
    if out[0] == out[1] == out[2] == 60:
        report.append("✓ grayscale")
    elif out[0] == out[1] == out[2]:
        report.append("✖ grayscale: ba kênh đã bằng nhau nhưng chưa phải trung bình cộng")
    else:
        report.append("✖ grayscale: ảnh đen trắng thì ba kênh màu phải bằng nhau")

    px = _row_stripes(2, 3, 40)
    out = [255] * len(px)
    flip_vertical(px, out, 2, 3)
    expected = []
    for row in range(3):
        for col in range(2):
            expected.append((2 - row) * 40)
            expected.append(col)
            expected.append(7)
            expected.append(255)
    if out == expected:
        report.append("✓ flip_vertical")
    else:
        report.append("✖ flip_vertical: ô hàng row phải lấy màu của hàng height - 1 - row")

    px = _solid(2, 1, 200, 150, 100)
    out = [255] * len(px)
    drop_blue(px, out, 2, 1)
    if out[0:3] == [200, 150, 0]:
        report.append("✓ drop_blue")
    else:
        report.append("✖ drop_blue: giữ nguyên đỏ và xanh lá, chỉ kênh xanh dương bằng 0")

    return "\n".join(report)
