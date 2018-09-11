###python知识点
1. os.path.dirname()
2. os.path.abspath(__file__)
3. optparse模块--解析命令行
```python
        #创建一个对象
        self.op = optparse.OptionParser()

        self.op.add_option('-s', '--server', dest='server')
        self.op.add_option('-P', '--port', dest='port')
        self.op.add_option('-u', '--username', dest='username')
        self.op.add_option('-p', '--password', dest='password')
        # 参数解析，返回两个结果
        # option返回的绑定的是数据，看着像是字典类型！！但注意类型为对象用.来取
        # args返回的是没有匹配的数据，返回的是列表类型
        self.options, self.args = self.op.parse_args()
```
4. configparser模块
```python
 cfg = configparser.ConfigParser()
        cfg.read(settings.ACCOUNTS_PATH)

        if user in cfg.sections():
            if cfg[user]['Password'] == pwd:
                self.user = user
                self.mainPath = os.path.join(settings.BASE_DIR, 'home', self, user)
                print('passed authentication.....')
                return user
```
5. 反射
```python
        if hasattr(self, cmd_list[0]):
            func = getattr(self, cmd_list[0])
            func(*cmd_list)
        def func(self):
            pass
```
6. os.path.exists(abs_path)判断文件是否存在
7. os.stat(abs_path).st_size获取文件的大小
8. 结构目录
```
ftp
bin conf core logger
```
9. socketserver模块
```python
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        #消息循环
        while True:
            data = self.request.recv(1024).strip()

    s = socketserver.TreaddingTCPServer((),MyServer)
    s.server_forever()#连接循环
```