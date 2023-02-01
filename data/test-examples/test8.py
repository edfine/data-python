import unittest
from unittest import mock


def echo_data(socket):
    data = socket.recv(42)
    socket.send(data)


class MyTest(unittest.TestCase):

    def test_send_recv(self):
        socket = mock.Mock()
        socket.recv.return_value = b'Some data'
        echo_data(socket)
        socket.recv.assert_called_with(42)
        socket.send.assert_called_with(b'Some data')
