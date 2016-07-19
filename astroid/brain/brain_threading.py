# Copyright (c) 2016 LOGILAB S.A. (Paris, FRANCE)
# http://www.logilab.fr/ -- mailto:contact@logilab.fr
# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/master/COPYING.LESSER

import astroid


def _thread_transform():
    return astroid.parse('''
    class lock(object):
        def acquire(self, blocking=True):
            pass
        def release(self):
            pass

    def Lock():
        return lock()
    ''')


astroid.register_module_extender(astroid.MANAGER, 'threading', _thread_transform)
