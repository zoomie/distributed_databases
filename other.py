from puffadder import PuffAdder
import subprocess
subprocess.run(["rm", "-r", "/Users/andrewarderne/work/distributed_databases/data"])

leader = PuffAdder(db='leader', port=2343)
leader.set_value('key', 'value')
leader.set_value('key', 'value')

follow1 = PuffAdder('follow1')
leader.send_heartbeat(follow1)

# leader = PuffAdder('lead')
# leader.set_value('key', 'value')
# leader.set_value('key', 'value')
# leader.set_value('key', 'value')

# follow1 = PuffAdder('follow1')
# follow1.sync_database('data/lead/history.puff')

# follow2 = PuffAdder('follow2')
# follow2.sync_database('data/lead/history.puff')

# leader.heart_beat(follow1, follow2)