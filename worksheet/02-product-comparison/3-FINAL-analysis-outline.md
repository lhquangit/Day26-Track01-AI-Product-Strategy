---
artifact: 3 - Outline 5 mục cho slide deck Analysis Report
bai-tap: 2 - Phân tích 2 sản phẩm AI
phase: Phase 3 - Dựng slide deck
input: 1-research-notes.md + 2-comparison-table.md + screenshots/
nop-cuoi: Có gián tiếp - dùng làm cốt cho analysis-report.pdf
---

# 3 - Outline 5 mục cho slide deck (S1 -> S5 với S5 mở rộng)

## Thông tin chung của báo cáo

- **Mã 2 thành viên + tên**: 2A202600201 (Nguyễn Quốc Nam) + [chưa có dữ liệu trong workspace]
- **Ngành chọn**: A - Tìm kiếm
- **Nhiệm vụ chung đã test**: Tóm tắt thị trường edtech Việt Nam năm 2024 trong 5 gạch đầu dòng, nêu 3 công ty tiêu biểu, 2 xu hướng, gắn link nguồn cho từng ý, và nói rõ nếu không chắc.
- **Sản phẩm A**: Perplexity - https://www.perplexity.ai/
- **Sản phẩm B**: Microsoft Copilot - https://copilot.microsoft.com/
- **Câu prompt chính xác đã dùng**:

```text
Tóm tắt thị trường edtech Việt Nam năm 2024 trong 5 gạch đầu dòng. Nêu 3 công ty tiêu biểu, 2 xu hướng, và gắn link nguồn cho từng ý. Nếu không chắc, hãy nói rõ.
```

## S1 - Product Moment

### S1.1 - Bảng so sánh nhanh

| Yếu tố | Perplexity | Microsoft Copilot |
|---|---|---|
| Tên + URL | Perplexity - perplexity.ai | Microsoft Copilot - copilot.microsoft.com |
| Entry point | Ô `Ask anything` + nút `Search` + search-first framing | Ô `Message Copilot` + starter prompts + mode `Smart` |
| Ý định người dùng | Tìm câu trả lời có dẫn nguồn trên web | Trợ lý tổng quát, creative + search + productivity |
| Surface chính | Chat/search hybrid | Assistant/chat hub |
| Có cần đăng nhập / paywall ngay không | Không | Không, nhưng guest flow gặp privacy modal và challenge sau khi gửi |

### S1.2 - Bằng chứng

- `screenshots/perplexity-1-entry.png` - entry box và search-first framing.
- `screenshots/copilot-1-entry.png` - assistant-style composer và starter prompts.

### S1.3 - Nhận định so sánh entry point

Perplexity cho thấy ý định sản phẩm rõ hơn cho use case "tìm và tổng hợp". Copilot đẹp và rộng hơn, nhưng cũng vì rộng hơn nên entry point ít specific hơn cho bài toán nghiên cứu có nguồn.

## S2 - Workflow Evidence

### S2.1 - Luồng người dùng

```text
TRƯỚC khi gặp AI:
- Người dùng cần tìm nhanh tổng quan thị trường EdTech Việt Nam 2024 và muốn có source để cross-check.

TRONG khi dùng Perplexity:
1. Mở trang guest.
2. Dán prompt vào entry box.
3. Nhận output trong ~12 giây, thấy source count và follow-up.

TRONG khi dùng Microsoft Copilot:
1. Mở trang guest.
2. Dán prompt vào ô Message Copilot.
3. Sau khi gửi, bị privacy modal và human verification chặn trước khi có answer.

SAU khi dùng AI:
- Với Perplexity, người dùng có thể tiếp tục hỏi và truy source.
- Với Copilot, người dùng phải giải quyết gate verification trước khi đánh giá kết quả.
```

### S2.2 - 3 Friction Areas

| Friction | Perplexity | Microsoft Copilot |
|---|---|---|
| Physical load | Thấp; few clicks, no login required | Cao hơn; modal + verification chen vào workflow |
| Cognitive burden | Thấp; prompt vào, nhận search answer | Trung bình-cao; nhiều surface, mode, và challenge |
| User workarounds | Bỏ qua cookie/sign-in overlay | Phải vượt privacy gate và human verification |

### S2.3 - Bằng chứng

- `screenshots/perplexity-2-input.png`
- `screenshots/perplexity-3-output.png`
- `screenshots/copilot-2-input.png`
- `screenshots/copilot-3-output.png`

### S2.4 - Nhận định

