import puffadder 

connection = puffadder.connect(host='localhost', port=010203)
value = {'pytyon': 3.7, 'data': 'this is a data string'}
key = 'one'
connection.save(key, value)