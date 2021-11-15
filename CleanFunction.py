#-------------------------------------------------------------------------------
# Name:        Clean function
# Purpose:
#
# Author:      Kawfi
#
# Created:     15/11/2021
# Copyright:   (c) Kawfi 2021
# Licence:     <Mihoyo>
#-------------------------------------------------------------------------------

def clean(x):
    return str(" ".join(x.split()).translate(str.maketrans('','',string.punctuation))).lower()

