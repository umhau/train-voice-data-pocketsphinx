#!/bin/bash
# Auto-train on new voice data.  This is a hardcoded script.  Run chmod 755 my_script to set permissions to execute.

# presumes a standard installation and set-up. see nixingaround.blogspot.com for instructions.

pocketsphinx_batch  -adcin yes  -cepdir ./test-data  -cepext .wav  -ctl ./test-data/test-data.fileids  -lm en-us.lm.bin  -dict cmudict-en-us.dict  -hmm en-us-adapt  -hyp ./test-data/test-data.hyp

../../pocketsphinx-5prealpha/test/word_align.pl ./test-data/test-data.transcription ./test-data/test-data.hyp



