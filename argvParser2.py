from typing import Literal
LIST = "list"
DICT = "dict"
# def parse_arguments_by_colon(argv:list,contain_parameters_identifiers:list,identifiers:list,renames:dict={}) -> dict:
#     '''
#     分割并简化命令行输入内容。
    
#     :param argv: 命令行参数列表，你应当输入sys.argv。
#     :type argv: list
#     :param contain_parameters_identifiers: 带参数的选项列表。
#     :type contain_parameters_identifiers: list
#     :param identifiers: 不带参数的选项列表。
#     :type identifiers: list
#     :param renames: 对各个选项作重命名，每个选项的重命名不是必须的。（格式如-U:--upgrade)
#     '''
#     argv = argv[1:]
#     result = {}
#     for i in contain_parameters_identifiers:
#         result[i] = None
#     for i in identifiers:
#         result[i] = 0
#     for i in argv:
#         if(":" in i): #选项有参数
#             identifier = [i[:i.index(":")],i[i.index(":")+1:]]
#             if(identifier[0] in contain_parameters_identifiers):#存在
#                 result[identifier[0]] = identifier[1]
#             elif(identifier[0] in renames.keys()):
#                 if(renames[identifier[0]] in contain_parameters_identifiers):
#                     result[renames[identifier[0]]] = identifier[1]
#                 else:
#                     raise ValueError(i+"选项不应有参数")
#             else:
#                 if(identifier[0] in identifiers):
#                     raise ValueError(identifier[0]+"选项不应有参数")
#                 else:
#                     raise ValueError(identifier[0]+"：未知选项（带冒号）")
#         else:
#             if(i in identifiers):
#                 result[i] = 1
#             elif(i in renames.keys()):
#                 if(renames[i] in identifiers):
#                     result[renames[i]] = 1
#                 else:
#                     raise ValueError(i+"选项应有参数")
#             else:
#                 if(i in contain_parameters_identifiers):
#                     raise ValueError(i+"选项应有参数")
#                 else:
#                     raise ValueError(i+"：未知选项（不带冒号）")
#     return result

def parse_arguments_by_colon(argv: list, contain_parameters_identifiers: list, identifiers: list, renames: dict = {}) -> dict:
    '''
    分割并简化命令行输入内容。
    
    :param argv: 命令行参数列表，你应当输入sys.argv。
    :type argv: list
    :param contain_parameters_identifiers: 带参数的选项列表。
    :type contain_parameters_identifiers: list
    :param identifiers: 不带参数的选项列表。
    :type identifiers: list
    :param renames: 对各个选项作重命名，每个选项的重命名不是必须的。（格式如-U:--upgrade)
    '''

    SEP = "="

    # 跳过可执行文件名
    if len(argv) >= 1:
        argv = argv[1:]

    # 初始化结果
    result = {}
    for i in contain_parameters_identifiers:
        result[i] = None
    for i in identifiers:
        result[i] = 0

    for arg in argv:
        # ---------------------
        # 带冒号参数（key:value）
        # ---------------------
        if SEP in arg:
            key = arg[:arg.index(SEP)]
            value = arg[arg.index(SEP) + 1:]
            
            # ✅ 优先应用重命名（修复核心bug）
            real_key = renames.get(key, key)

            # 判断真实key是否合法
            if real_key in contain_parameters_identifiers:
                result[real_key] = value
            elif real_key in identifiers:
                raise ValueError(f"[{key}] 此选项不支持带参数")
            else:
                raise ValueError(f"[{key}] 未知的带参数选项")

        # ---------------------
        # 不带冒号开关
        # ---------------------
        else:
            key = arg
            real_key = renames.get(key, key)

            if real_key in identifiers:
                result[real_key] = 1
            elif real_key in contain_parameters_identifiers:
                raise ValueError(f"[{key}] 此选项必须带参数（格式：{key}{SEP}xxx）")
            else:
                raise ValueError(f"[{key}] 未知选项")

    return result

def parse_arguments_oldversion(argv:list,identifiers:list,returnType:str) -> dict:
    '''
    旧版分割函数。
    此函数适用于从argvParser.py迁移过来的程序，而不是全新编辑的程序。
    
    :param argv: 命令行参数列表，你应当输入sys.argv。
    :type argv: list
    :param identifiers: 有效的标识符列表，每个标识符由名称和参数数量组成。
    :type identifiers: list
    :param returnType: 返回值类型。此参数已被弃用并忽略。
    :type returnType: str
    '''
    print("""You are using 'parse_arguments_oldversion'.
'returnType' argument was ignored.""")
    p_args = [item[0] for item in identifiers if item[1] >= 1]
    args = [item[0] for item in identifiers if item[1] == 0]
    return parse_arguments_by_colon(argv,p_args,args)

if __name__ == "__main__":
    import sys
    print(parse_arguments_by_colon(sys.argv,["--parameters1","--P","--parameters2"],["--no1","-N"],{"-P":"--parameters1"}))