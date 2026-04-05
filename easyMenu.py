from tkinter import *

class TopMenu(Menu): # 顶部菜单类，用于创建顶部菜单
    def __init__(self,root:Tk):
        '''
        顶部菜单类，用于创建顶部菜单。
        Args:
            root (Tk): 菜单所在的tkinter Tk窗口。
        '''
        super().__init__(root,tearoff=0)
        self.root = root
        self.child_menus = {}
        self.vars = {}

    def addItem(self,father:str,prompt:str,command:callable): # 添加菜单项，prompt为菜单项的名称，command为菜单项的命令
        '''
        添加菜单项。
        Args:
            father (str): 父菜单的id，如果id为空字符串或不存在则此菜单项将添加至根菜单。
            prompt (str): 菜单项内容。
            command (callable): 当点击菜单后调用的方法。
        '''
        if father != "" and (father in self.child_menus): # 如果父菜单存在，则添加菜单项到父菜单中
            self.child_menus[father].add_command(label=prompt,command=command)
            return
        self.add_command(label=prompt,command=command) # 添加菜单项，label为菜单项的名称，command为菜单项的命令
    
    def addMenu(self,father:str,id:str,prompt:str): # 添加子菜单，prompt为子菜单的名称，返回子菜单对象，用于添加子菜单项
        '''
        添加菜单。
        Args:
            father (str): 父菜单的id，如果id为空字符串或不存在则此菜单项将添加至根菜单。
            id (str): 菜单id，可用于在此菜单下添加子菜单或子项。此参数是必须的。
            prompt (str): 菜单内容。
        '''
        menu = Menu(self,tearoff=0) # 创建子菜单对象
        if father != "" and (father in self.child_menus):
            self.child_menus[father].add_cascade(label=prompt,menu=menu) # 添加子菜单，label为子菜单的名称，menu为子菜单对象
            self.child_menus[id] = menu # 将子菜单对象添加到子菜单字典中，id为子菜单的标识符，menu为子菜单对象
            return
        self.add_cascade(label=prompt,menu=menu) # 添加子菜单，label为子菜单的名称，menu为子菜单对象
        self.child_menus[id] = menu # 将子菜单对象添加到子菜单字典中，id为子菜单的标识符，menu为子菜单对象

    def addCheckbutton(self,father:str,prompt:str,varid:str): # 添加复选框菜单项，prompt为菜单项的名称，command为菜单项的命令，variable为变量对象，用于存储复选框的状态
        '''
        添加复选框菜单项。
        Args:
            father (str): 父菜单的id，如果id为空字符串或不存在则此菜单项将添加至根菜单。
            prompt (str): 菜单项内容。
            varid (callable): 该复选框绑定的变量id，稍后可通过get方法查询该复选框选中状态。
        '''
        self.vars[varid] = BooleanVar() # 创建变量对象，用于存储复选框的状态，varid为变量的标识符，用于存储复选框的状态
        if father != "" and (father in self.child_menus): # 如果父菜单存在，则添加菜单项到父菜单中
            self.child_menus[father].add_checkbutton(label=prompt,variable=self.vars[varid]) # 添加复选框菜单项，label为菜单项的名称，command为菜单项的命令，variable为变量对象，用于存储复选框的状态
            return
        self.add_checkbutton(label=prompt,variable=self.vars[varid]) # 添加复选框菜单项，label为菜单项的名称，command为菜单项的命令，variable为变量对象，用于存储复选框的状态

    def addLine(self,father:str):
        '''
        添加分割线。
        Args:
            father (str): 父菜单的id，此参数是必须且非空的。
        '''
        if father in self.child_menus: # 如果父菜单存在，则添加菜单项到父菜单中
            self.child_menus[father].add_separator() # 添加分隔符，用于分隔菜单项，用于添加子菜单项
            return

    def show(self): # 显示菜单
        '''
        将设置好的菜单添加至窗口。
        你也可以在添加后设置菜单任何内容，这些内容仍会显示至窗口。
        '''
        self.root.config(menu=self) # 将菜单对象添加到根窗口中，menu为菜单对象

    def get(self,varid:str):
        '''
        获取复选框选中状态。
        Args:
            varid (str): 复选框变量id。
        '''
        return self.vars[varid].get()

