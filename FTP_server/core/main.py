import socketserver
import optparse
from conf import settings
from core import server


class ArgvHandler(object):
    def __init__(self):
        # 获得命令行的参数列表，比sys.args更好用
        self.op = optparse.OptionParser()
        # self.op.add_option('-s', '--server', dest='server')
        # self.op.add_option('-P', '--port', dest='port')

        options, args = self.op.parse_args()

        self.verify_args(options, args)

    def verify_args(self, options, args):
        cmd = args[0]
        # 反射的应用
        if hasattr(self, cmd):
            func = getattr(self, cmd)
            func()

    # 反射的函数
    def start(self):
        print("server is start....")
        s = socketserver.ThreadingTCPServer((settings.IP, settings.PORT), server.ServerHandler)
        s.serve_forever()

    def help(self):
        pass