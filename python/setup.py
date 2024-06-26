#! /usr/bin/python3

import sys
from distutils.core import setup, Extension

pd_defines = [
  ('PD', 1),
  ('USEAPI_DUMMY', 1),
  ('PD_INTERNAL', 1),
  ('HAVE_UNISTD_H', 1),
  ('LIBPD_EXTRA', 1)
]
pd_libraries = [
  'm',
  'pthread'
]

# replicate libpd/Makefile PLATFORM_CFLAGS & LDFLAGS
if sys.platform.startswith('darwin'):
  pd_defines.append(('HAVE_ALLOCA_H', 1))
  pd_defines.append(('HAVE_MACHINE_ENDIAN_H', 1))
  pd_defines.append(('_DARWIN_C_SOURCE', 1))
  pd_defines.append(('_DARWIN_UNLIMITED_SELECT', 1))
  pd_defines.append(('FD_SETSIZE', 10240))
  pd_defines.append(('HAVE_LIBDL', 1))
  pd_libraries.append('dl')
elif sys.platform.startswith('win32') or sys.platform.startswith('msys'):
  # windows doesn't have alloca.h, endian.h, or libdl
  pd_libraries.append('ws2_32') # winsock
else: # assume posix env...
  pd_defines.append(('HAVE_ENDIAN_H', 1))
  if sys.platform.startswith('linux'):
    pd_defines.append(('HAVE_ALLOCA_H', 1))
    pd_defines.append(('HAVE_LIBDL', 1))
    pd_libraries.append('dl')

