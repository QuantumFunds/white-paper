#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"Original Image Size: {width} x {height}")
    resized_image = original_image.resize(size, Image.ANTIALIAS)
    width, height = resized_image.size
    print(f"Resized Image Size: {width} x {height}")    
    resized_image.save(output_image_path)

def init_logo():
    input_path = './4000_4000.png'
    output_path = './2000_2000.png'
    new_size = (2000, 2000)
    resize_image(input_path, output_path, new_size)

    output_path = './1000_1000.png'
    new_size = (1000, 1000)
    resize_image(input_path, output_path, new_size)

    output_path = './500_500.png'
    new_size = (500, 500)
    resize_image(input_path, output_path, new_size)

    output_path = './300_300.png'
    new_size = (300, 300)
    resize_image(input_path, output_path, new_size)

    output_path = './150_150.png'
    new_size = (150, 150)
    resize_image(input_path, output_path, new_size)

    output_path = './128_128.png'
    new_size = (128, 128)
    resize_image(input_path, output_path, new_size)

    output_path = './64_64.png'
    new_size = (64, 64)
    resize_image(input_path, output_path, new_size)

    output_path = './32_32.png'
    new_size = (32, 32)
    resize_image(input_path, output_path, new_size)

def resize():
    im = Image.open("./qft.png")

    box = (400, 400, 4400, 4400)
    region = im.crop(box)

    region.save("./4000_4000.png")

resize()
init_logo()