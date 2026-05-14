import fitz
from pathlib import Path

root = Path(r"C:\Using\Track_1\Day26-Track01-AI-Product-Strategy\worksheet\02-product-comparison")
out_path = root / "analysis-report.pdf"
shots = root / "screenshots"
font_path = r"C:\Windows\Fonts\arial.ttf"
font_bold_path = r"C:\Windows\Fonts\arialbd.ttf"

doc = fitz.open()
W, H = 1280, 720
M = 40

ACCENT = (0 / 255, 102 / 255, 204 / 255)
DARK = (20 / 255, 24 / 255, 28 / 255)
MUTED = (90 / 255, 98 / 255, 110 / 255)
BG = (248 / 255, 250 / 255, 252 / 255)
BORDER = (220 / 255, 226 / 255, 232 / 255)


def new_page():
    page = doc.new_page(width=W, height=H)
    page.draw_rect(fitz.Rect(0, 0, W, H), color=BG, fill=BG)
    return page


def add_text(page, point, text, size=12, color=DARK, bold=False):
    page.insert_text(
        point,
        text,
        fontsize=size,
        fontname="F0" if not bold else "F1",
        fontfile=font_path if not bold else font_bold_path,
        fill=color,
    )


def add_textbox(page, rect, text, size=12, color=DARK, align=0, bold=False):
    page.insert_textbox(
        rect,
        text,
        fontsize=size,
        fontname="F0" if not bold else "F1",
        fontfile=font_path if not bold else font_bold_path,
        fill=color,
        align=align,
    )


def add_title(page, text, subtitle=None):
    add_text(page, (M, 44), text, size=26, bold=True)
    if subtitle:
        add_text(page, (M, 68), subtitle, size=11, color=MUTED)
    page.draw_line((M, 82), (W - M, 82), color=BORDER, width=1)


def add_box(page, rect, heading, lines=None):
    page.draw_rect(rect, color=BORDER, fill=(1, 1, 1), width=1)
    add_text(page, (rect.x0 + 14, rect.y0 + 22), heading, size=15, bold=True)
    if not lines:
        return
    y = rect.y0 + 42
    for line in lines:
        add_textbox(page, fitz.Rect(rect.x0 + 14, y, rect.x1 - 14, y + 34), line, size=10)
        y += 30


def add_image(page, rect, path, caption):
    page.draw_rect(rect, color=BORDER, fill=(1, 1, 1), width=1)
    if Path(path).exists():
        img_rect = fitz.Rect(rect.x0 + 8, rect.y0 + 8, rect.x1 - 8, rect.y1 - 36)
        page.insert_image(img_rect, filename=str(path), keep_proportion=True)
    add_textbox(page, fitz.Rect(rect.x0 + 10, rect.y1 - 28, rect.x1 - 10, rect.y1 - 8), caption, size=9, color=MUTED, align=1)


def add_bullets(page, rect, items, size=11):
    y = rect.y0
    for item in items:
        add_text(page, (rect.x0, y), "•", size=size + 2, color=ACCENT, bold=True)
        add_textbox(page, fitz.Rect(rect.x0 + 16, y - 10, rect.x1, y + 28), item, size=size)
        y += 30


page = new_page()
add_title(page, "Day 26 - Phân tích sản phẩm AI", "Học viên: 2A202600201 Nguyễn Quốc Nam | Ngày test: 2026-05-14 (+07:00)")
add_text(page, (M, 150), "Perplexity vs Microsoft Copilot", size=34, bold=True)
add_text(page, (M, 195), "Ngành: Tìm kiếm", size=18, color=ACCENT)
add_textbox(
    page,
    fitz.Rect(M, 240, 720, 380),
    "Prompt dùng chung cho cả 2 sản phẩm:\nTóm tắt thị trường edtech Việt Nam năm 2024 trong 5 gạch đầu dòng. Nêu 3 công ty tiêu biểu, 2 xu hướng, và gắn link nguồn cho từng ý. Nếu không chắc, hãy nói rõ.",
    size=16,
)
add_box(
    page,
    fitz.Rect(M, 420, 600, 640),
    "Kết luận ngắn",
    [
        "Perplexity: STRONG cho guest-mode search có dẫn nguồn.",
        "Copilot: PROMISING nhưng bị hụt first-pass vì workflow chặn trước khi xuất hiện câu trả lời.",
        "Bài học chính: first-turn reliability quan trọng không kém model ambition.",
    ],
)
add_image(page, fitz.Rect(760, 120, 1230, 640), shots / "perplexity-1-entry.png", "Entry screen của Perplexity")

