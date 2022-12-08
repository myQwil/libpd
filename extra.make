PD_EXTRA_FILES += $(patsubst %, ../pd-quilt/src/%.c, \
0x40paq 0x40unpaq blunt chrd chrono delp fldec flenc fton has is linp linp~ \
metro~ muse ntof paq radix rand rind same slx sly tabosc2~ tabread2~ unpaq all/quilt)

PD_EXTRA_FILES += $(patsubst %, ../pd-cyclone/cyclone_objects/binaries/audio/%.c, \
curve lessthan greaterthan)

CFLAGS += -I../pd-cyclone/shared
