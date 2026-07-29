# ============================================================================
#  ĐÁP ÁN — BÀI TẬP 1: BỘ CHỌN THẦN CHÚ VÀ BẢNG NÚT CỦA BẠN
#  Cùng đề bài với trang làm bài. Sửa xong lưu file rồi bấm R ở sân khấu.
# ============================================================================

from magic_stage import play_effect, say, add_button


def setup():
    add_button("Rồng Lửa", "dragon")
    add_button("Phượng Hoàng", "phoenix")
    add_button("Hoa Anh Đào", "sakura")
    add_button("Mưa Giông", "rain")


def on_fingers(count):
    if count == 1:
        play_effect("dragon")
    elif count == 2:
        play_effect("phoenix")
    elif count == 3:
        play_effect("sakura")
    else:
        say("chưa gán phép cho số này")


def on_voice(word):
    if word == "rồng" or word == "dragon":
        play_effect("dragon")
    elif word == "hoa" or word == "sakura":
        play_effect("sakura")
    elif word == "mưa" or word == "rain":
        play_effect("rain")
    else:
        say("nghe được: " + word)
