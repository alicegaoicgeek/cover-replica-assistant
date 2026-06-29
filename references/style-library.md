# R2 封面风格库 · 7 种定稿风格

7 种独立美学体系，横跨精密→温度、权威→动能四个象限。每种风格有唯一 DNA、确定 prompt 模板和适用场景。

---

## 风格速查

| # | 风格 | 评分 | 构图DNA | 适用场景 |
|---|------|------|---------|---------|
| 1 | Swiss Editorial | 9.1 | 几何色块垂直分割，R2跨边界 | 品牌主封面、深度文章 |
| 2 | Alert Bar | 9.0 | 巨字+底部黑条带，YT验证CTR公式 | 重磅文章、必读内容 |
| 3 | Pure Type Poster | 9.0 | 单字占满画面，文字即封面 | 人文观点、品牌宣言 |
| 4 | Dark Monumental | 8.9 | 炭黑全底，R2如石碑雕刻+橙边光 | 年度回顾、里程碑 |
| 5 | Macro Type Crop | 8.8 | 字大到裁切出画，建筑感 | 系列开篇、专栏 |
| 6 | Highlighter Memo | 8.8 | 笔记本横线+荧光笔标记，亲切温度 | 教程、清单、干货 |
| 7 | Kinetic Diagonal | 8.7 | 15度斜切+速度线，动能冲击 | 快讯、解读、热点 |

---

## 铁律 · 100% 复现规则

### 规则 1：禁止 NEGATIVE 关键字
Agnes 会把 `NEGATIVE:` 后的文字渲染到画面中。
**正确做法**：用正向描述——`clean bottom-right corner, minimal, only 4 colors, no decorations`

### 规则 2：中文必须原文写入 prompt
不能用英文描述中文（如 "Chinese characters for..."），AI 会自造假中文。
**正确做法**：在 prompt 中直接写 `"芯片智能体"`

### 规则 3：PIL 修复时必须先取样真实背景色
不同 AI 生成的「奶油色」RGB 值不同（247,244,239 vs 237,222,187）。
**正确做法**：`bg = arr[center_y:center_y+100, center_x:center_x+40].mean(axis=(0,1)).astype(int)`

### 规则 4：交付前必过 agent QA
每张图交付前用 `agent --yolo --print` 检查：右下角干净、中文正确、无乱码。

---

## 风格 1 · Swiss Editorial (9.1)

