import hashlib
import ecdsa
import base58
from Crypto.Hash import RIPEMD160

# Function to generate redeem script in hex format
def generate_redeem_script(lock_hex):
    redeem_script = bytes.fromhex("a8" + lock_hex + "87").hex()  # a8 = OP_SHA256, 87 = OP_EQUAL
    return redeem_script

# Function to derive address from redeem script
def derive_address(redeem_script_hex):
    # Hash160 of redeem script
    redeem_script_bytes = bytes.fromhex(redeem_script_hex)
    hash160 = RIPEMD160.new(hashlib.sha256(redeem_script_bytes).digest()).digest()

    # Add version byte (0x05 for mainnet)
    hash160 = b"\x05" + hash160

    # Calculate checksum
    checksum = hashlib.sha256(hashlib.sha256(hash160).digest()).digest()[:4]

    # Append checksum
    hash160 += checksum

    # Encode in base58
    address = base58.b58encode(hash160)

    return address.decode('utf-8')

# Function to construct a transaction
def construct_transaction(output_address, value):
    # Construct transaction
    tx = Transaction()

    # Add input - Dummy data for demonstration
    tx.add_input('dummy_txid', 0)

    # Add output
    tx.add_output(value, output_address)

    return tx.serialize()

class Transaction:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def add_input(self, txid, vout):
        self.inputs.append({'txid': txid, 'vout': vout})

    def add_output(self, value, address):
        self.outputs.append({'value': value, 'address': address})

    def serialize(self):
        # Serialized transaction data construction
        serialized = ""
        # Add inputs
        serialized += str(len(self.inputs))
        for input in self.inputs:
            serialized += input['txid'] + str(input['vout'])

        # Add outputs
        serialized += str(len(self.outputs))
        for output in self.outputs:
            serialized += str(output['value']) + output['address']

        return serialized

# Given pre-image
pre_image = "Btrust Builders"

# Generate redeem script
redeem_script_hex = generate_redeem_script(pre_image.encode().hex())

# Derive address from redeem script
address = derive_address(redeem_script_hex)

# Construct transaction to send Bitcoins to the address
transaction_data = construct_transaction(address, 100000)  # Sending 0.001 BTC (in satoshis)
# Print Results Redirection to Results.txt By using 
# python3 main.py > Results.txt
print("Redeem Script (hex):", redeem_script_hex)
print("Derived Address:", address)
print("Constructed Transaction Data:", transaction_data)