setup(name='pypdlib',
      version='0.14.0',
      py_modules = [
        'pylibpd'
      ],
      ext_modules = [
        Extension('_pylibpd',
                  define_macros = pd_defines,
                  include_dirs = [
                    '../libpd_wrapper',
                    '../pure-data/src',
                    '../../pd-cyclone/shared'
                  ],
                  libraries = pd_libraries,
                  sources = [
                    'pylibpd.i',
                    '../libpd_wrapper/s_libpdmidi.c',
                    '../libpd_wrapper/x_libpdreceive.c',
                    '../libpd_wrapper/z_hooks.c',
                    '../libpd_wrapper/z_libpd.c',
                    '../pure-data/src/d_arithmetic.c',
                    '../pure-data/src/d_array.c',
                    '../pure-data/src/d_ctl.c',
                    '../pure-data/src/d_dac.c',
                    '../pure-data/src/d_delay.c',
                    '../pure-data/src/d_fft.c',
                    '../pure-data/src/d_fft_fftsg.c',
                    '../pure-data/src/d_filter.c',
                    '../pure-data/src/d_global.c',
                    '../pure-data/src/d_math.c',
                    '../pure-data/src/d_misc.c',
                    '../pure-data/src/d_osc.c',
                    '../pure-data/src/d_resample.c',
                    '../pure-data/src/d_soundfile.c',
                    '../pure-data/src/d_soundfile_aiff.c',
                    '../pure-data/src/d_soundfile_caf.c',
                    '../pure-data/src/d_soundfile_next.c',
                    '../pure-data/src/d_soundfile_wave.c',
                    '../pure-data/src/d_ugen.c',
                    '../pure-data/src/g_all_guis.c',
                    '../pure-data/src/g_array.c',
                    '../pure-data/src/g_bang.c',
                    '../pure-data/src/g_canvas.c',
                    '../pure-data/src/g_clone.c',
                    '../pure-data/src/g_editor.c',
                    '../pure-data/src/g_editor_extras.c',
                    '../pure-data/src/g_graph.c',
                    '../pure-data/src/g_guiconnect.c',
                    '../pure-data/src/g_io.c',
                    '../pure-data/src/g_mycanvas.c',
                    '../pure-data/src/g_numbox.c',
                    '../pure-data/src/g_radio.c',
                    '../pure-data/src/g_readwrite.c',
                    '../pure-data/src/g_rtext.c',
                    '../pure-data/src/g_scalar.c',
                    '../pure-data/src/g_slider.c',
                    '../pure-data/src/g_template.c',
                    '../pure-data/src/g_text.c',
                    '../pure-data/src/g_toggle.c',
                    '../pure-data/src/g_traversal.c',
                    '../pure-data/src/g_undo.c',
                    '../pure-data/src/g_vumeter.c',
                    '../pure-data/src/m_atom.c',
                    '../pure-data/src/m_binbuf.c',
                    '../pure-data/src/m_class.c',
                    '../pure-data/src/m_conf.c',
                    '../pure-data/src/m_glob.c',
                    '../pure-data/src/m_memory.c',
                    '../pure-data/src/m_obj.c',
                    '../pure-data/src/m_pd.c',
                    '../pure-data/src/m_sched.c',
                    '../pure-data/src/s_audio.c',
                    '../pure-data/src/s_audio_dummy.c',
                    '../pure-data/src/s_inter.c',
                    '../pure-data/src/s_inter_gui.c',
                    '../pure-data/src/s_loader.c',
                    '../pure-data/src/s_main.c',
                    '../pure-data/src/s_net.c',
                    '../pure-data/src/s_path.c',
                    '../pure-data/src/s_print.c',
                    '../pure-data/src/s_utf8.c',
                    '../pure-data/src/x_acoustics.c',
                    '../pure-data/src/x_array.c',
                    '../pure-data/src/x_arithmetic.c',
                    '../pure-data/src/x_connective.c',
                    '../pure-data/src/x_file.c',
                    '../pure-data/src/x_gui.c',
                    '../pure-data/src/x_interface.c',
                    '../pure-data/src/x_list.c',
                    '../pure-data/src/x_midi.c',
                    '../pure-data/src/x_misc.c',
                    '../pure-data/src/x_net.c',
                    '../pure-data/src/x_scalar.c',
                    '../pure-data/src/x_text.c',
                    '../pure-data/src/x_time.c',
                    '../pure-data/src/x_vexp.c',
                    '../pure-data/src/x_vexp_if.c',
                    '../pure-data/src/x_vexp_fun.c',
                    '../pure-data/extra/bob~/bob~.c',
                    '../pure-data/extra/bonk~/bonk~.c', \
                    '../pure-data/extra/choice/choice.c', \
                    '../pure-data/extra/fiddle~/fiddle~.c', \
                    '../pure-data/extra/loop~/loop~.c', \
                    '../pure-data/extra/lrshift~/lrshift~.c', \
                    '../pure-data/extra/pd~/pdsched.c', \
                    '../pure-data/extra/pd~/pd~.c', \
                    '../pure-data/extra/pique/pique.c', \
                    '../pure-data/extra/sigmund~/sigmund~.c', \
                    '../pure-data/extra/stdout/stdout.c', \
                    '../../pd-quilt/src/0x40paq.c', \
                    '../../pd-quilt/src/0x40unpaq.c', \
                    '../../pd-quilt/src/blunt.c', \
                    '../../pd-quilt/src/chrd.c', \
                    '../../pd-quilt/src/chrono.c', \
                    '../../pd-quilt/src/delp.c', \
                    '../../pd-quilt/src/fldec.c', \
                    '../../pd-quilt/src/flenc.c', \
                    '../../pd-quilt/src/fton.c', \
                    '../../pd-quilt/src/has.c', \
                    '../../pd-quilt/src/is.c', \
                    '../../pd-quilt/src/linp.c', \
                    '../../pd-quilt/src/linp~.c', \
                    '../../pd-quilt/src/metro~.c', \
                    '../../pd-quilt/src/muse.c', \
                    '../../pd-quilt/src/ntof.c', \
                    '../../pd-quilt/src/paq.c', \
                    '../../pd-quilt/src/radix.c', \
                    '../../pd-quilt/src/rand.c', \
                    '../../pd-quilt/src/rind.c', \
                    '../../pd-quilt/src/same.c', \
                    '../../pd-quilt/src/slx.c', \
                    '../../pd-quilt/src/sly.c', \
                    '../../pd-quilt/src/tabosc2~.c', \
                    '../../pd-quilt/src/tabread2~.c', \
                    '../../pd-quilt/src/unpaq.c', \
                    '../../pd-quilt/src/all/quilt.c', \
                    '../../pd-cyclone/cyclone_objects/binaries/audio/curve.c', \
                    '../../pd-cyclone/cyclone_objects/binaries/audio/lessthan.c', \
                    '../../pd-cyclone/cyclone_objects/binaries/audio/greaterthan.c'
                  ]
        )
      ]
)

