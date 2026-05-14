---
artifact: 2 - Bảng so sánh 2 sản phẩm theo 5 mục
bai-tap: 2 - Phân tích 2 sản phẩm AI
phase: Chuyển giao Phase 2 -> Phase 3
input: 1-research-notes.md + screenshots/
nop-cuoi: Không - file trung gian
---

# 2 - Bảng so sánh 2 sản phẩm theo 5 mục slide deck

## Phần A - Bảng so sánh 5 mục

| Mục | Sản phẩm A - Perplexity | Sản phẩm B - Microsoft Copilot |
|---|---|---|
| **S1 - Product Moment** | Search-native answer engine; entry point là ô `Ask anything` và nút `Search`, không cần đăng nhập để thử ngay. | Assistant surface rộng hơn search; entry point đẹp, có starter prompts, nhưng không tập trung bằng Perplexity cho tác vụ tìm kiếm có source. |
| **S2 - Workflow Evidence** | 1 ô nhập -> Enter -> output trong khoảng 12 giây -> follow-up suggestions. Ít bước hơn, ít tab-hop hơn. | 1 ô nhập -> Enter -> privacy modal + human verification. Workflow bị đứt đoạn trước khi có answer. |
| **S3 - Output & Trust** | Có output thật, có note uncertainty, hiện `10 sources`, và giữ thread để hỏi tiếp. | Không có output nội dung trong first pass guest mode, nên trust signal bị thua ngay từ gate đầu vào. |
| **S4 - Business Signal** | Định vị "mạnh hơn free search" với upsell Pro; trang official Perks nhấn mạnh `just $20/month`. | Consumer chat free, nhưng Microsoft đẩy giá trị trả phí vào hệ sinh thái Microsoft 365; pricing chính thức thể hiện gói cả năm và higher usage trong app suite. |
| **S5 - Product Judgment** | **Strong** cho use case search nhanh có citation. | **Promising / At Risk for guest research use**: tham vọng lớn, distribution lớn, nhưng first-use friction trong lượt test này quá cao. |

## Phần B - Đối chiếu 3 friction areas

- **Physical load**: Perplexity có ít click hơn; Copilot bị thêm modal và challenge nên số thao tác "không tạo giá trị" tăng lên.
- **Cognitive burden**: Perplexity framing rất rõ "ask + search"; Copilot buộc người dùng xử lý thêm context về mode, prompt cards, và gate verification.
- **User workarounds**: Với Perplexity, workaround chủ yếu là bỏ qua cookie/sign-in overlay. Với Copilot, workaround cần vượt qua human verification, nhưng điều này đã vượt quá mức "first-turn smoothness".

## Phần C - Đối chiếu 6 trust signals

| Tín hiệu đáng tin | Perplexity | Microsoft Copilot |
|---|---|---|
| 1. Dẫn nguồn mở được | Có - output hiện `10 sources` | Chưa quan sát được trong first pass guest mode |
| 2. Disclaimer khi không chắc | Có - output nêu độ chắc chắn / estimate | Chưa quan sát được do không có answer |
| 3. Fallback / dừng lại khi out-of-scope | Một phần - giải quyết bằng note uncertainty | Không phải fallback trí tuệ; hệ thống dừng ở verification gate |
| 4. Consistency | Chưa re-run do giới hạn thời gian, nhưng first pass thành công | First pass thất bại do verification gate |
| 5. User control | Có thread follow-up, có tiếp tục hỏi | Có ecosystem controls nhưng chưa đạt đến bước user có thể đánh giá answer |
| 6. Explanation | Có source badge và câu trả lời có cấu trúc | Chưa quan sát được |

## Phần D - Định vị trên Cost-Capability-Speed

- **Perplexity nghiêng về**: cân bằng giữa speed và capability  
  Lý do: trả kết quả nhanh, citation rõ, và gói Pro đặt vào chiều sâu nghiên cứu.

- **Copilot nghiêng về**: cân bằng hệ sinh thái / broad assistant hơn là search speed  
  Lý do: giá trị rất lớn nếu người dùng đã ở trong ecosystem Microsoft, nhưng first-pass speed cho guest research mode không tốt trong bài test này.

## Phần E - Verdict sơ bộ

- **Perplexity - verdict sơ bộ**: Strong  
  Lý do 1 câu: nó giải quyết đúng bài toán "tìm nhanh + có nguồn + hỏi tiếp" ngay ở lượt guest đầu tiên.

- **Microsoft Copilot - verdict sơ bộ**: Promising / At Risk for guest-mode search  
  Lý do 1 câu: distribution và product ambition mạnh, nhưng workflow thất bại trước khi sinh được answer trong first-turn test.
