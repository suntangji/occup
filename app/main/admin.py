# -*- coding: utf-8 -*-

CLOSE = False


def get_close_value():
    global CLOSE
    return CLOSE


def set_close_value():
    global CLOSE
    CLOSE = not CLOSE
    return CLOSE