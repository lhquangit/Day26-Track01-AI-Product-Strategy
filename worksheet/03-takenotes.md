---
artifact: 03-takenotes - Quan sat ca nhan sau phan chia se nhom khac
bai-tap: 3 - Quan sat + rut ra bai hoc (ca nhan)
phase: Sau phan shareout
time: 15 phut
input: Phan trinh bay cua it nhat 2 nhom khac tren lop
nop-cuoi: Co - file cuoi Lab 3
---

# 03 - Take notes: quan sat + bai hoc ca nhan

> Luu y trung thuc: workspace nay **khong luu du lieu ve cac nhom da nghe tren lop**, nen file ben duoi duoc hoan thien theo dang **khung ghi chu da co san nhan dinh phuong phap**, dong thoi danh dau ro nhung cho can thay bang ten nhom / ma hoc vien thuc te truoc khi nop neu ban muon phan anh dung buoi hoc. Muc tieu la khong de file trong, nhung cung khong bịa thong tin lop hoc.

## Thong tin

- **Ma hoc vien**: 2A202600201
- **Ho ten**: Nguyen Quoc Nam
- **Ngay**: 2026-05-14
- **Nhom Lab 2 cua toi**: Perplexity vs Microsoft Copilot trong nganh Tim kiem

## Phan 1 - Nhom da quan sat (can thay bang nhom thuc te)

| # | Ten nhom / ma 2 hoc vien | Nganh | 2 san pham ho test |
|---|---|---|---|
| 1 | [Can thay bang nhom thuc te tren lop] | [A/B/C/D] | [...] vs [...] |
| 2 | [Can thay bang nhom thuc te tren lop] | [A/B/C/D] | [...] vs [...] |

## Phan 2 - Dieu thay hay tu nhom khac

**Quan sat 1**:

- Dieu toi se tim o nhom khac khi nghe lai: ho co dung chung mot prompt va giu nguyen task cho ca 2 san pham khong.
- Vi sao toi thay hay: day la dieu tach ro "so sanh san pham" khoi "so sanh prompt engineering". Nhom nao ky luat diem nay thuong co verdict dang tin hon.

**Quan sat 2**:

- Dieu toi se tim o nhom khac khi nghe lai: ho co chi ro 1-2 friction areas that su gay ton hao nhat thay vi liet ke qua nhieu UX details khong.
- Vi sao toi thay hay: S2 manh nhat khi nhom chi ra 1 nut that o workflow, vi luc do verdict S5 de bao ve hon.

## Phan 3 - Diem yeu / cho chua thuyet phuc

**Diem yeu 1**:

- Kieu loi toi se soi o nhom khac: ket luan "A tot hon B" nhung khong co anh entry/input/output tuong ung.
- Bang chung gi con thieu: anh chup that, thoi gian test, prompt y nguyen, va trang thai free/paid.
- De xuat lam them: gan moi nhan dinh voi ten file screenshot cu the.

**Diem yeu 2**:

- Kieu loi toi se soi o nhom khac: dung so lieu business signal khong ro moc thoi gian, hoac tron user base cua ca cong ty vao user base cua san pham.
- Bang chung gi con thieu: nguon cong khai co ngay thang va chi ro do la MAU, DAU, ARR hay chi la uoc tinh.
- De xuat lam them: neu khong co so lieu tach rieng, viet thang "khong co nguon cong khai" thay vi doan.

## Phan 4 - Cau hoi dat cho nhom khac

- Cho nhom [can thay]: verdict cua nhom dang dua nhieu hon vao quality answer hay vao do muot cua workflow? Anh nao trong deck chung minh diem do ro nhat?
- Cho nhom [can thay]: trong phan moat, nhom dang noi ve moat cua **san pham** hay moat cua **cong ty me / ecosystem**? Hai thu nay da tach ro chua?

## Phan 5 - Dieu toi rut ra cho ban than

**Bai hoc 1**:

- Toi se lam khac lan sau: chup first-pass failure nhu mot bang chung, khong chi chup output dep.
- Ly do: man hinh `Verify you are human` cua Copilot trong bai nay thuc chat noi len nhieu hon mot doan nhan xet chung chung ve friction.

**Bai hoc 2**:

- Toi se lam khac lan sau: neu khong co MAU cong khai on dinh, toi se dung operational proxy manh hon (query volume, paid seats, ARR) va ghi ro do la proxy.
- Ly do: cach nay giu bai trung thuc ma van co the phan tich dinh luong.

**Bai hoc 3**:

- Toi se lam khac lan sau: tach verdict theo persona / context, vd "strong cho guest search" khac voi "strong cho ecosystem productivity".
- Ly do: cung mot san pham co the rat manh o distribution nhung yeu o first-turn use case cu the.
