
def huffman_encode(words, huffman_coding_map):
    result = ""
    for c in words:
        result = result + huffman_coding_map[c]   
    return result


def huffman_decode(words, huffman_coding_map):
    # reverse the huffman_coding_map make key as value and value as key.
    # After that replace each code with value and return string
    decodedstr=""
    t=huffman_coding_map.popitem()
    huffman_coding_map.setdefault(t[0],t[1])
    code_to_char={v: k for k ,v in huffman_coding_map.items()}
    for i in range(0,len(words),len(t[1])):
        temp=words[i:i+len(t[1])]
        decodedstr=decodedstr+code_to_char[temp]
    return decodedstr

def frequencycount(words):
    s=list(words)
    d={}
    for x in s:
        f=s.count(x)
        d[x]=f

    frequency=sorted(d.items(),key=lambda t:t[1])
    outputString=""
    for i in frequency:
        outputString=outputString+i[0]

    str1=outputString[::-1]
    return str1

def build_huffman_code(words):
    # do this based on frequency
    char_to_code = dict()
    arr1=[str(bin(i)) for i in range(0,len(words))]
    t=len(arr1[len(words)-1])-2
    arr=[i[2:].zfill(t) for i in arr1]
    for i in range(0,len(words)):
        char_to_code[words[i]] = arr[i]    
    return char_to_code


# Script execution should start from here
if __name__ == '__main__':
    sampleString1 =["aaj","2 feb","hai to kya kru"]
    for sampleString in sampleString1:
        countSTR=frequencycount(sampleString)
        huffmanCodingMap = build_huffman_code(countSTR)
        encoded_str = huffman_encode(sampleString, huffmanCodingMap)

        decoded_str = huffman_decode(encoded_str, huffmanCodingMap)

        # delete this line once encode function completed
        if decoded_str != sampleString:
            print("Error in decoding %s string should be same as %s", decoded_str, sampleString)


    exit(0)