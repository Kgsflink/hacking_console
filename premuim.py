import json
from datetime import datetime

def show_raw_bytes(hex_str):
    try:
        # Convert hex to bytes and then to a raw string of bytes
        byte_data = bytes.fromhex(hex_str)
        return ' '.join(f'{byte:02x}' for byte in byte_data)
    except Exception as e:
        return f"Error: {e}"

def decode_timestamp(timestamp):
    # Convert Unix timestamp to readable format
    try:
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        return f"Decoding timestamp failed: {e}"

def main():
    # JSON data input
    json_data = '''
    {"pageSize":10,"pageNo":1,"typeId":1,"language":0,"random":"0021cadbbc9545e78392e8c6858a1cbe","signature":"5E67F878ADB294342281C7EA86AD5C15","timestamp":1721643992}
    '''

    try:
        data = json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON data: {e}")
        return

    random_str = data.get('random', '')
    signature_str = data.get('signature', '')
    timestamp = data.get('timestamp', 0)
    
    raw_random = show_raw_bytes(random_str)
    raw_signature = show_raw_bytes(signature_str)
    decoded_timestamp = decode_timestamp(timestamp)
    
    print(f"Raw Random Bytes: {raw_random}")
    print(f"Raw Signature Bytes: {raw_signature}")
    print(f"Decoded Timestamp: {decoded_timestamp}")

if __name__ == "__main__":
    main()
