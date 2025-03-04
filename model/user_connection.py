import psycopg

class UserConnection():
    conn = None

    def __init__(self):

        try: 
            self.conn = psycopg.connect(
                dbname = "crud",
                user = "romo",
                password = "danielromo",
                host = "localhost",
                port = "5432"
                )
            
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()


    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute(""" 
            INSERT INTO users (name, phone) VALUES (%(name)s, %(phone)s) 
""", data)
            self.conn.commit()
            


    def __def__(self):
        self.conn.close()