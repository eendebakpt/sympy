"""A module that handles matrices.

Includes functions for fast creating matrices like zero, one/eye, random
matrix, etc.
"""
from __future__ import annotations

from sympy.core._lazy_imports import lazy_prefixes
__lazy_modules__ = lazy_prefixes('sympy.matrices')

from .exceptions import ShapeError, NonSquareMatrixError
from .kind import MatrixKind
from .dense import (
    GramSchmidt, casoratian, diag, eye, hessian, jordan_cell,
    list2numpy, matrix2numpy, matrix_multiply_elementwise, ones,
    randMatrix, rot_axis1, rot_axis2, rot_axis3, rot_ccw_axis1,
    rot_ccw_axis2, rot_ccw_axis3, rot_givens,
    symarray, wronskian, zeros)
from .dense import MutableDenseMatrix
from .dense import MutableDenseMatrix as MutableMatrix
from .dense import MutableDenseMatrix as Matrix
from .matrixbase import DeferredVector, MatrixBase

from .sparse import MutableSparseMatrix
from .sparse import MutableSparseMatrix as SparseMatrix
from .sparsetools import banded
from .immutable import ImmutableDenseMatrix, ImmutableSparseMatrix
from .immutable import ImmutableDenseMatrix as ImmutableMatrix

from .expressions import (
    MatrixSlice, BlockDiagMatrix, BlockMatrix, FunctionMatrix, Identity,
    Inverse, MatAdd, MatMul, MatPow, MatrixExpr, MatrixSymbol, Trace,
    Transpose, ZeroMatrix, OneMatrix, blockcut, block_collapse, matrix_symbols, Adjoint,
    hadamard_product, HadamardProduct, HadamardPower, Determinant, det,
    diagonalize_vector, DiagMatrix, DiagonalMatrix, DiagonalOf, trace,
    DotProduct, kronecker_product, KroneckerProduct,
    PermutationMatrix, MatrixPermute, MatrixSet, Permanent, per)

from .utilities import dotprodsimp

__all__ = [
    'ShapeError', 'NonSquareMatrixError', 'MatrixKind',

    'GramSchmidt', 'casoratian', 'diag', 'eye', 'hessian', 'jordan_cell',
    'list2numpy', 'matrix2numpy', 'matrix_multiply_elementwise', 'ones',
    'randMatrix', 'rot_axis1', 'rot_axis2', 'rot_axis3', 'symarray',
    'wronskian', 'zeros', 'rot_ccw_axis1', 'rot_ccw_axis2', 'rot_ccw_axis3',
    'rot_givens',

    'MutableDenseMatrix',

    'DeferredVector', 'MatrixBase',

    'Matrix', 'MutableMatrix',

    'MutableSparseMatrix',

    'banded',

    'ImmutableDenseMatrix', 'ImmutableSparseMatrix',

    'ImmutableMatrix', 'SparseMatrix',

    'MatrixSlice', 'BlockDiagMatrix', 'BlockMatrix', 'FunctionMatrix',
    'Identity', 'Inverse', 'MatAdd', 'MatMul', 'MatPow', 'MatrixExpr',
    'MatrixSymbol', 'Trace', 'Transpose', 'ZeroMatrix', 'OneMatrix',
    'blockcut', 'block_collapse', 'matrix_symbols', 'Adjoint',
    'hadamard_product', 'HadamardProduct', 'HadamardPower', 'Determinant',
    'det', 'diagonalize_vector', 'DiagMatrix', 'DiagonalMatrix',
    'DiagonalOf', 'trace', 'DotProduct', 'kronecker_product',
    'KroneckerProduct', 'PermutationMatrix', 'MatrixPermute', 'MatrixSet',
    'Permanent', 'per',

    'dotprodsimp',
]
