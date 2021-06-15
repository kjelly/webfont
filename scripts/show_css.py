#!/usr/bin/env python3
import sys
import os
from subprocess import check_output


def main():
    url = sys.argv[1]
    download_url = '%s?raw=true' % url
    os.system('wget "%s" -O /tmp/a.ttf -o /dev/null' % download_url)
    font_name = check_output('otfinfo --info /tmp/a.ttf|head -n 1|grep Family', shell=True).decode('utf-8').strip().split(':')[-1].strip()
    path = url.replace('https://github.com/ryanoasis/nerd-fonts/blob/master/patched-fonts', '').strip()

    output = '''
@font-face {
  font-family: %s;
  font-weight: normal;
  src: url("https://cdn.jsdelivr.net/gh/ryanoasis/nerd-fonts@bc4416e1/patched-fonts/%s");
}
    ''' % (font_name, path)
    print(output)


if __name__ == '__main__':
    main()
