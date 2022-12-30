#!/usr/bin/python
# app/utils/const.py
import os
ROOT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir
)

"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# URL of the Greasy Fork userscript used in Tampermonkey.
SCRIPT_URL = 'https://greasyfork.org/fr/scripts/448109-hcaptcha-solver'

# URL of the demonstration website.
DEMONSTRATION_URL = 'https://maximedrn.github.io/hcaptcha-solver-python-selenium/'

# Paths of the Tampermonkey extension.

CHROMEDRIVER_EXTENSION_PATH = os.path.join(ROOT_PATH, 'assets/Tampermonkey.crx')
GECKODRIVER_EXTENSION_PATH = os.path.join(ROOT_PATH, 'assets/Tampermonkey.xpi')
