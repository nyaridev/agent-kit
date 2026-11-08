import os
import tempfile
import unittest

import todo


class TodoTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        os.chdir(self.dir)
        todo.DB = todo.Path(self.dir) / "todos.json"

    def test_add_and_done(self):
        self.assertEqual(todo.add("milk"), 1)
        todo.done(1)
        self.assertTrue(todo.load()[0]["done"])


if __name__ == "__main__":
    unittest.main()
