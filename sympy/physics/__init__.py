"""
A module that helps solving problems in physics.
"""
from __future__ import annotations

from sympy.core._lazy_imports import lazy_prefixes
__lazy_modules__ = lazy_prefixes('sympy.physics')

from . import units
from .matrices import mgamma, msigma, minkowski_tensor, mdft

__all__ = [
    'units',

    'mgamma', 'msigma', 'minkowski_tensor', 'mdft',
]
