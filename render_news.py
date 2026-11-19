#!/usr/bin/env python3
"""Render a single 1920x1080 image summarizing 18 Nov 2026 world news."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
img = Image.new("RGB", (W, H), "#0b0e14")
draw = ImageDraw.Draw(img)

# ── Colors ──
BG      = "#0b0e14"
HEADER  = "#ffffff"
ACCENT  = "#38bdf8"
SUB     = "#94a3b8"
CARD    = "#131a26"
CARD2   = "#0f1520"
RED     = "#f87171"
GOLD    = "#fbbf24"
GREEN   = "#4ade80"
BLUE    = "#60a5fa"
PURPLE  = "#c084fc"
ORANGE  = "#fb923c"
TEAL    = "#2dd4bf"

# ── Fonts ──
def font(size):
    for f in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default(size)

def font_reg(size):
    for f in ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default(size)

bold = font(20)
title_font = font(32)
date_font = font_reg(22)
body_font = font_reg(17)
big_font = font(28)
small_font = font_reg(14)

# ── Header ──
draw.rectangle([0, 0, W, 80], fill="#1e293b")
draw.text((40, 14), "WORLD NEWS", fill=HEADER, font=title_font)
draw.text((40, 48), "18 November 2026", fill=ACCENT, font=date_font)
draw.text((1520, 48), "7 TOP STORIES", fill=SUB, font=font(18))

# ── Helper ──
def card(x, y, w, h, color, number, title, detail, tag, tag_color):
    draw.rectangle([x, y, x+w, y+h], fill=CARD, outline=color, width=2)
    # number circle
    draw.ellipse([x+12, y+12, x+12+36, y+12+36], fill=color)
    draw.text((x+20, y+16), str(number), fill="#fff", font=font(18))
    # tag
    draw.text((x+60, y+16), tag, fill=tag_color, font=small_font)
    # title
    draw.text((x+16, y+48), title, fill=HEADER, font=bold)
    # detail (wrap)
    words = detail.split()
    line = " "
    cy = y+76
    for word in words:
        test = line + word + " "
        if draw.textlength(test, font=body_font) > w-36:
            draw.text((x+16, cy), line.strip(), fill=SUB, font=body_font)
            line = word + " "
            cy += 22
        else:
            line = test
    if line.strip():
        draw.text((x+16, cy), line.strip(), fill=SUB, font=body_font)

# ── Layout: 2 cols, 3 rows + 1 center ──
cw = 910
ch = 200
gap_x = 16
gap_y = 14

# Row 1
card(20, 96, cw, ch, GOLD, 1,
     "Van Gogh Auction Record — $190.4M",
     "Châtaigniers en fleurs sold at Sotheby's New York, smashing previous record of $117M. Part of Blaquier-Arrieta collection ($412M total). Nazi-era provenance resolved with Fischer heirs.",
     "ART • AUCTION", GOLD)

card(946, 96, cw, ch, GREEN, 2,
     "Nvidia Soars Without Jensen Huang",
     "Q3 revenue $115.8B (+103% YoY), net income $65.3B. Board rules out Huang's CEO return. Interim CEO Colette Kress raises FY2028 growth forecast to 75%. Q4 guidance $130B beats Street.",
     "TECH • EARNINGS", GREEN)

# Row 2
card(20, 310, cw, ch, BLUE, 3,
     "Hakeem Jeffries Eyes House Speaker",
     "Secured 215 votes — closest Democrat to becoming first Black Speaker. Faces progressive demands on healthcare, immigration. Republicans unable to block nomination process.",
     "US POLITICS", BLUE)

card(946, 310, cw, ch, RED, 4,
     "APEC Summit: Xi, Putin, Trump Converge",
     "Xi-Putin bilateral talks in Shenzhen ahead of historic US-China-Russia trilateral. Xi defends free trade, warns against protectionism. Mexico's Sheinbaum negotiates USMCA tariff relief.",
     "DIPLOMACY", RED)

# Row 3
card(20, 524, cw, ch, PURPLE, 5,
     "Bukele Strikes Haitian Gang Leader's Mansion",
     "Salvadoran president confirms airstrike destroyed Jeff Larose's luxury home in Port-au-Prince. Unclear if gang leader was inside. Part of Bukele's expanding Caribbean security mission.",
     "HAITI • SECURITY", PURPLE)

card(946, 524, cw, ch, ORANGE, 6,
     "Russian Spy Arrested in Silicon Valley",
     "FBI arrests alleged Russian agent for spying on major US tech/defense firm with offices in Palo Alto. The company was not named in the indictment.",
     "CYBER • ESPIONAGE", ORANGE)

# Row 4 — full width
card(20, 738, 1880, 160, TEAL, 7,
     "Deutsche Bank Data Leak — 15M Files Exposed",
     "German data regulator opens investigation into massive breach of 15 million files. Possible GDPR violations under scrutiny. One of the largest financial data leaks in European history. Meanwhile — ICC to rule on Myanmar Rohingya genocide case (Nov 19); Europe warns of return to pre-antibiotic era amid drug-resistant superbugs; Robert Pattinson confirmed as new James Bond.",
     "EUROPE • DATA BREACH", TEAL)

# ── Footer ──
draw.rectangle([0, H-36, W, H], fill="#1e293b")
draw.text((20, H-32), "Sources: Euronews • AP • EL PAÍS • Reuters • CNBC • Sotheby's • Le Monde • Fortune", fill=SUB, font=small_font)
draw.text((1300, H-32), "Compiled 2026-11-19", fill=SUB, font=small_font)

out = "/root/agents/makefun/entries/news-image-20261118/repo/news-20261118.png"
img.save(out, "PNG")
print(f"Saved {out} ({img.size[0]}x{img.size[1]})")
