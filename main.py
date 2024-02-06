import hashlib
from bitcoinlib.wallets import wallet_create_or_open
from bitcoinlib.transactions import Transaction, Output


def generate_redeem_script(pre_image):
    # Step 1: Convert pre-image to bytes
    pre_image_bytes = pre_image.encode('utf-8')

    # Step 2: Perform SHA256 hash
    sha256_hash = hashlib.sha256(pre_image_bytes).hexdigest()

    # Step 3: Combine the hash in the redeem script format
    redeem_script = f"OP_SHA256 {sha256_hash} OP_EQUAL"

    return redeem_script

def derive_address(redeem_script):
    # Create a wallet on the desired network (e.g., testnet in this example)
    wallet = wallet_create_or_open('testnet')  # Adjust for mainnet if needed

    # Create a P2SH output using the redeem script
    output = Output(redeem_script, amount=0.0)

    # Add the output to a dummy transaction to get the address
    tx = Transaction()
    tx.add_output(output)

    # Get the address from the transaction
    address = tx.get_address()

    return address

if __name__ == "__main__":
    pre_image = "Btrust Builders"
    redeem_script_hex = generate_redeem_script(pre_image)
    print("Redeem Script Hex:", redeem_script_hex)
#  Deriving address
    redeem_script = redeem_script_hex
    
    address = derive_address(redeem_script)
    print("Derived Address:", address)