**构图**：垂直几何分割，炭黑矩形占右 40%，R2 跨奶油/炭黑边界。R 在奶油侧炭黑色，2 在炭黑侧橙色。
**气质**：精密、权威、瑞士、Bauhaus
**色彩**：奶油(#F7F4EF) + 炭黑(#141414) + 橙色(#E8501F) + 深灰

**Prompt 模板**：
```
A clean Swiss editorial magazine cover, 2.35:1 horizontal format.
Cream white paper background with subtle grain texture.
A solid dark charcoal rectangle occupies the right 40% of the image, with perfectly clean straight edges.
At the boundary between cream and charcoal: massive ultra-bold letters "R2". The "R" is dark charcoal sitting on the cream side. The "2" is bright orange sitting on the charcoal side.
Below the R2, on the cream side, in clean dark gray sans-serif: the Chinese text "{标题}".
The entire design is minimal, clean, and precise. Only the colors cream white, dark charcoal gray, bright orange, and medium gray exist. No other elements. No text in corners. No decorations. Pure Swiss design.
```

---

## 风格 2 · Alert Bar (9.0)

**构图**：上 70% 奶油底+巨字 R2，下 30% 炭黑横条+白色标题。三层水平 rhythm。
**气质**：醒觉、紧急、高 CTR、经过验证
**色彩**：奶油 + 炭黑 + 橙色 + 白

**Prompt 模板**：
```
A WeChat public account cover, 2.35:1 horizontal. Alert bar thumbnail layout.
Solid cream background for the upper 70% of the image.
A thick charcoal horizontal band across the bottom 30%, with clean straight edges.
On the cream area: massive bold "R2" in charcoal type. The "2" is bright orange.
On the charcoal band: "{标题}" in clean white sans-serif.
Simple. Bold. High contrast. Clean edges. No decorations.
```

---

## 风格 3 · Pure Type Poster (9.0)

**构图**：单汉字占满 60% 画面，橙色 R2 标记叠印其上。纯文字，零图形。
**气质**：人文、张力、书法碰撞科技、文字即画面
**色彩**：奶油 + 炭黑 + 橙色

**Prompt 模板**：
```
A WeChat public account cover, 2.35:1 horizontal. Pure typography poster.
Warm cream paper background. No images. No graphics. Only typography.
A single massive Chinese character "{主字}" fills 60% of the canvas, charcoal black, ultra-bold, slightly off-center left.
Superimposed on the character, a bright orange "R2" mark, like a highlighter annotation.
Below, clean dark gray sans-serif: "{标题}".
The composition feels personal and urgent, like a note left on your desk.
```

---

## 风格 4 · Dark Monumental (8.9)

**构图**：炭黑全底，R2 如奶油色石碑雕刻，有物理阴影，2 的边缘有橙色光 rim。
**气质**：电影级、纪念碑、厚重、权威
**色彩**：炭黑底 + 奶油石色 + 橙色 rim light

**Prompt 模板**：
```
A WeChat public account cover, 2.35:1 horizontal. Cinematic monument design.
Entire canvas deep charcoal with subtle paper texture.
"R2" rendered as if carved from cream stone, lit from above-left. The letters cast subtle shadows. The "2" has a thin edge of orange light catching its rim.
"{标题}" in small cream type below, understated.
Grounded, monumental, trustworthy. Only charcoal, cream stone, and one orange rim light.
```

---

## 风格 5 · Macro Type Crop (8.8)

**构图**：R 大到裁切出画，只可见 60% 字面。2 完整在框内，橙色。
**气质**：建筑感、神秘、极端尺度、Form 杂志风
**色彩**：奶油 + 炭黑 + 橙色

**Prompt 模板**：
```
A clean magazine cover, 2.35:1 horizontal. Macro type crop design.
Cream white paper background with subtle grain.
The letter "R" is extremely large, filling the entire height of the image and bleeding off the left edge. Only about two-thirds of the letterform is visible. Dark charcoal color. Clean edges, no debris around the letter.
To its right, fully within frame: the number "2" in bright orange, also very large.
Below the 2, in clean dark gray sans-serif: "{标题}".
Minimal, clean, architectural. Only cream white, dark charcoal, bright orange, and dark gray.
```

---

## 风格 6 · Highlighter Memo (8.8)

**构图**：笔记本横线纸底，左上角手写感 R2，2 后面有橙色荧光笔涂抹（略超出文字边界）。下方印刷体标题。
**气质**：亲切、温度、UGC 感、反企业、朋友分享
**色彩**：奶油横线纸 + 炭黑 + 橙色荧光笔

**Prompt 模板**：
```
A WeChat public account cover, 2.35:1 horizontal. Notebook memo aesthetic.
Cream paper with subtle horizontal ruled lines, like a real notebook page.
At the upper-left, handwritten bold "R2" in charcoal. The "2" has a bright orange highlighter swipe behind it, slightly extending past the text edges.
Below, on the ruled lines in clean printed sans-serif: "{标题}" in dark gray.
The contrast between handwritten logo and printed body text creates warmth. Like someone's desk notebook.
```

---

## 风格 7 · Kinetic Diagonal (8.7)

**构图**：R2 整体 15 度倾斜，背景有水平速度线，标题水平不倾斜。
**气质**：动能、紧急、动势、YouTube Here's Why 风
**色彩**：奶油 + 炭黑 + 橙色

**Prompt 模板**：
```
A WeChat public account cover, 2.35:1 horizontal. Kinetic diagonal headline.
Cream background. "R2" in massive bold typography, tilted at a 15-degree angle upward from left to right. The "R" is charcoal, the "2" is bright orange.
Behind the tilted text: several thin horizontal speed lines in charcoal, suggesting rapid movement.
"{标题}" is straight (not tilted), small, in dark gray below.
Pure typographic dynamism. No images. Clean and energetic.
```

---

## 生图命令

```bash
# 所有风格统一参数
agnes-img-cli -s 1410x600 -n 2 -o output-dir/ < prompt.txt

# 交付前 QA
agent --yolo --print "检查：1.右下角干净 2.中文正确 3.无乱码 图片: output.png"
```

## 交付文件规范

- 中间产物 → `taste-output/agnes-covers/`
- 最终版 → `~/Desktop/r2-swiss/final7/`
- 命名：`{序号}-{风格名}-{评分}.png`
