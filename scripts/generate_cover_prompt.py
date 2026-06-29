#!/usr/bin/env python3
"""生成 Agnes 封面提示词 — 基于参考图拆解结果 + 用户标题"""
import json, sys, argparse

TEMPLATE_DEEP = """参考上传的对标封面，本次为深度复刻：尽量保留原图的构图比例、标题位置、主体位置、画面密度、字体气质和视觉重心，但只复刻通用设计结构，不复制原图中的具体人物、签名、Logo、背景装饰、平台水印、原文案和独特识别元素。

请生成一张{brand}个人风格的{orientation}封面，画幅比例为{ratio}。

标题文字为：
- {title_main}
- {title_sub}
- {title_tag}

构图说明：
{composition}

字体说明：
{typography}

主体说明：
{subject}

氛围说明：
{atmosphere}

负面提示词（不要出现）：文字扭曲、畸形字体、多余手指、模糊低质、水印、签名、logo、杂乱背景
"""

SIZE_MAP = {
    "3:4": "1024x1536",
    "4:3": "1536x1024",
    "1:1": "1024x1024",
    "9:16": "768x1365",
    "16:9": "1536x864",
    "2.35:1": "1410x600",
}

def generate_prompt(args):
    return TEMPLATE_DEEP.format(
        brand=args.brand,
        orientation="竖版" if args.ratio in ("3:4","9:16") else "横版",
        ratio=args.ratio,
        title_main=args.main,
        title_sub=args.sub,
        title_tag=args.tag,
        composition=args.composition,
        typography=args.typography,
        subject=args.subject,
        atmosphere=args.atmosphere,
    )

def main():
    p = argparse.ArgumentParser(description="生成 Agnes 封面提示词")
    p.add_argument("--brand", default="R2芯片智能体")
    p.add_argument("--ratio", default="3:4")
    p.add_argument("--main", required=True, help="主标题")
    p.add_argument("--sub", required=True, help="副标题")
    p.add_argument("--tag", default="深度技术解析")
    p.add_argument("--composition", default="中央主体居中偏上，标题大字压画面上下区域，形成强压迫感。主体占画面中央约40%面积，背景深色带科技纹理。")
    p.add_argument("--typography", default="主标题白色超粗无衬线体，字距紧凑，像素级清晰。副标题青色系略小字重较轻。标签行底部白色大字。")
    p.add_argument("--subject", default="中央悬浮发光AI芯片，精密电路纹理，蓝色光效环绕。芯片表面有几何纹路，金属针脚细节锐利。")
    p.add_argument("--atmosphere", default="深蓝黑色渐变背景，电路板网格纹理，流动数据光线粒子，霓虹蓝紫光晕，赛博朋克科技感，4K高清，PBR物理材质，暗调高对比度。")
    p.add_argument("--json", action="store_true", help="输出 JSON")
    args = p.parse_args()
    prompt = generate_prompt(args)
    size = SIZE_MAP.get(args.ratio, "1024x1536")
    if args.json:
        print(json.dumps({"prompt":prompt, "size":size, "ratio":args.ratio}, ensure_ascii=False))
    else:
        print(prompt)
        print(f"\n# Size: {size}")

if __name__ == "__main__":
    main()
