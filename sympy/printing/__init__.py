"""Printing subsystem"""

from sympy.core.cache import lazy_function

from .pretty import pager_print, pretty, pretty_print, pprint, pprint_use_unicode, pprint_try_use_unicode


latex, print_latex, multiline_latex = lazy_function('sympy.printing.latex', ['latex', 'print_latex', 'multiline_latex'])


mathml = lazy_function('sympy.printing.mathml', 'mathml')
print_mathml = lazy_function('sympy.printing.mathml', 'print_mathml')
print_python = lazy_function('sympy.printing.python', 'print_python')
python = lazy_function('sympy.printing.python', 'python')
pycode = lazy_function('sympy.printing.pycode', 'pycode')


print_ccode, print_fcode= lazy_function('sympy.printing.codeprinter', ['print_ccode', 'print_fcode'])

ccode, fcode, cxxcode = lazy_function('sympy.printing.codeprinter', ['ccode', 'fcode', 'cxxcode'])


glsl_code = lazy_function('sympy.printing.glsl', 'glsl_code')
print_glsl = lazy_function('sympy.printing.glsl', 'print_glsl')

rcode = lazy_function('sympy.printing.rcode', 'rcode')
print_rcode = lazy_function('sympy.printing.rcode', 'print_rcode')
jscode = lazy_function('sympy.printing.jscode', 'jscode')
print_jscode = lazy_function('sympy.printing.jscode', 'print_jscode')


julia_code = lazy_function('sympy.printing.julia', 'julia_code')
mathematica_code = lazy_function('sympy.printing.mathematica', 'mathematica_code')
octave_code = lazy_function('sympy.printing.octave', 'octave_code')
rust_code = lazy_function('sympy.printing.rust', 'rust_code')
print_gtk = lazy_function('sympy.printing.gtk', 'print_gtk')
preview = lazy_function('sympy.printing.preview', 'preview')
srepr = lazy_function('sympy.printing.repr', 'srepr')
print_tree = lazy_function('sympy.printing.tree', 'print_tree')

dotprint = lazy_function('sympy.printing.dot', 'dotprint')
maple_code = lazy_function('sympy.printing.maple', 'maple_code')
print_maple_code = lazy_function('sympy.printing.maple', 'print_maple_code')

from .str import StrPrinter, sstr, sstrrepr

from .tableform import TableForm


__all__ = [
    # sympy.printing.pretty
    'pager_print', 'pretty', 'pretty_print', 'pprint', 'pprint_use_unicode',
    'pprint_try_use_unicode',

    # sympy.printing.latex
    'latex', 'print_latex', 'multiline_latex',

    # sympy.printing.mathml
    'mathml', 'print_mathml',

    # sympy.printing.python
    'python', 'print_python',

    # sympy.printing.pycode
    'pycode',

    # sympy.printing.codeprinter
    'ccode', 'print_ccode', 'cxxcode', 'fcode', 'print_fcode',

    # sympy.printing.glsl
    'glsl_code', 'print_glsl',

    # sympy.printing.rcode
    'rcode', 'print_rcode',

    # sympy.printing.jscode
    'jscode', 'print_jscode',

    # sympy.printing.julia
    'julia_code',

    # sympy.printing.mathematica
    'mathematica_code',

    # sympy.printing.octave
    'octave_code',

    # sympy.printing.rust
    'rust_code',

    # sympy.printing.gtk
    'print_gtk',

    # sympy.printing.preview
    'preview',

    # sympy.printing.repr
    'srepr',

    # sympy.printing.tree
    'print_tree',

    # sympy.printing.str
    'StrPrinter', 'sstr', 'sstrrepr',

    # sympy.printing.tableform
    'TableForm',

    # sympy.printing.dot
    'dotprint',

    # sympy.printing.maple
    'maple_code', 'print_maple_code',
]
