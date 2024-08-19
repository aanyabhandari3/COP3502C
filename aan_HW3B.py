def to_hex_string(data):
    res = ''.join('{:x}'.format(x) for x in data)
    return res

def count_runs(flat_data):
    counter = 0
    runs = encode_rle(flat_data)
    for i in range (0, len(runs), 2):
        count = int(runs[i])
        if count >= 15:
            counter += 1
    total = counter + i
    return total

def encode_rle(flat_data):
    compressed = []
    count = 1
    for i in range (1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1]:
            count+= 1
        else:
            if count >= 15:
                compressed.append(count)
                compressed.append(flat_data[i - 1])
                count = 1
            compressed.append(count)
            compressed.append(flat_data[i - 1])
            count = 1

    compressed.append(count)
    compressed.append(flat_data[-1])

    return compressed

def get_decoded_length(rle_data):
    count = 0
    for i in range (0, len(rle_data), 2):
        count += int(rle_data[i])
    
    return count

def decode_rle(rle_data):
    decompressed = []

    for i in range (0, len(rle_data), 2):
        count = rle_data[i]
        ch = rle_data[i +1]
        for j in range (0, count):
            decompressed.append(ch)
    return decompressed

def string_to_data(data_string):
    hex = ""
    for i in range(0, len(data_string), 2):
        hex += chr(int(data_string[i:i+2], 16))
    return hex