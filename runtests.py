#!/usr/bin/env python

import unittest
tests = unittest.defaultTestLoader.discover('corneal')
runner = unittest.runner.TextTestRunner()
runner.run(tests)
