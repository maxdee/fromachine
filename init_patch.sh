#! /bin/bash
pd-extended -nogui -nomidi -noadc pokeor.pd &
amixer set PCM 100%