Perplexity giảm friction tốt hơn rõ rệt trong task này, không phải vì giao diện đẹp hơn, mà vì nó đi thẳng vào "làm xong bài" nhanh hơn. Copilot bị trừ hao UX ngay giữa workflow, nên nhận định về quality answer chưa kịp xảy ra đã bị security friction lấn át.

## S3 - Output & Trust

### S3.1 - Chất lượng output

- **Perplexity**:
  - Trả lời đúng bài toán tổng hợp.
  - Có source count và follow-up.
  - Có note uncertainty thay vì khẳng định quá mức.
- **Microsoft Copilot**:
  - Không có output nội dung trong first pass guest mode.
  - Vì vậy, bài test này đánh giá Copilot theo "reliability of reaching an answer", không thể chấm content quality.

### S3.2 - 6 Tín hiệu đáng tin

| Tín hiệu | Perplexity | Microsoft Copilot |
|---|---|---|
| 1. Citation | Có, thấy `10 sources` | Chưa quan sát được |
| 2. Disclaimer | Có, nêu độ chắc chắn | Chưa quan sát được |
| 3. Fallback | Có xu hướng nói rõ uncertainty | Dừng ở human verification |
| 4. Consistency | Chưa test lần 2 | Chưa qua được first pass |
| 5. User control | Có follow-up và thread | Có ecosystem controls nhưng chưa tới mức answer |
| 6. Explanation | Có source-based answer surface | Chưa quan sát được |

### S3.3 - Nhận định

Perplexity tạo trust mạnh hơn vì nó cho thấy được cả "nguồn" lẫn "độ chắc chắn". Copilot có brand trust và ecosystem trust, nhưng trong bài test guest mode này, trust ở tầng answer không thể xác lập vì sản phẩm chưa deliver answer.

## S4 - Business Signal

### S4.1 - Định vị tam giác

- **Perplexity**: cân bằng  
  Lý do: free search utility đủ mạnh để hook, Pro $20/tháng để upsell chiều sâu và premium data.
- **Microsoft Copilot**: capability và distribution-first  
  Lý do: consumer chat free, nhưng value trả phí được đẩy vào gói Microsoft 365 và ecosystem usage higher-than-free.

### S4.2 - Pricing pattern

| Yếu tố | Perplexity | Microsoft Copilot |
|---|---|---|
| Mô hình giá | Freemium + Pro subscription | Free chat + Microsoft 365 paid plans / higher usage |
| Giá entry | Free guest search | Free consumer app |
| Giá trả phí | Pro surface nhấn `just $20/month` | Microsoft 365 Personal $99.99/year; Family/Premium cao hơn; higher AI usage trong paid plans |
| Paywall xuất hiện ở đâu | Nhu cầu nghiên cứu sâu / premium features | Giá trị trả phí gắn với app suite, storage, và higher usage |

### S4.3 - Nhận định

Perplexity bán một sản phẩm tìm kiếm AI ngay lập tức và đơn giá. Microsoft bán giá trị AI thông qua ecosystem rộng hơn, nên pricing signal của Copilot khó tách khỏi Microsoft 365. Điều này giúp Microsoft có distribution moat, nhưng cũng làm product story ít "thuần answer engine" hơn.

## S5 - Product Judgment

### S5.1 - Verdict

- **Perplexity**: Strong - Vì giải quyết đúng use case, có source, và tạo được trust ngay từ first pass.
- **Microsoft Copilot**: Promising / At Risk for guest research - Vì ambition và distribution lớn, nhưng guest-mode workflow thất bại trong bài test này.

### S5.2 - User base + tăng trưởng

- **Perplexity**:
  - TechCrunch ngày 2025-06-05: Perplexity đã xử lý **780 million queries trong tháng 5/2025**, tương đương khoảng **30 million queries/day**, và CEO nói tăng trưởng trên **20% month-over-month**.
  - Ghi chú: không có MAU công khai ổn định, nên query volume là proxy công khai mạnh hơn.
- **Microsoft Copilot**:
  - CNBC ngày 2025-07-30: "Copilot products" của Microsoft có **100 million monthly active users**.
  - TechCrunch ngày 2026-01-29: Microsoft nói tổng user base Copilot đã tăng lên **150 million total**, và daily users ở consumer products **nearly 3x YoY**.

### S5.3 - Doanh thu / pricing power

- **Perplexity**:
  - CNBC ngày 2025-03-20: ARR của Perplexity "just under **$100 million**".
  - Pricing power đến từ Pro subscription $20/tháng và premium data / deeper search.
- **Microsoft Copilot**:
  - Không có doanh thu consumer Copilot tách riêng công khai trong các nguồn đã tra.
  - Pricing power thể hiện gián tiếp qua Microsoft 365 plans và usage tiers, không phải qua một consumer subscription đơn lẻ để đo.

