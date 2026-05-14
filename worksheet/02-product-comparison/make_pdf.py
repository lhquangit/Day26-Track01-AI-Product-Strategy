import fitz
from pathlib import Path

root = Path(r"C:\Using\Track_1\Day26-Track01-AI-Product-Strategy\worksheet\02-product-comparison")
out_path = root / "analysis-report.pdf"
shots = root / "screenshots"

doc = fitz.open()
W, H = 1280, 720
M = 40

ACCENT = (0 / 255, 102 / 255, 204 / 255)
DARK = (20 / 255, 24 / 255, 28 / 255)
MUTED = (90 / 255, 98 / 255, 110 / 255)
BG = (248 / 255, 250 / 255, 252 / 255)
BORDER = (220 / 255, 226 / 255, 232 / 255)


def new_page():
    p = doc.new_page(width=W, height=H)
    p.draw_rect(fitz.Rect(0, 0, W, H), color=BG, fill=BG)
    return p


def add_title(page, text, subtitle=None):
    page.insert_text((M, 44), text, fontsize=26, fontname="helv", fill=DARK)
    if subtitle:
        page.insert_text((M, 68), subtitle, fontsize=11, fontname="helv", fill=MUTED)
    page.draw_line((M, 82), (W - M, 82), color=BORDER, width=1)


def add_box(page, rect, heading, lines=None):
    page.draw_rect(rect, color=BORDER, fill=(1, 1, 1), width=1)
    page.insert_text((rect.x0 + 14, rect.y0 + 22), heading, fontsize=15, fontname="helv", fill=DARK)
    if not lines:
        return
    y = rect.y0 + 44
    for line in lines:
        page.insert_textbox(
            fitz.Rect(rect.x0 + 14, y, rect.x1 - 14, y + 28),
            line,
            fontsize=9.5,
            fontname="helv",
            fill=DARK,
        )
        y += 28


def add_image(page, rect, path, caption):
    page.draw_rect(rect, color=BORDER, fill=(1, 1, 1), width=1)
    if Path(path).exists():
        img_rect = fitz.Rect(rect.x0 + 8, rect.y0 + 8, rect.x1 - 8, rect.y1 - 36)
        page.insert_image(img_rect, filename=str(path), keep_proportion=True)
    page.insert_textbox(
        fitz.Rect(rect.x0 + 10, rect.y1 - 28, rect.x1 - 10, rect.y1 - 8),
        caption,
        fontsize=9,
        fontname="helv",
        fill=MUTED,
        align=1,
    )


def add_bullets(page, rect, items, size=11):
    y = rect.y0
    for item in items:
        page.insert_text((rect.x0, y), chr(8226), fontsize=size + 2, fontname="helv", fill=ACCENT)
        page.insert_textbox(
            fitz.Rect(rect.x0 + 16, y - 10, rect.x1, y + 26),
            item,
            fontsize=size,
            fontname="helv",
            fill=DARK,
        )
        y += 28


page = new_page()
add_title(page, "Day 26 - AI Product Comparison", "Student: 2A202600201 Nguyen Quoc Nam | Date tested: 2026-05-14 (+07:00)")
page.insert_text((M, 150), "Perplexity vs Microsoft Copilot", fontsize=34, fontname="helv", fill=DARK)
page.insert_text((M, 195), "Industry: Search", fontsize=18, fontname="helv", fill=ACCENT)
page.insert_textbox(
    fitz.Rect(M, 240, 720, 370),
    "Task prompt used on both products:\nTom tat thi truong edtech Viet Nam nam 2024 trong 5 gach dau dong. Neu 3 cong ty tieu bieu, 2 xu huong, va gan link nguon cho tung y. Neu khong chac, hay noi ro.",
    fontsize=16,
    fontname="helv",
    fill=DARK,
)
add_box(
    page,
    fitz.Rect(M, 420, 600, 640),
    "Executive verdict",
    [
        "Perplexity: STRONG for guest-mode search.",
        "Copilot: PROMISING, but the first guest run was blocked before any answer appeared.",
        "Lesson: first-turn reliability matters as much as model ambition.",
    ],
)
add_image(page, fitz.Rect(760, 120, 1230, 640), shots / "perplexity-1-entry.png", "Perplexity entry screen")