page = new_page()
add_title(page, "Phương pháp và bằng chứng", "Cùng prompt, cùng ngày test, đều ở guest mode")
add_box(
    page,
    fitz.Rect(M, 110, 600, 320),
    "Thiết lập test",
    [
        "Sản phẩm A: Perplexity (guest mode)",
        "Sản phẩm B: Microsoft Copilot (guest mode)",
        "Môi trường: browser công khai trong workspace",
        "Bằng chứng: screenshots, pricing pages chính thức, nguồn công khai về user/growth",
    ],
)
add_box(
    page,
    fitz.Rect(M, 350, 600, 640),
    "Vì sao chọn task này",
    [
        "Task này ép lộ search quality, source transparency, follow-up usability và first-turn workflow friction.",
        "Nó cũng cho thấy sản phẩm đang hành xử như một answer engine hay một assistant surface rộng hơn.",
    ],
)
add_bullets(
    page,
    fitz.Rect(660, 120, 1220, 520),
    [
        "Nguyên tắc dùng: không có bằng chứng thì không có nhận định.",
        "Perplexity trả answer sau khoảng 12 giây và hiện 10 sources.",
        "Copilot nhận prompt nhưng bị privacy modal rồi human verification chặn trước khi có answer.",
        "Business signal chỉ dùng nguồn công khai; chỗ nào không có số tách riêng thì ghi thẳng là không có.",
    ],
    size=13,
)
add_image(page, fitz.Rect(700, 430, 1210, 650), shots / "copilot-2-input.png", "Copilot sau khi dán prompt, có privacy modal")

page = new_page()
add_title(page, "S1 - Product Moment")
add_image(page, fitz.Rect(40, 110, 610, 500), shots / "perplexity-1-entry.png", "Perplexity: search-first entry point")
add_image(page, fitz.Rect(670, 110, 1240, 500), shots / "copilot-1-entry.png", "Copilot: assistant-style entry point")
add_box(
    page,
    fitz.Rect(40, 530, 1240, 670),
    "Đọc entry point",
    [
        "Perplexity làm rõ ý định search ngay từ đầu: một ô hỏi, một động từ, chi phí vào bài thấp.",
        "Copilot nhìn rộng hơn và giống trợ lý hơn: new chat, library, tasks, projects, discover, imagine.",
        "Với tác vụ tìm nhanh có nguồn, độ rõ ràng ban đầu nghiêng về Perplexity.",
    ],
)

page = new_page()
add_title(page, "S2 - Workflow Evidence")
add_image(page, fitz.Rect(40, 110, 610, 520), shots / "perplexity-2-input.png", "Perplexity ở trạng thái input")
add_image(page, fitz.Rect(670, 110, 1240, 520), shots / "copilot-3-output.png", "Copilot bị chặn ở human verification")
add_box(
    page,
    fitz.Rect(40, 545, 1240, 675),
    "Nhận định workflow",
    [
        "Perplexity: mở trang -> dán prompt -> Enter -> answer -> follow-ups.",
        "Copilot: mở trang -> dán prompt -> Enter -> privacy friction -> Cloudflare verification -> không có answer.",
        "Vì thế, Perplexity thấp hơn rõ rệt ở physical load và workaround burden cho task này.",
    ],
)

page = new_page()
add_title(page, "S3 - Output và Trust")
add_image(page, fitz.Rect(40, 110, 610, 520), shots / "perplexity-3-output.png", "Perplexity trả về câu trả lời có cấu trúc")
add_image(page, fitz.Rect(670, 110, 1240, 520), shots / "perplexity-4-source.png", "Perplexity hiện 10 nguồn và follow-up")
add_box(
    page,
    fitz.Rect(40, 545, 1240, 675),
    "Trust signals quan sát được",
    [
        "Perplexity cho thấy citation, follow-up suggestions và note uncertainty thay vì overclaim.",
        "Copilot không thể chấm answer quality trong bài test này vì không có first-pass answer.",
        "Trong task này, việc có đi tới được câu trả lời hay không tự nó đã là một trust signal.",
    ],
)

page = new_page()
add_title(page, "S4 - Business Signal")
add_image(page, fitz.Rect(40, 110, 610, 420), shots / "perplexity-5-pricing.png", "Perplexity pricing surface: Pro ở mức $20/tháng")
add_image(page, fitz.Rect(670, 110, 1240, 420), shots / "copilot-5-pricing.png", "Trang kế hoạch / pricing chính thức của Microsoft")
add_box(
    page,
    fitz.Rect(40, 450, 1240, 675),
    "Sự thật pricing và tăng trưởng",
    [
        "Perplexity: TechCrunch (2025-06-05) nói Perplexity xử lý 780M queries trong tháng 5/2025, khoảng 30M/ngày, tăng trên 20% month-over-month. CNBC (2025-03-20) nói ARR ở mức gần 100M USD. Pricing surface chính thức cho thấy Pro là 20 USD/tháng.",
        "Copilot: CNBC (2025-07-30) cho biết các Copilot products của Microsoft có 100M monthly active users. TechCrunch (2026-01-29) nói tổng user base Copilot đã lên 150M và daily users ở consumer products gần gấp 3 YoY. Microsoft không tách riêng doanh thu consumer Copilot ở các nguồn dùng trong bài này.",
        "Diễn giải: Perplexity bán trực tiếp answer engine; Microsoft kiếm giá trị AI qua hệ Microsoft 365 rộng hơn.",
    ],
)

