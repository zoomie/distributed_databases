Goal: Build a distributed database in python.
Style: Aiming towards a NoSQL key-value data structure similar to Redis. 
I am thinking of using a simple json encoding so that it is flexible, 
but it could also be interesting to use Python objects and serialise 
them using Pickle.

Todo:
- Set functions that can bring a database a database backup to date.
- Think about ways that a database can sync when it is only a few logs behind.
- Think about way merge conflicts could be resolved.
- Think about having live servers and socket connections.
- Read about ways to reach conseneus.
- Start writing tests.