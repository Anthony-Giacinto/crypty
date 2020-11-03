import unittest
import os
import contextlib
import crypty.main as main


class TestEncrypt(unittest.TestCase):

    def test_encrypt_binary(self):
        message = main.encrypt('SOS', main.binary_dict)
        message_check = '01010011 01001111 01010011 '
        self.assertEqual(message, message_check)

    def test_encrypt_morse(self):
        message = main.encrypt('SOS', main.morse_code_dict)
        message_check = '... --- ... '
        self.assertEqual(message, message_check)


class TestDecrypt(unittest.TestCase):

    def test_decrypt_binary(self):
        message = main.decrypt('01010011 01001111 01010011', main.binary_dict)
        message_check = 'SOS'
        self.assertEqual(message, message_check)

    def test_decrypt_morse(self):
        message = main.decrypt('... --- ...', main.morse_code_dict)
        message_check = 'SOS'
        self.assertEqual(message, message_check)


class TestMorbin(unittest.TestCase):

    def test_morbin_encrypt_binary(self):
        message_input = 'SOS'
        message = main.morbin(switch=False, message_test=message_input)
        message_check = main.encrypt(message_input, main.binary_dict)
        self.assertEqual(message, message_check)

    def test_morbin_encrypt_morse(self):
        message_input = 'SOS'
        message = main.morbin(switch=True, message_test=message_input)
        message_check = main.encrypt(message_input, main.morse_code_dict)
        self.assertEqual(message, message_check)

    def test_morbin_decrypt_binary(self):
        message_input = '01010011 01001111 01010011'
        message = main.morbin(switch=False, message_test=message_input)
        message_check = main.decrypt(message_input, main.binary_dict)
        self.assertEqual(message, message_check)

    def test_morbin_decrypt_morse(self):
        message_input = '... --- ...'
        message = main.morbin(switch=True, message_test=message_input)
        message_check = main.decrypt(message_input, main.morse_code_dict)
        self.assertEqual(message, message_check)

    def test_morbin_invalid_message(self):
        message_input = '|||'
        with open(os.devnull, 'w') as f, contextlib.redirect_stdout(f):
            message = main.morbin(switch=True, message_test=message_input)
        message_check = main.end_message
        self.assertEqual(message, message_check)


class TestMorse(unittest.TestCase):

    def test_morse_encryption(self):
        message_input = 'SOS'
        message = main.encrypt(message_input, main.morse_code_dict)
        message_check = main.morbin(switch=True, message_test=message_input)
        self.assertEqual(message, message_check)

    def test_morse_decryption(self):
        message_input = '... --- ...'
        message = main.decrypt(message_input, main.morse_code_dict)
        message_check = main.morbin(switch=True, message_test=message_input)
        self.assertEqual(message, message_check)


class TestBinary(unittest.TestCase):

    def test_binary_encryption(self):
        message_input = 'SOS'
        message = main.encrypt(message_input, main.binary_dict)
        message_check = main.morbin(switch=False, message_test=message_input)
        self.assertEqual(message, message_check)

    def test_binary_decryption(self):
        message_input = '01010011 01001111 01010011'
        message = main.decrypt(message_input, main.binary_dict)
        message_check = main.morbin(switch=False, message_test=message_input)
        self.assertEqual(message, message_check)


if __name__ == '__main__':
    unittest.main()
