---
artifact: 1 - Ghi chu nghien cuu khi test 2 san pham AI
bai-tap: 2 - Phan tich 2 san pham AI (nhom 2 hoc vien)
phase: Phase 2 - Thu nghiem + chup anh + research
time: 20 phut
input: group-members.md
nop-cuoi: Khong - file trung gian
---

# 1 - Ghi chu nghien cuu khi test 2 san pham AI

Muc tieu cua file nay la ghi lai **quan sat thuc te** trong mot luot test cong khai ngay **2026-05-14 12:48 +07:00**. Toan bo nhan dinh ben duoi deu chi dua tren:

- anh chup man hinh luu trong `screenshots/`
- giao dien cong khai truy cap duoc trong workspace nay
- nguon cong khai hien hanh ve pricing, user base va tang truong

## Phan A - Setup chung

- **Nhiem vu chung**: Tom tat thi truong edtech Viet Nam nam 2024 trong 5 gach dau dong, neu 3 cong ty tieu bieu, 2 xu huong, va gan link nguon cho tung y. Neu khong chac, hay noi ro.
- **Cau prompt chinh xac**:

```text
Tom tat thi truong edtech Viet Nam nam 2024 trong 5 gach dau dong. Neu 3 cong ty tieu bieu, 2 xu huong, va gan link nguon cho tung y. Neu khong chac, hay noi ro.
```

- **Loai tai khoan dung**:
  - San pham A - Perplexity: guest / chua dang nhap
  - San pham B - Microsoft Copilot: guest / chua dang nhap
- **Moi truong test**: browser cong khai trong workspace, chup anh ngay 2026-05-14, mui gio +07:00

## Phan B - Log San pham A

**Ten san pham A**: Perplexity  
**URL**: https://www.perplexity.ai/  
**Model duoi mui xe**: giao dien guest chi hien "Model" picker, khong cong khai model cu the o anh chup

### B.1 - Entry point + lan cham dau

- Trang dau la mot o hoi dap dang search-first, ben duoi co nut `Search`, `Computer`, `Model`.
- Giao dien cho thay nguoi dung khong can dang nhap de bat dau hoi.
- Co overlay moi dang nhap o ben phai va cookie banner o goc duoi phai, nhung van nhin thay ro entry box.
- Anh da chup: `screenshots/perplexity-1-entry.png`

### B.2 - Khi go prompt + nhan output

- Thoi gian de co output doc duoc: khoang **12 giay**.
- Sau khi nhap, prompt nam trong cung o composer, khong bat nguoi dung doi surface.
- Output co cau truc bullet, co nêu do chac chan va co badge nguon; man hinh output cho thay `10 sources`.
- Anh da chup:
  - `screenshots/perplexity-2-input.png`
  - `screenshots/perplexity-3-output.png`
  - `screenshots/perplexity-4-source.png`

### B.3 - Phan hoi sau khi nhan output

- Co follow-up suggestions ngay ben duoi cau tra loi.
- Co dau vet ro rang ve citation / source count.
- Co kha nang tiep tuc hoi tiep trong cung thread.
- Cookie banner van ton tai, tao mot friction nho o goc duoi phai.

### B.4 - Quan sat noi

1. **Entry rat ro use case "ask + search"**: nguoi dung nhin thay ngay o hoi dap va nut `Search`, phu hop tac vu tim kiem co dan nguon. Tham chieu: `perplexity-1-entry.png`.
2. **Friction vat ly thap**: chi can mot o nhap va Enter la co cau tra loi, khong bi yeu cau dang nhap hoac xac minh nguoi dung trong first pass. Tham chieu: `perplexity-2-input.png`.
3. **Trust signal tot hon doi thu trong luot test nay**: output hien `10 sources`, co follow-up, va trong cau tra loi co note do chac chan. Tham chieu: `perplexity-3-output.png`, `perplexity-4-source.png`.

## Phan C - Log San pham B

**Ten san pham B**: Microsoft Copilot  
**URL**: https://copilot.microsoft.com/  
**Model duoi mui xe**: mode mac dinh `Smart`, giao dien guest khong hien model chi tiet

### C.1 - Entry point + lan cham dau

- Trang dau co o `Message Copilot`, mode `Smart`, va mot so starter prompts.
- Giao dien guest cho phep bat dau ma chua can dang nhap.
- Anh da chup: `screenshots/copilot-1-entry.png`

### C.2 - Khi go prompt + nhan output

- Prompt duoc nhap thanh cong, nhung ngay sau khi gui thi giao dien bi chen boi cookie/privacy modal va sau do la human verification cua Cloudflare.
- Sau **16 giay cho**, he thong khong tra ra cau tra loi noi dung; thay vao do la man hinh `Verify you are human`.
- Anh da chup:
  - `screenshots/copilot-2-input.png`
  - `screenshots/copilot-3-output.png`

### C.3 - Phan hoi sau khi nhan output

- Copilot co trang thai guest, nhung trong luot test nay khong deliver duoc answer o first pass.
- Co dau hieu friction lon ngay giua workflow: privacy modal + security challenge.
- Tinh nang share / library / tasks hien san, cho thay san pham muon mo rong thanh assistant da nhiem, khong chi la answer engine.

### C.4 - Quan sat noi

1. **Entry point dep va than thien**: composer lon, starter prompts ro, mode `Smart` nhin de dung. Tham chieu: `copilot-1-entry.png`.
2. **Workflow bi cat ngang som**: cookie modal xuat hien dè len ngay luc nguoi dung dang test, sau do Cloudflare challenge chan han first-turn success. Tham chieu: `copilot-2-input.png`, `copilot-3-output.png`.
3. **Surface rong hon search thuần**: co `Library`, `Tasks`, `Projects`, `Imagine`, nen tham vong san pham lon; doi lai, first-use flow o guest mode kem tap trung hon Perplexity cho tac vu "tim nhanh va co source". Tham chieu: `copilot-1-entry.png`.

## Phan D - First impressions

1. **San pham nao cam giac de dung hon lan dau?**  
   - Perplexity de dung hon trong luot test nay vi khong bi cat ngang boi modal / challenge va dua nguoi dung thang vao tac vu tim kiem.

2. **San pham nao cho output dang tin hon?**  
   - Perplexity thang theo bang chung quan sat duoc, vi no thuc su tra ra answer, hien source count, va neu do chac chan. Copilot khong co answer de so sanh trong first pass guest mode.

3. **Cau hoi nhom chua tra loi duoc sau 20 phut test**  
   - Copilot se cho output ra sao neu qua duoc challenge va dong privacy modal?
   - Chat guest mode cua Copilot co source citation nhat quan voi truy van mang tinh nghien cuu khu vuc Viet Nam khong?
   - Perplexity co duy tri do manh citation khi prompt chuyen sang tac vu phuc tap hon khong?

## Nguon business signal da tra cuu song song

- Perplexity Pro Perks / pricing surface: https://www.perplexity.ai/properks/
- Perplexity ARR: CNBC, 2025-03-20
- Perplexity query volume growth: TechCrunch, 2025-06-05
- Microsoft Copilot official product/pricing docs:
  - https://support.microsoft.com/en-us/topic/what-s-the-difference-between-the-microsoft-copilot-experiences-cfff4791-694a-4d90-9c9c-1eb3fb28e842
  - https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals
- Microsoft Copilot user base: CNBC, 2025-07-30; TechCrunch, 2026-01-29
