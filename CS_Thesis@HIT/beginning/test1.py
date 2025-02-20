# 明文M 的初始置换 IP
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4, 
      62, 54, 46, 38, 30, 22, 14, 6, 
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17,  9, 1, 
      59, 51, 43, 35, 27, 19, 11, 3, 
      61, 53, 45, 37, 29, 21, 13, 5, 
      63, 55, 47, 39, 31, 23, 15, 7]
 
# 逆初始置换 IP^-1
IP_INV = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41,  9, 49, 17, 57, 25]
 
# 右子密钥扩展表 32->48位 
E = [32, 1,   2,  3, 4,   5,
     4,  5,   6,  7, 8,   9,
     8,  9,  10, 11, 12, 13,
     12, 13, 14, 15, 16, 17, 
     16, 17, 18, 19, 20, 21, 
     20, 21, 22, 23, 24, 25, 
     24, 25, 26, 27, 28, 29, 
     28, 29, 30, 31, 32,  1]
 
# 轮结构中的F函数中的置换P
P = [16,  7, 20, 21,
     29, 12, 28, 17,
     1,  15, 23, 26, 
     5,  18, 31, 10, 
     2,   8, 24, 14, 
     32, 27,  3,  9, 
     19, 13, 30,  6,
     22, 11,  4, 25]
 
# 压缩置换: 64位母密钥->56位母密钥
PC_1 = [57, 49, 41, 33, 25, 17,  9,
        1,  58, 50, 42, 34, 26, 18, 
        10,  2, 59, 51, 43, 35, 27, 
        19, 11,  3, 60, 52, 44, 36, 
        63, 55, 47, 39, 31, 23, 15,
        7,  62, 54, 46, 38, 30, 22,
        14,  6, 61, 53, 45, 37, 29,
        21, 13,  5, 28, 20, 12,  4]
 
# 压缩置换: 56位左右密钥->48位子密钥
PC_2 = [14, 17, 11, 24,  1,  5,
        3,  28, 15,  6, 21, 10,
        23, 19, 12,  4, 26,  8, 
        16,  7, 27, 20, 13,  2, 
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]
 
# 左右子密钥的循环移位表
ROTATE = [1, 1, 2, 2, 2, 2, 2, 2,
          1, 2, 2, 2, 2, 2, 2, 1]
 
