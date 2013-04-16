#! /bin/bash
amixer set PCM 100%
pd-extended -nogui -nomidi -noadc sk_poke.pd
