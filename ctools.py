'''
Created on Apr 15, 2012

@author: wisp

Tools for crypto class 
'''
            
def ch2bit(in_char):
    """
    convert char into it 8-bit number
    """ 
    return str(bin(ord(in_char))[2:]).zfill(8)

def str2bit(in_string):
    """
    convert string into string of ascii bits
    #TODO: change for loop to map
    """
    bitstring = ''
    for ch in in_string:
        bitstring += ch2bit(ch)
    return bitstring

def hch2bit(in_hex):
    """
    replace hex char to 4 bits 
    note: every single char replaced by 4 digit
    example: '0' => 0000 '3' => 0011
    """
    return bin(int(in_hex,16))[2:].zfill(4)

def hstr2bit(in_hex_string):
    """
    convert string into string of ascii bits
    #TODO: change for loop to map
    #TODO: avoid copy pasting programmig
    this time bit want to sleep, will fix in nex time :D
    """
    bitstring = ''
    for ch in in_hex_string:
        bitstring += hch2bit(ch)
    return bitstring

def bit2ch(bit_ch):
    return chr(int(bit_ch))
 
def bit2str(bit_string):
    """
    convert bit string into ascii character string
    """
    ch_string = ''
    while bit_string:
        bit2ch(bit_string[:8])
        bit_string = bit_string[8:]
    return ch_string