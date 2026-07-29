# Magic Dust — Đáp Án

Đây là bản đã làm xong của cả bài chính lẫn bốn bài thêm trong
[**bộ đồ nghề**](https://github.com/nmnhut-it/magic-dust-kit). Thả hai file vào
là phép chạy được ngay: giơ 1 ngón ra rồng, 2 ngón ra phượng hoàng, 3 ngón ra
hoa anh đào, nói "mưa" thì mưa rơi, và ba phím `F` `B` `N` lật / làm mờ / ghép
lớp hiệu ứng lên chính khuôn mặt bạn.

> **Đã làm bài rồi hãy mở.** Cái đáng học nằm ở lúc tự viết `if / elif / else`
> và tự tìm ra vì sao ảnh bị vệt lạ, không nằm ở việc có file chạy được.

---

## Dùng thế nào

**Windows:** kéo thư mục `magic-dust-kit` thả vào **`CHEP-VAO.bat`**. Nó cất bài
cũ của bạn sang `student/bai-cua-toi/` rồi chép đáp án vào chỗ của nó.

**Cách nào cũng được:** chép tay hai file trong `student/` của repo này đè lên
`student/` của bộ đồ nghề.

```
magic-dust-kit/student/spells.py        <- student/spells.py
magic-dust-kit/student/image_spells.py  <- student/image_spells.py
```

Xong thì bấm đúp `CHAY.bat` trong bộ đồ nghề, chờ dòng `Python sẵn sàng`, bấm
phím `T` — phải thấy ba dòng `✓ flip` `✓ blur` `✓ blend`. Trang đang mở sẵn thì
chỉ cần bấm `R`, không phải tải lại.

---

## Kiểm luôn trên máy, khỏi cần trình duyệt

```bash
python TU-CHAM.py
```

Chạy được ngay cả khi máy không có camera và chưa cài gì thêm — nó dựng một
`magic_stage` giả rồi gọi thẳng vào hai file đáp án. Đây là cùng một bộ chấm mà
bộ đồ nghề chạy lúc bật `serve.py` và lúc bạn bấm `T` trong trang. Kết quả thật:

```
  ✓ flip
  ✓ blur
  ✓ blend
  ✓ negative
  ✓ grayscale
  ✓ flip_vertical
  ✓ drop_blue
  ✓ 1 ngón tay ra dragon
  ✓ 2 ngón tay ra phoenix
  ✓ 3 ngón tay ra sakura
  ✓ số chưa gán phép thì phải nói ra chứ không im lặng
  ✓ nói "rồng" ra dragon
  ...
XONG HET BAI.
```

---

## Bốn chỗ đáng đọc kỹ trong đáp án

**`else` luôn nằm cuối.** Nó là nhánh "không khớp cái nào ở trên", nên đặt nó
lên trước thì mấy `elif` phía sau không bao giờ tới lượt.

**Đọc `px`, ghi `out` — đừng ghi đè lên `px`.** Viết gọn thành `px[o] = px[f]`
trông có vẻ ổn, nhưng nửa ảnh sau sẽ lật đè lên phần vừa bị chính bạn sửa.

**`blur` chia cho `dem`, không chia cứng cho 9.** Ô sát mép chỉ có 4 hoặc 6
hàng xóm; chia cho 9 thì cả viền ảnh tối sầm lại.

**Chỉ số âm trong Python không báo lỗi.** `px[-4]` đếm ngược từ cuối danh sách,
nên nếu quên `continue` khi ra ngoài ảnh thì máy im lặng và ảnh mọc vệt lạ ở
mép. Loại lỗi khó tìm nhất là loại không có thông báo lỗi.

---

## Muốn đi xa hơn

Bốn bài thêm ở cuối `image_spells.py` (`negative`, `grayscale`,
`flip_vertical`, `drop_blue`) đều ngắn hơn `blur` — đọc xong thì tự viết phép
thứ năm: nửa ảnh soi gương, tăng tương phản, hay đổi chỗ hai kênh màu.

Đáp án mới dùng ba trong mười một hiệu ứng có sẵn (`dragon` `koto` `rose`
`phoenix` `butterfly` `sakura` `smoke` `rain` `flower` `magic` `lightning`).
Thêm một nhánh `elif` là thêm một phép. Muốn hiệu ứng của riêng mình thì tự
quay hoặc nhờ Gemini tạo video nền đen — xem `TAO-VIDEO-HIEU-UNG.md` trong bộ
đồ nghề.

Đáp án cho `blur` ở đây là trung bình 3×3. Thử đổi thành 5×5 xem mờ tới đâu, và
để ý máy chậm đi bao nhiêu — đó là lý do bộ đồ nghề chạy ảnh ở 96×72.

---

Cắt từ dự án Magic Dust của thầy Nhựt — <https://nmnhut.dev/magic-dust/>.
