import hashlib
import base58
from bitcoinlib.transactions import Transaction

# Step 1: Generate redeem script in hex format
def generate_redeem_script(pre_image):
    pre_image_bytes = pre_image.encode('utf-8')
    sha256_hash = hashlib.sha256(pre_image_bytes).hexdigest()
    redeem_script = f"OP_SHA256 {sha256_hash} OP_EQUAL"
    return redeem_script, sha256_hash

# Step 2: Derive address from redeem script
def derive_address(redeem_script_hash):
    # Calculate hash160 (ripemd160(sha256(redeem_script_hash)))
    hash_sha256 = hashlib.sha256(bytes.fromhex(redeem_script_hash)).digest()
    hash_ripemd160 = hashlib.new('ripemd160', hash_sha256).digest()

    # Add version byte (0x00 for mainnet)
    version_byte = b'\x00'  # Mainnet
    hash_with_version = version_byte + hash_ripemd160

    # Calculate checksum (double sha256)
    checksum = hashlib.sha256(hashlib.sha256(hash_with_version).digest()).digest()[:4]

    # Encode with base58
    address = base58.b58encode(hash_with_version + checksum).decode('utf-8')
    return address

# Step 3: Construct transaction to send Bitcoins to the address
def construct_transaction(address, amount):
    tx = Transaction()
    tx.add_output(address, amount)
    return tx

# Main function
if __name__ == "__main__":
    pre_image = "Btrust Builders"
    redeem_script, redeem_script_hash = generate_redeem_script(pre_image)
    print("Redeem Script Hex:", redeem_script)

    derived_address = derive_address(redeem_script_hash)
    print("Derived Address:", derived_address)

    # Example transaction construction (amount in satoshis)
    tx = construct_transaction(derived_address, 100000)
    print("Constructed Transaction Hex:", tx.serialize())
