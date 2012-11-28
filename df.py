#!/usr/bin/env python
# df.py
# inispirational code taken from:
# https://gist.github.com/1569253

from __future__ import with_statement
import contextlib, os, sys 

def fsinfo():
#  print "Filesystem\tMounted on\tUse%\tIUse%\n"
  array = "Filesystem\tMounted on\tUse%\tIUse%\n"
  with contextlib.closing(open('/etc/mtab')) as fp: 
    for m in fp: 
      fs_spec, fs_file, fs_vfstype, fs_mntops, fs_freq, fs_passno = m.split()
      if fs_spec.startswith('/'):
        r = os.statvfs(fs_file)
        try: 
          block_usage_pct = 100.0 - (float(r.f_bavail) / float(r.f_blocks) * 100)
        except ZeroDivisionError:
          block_usage_pct = 0
        try:
          inode_usage_pct = 100.0 - (float(r.f_favail) / float(r.f_files) * 100)
        except ZeroDivisionError:
          inode_usage_pct = 0
 #       print "%s\t%s\t\t%d%%\t%d%%" % (fs_spec, fs_file, block_usage_pct, inode_usage_pct)
        array = array + "%s\t%s\t\t%d%%\t%d%%\n" % (fs_spec, fs_file, block_usage_pct, inode_usage_pct)
  return array
# vim:set ft=python :
