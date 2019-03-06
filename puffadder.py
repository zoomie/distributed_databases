import json
import os


class PuffAdder:

    def __init__(self, db):
        mkdir = 'data/' + db
        if not os.path.exists(mkdir):
            os.makedirs(mkdir)
            with open(mkdir + '/history.puff', 'w'):
                pass
        self.db = db
        self.history = 'data/' + db + '/history.puff'

    def set_value(self, key: str, value: str):
        p_key = 'data/' + self.db + '/' + key + '.val'
        with open(p_key, 'w') as file:
            file.write(value)

        with open(self.history, 'a') as file:
            row = key + ' -- ' + value
            file.write(row)
            file.write('\n')

    def get_value(self, key: str):
        p_key = 'data/' + self.db + '/' + key + '.val'
        with open(p_key, 'r') as file:
            data = file.read()
        return data

    def sync_database(self, incoming_history: bytes):
        data = incoming_history.decode('utf-8')
        with open(self.history, 'r') as file:
            local = file.read().split('\n')
            # print(local)
            # start_index = len(inc) - len(loc) + 1
            for row in data.split('\n'):
                if row:
                    key, value = row.split(' -- ')
                    self.set_value(key, value)

    def send_heartbeat(self, *follower_list):
        # This should in theory contain the port
        # number and then I would be able to send
        # the data over a socket connection.
        with open(self.history, 'rb') as file:
            data = file.read()
        for follower in follower_list:
            follower.recieve_heartbeat(data)

    def recieve_heartbeat(self, data):
        # This heart_beat should recieve the data_sync
        # as a series of bytes and update its internal
        # state. It should then send a signal telling
        # the leader that it is upto date.
        print(f'{self.db} is getting {data}')
        self.sync_database(data)
