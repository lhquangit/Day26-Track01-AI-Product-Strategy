---
artifact: 1 - Ghi chú nghiên cứu khi test 2 sản phẩm AI
bai-tap: 2 - Phân tích 2 sản phẩm AI (nhóm 2 học viên)
phase: Phase 2 - Thử nghiệm + chụp ảnh + research
time: 20 phút
input: group-members.md
nop-cuoi: Không - file trung gian
---

# 1 - Ghi chú nghiên cứu khi test 2 sản phẩm AI

Mục tiêu của file này là ghi lại **quan sát thực tế** trong một lượt test công khai ngày **2026-05-14 12:48 +07:00**. Toàn bộ nhận định bên dưới đều chỉ dựa trên:

- ảnh chụp màn hình lưu trong `screenshots/`
- giao diện công khai truy cập được trong workspace này
- nguồn công khai hiện hành về pricing, user base và tăng trưởng

## Phần A - Setup chung

- **Nhiệm vụ chung**: Tóm tắt thị trường edtech Việt Nam năm 2024 trong 5 gạch đầu dòng, nêu 3 công ty tiêu biểu, 2 xu hướng, và gắn link nguồn cho từng ý. Nếu không chắc, hãy nói rõ.
- **Câu prompt chính xác**:

```text
Tóm tắt thị trường edtech Việt Nam năm 2024 trong 5 gạch đầu dòng. Nêu 3 công ty tiêu biểu, 2 xu hướng, và gắn link nguồn cho từng ý. Nếu không chắc, hãy nói rõ.
```

- **Loại tài khoản dùng**:
  - Sản phẩm A - Perplexity: guest / chưa đăng nhập
  - Sản phẩm B - Microsoft Copilot: guest / chưa đăng nhập
- **Môi trường test**: browser công khai trong workspace, chụp ảnh ngày 2026-05-14, múi giờ +07:00

## Phần B - Log Sản phẩm A

**Tên sản phẩm A**: Perplexity  
**URL**: https://www.perplexity.ai/  
**Model dưới mui xe**: giao diện guest chỉ hiện `Model` picker, không công khai model cụ thể ở ảnh chụp

### B.1 - Entry point + lần chạm đầu

- Trang đầu là một ô hỏi đáp dạng search-first, bên dưới có nút `Search`, `Computer`, `Model`.
- Giao diện cho thấy người dùng không cần đăng nhập để bắt đầu hỏi.
- Có overlay mời đăng nhập ở bên phải và cookie banner ở góc dưới phải, nhưng vẫn nhìn thấy rõ entry box.
- Ảnh đã chụp: `screenshots/perplexity-1-entry.png`

### B.2 - Khi gõ prompt + nhận output

- Thời gian để có output đọc được: khoảng **12 giây**.
- Sau khi nhập, prompt nằm trong cùng ô composer, không bắt người dùng đổi surface.
- Output có cấu trúc bullet, có nêu độ chắc chắn và có badge nguồn; màn hình output cho thấy `10 sources`.
- Ảnh đã chụp:
  - `screenshots/perplexity-2-input.png`
  - `screenshots/perplexity-3-output.png`
  - `screenshots/perplexity-4-source.png`

### B.3 - Phản hồi sau khi nhận output

- Có follow-up suggestions ngay bên dưới câu trả lời.
- Có dấu vết rõ ràng về citation / source count.
- Có khả năng tiếp tục hỏi tiếp trong cùng thread.
- Cookie banner vẫn tồn tại, tạo một friction nhỏ ở góc dưới phải.

### B.4 - Quan sát nổi

1. **Entry rất rõ use case "ask + search"**: người dùng nhìn thấy ngay ô hỏi đáp và nút `Search`, phù hợp tác vụ tìm kiếm có dẫn nguồn. Tham chiếu: `perplexity-1-entry.png`.
2. **Friction vật lý thấp**: chỉ cần một ô nhập và Enter là có câu trả lời, không bị yêu cầu đăng nhập hoặc xác minh người dùng trong first pass. Tham chiếu: `perplexity-2-input.png`.
3. **Trust signal tốt hơn đối thủ trong lượt test này**: output hiện `10 sources`, có follow-up, và trong câu trả lời có note độ chắc chắn. Tham chiếu: `perplexity-3-output.png`, `perplexity-4-source.png`.

