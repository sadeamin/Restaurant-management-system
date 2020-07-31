from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1,
                                       100,
                                       database="learning",
                                       user="postgres",
                                       password="782489",
                                       host="localhost")




