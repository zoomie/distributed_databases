import json
import os

class PuffAdder:

    def __init__(self, db: str):
        mkdir = 'data/' + db
        if not os.path.exists(mkdir):
            os.makedirs(mkdir)
            with open(mkdir + '/history.puff', 'w'):
                pass
        self.db = db

    def set_value(self, key: str, value: dict):
        p_key = 'data/' + self.db + '/' + key + '.json'
        with open(p_key, 'w') as file:
            json.dump(value, file)

        h_path = 'data/' + self.db + '/history.puff'
        with open(h_path, "a") as file:
            row = key + ' -- ' + str(value)
            file.write(row)
            file.write('\n')

    def get_value(self, key: str):
        p_key = 'data/' + self.db + '/' + key + '.json'
        with open(p_key, 'r') as file:
            data = json.load(file)
        return data

    def sync_database(self, incoming: str):
        local = 'data/' + self.db + '/history.puff'
        with open(incoming, 'r') as inc_conn,\
            open(local, 'r') as loc_conn:
            inc = inc_conn.read().split('\n')
            loc = loc_conn.read().split('\n')
            number_update = len(inc) - len(loc)
            for row in inc[number_update:]:
                if row:
                    key, value = row.split(' -- ')
                    self.set_value(key, value)
                #     self.set_value(key, value)

        # with open(history_file, 'r') as file:
        #     for line in file.read().split('\n'):
        #         if line:
        #             key, value = line.split(' -- ')
        #             self.set_value(key, value)
