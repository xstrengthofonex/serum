import unittest
import sys
from serum import Environment, load_ipython_extension, unload_ipython_extension
from serum.exceptions import NoEnvironment


class MockIpythonEnvironment:
    environment = Environment()


class IPythonExtensionTests(unittest.TestCase):

    def test_load_extension_no_ipython_environment(self):
        self.assertEqual(load_ipython_extension(None), None)

    def test_load_extension(self):
        sys.modules['ipython_environment'] = MockIpythonEnvironment
        load_ipython_extension(None)
        self.assertEqual(
            MockIpythonEnvironment.environment,
            Environment.current_env()
        )
        unload_ipython_extension(None)
        with self.assertRaises(NoEnvironment):
            Environment.current_env()
        sys.modules['ipython_environment'] = None

    def test_unload_extension_no_ipython_environment(self):
        self.assertEqual(unload_ipython_extension(None), None)