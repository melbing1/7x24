#!/bin/bash

#Usage ./merge.sh [desired name of consolidated file]

shopt -s extglob
cat !(combined|merge.sh) > combined