class Right_Click_Menu(Menu): # 右键菜单类，用于创建右键菜单
    def __init__(self,root:Tk): # root为根窗口对象，用于创建右键菜单
        '''
        顶部菜单类，用于创建顶部菜单。
        Args:
            root (Tk): 菜单所在的tkinter Tk窗口。
        '''
        super().__init__(root,tearoff=0) # 调用父类的构造函数，root为根窗口对象，用于创建右键菜单
        self.root:Tk = root # 将根窗口对象赋值给self.root，用于创建右键菜单
        self.child_menus = {} # 创建子菜单字典，用于存储子菜单对象，用于创建右键菜单

    def addItem(self,father:str,prompt:str,command:callable,disabled:bool=0,send_xy:bool=0): # 添加菜单项，prompt为菜单项的名称，command为菜单项的命令
        '''
        添加菜单项。
        Args:
            father (str): 父菜单的id，如果id为空字符串或不存在则此菜单项将添加至根菜单。
            prompt (str): 菜单项内容。
            command (callable): 当点击菜单后调用的方法。
        '''
        if father != "" and (father in self.child_menus): # 如果父菜单存在，则添加菜单项到父菜单中
            self.child_menus[father].add_command(label=prompt,command=command if not send_xy else lambda:command(self.root.winfo_pointerx()-self.root.winfo_x(),self.root.winfo_pointery()-self.root.winfo_y()))
            return
        self.add_command(label=prompt,command=command if not send_xy else lambda:command(self.root.winfo_pointerx()-self.root.winfo_x(),self.root.winfo_pointery()-self.root.winfo_y()), state=DISABLED if disabled else NORMAL) # 添加菜单项，label为菜单项的名称，command为菜单项的命令
        return self

    def addMenu(self,father:str,id:str,prompt:str): # 添加子菜单，prompt为子菜单的名称，返回子菜单对象，用于添加子菜单项
        '''
        添加菜单。
        Args:
            father (str): 父菜单的id，如果id为空字符串或不存在则此菜单项将添加至根菜单。
            id (str): 菜单id，可用于在此菜单下添加子菜单或子项。此参数是必须的。
            prompt (str): 菜单内容。
        '''
        menu = Menu(self,tearoff=0) # 创建子菜单对象
        if father != "" and (father in self.child_menus):
            self.child_menus[father].add_cascade(label=prompt,menu=menu) # 添加子菜单，label为子菜单的名称，menu为子菜单对象
            self.child_menus[id] = menu # 将子菜单对象添加到子菜单字典中，id为子菜单的标识符，menu为子菜单对象
            return
        self.add_cascade(label=prompt,menu=menu) # 添加子菜单，label为子菜单的名称，menu为子菜单对象
        self.child_menus[id] = menu # 将子菜单对象添加到子菜单字典中，id为子菜单的标识符，menu为子菜单对象
        return self

    def addLine(self,father:str):
        '''
        添加分割线。
        Args:
            father (str): 父菜单的id。
        '''
        if father in self.child_menus: # 如果父菜单存在，则添加菜单项到父菜单中
            self.child_menus[father].add_separator() # 添加分隔符，用于分隔菜单项，用于添加子菜单项
            return
        self.add_separator()
        return self

    def show(self,event:Event): # 显示右键菜单，event为鼠标事件对象，用于获取鼠标的位置信息，用于显示右键菜单
        '''
        在窗口中显示一次菜单。
        你可以使用```Right_Click_Menu.bindto()```将此菜单绑定至```<Button-3>```以实现更好的效果。
                
        Args:
            event (tkinter.Event): 说明
        '''
        self.post(event.x_root, event.y_root) # 显示右键菜单，x_root为右键菜单的x坐标，y_root为右键菜单的y坐标，用于显示右键菜单   
        return self

    def bindto(self): # 绑定右键菜单，root为根窗口对象，用于绑定右键菜单
        '''
        将此菜单绑定至窗口。
        '''
        self.root.bind("<Button-3>", self.show) # 绑定右键菜单，Button-3为右键鼠标按钮，show为右键菜单的显示函数，用于绑定右键菜单
        return self

if __name__ == "__main__": # 测试代码
    root = Tk() # 创建根窗口对象，用于创建右键菜单
    root.title("测试") # 设置根窗口的标题，用于创建右键菜单
    menu = Right_Click_Menu(root)
    #menu.addMenu("file","文件")
    menu.addItem("","打开",lambda:print("打开"))
    menu.addItem("","保存",lambda:print("保存"))
    menu.addLine("")
    menu.addItem("","检查",lambda:print("Hello"))
    menu.addMenu("","menu1","菜单1")
    menu.addItem("menu1","1",lambda:print("Hello1"))
    menu.addItem("menu1","2",lambda:print("Hello2"))
    menu.addItem("menu1","3",lambda:print("Hello3"))
    menu.addLine("")
    menu.addItem("","退出",exit)
    menu.bindto()
    #root.bind("<Button-3>",lambda event:menu.show())
    root.mainloop()