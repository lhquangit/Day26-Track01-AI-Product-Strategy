---
artifact: 2 - Bang so sanh 2 san pham theo 5 muc
bai-tap: 2 - Phan tich 2 san pham AI
phase: Chuyen giao Phase 2 -> Phase 3
input: 1-research-notes.md + screenshots/
nop-cuoi: Khong - file trung gian
---

# 2 - Bang so sanh 2 san pham theo 5 muc slide deck

## Phan A - Bang so sanh 5 muc

| Muc | San pham A - Perplexity | San pham B - Microsoft Copilot |
|---|---|---|
| **S1 - Product Moment** | Search-native answer engine; entry point la o `Ask anything` va nut `Search`, khong can dang nhap de thu ngay. | Assistant surface rong hon search; entry point dep, co starter prompts, nhung khong tap trung bang Perplexity cho tac vu tim kiem co source. |
| **S2 - Workflow Evidence** | 1 o nhap -> Enter -> output trong khoang 12 giay -> follow-up suggestions. Fewer steps, it tab-hops less. | 1 o nhap -> Enter -> privacy modal + human verification. Workflow bi dut doan truoc khi co answer. |
| **S3 - Output & Trust** | Co output that su, co note uncertainty, hien `10 sources`, va giu thread de hoi tiep. | Khong co output noi dung trong first pass guest mode, nen trust signal bi thua ngay tu gate dau vao. |
| **S4 - Business Signal** | Dinh vi "mạnh hơn free search" voi upsell Pro; trang official Perks nhan manh `just $20/month`. | Consumer chat free, nhung Microsoft day gia tri tra phi vao he sinh thai Microsoft 365; pricing chinh thuc the hien goi ca nam va higher usage trong app suite. |
| **S5 - Product Judgment** | **Strong** cho use case search nhanh co citation. | **Promising / At Risk for guest research use**: tham vong lon, distribution lon, nhung first-use friction trong luot test nay qua cao. |

## Phan B - Doi chieu 3 friction areas

- **Physical load**: Perplexity co it click hon; Copilot bi them modal va challenge nen so thao tac "khong tao gia tri" tang len.
- **Cognitive burden**: Perplexity framing rat ro "ask + search"; Copilot buoc nguoi dung xu ly them context ve mode, prompt cards, va gate verification.
- **User workarounds**: Voi Perplexity, workaround chu yeu la bo qua cookie/sign-in overlay. Voi Copilot, workaround can vuot qua human verification, nhung dieu nay da vuot qua muc "first-turn smoothness".

## Phan C - Doi chieu 6 trust signals

| Tin hieu dang tin | Perplexity | Microsoft Copilot |
|---|---|---|
| 1. Dan nguon mo duoc | Co - output hien `10 sources` | Chua quan sat duoc trong first pass guest mode |
| 2. Disclaimer khi khong chac | Co - output neu do chac chan / estimate | Chua quan sat duoc do khong co answer |
| 3. Fallback / dung lai khi out-of-scope | Mot phan - giai quyet bang note uncertainty | Khong phai fallback tri tue; he thong dung o verification gate |
| 4. Consistency | Chua re-run do gioi han thoi gian, nhung first pass thanh cong | First pass that bai do verification gate |
| 5. User control | Co thread follow-up, co tiep tuc hoi | Co library / share / tasks, nhung khong dat den buoc user co the danh gia answer |
| 6. Explanation | Co source badge va cau tra loi co cau truc | Chua quan sat duoc |

## Phan D - Dinh vi tren Cost-Capability-Speed

- **Perplexity nghieng ve**: can bang giua speed va capability  
  Ly do: tra ket qua nhanh, citation ro, va goi Pro dat vao chieu sau nghien cuu.

- **Copilot nghieng ve**: can bang he sinh thai / broad assistant hon la search speed  
  Ly do: gia tri rat lon neu nguoi dung da o trong ecosystem Microsoft, nhung first-pass speed cho guest research mode khong tot trong bai test nay.

## Phan E - Verdict so bo

- **Perplexity - verdict so bo**: Strong  
  Ly do 1 cau: no giai quyet dung bai toan "tim nhanh + co nguon + hoi tiep" ngay o luot guest dau tien.

- **Microsoft Copilot - verdict so bo**: Promising / At Risk for guest-mode search  
  Ly do 1 cau: distribution va product ambition manh, nhung workflow that bai truoc khi sinh duoc answer trong first-turn test.
