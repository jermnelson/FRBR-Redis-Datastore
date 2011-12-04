"""
 :mod:`profile` - Profile code for :mod:`marc2frbr`
"""
__author__ = 'Jeremy Nelson'

import pstats, cProfile

import marc2frbr

cProfile.runctxt("marc2frbr.process_marc_file('../fixures/ccweb.mrc')", 
                 globals(), 
                 locals(), 
                 "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()
