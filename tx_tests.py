import unittest
from main import *

class TestTransactionBuilder(unittest.TestCase):
    def test_generate_redeem_script(self):
        lock_hex = "74657374"  # "test" in hexadecimal
        expected_redeem_script = "a87465737487"  # Corresponding redeem script for OP_SHA256 test OP_EQUAL
        self.assertEqual(generate_redeem_script(lock_hex), expected_redeem_script)

    def test_derive_address(self):
        redeem_script_hex = "a8427472757374204275696c6465727387"  # Based on provided output
        expected_address = "38FwbzpG5tSqvvDuicyXj1GZ4NBfSjdpDP"
        self.assertEqual(derive_address(redeem_script_hex), expected_address)

    def test_construct_transaction(self):
        output_address = "38FwbzpG5tSqvvDuicyXj1GZ4NBfSjdpDP"  # Based on provided output
        value = 100000
        expected_transaction_data = "1dummy_txid0110000038FwbzpG5tSqvvDuicyXj1GZ4NBfSjdpDP"
        self.assertEqual(construct_transaction(output_address, value), expected_transaction_data)

    def test_construct_spending_transaction(self):
        previous_txid = "previous_txid"
        previous_vout = 0
        unlocking_script_hex = "4752210222b23b"  # Based on provided output
        output_address = "38FwbzpG5tSqvvDuicyXj1GZ4NBfSjdpDP"  # Based on provided output
        value = 50000
        expected_spending_transaction_data = "1previous_txid04752210222b23b15000038FwbzpG5tSqvvDuicyXj1GZ4NBfSjdpDP"  # Based on provided output
        self.assertEqual(construct_spending_transaction(previous_txid, previous_vout, unlocking_script_hex, output_address, value), expected_spending_transaction_data)

if __name__ == '__main__':
    unittest.main()
