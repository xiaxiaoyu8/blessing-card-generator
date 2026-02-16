import tkinter as tk
from tkinter import ttk
import random
import pyperclip
import json
import os
import sys

# 获取资源路径（兼容开发和打包环境）
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

def load_wishes():
    json_path = resource_path("data.json")
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# 全局变量
wishes = load_wishes()

def wish_text(wish_name, category):
    """获取指定节日和类别的祝福语"""
    if wish_name in wishes and category in wishes[wish_name]:
        return random.choice(wishes[wish_name][category])
    return ""


def show_wish():
    """显示祝福语并复制到剪贴板"""
    wish_name = combo_var.get()
    category = category_var.get()
    custom_name = name_entry.get().strip()

    selected_wish = wish_text(wish_name, category)

    # 添加自定义署名
    if selected_wish and custom_name:
        selected_wish = f"{selected_wish}\n\n{custom_name}给您拜年啦！"
    elif selected_wish:
        selected_wish = f"{selected_wish}"

    wish_label.config(text=selected_wish)
    pyperclip.copy(selected_wish)
    status_label.config(text="✓ 已复制到剪贴板", foreground="#27ae60")
    root.after(2000, lambda: status_label.config(text=""))


# 创建主窗口
root = tk.Tk()
root.geometry("700x550")
root.title("夏小雨8：节日祝福生成器 V2.0")
root.resizable(False, False)

# 设置整体背景色
root.configure(bg="#f5f6fa")

# 创建主框架
main_frame = tk.Frame(root, bg="#f5f6fa")
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# 标题区域
title_frame = tk.Frame(main_frame, bg="#f5f6fa")
title_frame.pack(fill=tk.X, pady=(0, 20))

title_label = tk.Label(
    title_frame,
    text="🎉 节日祝福生成器 V2.0 🎉",
    font=("Microsoft YaHei UI", 24, "bold"),
    bg="#f5f6fa",
    fg="#00ffff"
)
title_label.pack()

subtitle_label = tk.Label(
    title_frame,
    text="选择节日和对象，一键生成温馨祝福",
    font=("Microsoft YaHei UI", 10),
    bg="#f5f6fa",
    fg="#7f8c8d"
)
subtitle_label.pack()

# 选择区域
select_frame = tk.Frame(main_frame, bg="#ffffff", relief=tk.FLAT, bd=0)
select_frame.pack(fill=tk.X, pady=(0, 15))

# 添加内边距
inner_frame = tk.Frame(select_frame, bg="#ffffff")
inner_frame.pack(padx=20, pady=15)

# 节日选择
label1 = tk.Label(
    inner_frame,
    text="选择节日：",
    font=("Microsoft YaHei UI", 11),
    bg="#ffffff",
    fg="#2c3e50"
)
label1.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")

# 自定义样式
style = ttk.Style()
style.theme_use('clam')

# 下拉框样式
style.configure(
    "Custom.TCombobox",
    fieldbackground="#ffffff",
    background="#3498db",
    foreground="#2c3e50",
    arrowcolor="#3498db",
    borderwidth=1,
    relief="solid"
)

combo_var = tk.StringVar()
combo = ttk.Combobox(
    inner_frame,
    textvariable=combo_var,
    font=("Microsoft YaHei UI", 10),
    width=12,
    state="readonly",
    style="Custom.TCombobox"
)
combo["values"] = ["春节", "除夕", "元宵节", "端午节", "中秋节", "国庆节"]
combo.current(0)
combo.grid(row=0, column=1, padx=10, pady=5)

# 对象分类选择
label2 = tk.Label(
    inner_frame,
    text="祝福对象：",
    font=("Microsoft YaHei UI", 11),
    bg="#ffffff",
    fg="#2c3e50"
)
label2.grid(row=0, column=2, padx=(20, 10), pady=5, sticky="w")

category_var = tk.StringVar()
category_combo = ttk.Combobox(
    inner_frame,
    textvariable=category_var,
    font=("Microsoft YaHei UI", 10),
    width=12,
    state="readonly",
    style="Custom.TCombobox"
)
category_combo["values"] = ["长辈", "平辈", "晚辈"]
category_combo.current(0)
category_combo.grid(row=0, column=3, padx=10, pady=5)

# 自定义署名
label3 = tk.Label(
    inner_frame,
    text="您的称呼：",
    font=("Microsoft YaHei UI", 11),
    bg="#ffffff",
    fg="#2c3e50"
)
label3.grid(row=1, column=0, padx=(0, 10), pady=5, sticky="w")

name_entry = tk.Entry(
    inner_frame,
    font=("Microsoft YaHei UI", 10),
    width=14,
    relief="solid",
    borderwidth=1
)
name_entry.grid(row=1, column=1, padx=10, pady=5)
name_entry.insert(0, "")

# 提示文本
hint_label = tk.Label(
    inner_frame,
    text="（可选，如：小明、小红等）",
    font=("Microsoft YaHei UI", 8),
    bg="#ffffff",
    fg="#95a5a6"
)
hint_label.grid(row=1, column=2, columnspan=2, padx=10, pady=5, sticky="w")

# 按钮样式
style.configure(
    "Custom.TButton",
    font=("Microsoft YaHei UI", 10, "bold"),
    background="#3498db",
    foreground="#ffffff",
    borderwidth=0,
    focuscolor="none",
    padding=10
)

show_button = ttk.Button(
    inner_frame,
    text="🎁 生成祝福",
    command=show_wish,
    style="Custom.TButton",
    width=15
)
show_button.grid(row=2, column=1, columnspan=2, padx=10, pady=(10, 5))

# 状态提示
status_label = tk.Label(
    main_frame,
    text="",
    font=("Microsoft YaHei UI", 9),
    bg="#f5f6fa",
    fg="#27ae60"
)
status_label.pack()

# 祝福语显示区域
wish_frame = tk.Frame(main_frame, bg="#ffffff", relief=tk.FLAT, bd=0)
wish_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

# 添加滚动条
canvas = tk.Canvas(wish_frame, bg="#ffffff", highlightthickness=0)
scrollbar = ttk.Scrollbar(wish_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#ffffff")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

wish_label = tk.Label(
    scrollable_frame,
    text="👆 请选择节日、祝福对象，输入您的称呼（可选），然后点击生成按钮",
    font=("Microsoft YaHei UI", 11),
    bg="#ffffff",
    fg="#7f8c8d",
    wraplength=630,
    justify="left",
    padx=20,
    pady=20
)
wish_label.pack(fill=tk.BOTH, expand=True)

canvas.pack(side="left", fill="both", expand=True, padx=2, pady=2)
scrollbar.pack(side="right", fill="y")


# 鼠标滚轮绑定
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


canvas.bind_all("<MouseWheel>", _on_mousewheel)

# 底部信息
footer_frame = tk.Frame(main_frame, bg="#f5f6fa")
footer_frame.pack(pady=(10, 0))

footer_label1 = tk.Label(
    footer_frame,
    text="💡 祝福语已自动复制到剪贴板",
    font=("Microsoft YaHei UI", 9),
    bg="#f5f6fa",
    fg="#95a5a6"
)
footer_label1.pack()

footer_label2 = tk.Label(
    footer_frame,
    text="✨ 升级功能：支持长辈/平辈/晚辈分类 + 自定义署名",
    font=("Microsoft YaHei UI", 8),
    bg="#f5f6fa",
    fg="#9b59b6"
)
footer_label2.pack()

root.mainloop()