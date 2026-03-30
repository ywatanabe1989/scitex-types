#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Timestamp: "2025-05-02 17:09:16 (ywatanabe)"
# File: src/scitex_types/_ColorLike.py

from typing import List, Tuple, Union

# Define ColorLike type
ColorLike = Union[
    str,
    Tuple[float, float, float],
    Tuple[float, float, float, float],
    List[float],
]

# EOF
