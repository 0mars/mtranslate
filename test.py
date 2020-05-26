#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.mtranslate import translate


def main():
    to_translate = 'Bonjour comment allez vous?'
    print(translate(to_translate))
    print(translate(to_translate, 'ar'))
    print(translate(to_translate, 'ru'))

if __name__ == '__main__':
    main()