### S5.4 - Moat phân tích

| Moat | Perplexity | Microsoft Copilot |
|---|---|---|
| Data | Trung bình - source graph và query logs có giá trị, nhưng model phụ thuộc partly vào external providers | Trung bình-mạnh - query logs + usage across Windows, Edge, Bing, M365 |
| Network effects | Yếu | Yếu-trung bình |
| Switching cost | Yếu-trung bình | Trung bình-mạnh nếu đã sống trong M365 / Windows |
| Brand | Trung bình, tăng nhanh trong niche AI search | Mạnh nhờ Microsoft brand |
| Distribution | Trung bình | Rất mạnh nhờ Windows, Edge, Bing, Microsoft 365 |

### S5.5 - Data flywheel + feedback loop

- **Perplexity**: mỗi truy vấn search + click vào source + follow-up giúp sản phẩm học về ý định tìm kiếm và citation preferences. Loop có dấu hiệu compounding, nhưng moat data chưa khó copy bằng distribution.
- **Microsoft Copilot**: loop data mạnh hơn nếu tính cả M365, Bing, Windows và shopping/search surfaces. Vấn đề là feedback loop mạnh không tự động biến thành first-turn UX tốt trong guest mode.

### S5.6 - Niche Down + AI Feature Map

- **Perplexity**:
  - Niche: AI answer engine cho người cần tìm nhanh, có source, có follow-up.
  - User Value: Cao - bài test thành công và có citation.
  - User Alignment: Cao - entry point khớp đúng ý định search.
  - Business Value: Cao - có free-to-Pro path rõ.
- **Microsoft Copilot**:
  - Niche: general AI companion trong ecosystem Microsoft.
  - User Value: Trung bình trong guest search use case này, vì answer không xuất hiện.
  - User Alignment: Trung bình - sản phẩm rộng, không zoom vào search-first.
  - Business Value: Cao - gói với Microsoft 365, distribution rộng.

### S5.7 - Spark -> Loop -> System

- **Perplexity**: Loop  
  Lý do: đã có repeat behavior rõ (search -> source -> follow-up -> deeper search), monetization và premium data đang đẩy loop mạnh lên.  
  Dự báo 12 tháng tới: tiếp tục mở rộng từ answer engine sang browser / discovery system.

- **Microsoft Copilot**: System  
  Lý do: nằm trong một hệ sinh thái sản phẩm lớn hơn nhiều một app search; có distribution và app-level embedding rõ.  
  Dự báo 12 tháng tới: sẽ tiếp tục tăng usage nhờ bundling, nhưng sẽ cần giảm friction ở first-use consumer flows.

### S5.8 - Liên hệ Lab 1

- **Liên hệ với Chegg vs ChatGPT**:
  - Bài học Lab 1 là: khi user expectation chuyển từ "tôi tự làm trên giao diện cũ" sang "AI làm ngay cho tôi", sản phẩm nào rút ngắn khoảng cách đến answer sẽ ăn điểm lớn.
  - Perplexity đang sống đúng theo expectation mới đó: search không chỉ "tìm link" mà "tổng hợp có source".
  - Copilot có nguy cơ giống các case bị squeeze nếu product story quá rộng, còn first-turn answer lại chưa sắc bằng sản phẩm đúng-niche.
- **Rủi ro disruption-style**:
  - Perplexity có thể bị big tech squeeze ở distribution.
  - Copilot ít lo distribution risk hơn, nhưng có risk bị user đánh giá là "broad but not sharp" nếu workflow research search chưa tốt bằng specialist.

## Nguồn tham khảo chính

1. Perplexity live product: https://www.perplexity.ai/
2. Perplexity shared result tested on 2026-05-14: https://www.perplexity.ai/search/99f1501c-af5b-4b72-aeb6-095e91e98ad5
3. Perplexity Pro Perks / pricing surface: https://www.perplexity.ai/properks/
4. TechCrunch, 2025-06-05 - Perplexity received 780 million queries last month, CEO says
5. CNBC, 2025-03-20 - Perplexity in talks to double valuation to $18 billion via new funding
6. Microsoft Copilot live product: https://copilot.microsoft.com/
7. Microsoft Support - What's the difference between the Microsoft Copilot experiences?
8. Microsoft pricing for individuals: https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals
9. CNBC, 2025-07-30 - Microsoft Q4 earnings report 2025
10. TechCrunch, 2026-01-29 - Satya Nadella insists people are using Microsoft's Copilot AI a lot
