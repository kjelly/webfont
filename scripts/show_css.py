#!/usr/bin/env python3
import sys
import os
import re
import shutil
from subprocess import check_output
from fontTools import ttLib

FONT_SPECIFIER_FAMILY_ID = 1
FONT_SPECIFIER_SUB_FAMILY_ID = 2


def get_font_name(path: str) -> str:
    with open(path, 'r') as ftr:
        font_meta = ttLib.TTFont(ftr.buffer)
    family, sub_family = "", ""
    for record in font_meta["name"].names:
        if record.nameID == FONT_SPECIFIER_SUB_FAMILY_ID and not sub_family:
            sub_family = record.string.decode('utf-8')
        elif record.nameID == FONT_SPECIFIER_FAMILY_ID and not family:
            family = record.string.decode('utf-8')
        if sub_family and family:
            break
    return family


def main():
    font_dir_path = sys.argv[1]
    font_path = check_output("find %s -name '*Nerd Font Complete Mono*f' -type f|grep Mono|grep Regu|fzf" %
                             font_dir_path, shell=True).decode('utf-8').strip()
    shutil.copy(font_path, '/tmp/a.ttf')
    font_name = get_font_name('/tmp/a.ttf')
    url = re.sub(r'.*patched-fonts/', '', font_path)
    font_dir_path = font_dir_path.replace(
        'https://github.com/ryanoasis/nerd-fonts/blob/master/patched-fonts', '').strip()

    output = '''
@font-face {
  font-family: %s;
  font-weight: normal;
  src: url("https://cdn.jsdelivr.net/gh/ryanoasis/nerd-fonts@bc4416e1/patched-fonts/%s");
}
    ''' % (font_name, url)
    print(output)


if __name__ == '__main__':
    main()
