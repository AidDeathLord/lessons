from connected import ConnectedState
from disconnected import DisconnectedState
from errors import TcpConnectionError
import pytest


class TcpConnection:
# BEGIN (write your solution here)
    def __init__(self, ip, port):
        self.states = {
            'disconnected': DisconnectedState,
            'connected': ConnectedState,
        }
        self.ip = ip
        self.port = port
        self.buffer = []
        self.set_state('disconnected')

    def get_current_state(self):
        return self.state.get_name()

    def connect(self):
        self.state.connect()

    def disconnect(self):
        self.state.disconnect()

    def write(self, data):
        self.state.write(data)

    def set_state(self, name):
        self.state = self.states[name](self)
# END


connection = TcpConnection('11.22.33.11', 20)
connection.connect()
assert connection.get_current_state() == 'connected'
connection.write('one')
connection.write('two')
connection.disconnect()
assert connection.get_current_state() == 'disconnected'


connection = TcpConnection('11.22.33.11', 20)
print(connection.get_current_state())
connection.connect()
print(connection.get_current_state())
print(connection.connect())
with pytest.raises(TcpConnectionError):
    connection.connect()
