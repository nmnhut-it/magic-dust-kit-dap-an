# ============================================================================
#  ĐÁP ÁN — BÀI TẬP 2: BA PHÉP XỬ LÝ ẢNH
#  Chép file này đè lên `student/image_spells.py` trong bộ đồ nghề.
#  Mở trang, bấm  T  để máy tự chấm — phải ra ba dòng ✓.
#  Bấm  F  lật · B làm mờ · N ghép lớp · X tắt · R nạp lại file.
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
            o = (row * width + col) * 4                  # chỗ ghi
            f = (row * width + (width - 1 - col)) * 4    # chỗ lấy màu
            out[o] = px[f]
            out[o + 1] = px[f + 1]
            out[o + 2] = px[f + 2]


# ── LÀM MỜ ──────────────────────────────────────────────────────────────────
# Mỗi ô lấy màu trung bình của chính nó và các ô hàng xóm sát bên.
#
# Hai chỗ dễ sai:
#   · Ô sát mép chỉ có 4 hoặc 6 hàng xóm. Chia cứng cho 9 thì viền ảnh tối
#     sầm lại, nên phải đếm `dem` rồi chia cho `dem`.
#   · `nr` hoặc `nc` âm trong Python KHÔNG báo lỗi — nó đếm ngược từ cuối
#     danh sách, ảnh sẽ có vệt lạ mà máy im lặng. Phải `continue` khi ra ngoài.
def blur(px, out, width, height):
    for row in range(height):
        for col in range(width):
            do = xanh_la = xanh_duong = dem = 0
            for dr in (-1, 0, 1):
                nr = row + dr
                if nr < 0 or nr >= height:
                    continue
                for dc in (-1, 0, 1):
                    nc = col + dc
                    if nc < 0 or nc >= width:
                        continue
                    i = (nr * width + nc) * 4
                    do += px[i]
                    xanh_la += px[i + 1]
                    xanh_duong += px[i + 2]
                    dem += 1
            o = (row * width + col) * 4
            out[o] = do // dem
            out[o + 1] = xanh_la // dem
            out[o + 2] = xanh_duong // dem


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
#  NGƯỜI CHẤM BÀI — bấm phím T. Giữ nguyên phần dưới đây.
# ============================================================================

def _anh(width, height, mau):
    px = []
    for row in range(height):
        for col in range(width):
            px += mau(row, col) + [255]
    return px


def kiem_tra():
    ket_qua = []

    px = _anh(3, 2, lambda r, c: [c * 10, r, 7])
    out = [255] * len(px)
    flip(px, out, 3, 2)
    mong_doi = _anh(3, 2, lambda r, c: [(2 - c) * 10, r, 7])
    ket_qua.append("✓ flip" if out == mong_doi
                   else "✖ flip: ô cột col phải lấy màu của cột width - 1 - col")

    px = _anh(3, 3, lambda r, c: [255, 255, 255] if (r == 1 and c == 1) else [0, 0, 0])
    out = [255] * len(px)
    blur(px, out, 3, 3)
    giua = out[(1 * 3 + 1) * 4]
    goc = out[0]
    if giua >= 250:
        ket_qua.append("✖ blur: ô giữa vẫn trắng nguyên — chưa lấy trung bình với hàng xóm")
    elif goc == 0:
        ket_qua.append("✖ blur: ô góc vẫn đen — ánh sáng chưa lan sang hàng xóm")
    else:
        ket_qua.append("✓ blur")

    px = _anh(2, 1, lambda r, c: [200, 10, 0])
    layer = _anh(2, 1, lambda r, c: [0, 0, 0] if c == 0 else [100, 100, 100])
    out = [255] * len(px)
    blend(px, layer, out, 2, 1)
    if out[0] != 200 or out[1] != 10:
        ket_qua.append("✖ blend: ô đen của lớp hiệu ứng phải giữ nguyên nền")
    elif out[4] != 255:
        ket_qua.append("✖ blend: ô sáng phải cộng vào nền rồi kẹp ở 255")
    else:
        ket_qua.append("✓ blend")

    return "\n".join(ket_qua)
