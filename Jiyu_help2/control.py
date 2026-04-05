import binascii
import socket

'''
This file has been deprecated.
-> udp.py
'''


def sendMessage(message: str, ip_address: str, port: int = 4075) -> None:
    """
    构建符合指定格式的数据包并发送到指定IP和端口
    
    参数:
        message: 要发送的信息字符串
        ip_address: 目标IP地址
        port: 目标端口，默认为4075
    """
    # 十六进制固定数据包头
    hex_header = "444d4f43000001009e030000dc79fabb169ec04ca009db380f7f34ee204e0000c0a803fe9103000091030000000800000000000005000000"
    
    # 将十六进制头部转换为bytes
    try:
        header = binascii.unhexlify(hex_header)
    except binascii.Error as e:
        raise ValueError(f"无效的十六进制头部: {e}")
    
    # 计算头部长度
    header_length = len(header)
    
    # 将消息转换为bytes(使用UTF-8编码)
    message_bytes = message.encode('utf-8')
    
    # 消息长度
    message_length = len(message_bytes)
    
    # 单个空字节分隔符
    separator = b'\x00'
    
    # 计算已使用的长度
    used_length = header_length + message_length + len(separator)
    
    # 计算需要填充的空字节数量(总长度1906)
    total_length = 1906
    padding_length = total_length - used_length
    
    # 确保填充长度不为负数
    if padding_length < 0:
        raise ValueError(f"消息太长，无法放入 {total_length} 字节的数据包中。最大允许消息长度: {total_length - header_length - len(separator)} 字节")
    
    # 创建填充字节
    padding = b'\x00' * padding_length
    
    # 构建完整数据包
    packet = header + message_bytes + separator + padding
    
    # 验证数据包长度
    if len(packet) != total_length:
        raise AssertionError(f"数据包长度错误: 预期 {total_length} 字节，实际 {len(packet)} 字节")
    
    # 发送数据包
    try:
        # 创建UDP套接字
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            # 设置超时时间为5秒
            sock.settimeout(5.0)
            
            # 发送数据包
            bytes_sent = sock.sendto(packet, (ip_address, port))
            
            if bytes_sent != len(packet):
                raise RuntimeError(f"发送失败，只发送了 {bytes_sent}/{len(packet)} 字节")
            
            return 0
            
    except socket.timeout:
        raise ConnectionError(f"连接超时，无法发送到 {ip_address}:{port}")
    except socket.error as e:
        raise ConnectionError(f"发送失败: {e}")


print("\n\n\ncontrol.py\n\nThis file has been deprecated.\n\nGo to -> udp.py!\n\n\n")