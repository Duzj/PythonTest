# -*- coding=utf-8 -*-

from PIL import Image
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')     # 输入文件
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
# 使用的字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha):
    # 判断alpha的值
    if alpha == 0:
        return ' '
    # 获取字符集的长度
    length = len(ascii_char)

    # 将RGB值转换为灰度值gray，灰度值范围为0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 灰度值范围为0-255，而字符集长度只有70
    # 需要进行处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1)/length

    # 返回灰度值对应的字符
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':
    # 打开并调整图片的宽和高
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 初始化输出的字符串
    txt = ""

    # 遍历图片中的每一行
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # 将 (j,i) 坐标的 RGB 像素转为字符后添加到 txt 字符串
            txt += get_char(*im.getpixel((j, i)))
        # 遍历完一行后需要增加换行符
        txt += '\n'
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)
