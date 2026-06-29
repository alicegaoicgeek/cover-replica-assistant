#!/usr/bin/env python3
"""生成 R2 封面提示词 — 7 种定稿风格，一键复现"""
import json, sys, argparse

SIZE_MAP = {
    "3:4": "1024x1536", "1:1": "1024x1024", "9:16": "768x1365",
    "2.35:1": "1410x600", "wechat": "1410x600", "bigcover": "1410x600",
}

STYLES = {
    "1": {"name": "Swiss Editorial", "score": 9.1},
    "2": {"name": "Alert Bar", "score": 9.0},
    "3": {"name": "Pure Type Poster", "score": 9.0},
    "4": {"name": "Dark Monumental", "score": 8.9},
    "5": {"name": "Macro Type Crop", "score": 8.8},
    "6": {"name": "Highlighter Memo", "score": 8.8},
    "7": {"name": "Kinetic Diagonal", "score": 8.7},
}

# 7 种风格的 prompt 模板（{title} 为可变占位符）
STYLE_PROMPTS = {
    "1": """A clean Swiss editorial magazine cover, 2.35:1 horizontal format.
Cream white paper background with subtle grain texture.
A solid dark charcoal rectangle occupies the right 40% of the image, with perfectly clean straight edges.
At the boundary between cream and charcoal: massive ultra-bold letters "R2". The "R" is dark charcoal sitting on the cream side. The "2" is bright orange sitting on the charcoal side.
Below the R2, on the cream side, in clean dark gray sans-serif: the Chinese text "{title}".
The entire design is minimal, clean, and precise. Only the colors cream white, dark charcoal gray, bright orange, and medium gray exist. No other elements. No text in corners. No decorations. Pure Swiss design.""",

    "2": """A WeChat public account cover, 2.35:1 horizontal. Alert bar thumbnail layout.
Solid cream background for the upper 70% of the image.
A thick charcoal horizontal band across the bottom 30%, with clean straight edges.
On the cream area: massive bold "R2" in charcoal type. The "2" is bright orange.
On the charcoal band: "{title}" in clean white sans-serif.
Simple. Bold. High contrast. Clean edges. No decorations.""",

    "3": """A WeChat public account cover, 2.35:1 horizontal. Pure typography poster.
Warm cream paper background. No images. No graphics. Only typography.
A single massive Chinese character fills 60% of the canvas, charcoal black, ultra-bold, slightly off-center left.
Superimposed on the character, a bright orange "R2" mark, like a highlighter annotation.
Below, clean dark gray sans-serif: "{title}".
The composition feels personal and urgent, like a note left on your desk.""",

    "4": """A WeChat public account cover, 2.35:1 horizontal. Cinematic monument design.
Entire canvas deep charcoal with subtle paper texture.
"R2" rendered as if carved from cream stone, lit from above-left. The letters cast subtle shadows. The "2" has a thin edge of orange light catching its rim.
"{title}" in small cream type below, understated.
Grounded, monumental, trustworthy. Only charcoal, cream stone, and one orange rim light.""",

    "5": """A clean magazine cover, 2.35:1 horizontal. Macro type crop design.
Cream white paper background with subtle grain.
The letter "R" is extremely large, filling the entire height of the image and bleeding off the left edge. Only about two-thirds of the letterform is visible. Dark charcoal color. Clean edges, no debris around the letter.
To its right, fully within frame: the number "2" in bright orange, also very large.
Below the 2, in clean dark gray sans-serif: "{title}".
Minimal, clean, architectural. Only cream white, dark charcoal, bright orange, and dark gray.""",

    "6": """A WeChat public account cover, 2.35:1 horizontal. Notebook memo aesthetic.
Cream paper with subtle horizontal ruled lines, like a real notebook page.
At the upper-left, handwritten bold "R2" in charcoal. The "2" has a bright orange highlighter swipe behind it, slightly extending past the text edges.
Below, on the ruled lines in clean printed sans-serif: "{title}" in dark gray.
The contrast between handwritten logo and printed body text creates warmth. Like someone's desk notebook.""",

    "7": """A WeChat public account cover, 2.35:1 horizontal. Kinetic diagonal headline.
Cream background. "R2" in massive bold typography, tilted at a 15-degree angle upward from left to right. The "R" is charcoal, the "2" is bright orange.
Behind the tilted text: several thin horizontal speed lines in charcoal, suggesting rapid movement.
"{title}" is straight (not tilted), small, in dark gray below.
Pure typographic dynamism. No images. Clean and energetic.""",
}

def main():
    p = argparse.ArgumentParser(description="R2 封面提示词生成器 — 7 种定稿风格")
    p.add_argument("--style", "-s", choices=list(STYLES.keys()), help="风格编号 1-7")
    p.add_argument("--title", "-t", default="芯片智能体", help="替换 {title} 的文案")
    p.add_argument("--ratio", default="2.35:1", help="画幅比例 (默认 2.35:1)")
    p.add_argument("--list", action="store_true", help="列出所有风格")
    p.add_argument("--json", action="store_true", help="JSON 输出")
    args = p.parse_args()

    if args.list:
        print("R2 封面 7 种定稿风格:\n")
        for k, v in STYLES.items():
            print(f"  [{k}] {v['name']} — {v['score']}/10")
        return

    if not args.style:
        p.error("需要 --style 1-7，或 --list 查看所有风格")

    prompt = STYLE_PROMPTS[args.style].replace("{title}", args.title)
    size = SIZE_MAP.get(args.ratio, "1410x600")
    info = STYLES[args.style]

    if args.json:
        print(json.dumps({
            "style": info["name"], "score": info["score"],
            "prompt": prompt, "size": size, "ratio": args.ratio
        }, ensure_ascii=False))
    else:
        print(prompt)
        print(f"\n# Style: {info['name']} ({info['score']}/10) | Size: {size} | Title: {args.title}")

if __name__ == "__main__":
    main()
