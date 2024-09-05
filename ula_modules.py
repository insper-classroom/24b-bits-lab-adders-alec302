#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = (a and not b) or (not a and b)
        carry.next = (a and b)

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]

    half_1 = halfAdder(a, b, s[0], s[1]) 
    half_2 = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()


@block
def adder2bits(x, y, soma, carry):

    c0 = Signal(bool(0))

    ha = halfAdder(x[0], y[0], soma[0], c0)
    fa = fullAdder(x[1], y[1], c0, soma[1], carry)


    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        

    return instances()
