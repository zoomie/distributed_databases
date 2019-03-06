from socketserver import StreamRequestHandler
from socketserver import TCPServer
import subprocess
from puffadder import PuffAdder

subprocess.run(
    ["rm", "-r", "/Users/andrewarderne/work/distributed_databases/data"])


def create_db_handler(puffadder):
    class Handler(StreamRequestHandler):
        def handle(self):
            print("{} wrote:".format(self.client_address[0]))
            data_bytes = self.rfile.readline().strip()
            data = data_bytes.decode()
            method, key, value = data.split(' ')
            method_to_call = getattr(puffadder, method)
            method_to_call(key, value)
            # print(method_to_call, method, key, value)
            self.wfile.write(data_bytes.upper())
    return Handler

p = PuffAdder('leader')
Handler_lead = create_db_handler(p)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    db = 'Leader'
    with TCPServer((HOST, PORT), Handler_lead) as server:
        server.serve_forever()
