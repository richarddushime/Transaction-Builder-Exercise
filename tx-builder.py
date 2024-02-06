import hashlib
from bitcoin import *

def generate_redeem_script(preimage_hex):
    """Generates the redeem script in hex format for the given pre-image."""
    preimage_hash = hashlib.sha256(bytes.fromhex(preimage_hex)).digest()
    redeem_script = script_to_p2wsh_script(preimage_hash)  # Using P2WPKH-nested-in-P2WSH
    return redeem_script.hex()

def derive_address(redeem_script):
    """Derives a P2SH address from the given redeem script."""
    script_pubkey = p2sh_script(redeem_script)
    address = script_to_address(script_pubkey)
    return address

def create_transaction(address, amount, inputs=[]):
    """Creates a transaction that sends Bitcoins to the given address."""
    tx = Transaction()
    tx.add_inputs(inputs)  # Add any necessary inputs
    tx.add_output(address, amount)
    tx.finalize()
    return tx

def spend_transaction(prev_tx, prev_output_index, redeem_script, output_amount, change_address):
    """Constructs a transaction that spends from a previous transaction."""
    tx = Transaction()
    tx.add_input(prev_tx.hash, prev_output_index)
    tx.add_output(output_amount, address=output_address)
    if change_amount > 0:
        change_output = tx.add_output(change_amount, address=change_address)
        tx.sign(redeem_script, change_output)  # Sign using redeem script for change
    tx.finalize()
    return tx

# Example usage:
preimage_hex = '427472757374204275696c64657273'
redeem_script = generate_redeem_script(preimage_hex)
address = derive_address(redeem_script)
print("Redeem script:", redeem_script)
print("Address:", address)

# Create a transaction sending 0.1 BTC to the address
funding_tx = create_transaction(address, 100000000, inputs=[('prev_tx_hash', 0)])
print("Funding transaction:", funding_tx)

# Spend the transaction, sending 0.05 BTC to another address and the rest as change
spending_tx = spend_transaction(funding_tx, 0, redeem_script, 50000000, change_address)
print("Spending transaction:", spending_tx)
