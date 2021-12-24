import hashlib
import random
# z = random.getrandbits(8)
# print(z)
m =hashlib.md5()
m.update(b'bgvyzdsv254575')

print(m.hexdigest())


thekey=[]

def letsgo():
    for i in range(1000000, 10000000):
        print(i)
        bajts = bytes('bgvyzdsv' + str(i), 'utf-8')
        m = hashlib.md5()
        m.update(bajts)
        gorg =m.hexdigest()
        # !v! edit this line for part 1 or 2 !v!
        if gorg[:6] == '000000':
            print('OMG')
            thekey.append(gorg)
            break
    print(thekey)
letsgo()