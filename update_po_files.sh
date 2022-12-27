#!/usr/bin/env bash

find . -name *.po -exec xgettext --omit-header -j -f po/POTFILES -o {} \;
