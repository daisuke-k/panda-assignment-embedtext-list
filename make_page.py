#!/usr/bin/env python

import glob
import argparse
import sys
import re

p = re.compile('.* \((\d+)\)')

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--dir", help="PandAからダウンロードしたzipファイルを解答したディレクトリ")
args = parser.parse_args()

if args.dir is None:
    print("no directory")
    sys.exit(1)

ids = []
dl = {}

dirlist = glob.glob("{}/* (*)".format(args.dir))
for d in dirlist:
    d1 = d.split('/')[-1]
    m = p.match(d1)
    if m is None:
        continue
    id = m.group(1)
    dl[id] =  [d, d1]
    ids.append(id)

for i in sorted(ids):
    print("<p>{}</p><iframe src=\"{}/{}_submissionText.html\" width=\"800\" height=\"125\"></iframe>".format(dl[i][1], dl[i][0], dl[i][1]))
    