page = new_page()
add_title(page, "S5.1-S5.5 - Product Judgment, Metrics, Moat")
add_box(
    page,
    fitz.Rect(40, 110, 390, 330),
    "Perplexity - verdict: STRONG",
    [
        "Thắng ở first-turn task completion",
        "Search-first framing rất rõ",
        "Citation behavior nhìn thấy được",
        "Freemium-to-Pro path trực diện",
    ],
)
add_box(
    page,
    fitz.Rect(430, 110, 780, 330),
    "Copilot - verdict: PROMISING / AT RISK",
    [
        "Ecosystem và distribution rất mạnh",
        "Assistant ambition rộng",
        "Nhưng first-pass guest research flow thất bại",
        "Cần friction thấp hơn để thắng task này",
    ],
)
add_box(
    page,
    fitz.Rect(820, 110, 1240, 330),
    "Moat snapshot",
    [
        "Perplexity: brand trung bình, data loop khá, distribution moat yếu hơn.",
        "Copilot: distribution moat rất mạnh nhờ Microsoft, switching cost cao hơn trong M365, nhưng product sharpness chưa chuyên cho search.",
    ],
)
add_box(
    page,
    fitz.Rect(40, 370, 1240, 675),
    "Ghi chú về metric",
    [
        "Perplexity không có MAU công khai ổn định, nên deck dùng query volume như operational proxy mạnh hơn.",
        "Copilot user count ở mức family-of-products; bài ghi rõ scope đó thay vì giả vờ như đây chỉ là số của web chat.",
        "Chỗ nào không có revenue figure tách riêng, bài viết thẳng là không có nguồn công khai.",
    ],
)

page = new_page()
add_title(page, "S5.6-S5.8 - Niche, Spark -> Loop -> System, Liên hệ Lab 1")
add_box(
    page,
    fitz.Rect(40, 110, 610, 310),
    "Perplexity",
    [
        "Niche: answer engine cho người cần tìm nhanh, có dẫn nguồn.",
        "Giai đoạn: LOOP.",
        "Lý do: hành vi lặp đã rõ - query, kiểm nguồn, follow-up, đào sâu.",
        "Rủi ro: có thể bị big-tech squeeze ở distribution.",
    ],
)
add_box(
    page,
    fitz.Rect(670, 110, 1240, 310),
    "Microsoft Copilot",
    [
        "Niche: AI companion rộng trong hệ Microsoft.",
        "Giai đoạn: SYSTEM.",
        "Lý do: đã nằm trong ecosystem lớn hơn nhiều một app search đơn lẻ.",
        "Rủi ro: broadness có thể làm giảm độ sắc ở task search chuyên biệt.",
    ],
)
add_box(
    page,
    fitz.Rect(40, 350, 1240, 670),
    "Liên hệ với Lab 1 (Chegg vs ChatGPT)",
    [
        "Lab 1 cho thấy user expectation đang dịch từ workflow cũ sang kỳ vọng 'AI làm ngay cho tôi'. Trong bài test này, Perplexity khớp expectation mới đó tốt hơn.",
        "Chegg bị squeeze vì workflow cũ quá chậm so với AI-native alternatives. Copilot ít lo distribution risk hơn, nhưng vẫn có thể mất điểm nếu first-turn flow chặn answer.",
        "Bài học mang sang: first-turn completion, bằng chứng hiển thị được và product focus quan trọng hơn brand đơn thuần.",
    ],
)

page = new_page()
add_title(page, "Nguồn")
add_bullets(
    page,
    fitz.Rect(50, 120, 1230, 660),
    [
        "1. Live product test - Perplexity: https://www.perplexity.ai/",
        "2. Shared result tested on 2026-05-14: https://www.perplexity.ai/search/99f1501c-af5b-4b72-aeb6-095e91e98ad5",
        "3. Perplexity Pro pricing surface: https://www.perplexity.ai/properks/",
        "4. TechCrunch - 2025-06-05 - Perplexity received 780 million queries last month, CEO says",
        "5. CNBC - 2025-03-20 - Perplexity in talks to double valuation to $18 billion via new funding",
        "6. Live product test - Microsoft Copilot: https://copilot.microsoft.com/",
        "7. Microsoft Support - What's the difference between the Microsoft Copilot experiences?",
        "8. Microsoft official pricing page for individuals: https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals",
        "9. CNBC - 2025-07-30 - Microsoft Q4 earnings report 2025",
        "10. TechCrunch - 2026-01-29 - Satya Nadella insists people are using Microsoft's Copilot AI a lot",
    ],
    size=12,
)

if out_path.exists():
    out_path.unlink()

doc.save(out_path)
print(out_path)
