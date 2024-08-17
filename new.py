import hashlib

def get_result(hash_value, client_seed):
    # Combine the hash and the client seed
    combined = f"{hash_value}{client_seed}"
    
    # Hash the combined string using SHA-256
    result_hash = hashlib.sha256(combined.encode()).hexdigest()
    
    # Convert the hash to a number (you can decide how many bits or bytes you need)
    # For example, we'll take the first 8 characters and convert to an integer
    result_number = int(result_hash[:8], 16)

    return result_number

hash_value = 'ecd7c90d67f0dea8a2d1eb1ac2690fd3e0a1533c36e92b32abff5b73c485e6eb'
client_seed = 'R8mZWCPE7KtEWCTJhAbA-0'

result = get_result(hash_value, client_seed)
print('Result:', result)
