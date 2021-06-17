#!/usr/bin/env python3
import sys
import os
import re
import shutil
from subprocess import check_output
from subprocess import check_output


def main():
    font_dir_path = sys.argv[1]
    font_path = check_output("find %s -name '*Nerd Font Complete Mono*f' -type f|grep Mono|grep Regu|fzf" % font_dir_path, shell=True).decode('utf-8').strip()
    shutil.copy(font_path, '/tmp/a.ttf')
    font_name = check_output('otfinfo --info /tmp/a.ttf|head -n 1|grep Family', shell=True).decode('utf-8').strip().split(':')[-1].strip()
    url = re.sub(r'.*patched-fonts/', '', font_path)
    font_dir_path = font_dir_path.replace('https://github.com/ryanoasis/nerd-fonts/blob/master/patched-fonts', '').strip()

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
