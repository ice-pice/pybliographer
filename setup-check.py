# -*- coding: utf-8 -*-

import sys, string, re, traceback, os

base_version = string.split (sys.version) [0]
base_version = re.match ('[\d\.]+', base_version).group (0)

version = map (int, string.split (base_version, '.'))
if len (version) < 3: version.append (0)
fd = open ('conftest.out', 'w')
fd.write ('Python_Version=%s\n' % base_version)
fd.write ('Python_Major_Version=%d\n' % version [0])
fd.write ('Python_Minor_Version=%d\n' % version [1])
fd.write ('Python_Micro_Version=%d\n' % version [2])
fd.write ('Python_Prefix="%s"\n' % sys.exec_prefix)
fd.close ()


def error (msg):
    fd = open ('conftest.out', 'a')
    fd.write ('Status="%s"\n' % msg)
    fd.close ()

    sys.exit (1)

def warning (msg):
    fd = open ('conftest.out', 'a')
    fd.write ('Status="%s"\n' % msg)
    fd.close ()
    
    return


testversion = map (int, string.split (sys.argv [1], '.'))
if len (testversion) < 3: testversion.append (0)

for pair in map (None, version, testversion):
    if pair [0] > pair [1]: break
    
    if pair [0] < pair [1]:
        error ('requested version for python is %s, but I detected %s' % (
            sys.argv [1], sys.version))
        
# check for gtk and gnome 2.0
err = None

try:
    import gi
	
    gi.require_version('Gtk', '3.0')
    
    #import gnome
    from gi.repository import Gtk
    #import Gtk.glade   #### -> GTK3 objects don't have a glade property. Gtk.Builder() does the work.
    #import gnome.ui
    from gi.repository import GConf

    v = string.join (map (str, (Gtk.get_major_version(), Gtk.get_minor_version(),Gtk.get_micro_version())), '.')

    fd = open ('conftest.out', 'a')
    fd.write ('Gtk_Version="%s"\n' % v)
    fd.close ()

    
except ImportError, msg:

    error ('error in python modules dependencies: %s' % msg)

except AssertionError, msg:

    error ('gtk problem: %s' % msg)

except RuntimeError, msg:

    if os.environ.get ('DISPLAY', '') != '':

        etype, value, tb = sys.exc_info ()
        traceback.print_exception (etype, value, tb)

        error ('unexpected runtime error')

    warning ('cannot test gtk [no DISPLAY]')

except:
    etype, value, tb = sys.exc_info ()
    traceback.print_exception (etype, value, tb)

    error ('unexpected error')

else:
    if (Gtk.get_major_version(), Gtk.get_minor_version(),Gtk.get_micro_version()) < (3,4,2):
        error ('requested version for Gtk is %s, but I detected %s' % ('3.4.2', v))


try:
    import _recode
    import _bibtex

    rq = _recode.request ('latin1..latex')

    l = 'abcd'
    c = _recode.recode (rq, l)

    if l != c:
        error ('broken recode version')

except ImportError, msg:

    error ('error in python modules dependencies: %s' % msg)

try:
    _bibtex.next_unfiltered

except AttributeError, msg:

    error ('Error in python-bibtex module: required function »next_unfiltered« missing: %s'
	   % msg)
    
except:
    etype, value, tb = sys.exc_info ()
    traceback.print_exception (etype, value, tb)

    error ('unexpected error')

    
