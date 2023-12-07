from connected import ConnectedState
from disconnected import DisconnectedState
from errors import TcpConnectionError
import pytest


class TcpConnection:
# BEGIN (write your solution here)
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.states = {
            'connected': ConnectedState,
            'disconnected': DisconnectedState,
        }
        self.state = self.states['disconnected']()

    def connect(self):
        return self.state.connect()

    def write(self, text):
        return self.state.write()

    def disconnect(self):
        return self.state.disconnect()

    def get_current_state(self):
        return self.state.get_state()
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
