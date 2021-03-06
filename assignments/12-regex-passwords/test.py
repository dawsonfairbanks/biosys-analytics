#!/usr/bin/env python3
"""tests for password.py"""

import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = './pass.py'


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_usage():
    """usage"""

    rv1, out1 = getstatusoutput('{}'.format(prg))
    assert rv1 == 1
    assert re.match("usage", out1, re.IGNORECASE)

    rv2, out2 = getstatusoutput('{} {}'.format(prg, random_string()))
    assert rv2 == 1
    assert re.match("usage", out1, re.IGNORECASE)


# --------------------------------------------------
def test_reject():
    p1 = random_string()
    p2 = random_string()
    out = getoutput('{} {} {}'.format(prg, p1, p2))
    assert out == 'nah'


# --------------------------------------------------
def test_accept_01():
    p = random_string()
    out = getoutput('{} {} {}'.format(prg, p, p))
    assert out == 'ok'


# --------------------------------------------------
def test_accept_02():
    p = random_string()
    u = p[0].upper() + p[1:]
    out = getoutput('{} {} {}'.format(prg, p, u))
    assert out == 'ok'


# --------------------------------------------------
def test_accept_03():
    p = random_string()
    out = getoutput('{} {} {}'.format(prg, p, p.upper()))
    assert out == 'ok'


# --------------------------------------------------
def test_accept_04():
    p = random_string()
    c = random.choice(string.printable)
    out = getoutput('{} {} {}'.format(prg, p, c + p))
    assert out == 'ok'


# --------------------------------------------------
def test_accept_05():
    p = random_string()
    c = random.choice(string.printable)
    out = getoutput('{} {} {}'.format(prg, p, p + c))
    assert out == 'ok'


# --------------------------------------------------
def test_accept_06():
    p = random_string()
    c1 = random.choice(string.printable)
    c2 = random.choice(string.printable)
    out = getoutput('{} {} {}'.format(prg, p, c1 + p + c2))
    assert out == 'ok'
