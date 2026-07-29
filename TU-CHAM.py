# Chấm đáp án ngay trên máy, không cần trình duyệt, không cần camera.
#     python TU-CHAM.py
#
# Nó làm hai việc: chạy đúng người-chấm-bài mà học sinh bấm phím T trong trang,
# rồi kiểm thêm mấy trường hợp mà bản chấm nhỏ kia không với tới (ảnh rộng
# hơn, ô sát mép, giá trị cộng tràn 255) và thử gọi hai hàm trong spells.py
# với một `magic_stage` giả để xem nhánh if/elif có ra đúng hiệu ứng không.

import sys, types, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent / "student"))

# ── magic_stage giả: ghi lại lệnh thay vì vẽ lên màn hình ───────────────────
da_goi = []
gia = types.ModuleType("magic_stage")
gia.play_effect = lambda ten: da_goi.append(("fx", ten))
gia.say = lambda chu: da_goi.append(("say", chu))
sys.modules["magic_stage"] = gia

import image_spells, spells

loi = []


def can(dieu_kien, mo_ta):
    print(("  ✓ " if dieu_kien else "  ✖ ") + mo_ta)
    if not dieu_kien:
        loi.append(mo_ta)


def anh(width, height, mau):
    px = []
    for row in range(height):
        for col in range(width):
            px += mau(row, col) + [255]
    return px


print("\n[1] người chấm bài trong trang (phím T)")
for dong in image_spells.kiem_tra().split("\n"):
    print("  " + dong)
    if dong.startswith("✖"):
        loi.append(dong)

print("\n[2] kiểm thêm phần xử lý ảnh")

w, h = 5, 4
px = anh(w, h, lambda r, c: [c * 5, r * 5, 100])
out = [0] * len(px)
image_spells.flip(px, out, w, h)
can(all(out[(r * w + c) * 4] == px[(r * w + (w - 1 - c)) * 4]
        for r in range(h) for c in range(w)), "flip đúng trên ảnh 5x4")

px = anh(3, 3, lambda r, c: [90, 90, 90])
out = [0] * len(px)
image_spells.blur(px, out, 3, 3)
can(all(out[(r * 3 + c) * 4] == 90 for r in range(3) for c in range(3)),
    "blur giữ nguyên ảnh phẳng, kể cả ô sát mép (chia đúng số hàng xóm)")

px = anh(2, 1, lambda r, c: [250, 10, 0])
layer = anh(2, 1, lambda r, c: [50, 10, 0] if c == 0 else [200, 0, 0])
out = [0] * len(px)
image_spells.blend(px, layer, out, 2, 1)
can(out[0] == 255 and out[1] == 20, "blend kẹp 255 riêng từng kênh màu")
can(out[4] == 255 and out[5] == 10, "blend cộng đúng ô thứ hai")

print("\n[3] bộ chọn thần chú")
for so, mong in ((1, "dragon"), (2, "phoenix"), (3, "sakura")):
    da_goi.clear()
    spells.on_fingers(so)
    can(("fx", mong) in da_goi, f"{so} ngón tay ra {mong}")
da_goi.clear()
spells.on_fingers(9)
can(da_goi and da_goi[0][0] == "say", "số chưa gán thì nói ra chứ không im lặng")

for tu, mong in (("rồng", "dragon"), ("dragon", "dragon"),
                 ("hoa", "sakura"), ("mưa", "rain"), ("rain", "rain")):
    da_goi.clear()
    spells.on_voice(tu)
    can(("fx", mong) in da_goi, f'nói "{tu}" ra {mong}')
da_goi.clear()
spells.on_voice("bâng quơ")
can(da_goi and da_goi[0][0] == "say", "từ lạ thì đọc lại cho biết máy nghe ra gì")

print("\n" + ("ĐÁP ÁN CHẠY ĐÚNG HẾT." if not loi else f"CÒN {len(loi)} CHỖ SAI."))
sys.exit(1 if loi else 0)
