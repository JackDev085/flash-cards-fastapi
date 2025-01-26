import sqlite3

class Connection:
    def __init__(self,db_name):
        """Inicializa uma instância de conexão com o banco de dados"""
        self.db_name = db_name
        self._cursor = None
        self._connection = None

        try:
            self._connection = sqlite3.connect(self.db_name,check_same_thread=False)
            self._connection.row_factory=sqlite3.Row
            self._cursor = self._connection.cursor()

            print("Conexão estabelecida com o banco de dados")
        except sqlite3.Error as e:
            print(f"Erro ao conectar no banco de dados: {e}")
            

    def execute_query(self, query,params:tuple=None):
        """Executa uma intrução sql no banco de dados"""
        if not self._cursor:
            print("Conexão não inicializada")  
            return
        try: 
            if not params:
                self._cursor.execute(query)
                return self._cursor.execute(query)
            
            return self._cursor.execute(query,params)
        except sqlite3.Error as e:
            print(f"Erro ao realizar query no banco de dados: {e}")
            return None
        
    def fetch_all(self)->list:
        """Retorna todas as linhas de uma consulta"""
        if self._cursor:
            return self._cursor.fetchall()
        print("Nenhuma consulta foi realizada")
        return []

    def fetch_one(self)->sqlite3.Row:
        """Retorna a primeira linha de uma consulta"""
        if self._cursor:
            return self._cursor.fetchone()
        print("Nenhuma consulta foi realizada")
        return []     
    
    def commit(self)->None:
        if self._connection:
            self._connection.commit()
        raise Exception("Conexão não inicializada")
    
    def refresh(self, object)->None:
        """Recarrega um objeto do banco de dados"""
        if self._connection:
            self._connection.commit()
            print(f"Recarregando objeto {object.__class__.__name__} com id {object.id}")
            self._cursor.execute(f"SELECT * FROM {object.__class__.__name__} WHERE id = ?", (object.id,))
            row = self._cursor.fetchone()
            if row:
                for key in row.keys():
                    setattr(object, key, row[key])
        raise Exception("Conexão não inicializada")
        

    def rollback(self)->None:
        """Desfaz as alterações realizadas no banco de dados"""
        if self._connection:
            self._connection.rollback()
        raise Exception("Conexão não inicializada")
        
        
    def __del__(self)->None:
        """Encerra a conexão com o banco de dados"""
        if self._connection:
            print("Encerrando conexão com o banco de dados")
            self._connection.close()
        raise Exception("Conexão não inicializada")
        