# ============================================================================
#  ĐÁP ÁN — BÀI TẬP 1: BỘ CHỌN THẦN CHÚ
#  Chép file này đè lên `student/spells.py` trong bộ đồ nghề là chạy được ngay.
#  Sửa xong nhớ quay ra trang web bấm phím  R  để nạp lại.
# ============================================================================
#
# Gương cho hai lệnh:
#     play_effect("dragon")   mở một lớp hiệu ứng quay sẵn lên khung hình
#     say("chữ gì đó")        hiện một dòng chữ ở góc màn hình
#
# Tên hiệu ứng dùng được:
#     dragon · koto · rose · phoenix · butterfly · sakura · smoke · rain
#     flower · magic · lightning
#
# ---------------------------------------------------------------------------

from magic_stage import play_effect, say


# ── GIƠ MẤY NGÓN TAY THÌ RA PHÉP GÌ ─────────────────────────────────────────
# Máy đếm số ngón tay giơ lên camera rồi gọi hàm này, đưa vào số đó.
# Chuỗi if / elif / else chạy từ trên xuống: gặp điều kiện đúng đầu tiên thì
# làm việc của nhánh đó rồi bỏ qua hết phần còn lại.
def on_fingers(count):
    if count == 1:
        play_effect("dragon")
    elif count == 2:
        play_effect("phoenix")
    elif count == 3:
        play_effect("sakura")
    else:
        say("chưa gán phép cho số này")


# ── NÓI GÌ THÌ RA PHÉP GÌ ───────────────────────────────────────────────────
# Micro nghe được một từ thì máy gọi hàm này và đưa vào từ đó, đã chuyển sang
# chữ thường. Vẫn là if / elif / else, chỉ khác chỗ so sánh chuỗi thay vì số.
#
# `or` cho phép một nhánh nhận nhiều từ: nói tiếng Việt hay tiếng Anh đều ra
# đúng phép. Chú ý dấu tiếng Việt — "rong" không khớp "rồng".
def on_voice(word):
    if word == "rồng" or word == "dragon":
        play_effect("dragon")
    elif word == "hoa" or word == "sakura":
        play_effect("sakura")
    elif word == "mưa" or word == "rain":
        play_effect("rain")
    else:
        say("nghe được: " + word)


# ============================================================================
#  Muốn thêm phép của mình: viết thêm một nhánh `elif`, đặt TRƯỚC `else`.
#  Ví dụ 4 ngón tay ra bươm bướm:
#
#      elif count == 4:
#          play_effect("butterfly")
#
#  `else` phải nằm cuối cùng, vì nó là nhánh "không khớp cái nào ở trên".
# ============================================================================
