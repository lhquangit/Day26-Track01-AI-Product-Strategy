---
artifact: 3 - Outline 5 muc cho slide deck Analysis Report
bai-tap: 2 - Phan tich 2 san pham AI
phase: Phase 3 - Dung slide deck
input: 1-research-notes.md + 2-comparison-table.md + screenshots/
nop-cuoi: Co gian tiep - dung lam cot cho analysis-report.pdf
---

# 3 - Outline 5 muc cho slide deck (S1 -> S5 voi S5 mo rong)

## Thong tin chung cua bao cao

- **Ma 2 thanh vien + ten**: 2A202600201 (Nguyen Quoc Nam) + [chua co du lieu trong workspace]
- **Nganh chon**: A - Tim kiem
- **Nhiem vu chung da test**: Tom tat thi truong edtech Viet Nam nam 2024 trong 5 gach dau dong, neu 3 cong ty tieu bieu, 2 xu huong, gan link nguon cho tung y, va noi ro neu khong chac.
- **San pham A**: Perplexity - https://www.perplexity.ai/
- **San pham B**: Microsoft Copilot - https://copilot.microsoft.com/
- **Cau prompt chinh xac da dung**:

```text
Tom tat thi truong edtech Viet Nam nam 2024 trong 5 gach dau dong. Neu 3 cong ty tieu bieu, 2 xu huong, va gan link nguon cho tung y. Neu khong chac, hay noi ro.
```

## S1 - Product Moment

### S1.1 - Bang so sanh nhanh

| Yeu to | Perplexity | Microsoft Copilot |
|---|---|---|
| Ten + URL | Perplexity - perplexity.ai | Microsoft Copilot - copilot.microsoft.com |
| Entry point | O `Ask anything` + nut `Search` + search-first framing | O `Message Copilot` + starter prompts + mode `Smart` |
| Y dinh nguoi dung | Tim cau tra loi co dan nguon tren web | Tro ly tong quat, creative + search + productivity |
| Surface chinh | Chat/search hybrid | Assistant/chat hub |
| Co can dang nhap / paywall ngay khong | Khong | Khong, nhung guest flow gap privacy modal va challenge sau khi gui |

### S1.2 - Bang chung

- `screenshots/perplexity-1-entry.png` - entry box va search-first framing.
- `screenshots/copilot-1-entry.png` - assistant-style composer va starter prompts.

### S1.3 - Nhan dinh so sanh entry point

Perplexity cho thay y dinh san pham ro hon cho use case "tim va tong hop". Copilot dep va rong hon, nhung cung vi rong hon nen entry point it specific hon cho bai toan nghien cuu co nguon.

## S2 - Workflow Evidence

### S2.1 - Luong nguoi dung

```text
TRUOC khi gap AI:
- Nguoi dung can tim nhanh tong quan thi truong EdTech Viet Nam 2024 va muon co source de cross-check.

TRONG khi dung Perplexity:
1. Mo trang guest.
2. Dan prompt vao entry box.
3. Nhan output trong ~12 giay, thay source count va follow-up.

TRONG khi dung Microsoft Copilot:
1. Mo trang guest.
2. Dan prompt vao o Message Copilot.
3. Sau khi gui, bi privacy modal va human verification chan truoc khi co answer.

SAU khi dung AI:
- Voi Perplexity, nguoi dung co the tiep tuc hoi va truy source.
- Voi Copilot, nguoi dung phai giai quyet gate verification truoc khi danh gia ket qua.
```

### S2.2 - 3 Friction Areas

| Friction | Perplexity | Microsoft Copilot |
|---|---|---|
| Physical load | Thap; few clicks, no login required | Cao hon; modal + verification chen vao workflow |
| Cognitive burden | Thap; prompt vao, nhan search answer | Trung binh-cao; nhieu surface, mode, va challenge |
| User workarounds | Bo qua cookie/sign-in overlay | Phai vuot privacy gate va human verification |

### S2.3 - Bang chung

