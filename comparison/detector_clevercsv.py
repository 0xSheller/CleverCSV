#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Wrapper for comparing with CleverCSV.

Author: Gertjan van den Burg

"""

import clevercsv
import sys

from utils import DetectionError, get_sample


def detector(gz_filename, encoding, n_lines=None):
    det = clevercsv.Detector()
    sample = get_sample(gz_filename, encoding, n_lines=n_lines)

    try:
        dialect = det.detect(sample)
    except clevercsv.Error:
        raise DetectionError

    if dialect is None:
        return None
    return dict(
        delimiter=dialect.delimiter,
        quotechar=dialect.quotechar,
        escapechar=dialect.escapechar,
    )

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        encoding = clevercsv.utils.get_encoding(filename)
        print(detector(filename, encoding))
    else:
        print(f"Usage: {sys.argv[0]} filename", file=sys.stderr)
