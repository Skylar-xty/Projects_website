def caesar_encrypt_decrypt(data, shift):
    """ 凯撒密码加密和解密 """
    result = []
    
    for char in data:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result.append(chr((ord(char) - offset + shift) % 26 + offset))
        else:
            result.append(char)  # 非字母字符不加密
    
    return ''.join(result)

def encrypt_file(file_path, shift):
    """ 使用凯撒密码加密文件 """
    with open(file_path, 'r') as f:
        data = f.read()

    encrypted_data = caesar_encrypt_decrypt(data, shift)
    
    with open(file_path + '.enc', 'w') as f:
        f.write(encrypted_data)

    print(f"文件 {file_path} 已加密为 {file_path}.enc")

def decrypt_file(file_path, shift):
    """ 使用凯撒密码解密文件 """
    with open(file_path, 'r') as f:
        data = f.read()

    decrypted_data = caesar_encrypt_decrypt(data, -shift)

    with open(file_path.replace('.enc', '.dec'), 'w') as f:
        f.write(decrypted_data)

    print(f"文件 {file_path} 已解密为 {file_path.replace('.enc', '.dec')}")


def main():
    shift = 3  # 密钥，位移数量
    # file_path = "input.txt"  # 文件路径
    print("please input file: ")
    file_path = input()
    # 加密文件
    encrypt_file(file_path, shift)
    
    # 解密文件
    decrypt_file(file_path + ".enc", shift)

if __name__ == '__main__':
    main()
