import sqlite3


class PassStore():
    
    def __init__(self):
        self.conn = sqlite3.connect('password_storage.db')
        self.c = self.conn.cursor()        
    
    def create_table(self):   
        self.c.execute('CREATE TABLE IF NOT EXISTS PASSWORDS (id INTEGER primary key autoincrement, Name TEXT)')
 
    def data_entry(self, hashPas):
        self.c.execute("INSERT INTO PASSWORDS (Name) VALUES(?)", [hashPas])
        self.conn.commit()
    
    def show_data(self):
        
        data = self.c.execute("SELECT * FROM PASSWORDS")
        
        print("Passwords:")
        for row in data:
            print(row)
            
    def close_con(self):
        self.c.close()
        self.conn.close()  