- `screenshots/perplexity-2-input.png`
- `screenshots/perplexity-3-output.png`
- `screenshots/copilot-2-input.png`
- `screenshots/copilot-3-output.png`

### S2.4 - Nhan dinh

Perplexity giam friction tot hon ro ret trong task nay, khong phai vi giao dien dep hon, ma vi no di thang vao "lam xong bai" nhanh hon. Copilot bi tru hao UX ngay giua workflow, nen nhan dinh ve quality answer chua kip xay ra da bi security friction lấn át.

## S3 - Output & Trust

### S3.1 - Chat luong output

- **Perplexity**:
  - Tra loi dung bai toan tong hop.
  - Co source count va follow-up.
  - Co note uncertainty thay vi khang dinh qua muc.
- **Microsoft Copilot**:
  - Khong co output noi dung trong first pass guest mode.
  - Vi vay, bai test nay danh gia Copilot theo "reliability of reaching an answer", khong the cham content quality.

### S3.2 - 6 Tin hieu dang tin

| Tin hieu | Perplexity | Microsoft Copilot |
|---|---|---|
| 1. Citation | Co, thay `10 sources` | Chua quan sat duoc |
| 2. Disclaimer | Co, nêu do chac chan | Chua quan sat duoc |
| 3. Fallback | Co xu huong noi ro uncertainty | Dung o human verification |
| 4. Consistency | Chua test lan 2 | Chua qua duoc first pass |
| 5. User control | Co follow-up va thread | Co ecosystem controls nhung chua toi muc answer |
| 6. Explanation | Co source-based answer surface | Chua quan sat duoc |

### S3.3 - Nhan dinh

Perplexity tao trust manh hon vi no cho thay duoc ca "nguon" lan "do chac chan". Copilot co brand trust va ecosystem trust, nhung trong bai test guest mode nay, trust o tang answer khong the xac lap vi san pham chua deliver answer.

## S4 - Business Signal

### S4.1 - Dinh vi tam giac

- **Perplexity**: can bang  
  Ly do: free search utility du manh de hook, Pro $20/thang de upsell chieu sau va premium data.
- **Microsoft Copilot**: capability va distribution-first  
  Ly do: consumer chat free, nhung value tra phi duoc day vao goi Microsoft 365 va ecosystem usage higher-than-free.

### S4.2 - Pricing pattern

| Yeu to | Perplexity | Microsoft Copilot |
|---|---|---|
| Mo hinh gia | Freemium + Pro subscription | Free chat + Microsoft 365 paid plans / higher usage |
| Gia entry | Free guest search | Free consumer app |
| Gia tra phi | Pro surface nhan `just $20/month` | Microsoft 365 Personal $99.99/year; Family/Premium cao hon; higher AI usage trong paid plans |
| Paywall xuat hien o dau | Nhu cau nghien cuu sau / premium features | Gia tri tra phi gan voi app suite, storage, va higher usage |

### S4.3 - Nhan dinh

Perplexity ban mot san pham tim kiem AI ngay lap tuc va don gia. Microsoft ban gia tri AI thong qua ecosystem rong hon, nen pricing signal cua Copilot kho tach khoi Microsoft 365. Dieu nay giup Microsoft co distribution moat, nhung cung lam product story it "thuần answer engine" hon.

## S5 - Product Judgment

### S5.1 - Verdict

- **Perplexity**: Strong - Vi giai quyet dung use case, co source, va tao duoc trust ngay tu first pass.
- **Microsoft Copilot**: Promising / At Risk for guest research - Vi ambition va distribution lon, nhung guest-mode workflow that bai trong bai test nay.

### S5.2 - User base + tang truong

- **Perplexity**:
  - TechCrunch ngay 2025-06-05: Perplexity da xu ly **780 million queries trong thang 5/2025**, tuong duong khoang **30 million queries/day**, va CEO noi tang truong tren **20% month-over-month**.
  - Ghi chu: khong co MAU cong khai on dinh, nen query volume la proxy cong khai manh hon.
