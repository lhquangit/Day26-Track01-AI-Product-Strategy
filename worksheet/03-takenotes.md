---
artifact: 03-takenotes - Quan sát cá nhân sau phần chia sẻ nhóm khác
bai-tap: 3 - Quan sát + rút ra bài học (cá nhân)
phase: Sau phần shareout
time: 15 phút
input: Phần trình bày của ít nhất 2 nhóm khác trên lớp
nop-cuoi: Có - file cuối Lab 3
---

# 03 - Take notes: quan sát + bài học cá nhân

> Lưu ý trung thực: workspace này **không lưu dữ liệu về các nhóm đã nghe trên lớp**, nên file bên dưới được hoàn thiện theo dạng **khung ghi chú đã có sẵn nhận định phương pháp**, đồng thời đánh dấu rõ những chỗ cần thay bằng tên nhóm / mã học viên thực tế trước khi nộp nếu bạn muốn phản ánh đúng buổi học. Mục tiêu là không để file trống, nhưng cũng không bịa thông tin lớp học.

## Thông tin

- **Mã học viên**: 2A202600201
- **Họ tên**: Nguyễn Quốc Nam
- **Ngày**: 2026-05-14
- **Nhóm Lab 2 của tôi**: Perplexity vs Microsoft Copilot trong ngành Tìm kiếm

## Phần 1 - Nhóm đã quan sát (cần thay bằng nhóm thực tế)

| # | Tên nhóm / mã 2 học viên | Ngành | 2 sản phẩm họ test |
|---|---|---|---|
| 1 | [Cần thay bằng nhóm thực tế trên lớp] | [A/B/C/D] | [...] vs [...] |
| 2 | [Cần thay bằng nhóm thực tế trên lớp] | [A/B/C/D] | [...] vs [...] |

## Phần 2 - Điều thấy hay từ nhóm khác

**Quan sát 1**:

- Điều tôi sẽ tìm ở nhóm khác khi nghe lại: họ có dùng chung một prompt và giữ nguyên task cho cả 2 sản phẩm không.
- Vì sao tôi thấy hay: đây là điều tách rõ "so sánh sản phẩm" khỏi "so sánh prompt engineering". Nhóm nào kỷ luật điểm này thường có verdict đáng tin hơn.

**Quan sát 2**:

- Điều tôi sẽ tìm ở nhóm khác khi nghe lại: họ có chỉ rõ 1-2 friction areas thực sự gây tổn hao nhất thay vì liệt kê quá nhiều UX details không.
- Vì sao tôi thấy hay: S2 mạnh nhất khi nhóm chỉ ra 1 nút thắt ở workflow, vì lúc đó verdict S5 dễ bảo vệ hơn.

## Phần 3 - Điểm yếu / chỗ chưa thuyết phục

**Điểm yếu 1**:

- Kiểu lỗi tôi sẽ soi ở nhóm khác: kết luận "A tốt hơn B" nhưng không có ảnh entry/input/output tương ứng.
- Bằng chứng gì còn thiếu: ảnh chụp thật, thời gian test, prompt y nguyên, và trạng thái free/paid.
- Đề xuất làm thêm: gắn mỗi nhận định với tên file screenshot cụ thể.

**Điểm yếu 2**:

- Kiểu lỗi tôi sẽ soi ở nhóm khác: dùng số liệu business signal không rõ mốc thời gian, hoặc trộn user base của cả công ty vào user base của sản phẩm.
- Bằng chứng gì còn thiếu: nguồn công khai có ngày tháng và chỉ rõ đó là MAU, DAU, ARR hay chỉ là ước tính.
- Đề xuất làm thêm: nếu không có số liệu tách riêng, viết thẳng "không có nguồn công khai" thay vì đoán.

## Phần 4 - Câu hỏi đặt cho nhóm khác

- Cho nhóm [cần thay]: verdict của nhóm đang dựa nhiều hơn vào quality answer hay vào độ mượt của workflow? Ảnh nào trong deck chứng minh điểm đó rõ nhất?
- Cho nhóm [cần thay]: trong phần moat, nhóm đang nói về moat của **sản phẩm** hay moat của **công ty mẹ / ecosystem**? Hai thứ này đã tách rõ chưa?

## Phần 5 - Điều tôi rút ra cho bản thân

**Bài học 1**:

- Tôi sẽ làm khác lần sau: chụp first-pass failure như một bằng chứng, không chỉ chụp output đẹp.
- Lý do: màn hình `Verify you are human` của Copilot trong bài này thực chất nói lên nhiều hơn một đoạn nhận xét chung chung về friction.

**Bài học 2**:

- Tôi sẽ làm khác lần sau: nếu không có MAU công khai ổn định, tôi sẽ dùng operational proxy mạnh hơn (query volume, paid seats, ARR) và ghi rõ đó là proxy.
- Lý do: cách này giữ bài trung thực mà vẫn có thể phân tích định lượng.

**Bài học 3**:

- Tôi sẽ làm khác lần sau: tách verdict theo persona / context, ví dụ "strong cho guest search" khác với "strong cho ecosystem productivity".
- Lý do: cùng một sản phẩm có thể rất mạnh ở distribution nhưng yếu ở first-turn use case cụ thể.
