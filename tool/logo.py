# -*- coding: utf-8 -*-
# @Author  : Shajiu
# @FileName: logo.py
# @Time    : 2022/1/15 16:13
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import Stroke
def logo():
    # 解决 matplotlib 显示中文问题
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
    # 解决保存图像是负号 '-' 显示为方块的问题
    plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
    fig = plt.figure(figsize=(15, 4))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_xticks([])
    ax.set_yticks([])
    family = "SimHei"
    size = 80
    cmap = plt.cm.Blues_r
    text = "源码上门取算法码上到"
    for x in np.linspace(0, 1, 20):
        lw, color = x * 225, cmap(1 - x)
        t = ax.text(
            0.5,
            0.45,
            text,
            size=size,
            color="none",
            weight="bold",
            va="center",
            ha="center",
            family=family,
            zorder=-lw,
        )
        t.set_path_effects([Stroke(linewidth=lw + 1, foreground="black")])
        t = ax.text(
            0.5,
            0.45,
            text,
            size=size,
            color='black',  # 中心文字颜色
            weight="bold",
            va="center",
            ha="center",
            family=family,
            zorder=-lw + 1,
        )
        t.set_path_effects([Stroke(linewidth=lw, foreground=color)])
    t = ax.text(
        1.0,
        0.01,
        "https://shajiu.github.io",
        va="bottom",
        ha="right",
        size=20,
        color="white",
        family=family,
        alpha=0.50,
    )
    # plt.savefig("./01Practice/Matplotlib/text-outline.pdf")
    # plt.savefig("text-outline.pdf")
    plt.savefig("text-outline.png")
    plt.show()

if __name__ == '__main__':
    logo()