# 8 个 S 盒
SBOX = [
   [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
    0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
    4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
    15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
 
   [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
    3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
    0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
    13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
 
   [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
    13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
    13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
    1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
 
   [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
    13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
    10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
    3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
 
   [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
    14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
    4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
    11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
 
   [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
    10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
    9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
    4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
 
   [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
    13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
    1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
    6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
 
   [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
    1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
    7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
    2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

import time
 
 
def permutate(bitstr, table):
    """ 通用置换运算
        @table: 置换盒
    """
    res = ""
    for i in table:   
        res += bitstr[i-1]
    
    return res
 
 
def leftShift(key, num):
    """ 子密钥LR: 左循环移位
        @key: 待移位的子密钥
        @num: 列表左移位位数
    """
    return key[num:] + key[0:num]
 
 
def XOR(str1, str2):
    """ 两比特串进行异或 """
    res = ""
    for i in range(0, len(str1)):
        xor = int(str1[i]) ^ int(str2[i])
        res += str(xor)
    return res
 
 
def Sbox(binstr):
    """ S盒置换: 48位->32位 """
    box = 0 # S盒的索引
    res = ""
    for i in range(0, len(binstr), 6):
        tmp = binstr[i:i+6]
        row = int(tmp[0] + tmp[5], 2)
        col = int(tmp[1:5], 2)
 
        num = bin(SBOX[box][16*row+col])[2:]
        num = '0' * (4-len(num)) + num #以0左补全4位
 
        res += num
        box += 1
 
    return res
 
 
def createSubKey(key64):
    """ 64位母密钥->16轮的48位子密钥列表
        @key64: 输入的64位加密密钥
        @return: 16轮子密钥列表
    """
    subkey = []
    key56  = permutate(key64, PC_1)       # 64位密钥压缩置换
    C28b, D28b = key56[0:28], key56[28:]  # 56位密钥左右平分
    
    for i in range(16):
        C28b = leftShift(C28b, ROTATE[i]) # 子密钥左循环移位
        D28b = leftShift(D28b, ROTATE[i]) # 子密钥左循环移位
        subkey.append(permutate(C28b + D28b, PC_2))
 
    return subkey
 
 
def turnFunction(R32b, subkey):
    """ 轮结构中的F函数
        @R32b: F函数输入参数 32位的右明文
        @subkey: F函数输入参数 48位子密钥
    """
    R48b = permutate(R32b, E) # E盒扩展: 右明文32位->48位
    R48b = XOR(R48b, subkey)  # 两异或:  扩展流与子密钥异或
    R32b = Sbox(R48b)         # S盒压缩: 压缩48位->32位
    Fout = permutate(R32b, P) # P盒置换
 
    return Fout
 
 
def hexToBit(hexstr):
    """ 十六进制字符串->二进制比特流(每字符4位) """
    binstr = ""
    decstr = [str(int(i, 16)) for i in hexstr]
    for i in decstr:
        octbin = bin(int(i, 10))[2:]
        binstr += (4-len(octbin)) * '0' + octbin
    return binstr
 
 
def bitToHex(bitstr):
    """ 二进制比特流->十六进制字符串 """
    bitlst = [bitstr[i:i+4] for i in range(0, len(bitstr), 4)]
    hexlst = [hex(int(i, 2))[2:].upper() for i in bitlst]
 
    return ''.join(hexlst)
 
 
def takeTime(func):
    """ 装饰器: 计算函数运行耗时"""
    def decorated(*args):
        startime = time.time()
        func(*args)
        endtime  = time.time()
        taketime = round((endtime - startime)*10**6)
        print(f"\n->运算耗时: {taketime} 微秒")
        return func(*args)
    return decorated


 
class DES():
    """ DES 加解密 """
    
    def __init__(self, scrkey):
        self.scrkey = hexToBit(scrkey) # 初始化密钥 16进制字符->比特流
 
    def feistel(self, in64bit, flag):
        """ Feistel 网络结构算法
            @in64bit: 输入64位比特流
            @flag: 正向算法/反向算法
            单字符由8比特表示
        """
        bit64  = permutate(in64bit, IP)      # 初置换IP重排明文
        L32b, R32b = bit64[0:32], bit64[32:] # 64位明文左右平分
        
        subkey = createSubKey(self.scrkey)   # 生成所有的子密钥  
        if flag == 0: subkey = subkey[::-1]  # 解密用的逆子密钥
 
        for i in range(16):
            Fout = turnFunction(R32b, subkey[i])
            L32b, R32b = R32b, XOR(L32b, Fout)
        out64bit = permutate(R32b + L32b, IP_INV) # 左右交换 逆初始置换
 
        return out64bit
 
    @takeTime
    def encrypt(self, messag):
        """ DES加密
            @messag: 16进制明文字符串
            @return: 16进制密文字符串
        """
        mesbit = hexToBit(messag)
        cipbit = self.feistel(mesbit, 1)
        cipher = bitToHex(cipbit)
 
        return cipher
 
    @takeTime
    def decrypt(self, cipher):
        """ DES 解密
            @cipher: 16进制密文字符串
        """
        cipher = hexToBit(cipher)
        mesbit = self.feistel(cipher, 0)
        messag = bitToHex(mesbit)
 
        return messag
 
 
if __name__ == '__main__':
 
    scrkey = "133457799BBCDFF1" 
    messag = "0123456789ABCDEF"
    cipher = "85E813540F0AB405"
 
    crypto = DES(scrkey)
    print("16进制密文:", crypto.encrypt(messag))
    print("16进制明文:", crypto.decrypt(cipher))