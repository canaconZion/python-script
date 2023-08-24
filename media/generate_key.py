#!/usr/bin/python3
#coding:utf-8
'''
生成用于aes加密的key和iv，写入encrypt.key中
'''
import os
import binascii

def generate_key(file_path: str, key_url=None, length=16) -> str:
    # 随机生成16位AES密钥
    key = os.urandom(length)
    # 随机生成16位IV
    iv = os.urandom(length)
    # 将IV转化为16进制，用字符串表示，生成的16进制字符串将具有双倍的长度，因为每个字节对应两个十六进制字符
    iv_string = binascii.hexlify(iv).decode('utf-8')
    file_name = f"{file_path}/encrypt.key"
    key_info = f"{file_path}/encrypt.keyinfo"
    if key_url is None:
        key_url = file_name
    # 将密钥写入key文件
    with open(file_name, 'wb') as f:
        f.write(key)
    # 将密钥信息和IV写入keyinfo文件
    with open(key_info, 'wb') as f:
        f.write(key_url.encode('utf-8'))
        f.write('\n'.encode('utf-8'))
        f.write(file_name.encode('utf-8'))
        f.write('\n'.encode('utf-8'))
        f.write(iv_string.encode('utf-8'))
    return file_name


if __name__ == "__main__":
    ret = generate_key("./aes_files")
    print(f"key file path < {ret} >")