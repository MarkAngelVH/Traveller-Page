# Importar librerías
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.pool import SimpleConnectionPool

# Clase para conectar a BD 
class Database:
    def __init__(self, cliente=None, cursor=None):
        self._cliente = cliente
        self._cursor = cursor

    def connect(self, host, port, user, password, database, schema='public', ssl_mode=None, ssl_server_ca=None,
                ssl_client_cert=None, ssl_client_key=None):
        try:
            options = f'-c search_path={schema} -c statement_timeout=540000'
            self._cliente = psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                sslmode=ssl_mode,
                sslrootcert=ssl_server_ca,
                sslcert=ssl_client_cert,
                sslkey=ssl_client_key,
                options=options,
                application_name='Traveller'
            )
            self.set_cursor()
        except Exception as e:
            print('Error en la conexión:', repr(e))
            raise e

    def connect_pool(self, host, port, user, password, database, schema='public'):
        try:
            options = f'-c search_path={schema}'
            pool = SimpleConnectionPool(
                minconn=1,
                maxconn=1,
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                options=options
            )
            self._cliente = pool.getconn()
            self.set_cursor()
        except Exception as e:
            print('Error en la conexión del pool:', repr(e))
            raise e

    def disconnect(self):
        if self._cliente:
            if isinstance(self._cliente, psycopg2.extensions.connection):
                self._cliente.close()
            elif isinstance(self._cliente, psycopg2.extensions.connection):
                self._cliente.putconn(self._cliente)
        if self._cursor:
            self._cursor.close()

    def get_client(self):
        return self._cliente

    def get_cursor(self):
        return self._cursor

    def load_config(self):
        self._cliente.autocommit = False

    def set_cursor(self):
        self._cursor = self._cliente.cursor(cursor_factory=RealDictCursor)


# Uso de la clase
db = Database()
try:
    db.connect(host='34.29.69.18', port='5432', user='postgres', password='lambo123456', database='postgres')
    db.get_cursor().execute("SELECT * FROM contactanos;")
    results = db.get_cursor().fetchall()
    for row in results:
        print(row)
except Exception as e:
    print('Error en la consulta:', repr(e))
finally:
    db.disconnect()
