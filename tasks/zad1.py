#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    word = str(input('Введите слово --> ')).lower()
    count = 0
    vowels = set("аоэеиыуёюя")
    for letter in word:
        if letter in vowels:
            count += 1
    print(f"Количество гласных букв в слове {word} --> {count}")