- **Microsoft Copilot**:
  - CNBC ngay 2025-07-30: "Copilot products" cua Microsoft co **100 million monthly active users**.
  - TechCrunch ngay 2026-01-29: Microsoft noi tong user base Copilot da tang len **150 million total**, va daily users o consumer products **nearly 3x YoY**.

### S5.3 - Doanh thu / pricing power

- **Perplexity**:
  - CNBC ngay 2025-03-20: ARR cua Perplexity "just under **$100 million**".
  - Pricing power den tu Pro subscription $20/thang va premium data / deeper search.
- **Microsoft Copilot**:
  - Khong co doanh thu consumer Copilot tach rieng cong khai trong cac nguon da tra.
  - Pricing power the hien gian tiep qua Microsoft 365 plans va usage tiers, khong phai qua mot consumer subscription don le de do.

### S5.4 - Moat phan tich

| Moat | Perplexity | Microsoft Copilot |
|---|---|---|
| Data | Trung binh - source graph va query logs co gia tri, nhung model phu thuoc partly vao external providers | Trung binh-manh - query logs + usage across Windows, Edge, Bing, M365 |
| Network effects | Yeu | Yeu-trung binh |
| Switching cost | Yeu-trung binh | Trung binh-manh neu da song trong M365 / Windows |
| Brand | Trung binh, tang nhanh trong niche AI search | Manh nhờ Microsoft brand |
| Distribution | Trung binh | Rat manh nhờ Windows, Edge, Bing, Microsoft 365 |

### S5.5 - Data flywheel + feedback loop

- **Perplexity**: moi truy van search + click vao source + follow-up giup san pham hoc ve y dinh tim kiem va citation preferences. Loop co dau hieu compounding, nhung moat data chua kho copy bang distribution.
- **Microsoft Copilot**: loop data manh hon neu tinh ca M365, Bing, Windows va shopping/search surfaces. Van de la feedback loop manh khong tu dong bien thanh first-turn UX tot trong guest mode.

### S5.6 - Niche Down + AI Feature Map

- **Perplexity**:
  - Niche: AI answer engine cho nguoi can tim nhanh, co source, co follow-up.
  - User Value: Cao - bai test thanh cong va co citation.
  - User Alignment: Cao - entry point khop dung y dinh search.
  - Business Value: Cao - co free-to-Pro path ro.
- **Microsoft Copilot**:
  - Niche: general AI companion trong ecosystem Microsoft.
  - User Value: Trung binh trong guest search use case nay, vi answer khong xuat hien.
  - User Alignment: Trung binh - san pham rong, khong zoom vao search-first.
  - Business Value: Cao - goi voi Microsoft 365, distribution rong.

### S5.7 - Spark -> Loop -> System

- **Perplexity**: Loop  
  Ly do: da co repeat behavior ro (search -> source -> follow-up -> deeper search), monetization va premium data dang day loop manh len.  
  Du bao 12 thang toi: tiep tuc mo rong tu answer engine sang browser / discovery system.

- **Microsoft Copilot**: System  
  Ly do: nam trong mot he sinh thai san pham lon hon nhieu mot app search; co distribution va app-level embedding ro.  
  Du bao 12 thang toi: se tiep tuc tang usage nho bundling, nhung se can giam friction o first-use consumer flows.

### S5.8 - Lien he Lab 1

- **Lien he voi Chegg vs ChatGPT**:
  - Bai hoc Lab 1 la: khi user expectation chuyen tu "toi tu lam tren giao dien cu" sang "AI lam ngay cho toi", san pham nao rut ngan khoang cach den answer se an diem lon.
  - Perplexity dang song dung theo expectation moi do: search khong chi "tim link" ma "tong hop co source".
  - Copilot co nguy co giong cac case bi squeeze neu product story qua rong, con first-turn answer lai chua sac bang san pham dung-niche.
- **Rui ro disruption-style**:
  - Perplexity co the bi big tech squeeze o distribution.
  - Copilot it lo distribution risk hon, nhung co risk bi user danh gia la "broad but not sharp" neu workflow research search chua tot bang specialist.

## Nguon tham khao chinh

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
