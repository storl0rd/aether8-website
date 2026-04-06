"""
Generate 4 OG images (1200x630) for aether8.ai website.
Luminous Signal design philosophy — dark, typographic, premium.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os

FONTS = "/Users/aether/.claude/skills/canvas-design/canvas-fonts"
OUT = "/Users/aether/codespace/aether8-website/public"

W, H = 1200, 630
LM, RM = 80, 1120   # left / right margins
RULE_Y = 108         # horizontal divider line y

def hex_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# Palette
BG        = hex_rgb('#06060e')
SLATE_300 = hex_rgb('#cbd5e1')
SLATE_400 = hex_rgb('#94a3b8')
SLATE_500 = hex_rgb('#64748b')
WHITE     = (255, 255, 255)

CYAN    = hex_rgb('#00d4ff')
PURPLE  = hex_rgb('#a78bfa')
EMERALD = hex_rgb('#34d399')
AMBER   = hex_rgb('#f59e0b')

DARK_GREEN = hex_rgb('#031a0e')
GREEN_TEXT = hex_rgb('#4ade80')
GREEN_DOT  = hex_rgb('#22c55e')
DARK_AMBER = hex_rgb('#3b1e06')
AMBER_TEXT = hex_rgb('#fcd34d')


# ── Fonts ──────────────────────────────────────────────────────────────────────
def fnt(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

font_hero_xl  = fnt('BigShoulders-Bold.ttf', 148)
font_hero_lg  = fnt('BigShoulders-Bold.ttf', 116)
font_hero_md  = fnt('BigShoulders-Bold.ttf', 104)
font_tagline  = fnt('InstrumentSans-Regular.ttf', 27)
font_sub      = fnt('InstrumentSans-Regular.ttf', 18)
font_brand    = fnt('GeistMono-Bold.ttf', 12)
font_badge    = fnt('InstrumentSans-Bold.ttf', 11)


# ── Helpers ───────────────────────────────────────────────────────────────────
def measure(text, font):
    """Return (w, h) of rendered text."""
    d = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    bb = d.textbbox((0, 0), text, font=font)
    return bb[2] - bb[0], bb[3] - bb[1]


def make_grain_base():
    base = np.full((H, W, 3), BG, dtype=np.uint8)
    np.random.seed(2025)
    noise = np.random.randint(0, 255, (H, W, 3), dtype=np.uint8)
    blended = (base.astype(np.float32) * 0.979 + noise.astype(np.float32) * 0.021).clip(0, 255)
    return Image.fromarray(blended.astype(np.uint8), 'RGB')


def add_glow(img, color, cx, cy, radius=520, peak=0.062):
    """Soft radial glow via layered ellipses + gaussian blur."""
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    steps = 90
    for i in range(steps, 0, -1):
        r = int(radius * i / steps)
        t = i / steps
        alpha = int(255 * peak * (1 - t) ** 1.8)
        if alpha < 1:
            continue
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, alpha))
    overlay = overlay.filter(ImageFilter.GaussianBlur(55))
    result = Image.alpha_composite(img.convert('RGBA'), overlay)
    return result.convert('RGB')


def gradient_text(img, text, x, y, font, c1, c2, anchor='lm'):
    """Draw text with a left-to-right gradient from c1 to c2."""
    dummy = ImageDraw.Draw(Image.new('RGBA', (2, 2)))
    bb = dummy.textbbox((x, y), text, font=font, anchor=anchor)
    x0, y0_bb, x1, y1_bb = bb
    tw = x1 - x0
    th = y1_bb - y0_bb
    if tw <= 0 or th <= 0:
        return img

    # Build gradient strip via numpy
    t = np.linspace(0, 1, tw, dtype=np.float32)
    r_ch = (c1[0] * (1 - t) + c2[0] * t).astype(np.uint8)
    g_ch = (c1[1] * (1 - t) + c2[1] * t).astype(np.uint8)
    b_ch = (c1[2] * (1 - t) + c2[2] * t).astype(np.uint8)
    a_ch = np.full(tw, 255, dtype=np.uint8)
    row = np.stack([r_ch, g_ch, b_ch, a_ch], axis=1)     # (tw, 4)
    grad_arr = np.tile(row, (th, 1, 1))                    # (th, tw, 4)
    grad_img = Image.fromarray(grad_arr, 'RGBA')

    # Text mask
    mask_full = Image.new('L', (W, H), 0)
    ImageDraw.Draw(mask_full).text((x, y), text, fill=255, font=font, anchor=anchor)
    mask_crop = mask_full.crop(bb)

    # Composite
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    layer.paste(grad_img, (x0, y0_bb), mask_crop)
    result = Image.alpha_composite(img.convert('RGBA'), layer)
    return result.convert('RGB')


def draw_rule(img, y=RULE_Y, alpha=35):
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.line([(LM, y), (RM, y)], fill=(255, 255, 255, alpha), width=1)
    return Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')


def draw_bottom_rule(img, alpha=20):
    y = H - 60
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.line([(LM, y), (RM, y)], fill=(255, 255, 255, alpha), width=1)
    return Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')


def draw_badge(img, text, right_x, top_y, bg_color, text_color, dot_color=None, font=None):
    d = ImageDraw.Draw(img)
    bb = d.textbbox((0, 0), text, font=font)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    px, py = 13, 6
    dot_space = 15 if dot_color else 0
    pw = tw + px * 2 + dot_space
    ph = th + py * 2
    x0 = right_x - pw
    y0 = top_y
    x1 = right_x
    y1 = y0 + ph
    radius = ph // 2

    d.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=bg_color)

    tx = x0 + px
    ty = y0 + py

    if dot_color:
        dr = 3
        dcx = tx + dr + 1
        dcy = (y0 + y1) // 2
        d.ellipse([dcx - dr, dcy - dr, dcx + dr, dcy + dr], fill=dot_color)
        tx = dcx + dr + 7

    d.text((tx, ty), text, fill=text_color, font=font)
    return img


def draw_chrome(img, badge_text=None, badge_type='early'):
    """Draw persistent chrome: brand mark top-left, URL bottom-left, rules, optional badge."""
    img = draw_rule(img)
    img = draw_bottom_rule(img)

    d = ImageDraw.Draw(img)
    # Top-left brand mark
    d.text((LM, 42), 'AETHER8.AI', fill=SLATE_400, font=font_brand)
    # Bottom-left URL
    d.text((LM, H - 42), 'aether8.ai', fill=SLATE_500, font=font_brand)

    if badge_text:
        if badge_type == 'live':
            draw_badge(img, badge_text, RM, 38, DARK_GREEN, GREEN_TEXT, dot_color=GREEN_DOT, font=font_badge)
        else:
            draw_badge(img, badge_text, RM, 38, DARK_AMBER, AMBER_TEXT, font=font_badge)

    return img


def vertical_center_y(block_height, top=RULE_Y + 10, bottom=H - 60):
    """Return the y that centers a block_height-tall block in [top, bottom]."""
    available = bottom - top
    return top + (available - block_height) // 2


# ── Page generators ───────────────────────────────────────────────────────────

def make_pursuit():
    img = make_grain_base()
    img = add_glow(img, CYAN, 860, 310, radius=540, peak=0.058)
    img = draw_chrome(img, badge_text='Live', badge_type='live')

    # Wordmark
    wm_font = font_hero_xl
    wm_text = 'PURSUIT'
    tw, th = measure(wm_text, wm_font)
    tag_text = 'AI Research Agent for B2B Sales Teams'
    t_tw, t_th = measure(tag_text, font_tagline)

    block_h = th + 20 + t_th
    y_top = vertical_center_y(block_h)
    wm_y = y_top + th // 2   # anchor lm = middle of text

    img = gradient_text(img, wm_text, LM, wm_y, wm_font, CYAN, (220, 248, 255), anchor='lm')

    d = ImageDraw.Draw(img)
    d.text((LM, y_top + th + 20), tag_text, fill=SLATE_300, font=font_tagline)

    img.save(os.path.join(OUT, 'og-pursuit.png'), 'PNG', optimize=True)
    print('✓ og-pursuit.png')


def make_showwalker():
    img = make_grain_base()
    img = add_glow(img, PURPLE, 870, 315, radius=520, peak=0.060)
    img = draw_chrome(img, badge_text='Early Access', badge_type='early')

    wm_font = font_hero_md   # slightly smaller to fit SHOWWALKER
    wm_text = 'SHOWWALKER'
    tw, th = measure(wm_text, wm_font)
    tag_text = 'AI Exhibitor Intelligence for Tradeshows'
    t_tw, t_th = measure(tag_text, font_tagline)

    block_h = th + 20 + t_th
    y_top = vertical_center_y(block_h)
    wm_y = y_top + th // 2

    img = gradient_text(img, wm_text, LM, wm_y, wm_font, PURPLE, (237, 225, 255), anchor='lm')

    d = ImageDraw.Draw(img)
    d.text((LM, y_top + th + 20), tag_text, fill=SLATE_300, font=font_tagline)

    img.save(os.path.join(OUT, 'og-showwalker.png'), 'PNG', optimize=True)
    print('✓ og-showwalker.png')


def make_scrnr():
    img = make_grain_base()
    img = add_glow(img, EMERALD, 860, 310, radius=520, peak=0.056)
    img = draw_chrome(img, badge_text='Early Access', badge_type='early')

    wm_font = font_hero_xl
    wm_text = 'SCRNR'
    tw, th = measure(wm_text, wm_font)
    tag_text = 'AI Pre-Screening for B2C Lead Teams'
    t_tw, t_th = measure(tag_text, font_tagline)

    block_h = th + 20 + t_th
    y_top = vertical_center_y(block_h)
    wm_y = y_top + th // 2

    img = gradient_text(img, wm_text, LM, wm_y, wm_font, EMERALD, (220, 255, 240), anchor='lm')

    d = ImageDraw.Draw(img)
    d.text((LM, y_top + th + 20), tag_text, fill=SLATE_300, font=font_tagline)

    img.save(os.path.join(OUT, 'og-scrnr.png'), 'PNG', optimize=True)
    print('✓ og-scrnr.png')


def make_home():
    img = make_grain_base()
    # Dual glow — cyan left, purple right
    img = add_glow(img, CYAN,   380, 315, radius=460, peak=0.038)
    img = add_glow(img, PURPLE, 900, 315, radius=400, peak=0.036)
    img = draw_chrome(img, badge_text=None)

    wm_font = font_hero_xl
    wm_text = 'AETHER8'
    tw, th = measure(wm_text, wm_font)
    tag_text = 'Forward-Deployed AI Engineering'
    t_tw, t_th = measure(tag_text, font_tagline)
    sub_text = 'Pursuit  ·  Showwalker  ·  Scrnr'
    s_tw, s_th = measure(sub_text, font_sub)

    block_h = th + 18 + t_th + 14 + s_th
    y_top = vertical_center_y(block_h)
    wm_y = y_top + th // 2

    img = gradient_text(img, wm_text, LM, wm_y, wm_font, CYAN, PURPLE, anchor='lm')

    d = ImageDraw.Draw(img)
    d.text((LM, y_top + th + 18), tag_text, fill=SLATE_300, font=font_tagline)
    d.text((LM, y_top + th + 18 + t_th + 14), sub_text, fill=SLATE_500, font=font_sub)

    img.save(os.path.join(OUT, 'og-home.png'), 'PNG', optimize=True)
    print('✓ og-home.png')


if __name__ == '__main__':
    make_pursuit()
    make_showwalker()
    make_scrnr()
    make_home()
    print('\nAll 4 OG images saved to', OUT)
