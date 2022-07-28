#!/usr/bin/env python
"""
Test that the lazy_function is indeed lazy. The test is done in this script
to avoid failure of the test when executed twice in the same script.
"""
import sys
from sympy.core.cache import lazy_function

def test_lazy_function():
    module_name='xmlrpc.client'
    function_name = 'gzip_decode'
    lazy = lazy_function(module_name, function_name)
    assert module_name not in sys.modules
    assert lazy(b'') == b''
    assert module_name in sys.modules


if __name__ == '__main__':
    test_lazy_function()
