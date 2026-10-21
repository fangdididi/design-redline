#!/usr/bin/env python3
"""contrast.py — WCAG 2.2 contrast checker for design-redline.

Computes the contrast ratio between two colors and reports which WCAG levels
each use case passes (normal text, large text, UI components / graphics).

Usage:
    python3 contrast.py "#1a1a1a" "#ffffff"
    python3 contrast.py "rgb(230,115,115)" "white" --size 24
    python3 contrast.py --pairs pairs.csv      # CSV: fg,bg[,label]

No dependencies beyond the Python standard library.
"""
import argparse
import csv
import re
import sys

NAMED = {
    "white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0),
    "green": (0, 128, 0), "blue": (0, 0, 255), "gray": (128, 128, 128),
    "grey": (128, 128, 128), "silver": (192, 192, 192), "transparent": None,
}


def parse_color(value):
    """Parse #rgb, #rrggbb, rgb()/rgba(), or a basic named color to (r,g,b)."""
    if value is None:
        raise ValueError("no color given")
    s = value.strip().lower()
    if s in NAMED:
        c = NAMED[s]
        if c is None:
            raise ValueError("'transparent' has no fixed color; resolve it to the layer behind it first")
        return c
    m = re.fullmatch(r"#([0-9a-f]{3})", s)
    if m:
        return tuple(int(ch * 2, 16) for ch in m.group(1))
    m = re.fullmatch(r"#([0-9a-f]{6})", s)
    if m:
        h = m.group(1)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*[\d.]+\s*)?\)", s)
    if m:
        vals = [int(round(float(x))) for x in m.groups()]
        if any(v < 0 or v > 255 for v in vals):
            raise ValueError("rgb channels must be 0-255: " + value)
        return tuple(vals)
    raise ValueError("unrecognized color: " + value)


def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb):
    r, g, b = (_lin(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg, bg):
    l1 = relative_luminance(fg)
    l2 = relative_luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def is_large(size_px=None, bold=False):
    """WCAG large text: >=24px, or >=18.66px (14pt) bold."""
    if size_px is None:
        return False
    return size_px >= 24 or (bold and size_px >= 18.66)


def assess(ratio, size_px=None, bold=False):
    large = is_large(size_px, bold)
    text_aa = 3.0 if large else 4.5
    text_aaa = 4.5 if large else 7.0
    return {
        "ratio": round(ratio, 2),
        "large_text": large,
        "text_AA": ratio >= text_aa,
        "text_AAA": ratio >= text_aaa,
        "ui_component_AA": ratio >= 3.0,  # 1.4.11 non-text (no AAA tier)
    }


def _fmt(label, fg, bg, size, bold):
    r = contrast_ratio(fg, bg)
    a = assess(r, size, bold)
    tag = "large text" if a["large_text"] else "normal text"
    yn = lambda b: "PASS" if b else "FAIL"
    head = f"{label}: {a['ratio']}:1  ({tag})"
    lines = [
        head,
        f"  text AA (>= {'3' if a['large_text'] else '4.5'}:1):   {yn(a['text_AA'])}",
        f"  text AAA (>= {'4.5' if a['large_text'] else '7'}:1):  {yn(a['text_AAA'])}",
        f"  UI/graphic AA (>= 3:1):  {yn(a['ui_component_AA'])}",
    ]
    return "\n".join(lines), a


def main(argv=None):
    p = argparse.ArgumentParser(description="WCAG 2.2 contrast checker")
    p.add_argument("fg", nargs="?", help="foreground color")
    p.add_argument("bg", nargs="?", help="background color")
    p.add_argument("--size", type=float, default=None, help="text size in px (for large-text rule)")
    p.add_argument("--bold", action="store_true", help="text is bold")
    p.add_argument("--pairs", help="CSV file of fg,bg[,label] rows")
    args = p.parse_args(argv)

    if args.pairs:
        fail = 0
        with open(args.pairs, newline="") as f:
            for i, row in enumerate(csv.reader(f), 1):
                row = [c for c in row if c.strip() != ""]
                if not row or row[0].lstrip().startswith("#") and len(row) == 1:
                    continue
                label = row[2] if len(row) > 2 else f"pair {i}"
                try:
                    out, a = _fmt(label, parse_color(row[0]), parse_color(row[1]), args.size, args.bold)
                except (ValueError, IndexError) as e:
                    print(f"{label}: ERROR {e}", file=sys.stderr)
                    fail += 1
                    continue
                print(out + "\n")
                if not a["text_AA"]:
                    fail += 1
        return 1 if fail else 0

    if not args.fg or not args.bg:
        p.error("provide two colors, or --pairs FILE")
    try:
        out, a = _fmt(f"{args.fg} on {args.bg}", parse_color(args.fg), parse_color(args.bg), args.size, args.bold)
    except ValueError as e:
        print("ERROR:", e, file=sys.stderr)
        return 2
    print(out)
    return 0 if a["text_AA"] else 1


if __name__ == "__main__":
    sys.exit(main())
