#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    class Point:
        def __init__(x, y):
            x = int(x)
            y = int(y)
            return x, y

        def peremeshenie(self):
            x = x + 1
            y = y + 1
            return x, y

        def rasstoyanie(self):
            to_x = x
            to_y = y
            return to_x, to_y

        def sravnenie(self):
            if x == y:
                return True
            else:
                return False


