#!/usr/bin/python

import sys
import thread
import time
import hashlib
import ltc_scrypt    # Packaged with litecoin p2pool - https://github.com/coblee/p2pool

#header_hex = "020000004c1271c211717198227392b029a64a7971931d351b387bb80db027f270411e398a07046f7d4a08dd815412a8712f874a7ebf0507e3878bd24e20a3b73fd750a667d2f451eac7471b00de6659"
#header_hex ="01000000f615f7ce3b4fc6b8f61e8f89aedb1d0852507650533a9e3b10b9bbcc30639f279fcaa86746e1ef52d3edb3c4ad8259920d509bd073605c9bf1d59983752a6b06b817bb4ea78e011d012d59d4"
#header_hex =  "000000204ac4bbcd97fb85ba80a968c869ab20cde1b1d429024302a3b9596fd55651bc72320cd2ed8705ccf53e291d6fce6bd051b2aa024e937f37ea92029d2e10a8c67c79fdf05a1bb8011a01811900"
def cal_nonce(start,end):
    value = 2**16
    for i in range(start,end):
        for nonce in range(0, 2** 16):
            nonce = nonce + value * i
#            print(nonce)
            header_hex ="000000208e930321ddc9e81115c2bca446f98fd216f10abb95554b5fc0c5bc20ddbbc851eed8022fd1b482072b353334031c26f212eefd61d1575426452d7f3d04b3d1f0dc1aa25bdeed011a" + \
                str(hex(nonce))[2:].zfill(8)
        #    print header_hex 
            header_bin = header_hex.decode('hex')
        
            #hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
            #hash.encode('hex_codec')
            #print "hash:"
            #print(hash[::-1].encode('hex_codec'))    # convert from big-endian to little-endian
        
            scrypt = ltc_scrypt.getPoWHash(header_bin)
            scrypt.encode('hex_codec')
        #    print "scrypt:"
        #    ts = str((scrypt[::-1].encode('hex_codec')))[0:5]    # convert from big-endian to little-endian
            ts = (scrypt[::-1].encode('hex_codec'))[0:5]    # convert from big-endian to little-endian
            if ts=='00000':
                print header_hex 
                print(scrypt[::-1].encode('hex_codec'))
        #    print(scrypt[::-1].encode('hex_codec'))    # convert from big-endian to little-endian
    thread.exit_thread()
    
def mul_thread():
    thread.start_new_thread(cal_nonce,(0,16384))
    thread.start_new_thread(cal_nonce,(16385,52768))
    thread.start_new_thread(cal_nonce,(52769,49152))
    thread.start_new_thread(cal_nonce,(49153,65536))
if __name__=='__main__':
    mul_thread()
    while 1:
        continue
