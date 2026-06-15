"""Helper for PEP 810 lazy imports.

PEP 810 tests ``name in __lazy_modules__``, so ``__lazy_modules__`` may be any
object implementing ``__contains__``. ``lazy_prefixes`` returns one that defers
every import whose module name starts with a given prefix -- letting a module
lazify all imports from heavy sibling subpackages in one declaration.
"""


class _PrefixLazyModules:
    __slots__ = ('_prefixes', '_exclude')

    def __init__(self, prefixes, exclude=()):
        self._prefixes = tuple(prefixes)
        self._exclude = frozenset(exclude)

    def __contains__(self, name):
        return name.startswith(self._prefixes) and name not in self._exclude

    def __repr__(self):
        return 'lazy_prefixes%r' % (self._prefixes,)


def lazy_prefixes(*prefixes, exclude=()):
    """Return a ``__lazy_modules__`` value matching the given name prefixes.

    ``exclude`` lists fully qualified names to keep eager -- e.g. a submodule
    whose name collides with a function of the same name exported alongside it.
    """
    return _PrefixLazyModules(prefixes, exclude)
