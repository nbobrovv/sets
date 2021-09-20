#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    str1 = str(input('Введите что-нибудь --> ')).lower()
    str2 = str(input('Введите что-нибудь ещё раз --> ')).lower()

    common_letters = set(str1) & set(str2)

    print(common_letters)
