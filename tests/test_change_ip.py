# 📂 tests/test_change_ip.py - Pruebas para cambio de IP
import unittest
from src.change_ip import change_ip

class TestChangeIP(unittest.TestCase):
    def test_change_ip(self):
        try:
            change_ip("192.168.1.101", "255.255.255.0", "192.168.1.1")
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()