import unittest
from main import *

class TestTransactionBuilder(unittest.TestCase):
    def test_generate_redeem_script(self):
        lock_hex = "427472757374204275696c64657273"  # "test" in hexadecimal
        expected_redeem_script = "a8427472757374204275696c6465727387"  # Corresponding redeem script for OP_SHA256 test OP_EQUAL
        self.assertEqual(generate_redeem_script(lock_hex), expected_redeem_script)

    def test_derive_address(self):
        redeem_script_hex = "a8427472757374204275696c6465727387"  # Based on provided output
        expected_address = "38FwbzpG5tSqvvDuicyXj1GZ4NBfSjdpDP"
        self.assertEqual(derive_address(redeem_script_hex), expected_address)

    def test_construct_transaction(self):
        output_address = "38FwbzpG5tSqvvDuicyXj1GZ4NBfSjdpDP"  # Based on provided output
        value = 100000
        expected_transaction_data = "1535dfa3634abac4ed004803331f23144dddf5e237539534e524c9f2d9afa44840110000038FwbzpG5tSqvvDuicyXj1GZ4NBfSjdpDP"
        self.assertEqual(construct_transaction(output_address, value), expected_transaction_data)

    def test_construct_spending_transaction(self):
        previous_txid = "535dfa3634abac4ed004803331f23144dddf5e237539534e524c9f2d9afa4484"
        previous_vout = 0
        unlocking_script_hex = "00140293308b68f473a15885ab1776674a3a70c77110"  # Based on provided output
        output_address = "38FwbzpG5tSqvvDuicyXj1GZ4NBfSjdpDP"  # Based on provided output
        value = 50000
        expected_spending_transaction_data = "1535dfa3634abac4ed004803331f23144dddf5e237539534e524c9f2d9afa4484011000140293308b68f473a15885ab1776674a3a70c7711015000038FwbzpG5tSqvvDuicyXj1GZ4NBfSjdpDP"  # Based on provided output
        self.assertEqual(construct_spending_transaction(previous_txid, previous_vout, unlocking_script_hex, output_address, value), expected_spending_transaction_data)

if __name__ == '__main__':
    unittest.main()
