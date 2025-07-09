import unittest

SERVER = "server_b"  # Example server variable, can be changed for testing

class AllAssertsTestCase(unittest.TestCase):
    
    def test_assert(self):
        self.assertEqual(1, 1, "This should always pass")
        self.assertEqual("hello", "hello", "Strings should match")

    def test_assert_true_or_false(self):
        self.assertTrue(True, "This should always pass")
        self.assertFalse(False, "This should always pass")

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("not a number")

    def test_assert_in(self):
        self.assertIn(1, [1, 2, 3], "1 should be in the list")
        self.assertNotIn(4, [1, 2, 3], "4 should not be in the list")

    def test_assert_ditch(self):
        self.assertDictEqual({'a': 1}, {'a': 1}, "Dictionaries should match")
        #self.assertDictEqual({'a': 1}, {'b': 2}, "Dictionaries should not match")

    @unittest.skip("Skipping this test intentionally")
    def test_skip(self):
        self.assertEqual("Hola", "Chao", "This will fail but is skipped")

    @unittest.skipIf(SERVER == "server_b", "Skipping this test because condition is server_b")
    def test_skip_if(self):
        self.assertEqual(100, 100, "This will ok but is skipped if SERVER is server_b")

    @unittest.expectedFailure
    def test_expected_failure(self):
       self.assertEqual(100, 150, "This will fail but is expected to fail")