page = new_page()
add_title(page, "Method and Evidence", "Same prompt, same date, guest mode on both products")
add_box(
    page,
    fitz.Rect(M, 110, 600, 320),
    "Test setup",
    [
        "Product A: Perplexity (guest mode)",
        "Product B: Microsoft Copilot (guest mode)",
        "Environment: public web access inside the workspace browser",
        "Evidence types: screenshots, official pricing pages, public user/growth sources",
    ],
)
add_box(
    page,
    fitz.Rect(M, 350, 600, 640),
    "Why this task",
    [
        "The task stresses search quality, source transparency, follow-up usability, and first-turn workflow friction.",
        "It also exposes whether the product behaves like an answer engine or a broader assistant surface.",
    ],
)
add_bullets(
    page,
    fitz.Rect(660, 120, 1220, 520),
    [
        "Rule used: no evidence = no judgment.",
        "Perplexity produced an answer in about 12 seconds and showed 10 sources.",
        "Copilot accepted the prompt but the workflow was interrupted by a privacy modal and then a human-verification gate.",
        "Business signal used public sources only; where a product-specific metric was not public, the report says so directly.",
    ],
    size=13,
)
add_image(page, fitz.Rect(700, 430, 1210, 650), shots / "copilot-2-input.png", "Copilot prompt entered with privacy modal visible")

page = new_page()
add_title(page, "S1 - Product Moment")
add_image(page, fitz.Rect(40, 110, 610, 500), shots / "perplexity-1-entry.png", "Perplexity: search-first entry point")
add_image(page, fitz.Rect(670, 110, 1240, 500), shots / "copilot-1-entry.png", "Copilot: assistant-style entry point")
add_box(
    page,
    fitz.Rect(40, 530, 1240, 670),
    "Reading the entry points",
    [
        "Perplexity makes the search intention obvious immediately: one box, one verb, low setup cost.",
        "Copilot looks broader and more assistant-like: new chat, library, tasks, projects, discover, imagine. That is powerful but less specific for a fast cited-search task.",
        "First-turn clarity favors Perplexity.",
    ],
)

page = new_page()
add_title(page, "S2 - Workflow Evidence")
add_image(page, fitz.Rect(40, 110, 610, 520), shots / "perplexity-2-input.png", "Perplexity input state")
add_image(page, fitz.Rect(670, 110, 1240, 520), shots / "copilot-3-output.png", "Copilot blocked by human verification")
add_box(
    page,
    fitz.Rect(40, 545, 1240, 675),
    "Workflow verdict",
    [
        "Perplexity flow: open -> paste prompt -> Enter -> answer -> follow-ups.",
        "Copilot flow in this test: open -> paste prompt -> Enter -> privacy friction -> Cloudflare verification -> no answer.",
        "This makes Perplexity lower on physical load and workaround burden for the chosen task.",
    ],
)

page = new_page()
add_title(page, "S3 - Output and Trust")
add_image(page, fitz.Rect(40, 110, 610, 520), shots / "perplexity-3-output.png", "Perplexity returned a structured answer")
add_image(page, fitz.Rect(670, 110, 1240, 520), shots / "perplexity-4-source.png", "Perplexity showed a 10-source state and follow-ups")
add_box(
    page,
    fitz.Rect(40, 545, 1240, 675),
    "Trust signals observed",
    [
        "Perplexity showed citations, follow-up suggestions, and a note of uncertainty instead of overclaiming.",
        "Copilot could not be scored for answer quality because no first-pass answer was returned in guest mode.",
        "For this test, answer availability itself became a trust signal.",
    ],
)

