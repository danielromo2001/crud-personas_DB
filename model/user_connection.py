import psycopg

class UserConnection(): #Aca se hace la conexion a la BD, se le da la información de la BD. 
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


    def write(self, data): #Aca se inserta un usuario a la BD
        with self.conn.cursor() as cur:
            cur.execute(""" 
            INSERT INTO users (name, phone) VALUES (%(name)s, %(phone)s) 
            """, data)
            self.conn.commit()

    def read_all(self): #Aca se muestra la lista de usuarios guardados en la BD
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM "users"
                    """)
            return cur.fetchall()
        
    def read_one(self, id): #Aca se muestra un usuario en especifico que esta almacenado en la BD
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM "users" WHERE id = %s
                    """, (id,))
            return cur.fetchone()
        
    def update(self, data): #Aca actualizamos un usuario en especifico que esta almacenado en la BD
        with self.conn.cursor() as cur:
            cur.execute(""" UPDATE users SET name = %(name)s, phone = %(phone)s WHERE id = %(id)s
                        """, data)
            self.conn.commit()

    def delete(self, id): #Aca se elimina un usuario en especifico que esta almacenado en la BD
        with self.conn.cursor() as cur:
            cur.execute("""
            DELETE FROM "users" WHERE id = %s
                        """, (id,))
            self.conn.commit()


    def __def__(self): #Aca se cierra la conexion a la BD
        self.conn.close()