## Phần C - Log Sản phẩm B

**Tên sản phẩm B**: Microsoft Copilot  
**URL**: https://copilot.microsoft.com/  
**Model dưới mui xe**: mode mặc định `Smart`, giao diện guest không hiện model chi tiết

### C.1 - Entry point + lần chạm đầu

- Trang đầu có ô `Message Copilot`, mode `Smart`, và một số starter prompts.
- Giao diện guest cho phép bắt đầu mà chưa cần đăng nhập.
- Ảnh đã chụp: `screenshots/copilot-1-entry.png`

### C.2 - Khi gõ prompt + nhận output

- Prompt được nhập thành công, nhưng ngay sau khi gửi thì giao diện bị chèn bởi cookie/privacy modal và sau đó là human verification của Cloudflare.
- Sau **16 giây chờ**, hệ thống không trả ra câu trả lời nội dung; thay vào đó là màn hình `Verify you are human`.
- Ảnh đã chụp:
  - `screenshots/copilot-2-input.png`
  - `screenshots/copilot-3-output.png`

### C.3 - Phản hồi sau khi nhận output

- Copilot có trạng thái guest, nhưng trong lượt test này không deliver được answer ở first pass.
- Có dấu hiệu friction lớn ngay giữa workflow: privacy modal + security challenge.
- Tính năng share / library / tasks hiện sẵn, cho thấy sản phẩm muốn mở rộng thành assistant đa nhiệm, không chỉ là answer engine.

### C.4 - Quan sát nổi

1. **Entry point đẹp và thân thiện**: composer lớn, starter prompts rõ, mode `Smart` nhìn dễ dùng. Tham chiếu: `copilot-1-entry.png`.
2. **Workflow bị cắt ngang sớm**: cookie modal xuất hiện đè lên ngay lúc người dùng đang test, sau đó Cloudflare challenge chặn hẳn first-turn success. Tham chiếu: `copilot-2-input.png`, `copilot-3-output.png`.
3. **Surface rộng hơn search thuần**: có `Library`, `Tasks`, `Projects`, `Imagine`, nên tham vọng sản phẩm lớn; đổi lại, first-use flow ở guest mode kém tập trung hơn Perplexity cho tác vụ "tìm nhanh và có source". Tham chiếu: `copilot-1-entry.png`.

## Phần D - First impressions

1. **Sản phẩm nào cảm giác dễ dùng hơn lần đầu?**  
   - Perplexity dễ dùng hơn trong lượt test này vì không bị cắt ngang bởi modal / challenge và đưa người dùng thẳng vào tác vụ tìm kiếm.

2. **Sản phẩm nào cho output đáng tin hơn?**  
   - Perplexity thắng theo bằng chứng quan sát được, vì nó thực sự trả ra answer, hiện source count, và nêu độ chắc chắn. Copilot không có answer để so sánh trong first pass guest mode.

3. **Câu hỏi nhóm chưa trả lời được sau 20 phút test**  
   - Copilot sẽ cho output ra sao nếu qua được challenge và đóng privacy modal?
   - Chat guest mode của Copilot có source citation nhất quán với truy vấn mang tính nghiên cứu khu vực Việt Nam không?
   - Perplexity có duy trì độ mạnh citation khi prompt chuyển sang tác vụ phức tạp hơn không?

## Nguồn business signal đã tra cứu song song

- Perplexity Pro Perks / pricing surface: https://www.perplexity.ai/properks/
- Perplexity ARR: CNBC, 2025-03-20
- Perplexity query volume growth: TechCrunch, 2025-06-05
- Microsoft Copilot official product/pricing docs:
  - https://support.microsoft.com/en-us/topic/what-s-the-difference-between-the-microsoft-copilot-experiences-cfff4791-694a-4d90-9c9c-1eb3fb28e842
  - https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals
- Microsoft Copilot user base: CNBC, 2025-07-30; TechCrunch, 2026-01-29