page = new_page()
add_title(page, "S4 - Business Signal")
add_image(page, fitz.Rect(40, 110, 610, 420), shots / "perplexity-5-pricing.png", "Perplexity pricing surface: Pro at just $20/month")
add_image(page, fitz.Rect(670, 110, 1240, 420), shots / "copilot-5-pricing.png", "Microsoft official Copilot plan page")
add_box(
    page,
    fitz.Rect(40, 450, 1240, 675),
    "Public pricing and growth facts",
    [
        "Perplexity: TechCrunch (2025-06-05) reported 780M queries in May 2025, about 30M/day, with 20%+ month-over-month growth. CNBC (2025-03-20) reported ARR just under $100M. Official pricing surface shows Pro at $20/month.",
        "Copilot: CNBC (2025-07-30) reported 100M monthly active users across Copilot products. TechCrunch (2026-01-29) said Microsoft told it total Copilot users had grown to 150M and consumer daily users were nearly 3x year-over-year. Microsoft does not publicly break out standalone consumer Copilot revenue in the sources used here.",
        "Interpretation: Perplexity monetizes the answer engine directly; Microsoft monetizes AI through a wider Microsoft 365 ecosystem.",
    ],
)

page = new_page()
add_title(page, "S5.1-S5.5 - Product Judgment, Metrics, Moat")
add_box(
    page,
    fitz.Rect(40, 110, 390, 330),
    "Perplexity verdict: STRONG",
    [
        "Wins on first-turn task completion",
        "Clear search-first framing",
        "Visible citation behavior",
        "Direct freemium-to-Pro upsell",
    ],
)
add_box(
    page,
    fitz.Rect(430, 110, 780, 330),
    "Copilot verdict: PROMISING / AT RISK",
    [
        "Huge ecosystem and distribution",
        "Broad assistant ambition",
        "But first-pass guest research flow failed in this test",
        "Needs lower friction to win this exact use case",
    ],
)
add_box(
    page,
    fitz.Rect(820, 110, 1240, 330),
    "Moat snapshot",
    [
        "Perplexity: medium brand, medium data loop, weaker distribution moat.",
        "Copilot: very strong distribution moat via Microsoft, stronger switching costs inside M365, but product sharpness is less focused.",
    ],
)
add_box(
    page,
    fitz.Rect(40, 370, 1240, 675),
    "Metric notes used in the deck",
    [
        "Perplexity MAU is not consistently public, so the deck uses query volume as the stronger public operational proxy.",
        "Copilot user counts are public at the family-of-products level; the report marks that scope explicitly instead of pretending it is only the web chat product.",
        "Where no standalone revenue figure was public, the deck says so directly.",
    ],
)

page = new_page()
add_title(page, "S5.6-S5.8 - Niche, Spark -> Loop -> System, Link to Lab 1")
add_box(
    page,
    fitz.Rect(40, 110, 610, 310),
    "Perplexity",
    [
        "Niche: answer engine for users who want fast search with citations.",
        "Stage: LOOP.",
        "Why: repeat behavior is already clear - query, source-check, follow-up, deeper search.",
        "Risk: can be squeezed by big-tech distribution.",
    ],
)
add_box(
    page,
    fitz.Rect(670, 110, 1240, 310),
    "Microsoft Copilot",
    [
        "Niche: broad AI companion inside Microsoft surfaces.",
        "Stage: SYSTEM.",
        "Why: embedded across a larger ecosystem, not just a single search surface.",
        "Risk: broadness may weaken sharpness on a specialist search task.",
    ],
)
add_box(
    page,
    fitz.Rect(40, 350, 1240, 670),
    "Link back to Lab 1 (Chegg vs ChatGPT)",
    [
        "Lab 1 showed that user expectations shift from old workflow navigation to do-the-answer-for-me-now. Perplexity fits that new expectation better in this test.",
        "Chegg was squeezed because the old workflow became too slow relative to AI-native alternatives. Copilot is less exposed on distribution, but it can still lose task-level trust if the first-turn flow blocks the answer.",
        "Key lesson carried forward: first-turn completion, visible evidence, and product focus matter more than brand alone.",
    ],
)

page = new_page()
add_title(page, "Sources")
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
        "7. Microsoft Support - What is the difference between the Microsoft Copilot experiences?",
        "8. Microsoft official pricing page for individuals: https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals",
        "9. CNBC - 2025-07-30 - Microsoft Q4 earnings report 2025",
        "10. TechCrunch - 2026-01-29 - Satya Nadella insists people are using Microsofts Copilot AI a lot",
    ],
    size=12,
)

if out_path.exists():
    out_path.unlink()
doc.save(out_path)
print(out_path)
