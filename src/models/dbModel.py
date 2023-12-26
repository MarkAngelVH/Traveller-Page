import yaml as yml
from src.cn.data_base_connection import Database

class dbModel(object):

    def __init__(self):
        with open('src/cn/.env.yml') as f:
            env_vars = yml.full_load(stream=f)
        self.host = env_vars['PG_HOST']
        self.port = env_vars['PG_PORT']
        self.user = env_vars['PG_USER']
        self.password = env_vars['PG_PASS']
        self.database = env_vars['PG_NAME']

    def add_log(self,p_e, p_class):
        _db = None
        _id_user = 0
        _status = 1
        _i = 0
        try:
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd LOG')
            print('error :'+ p_e + 'clase: ' + p_class)
            _con_client = _db.get_client()
            _sql = """INSERT INTO main.log_error (error, class_name, date_transaction) 
                    VALUES(%s,%s,current_timestamp);"""
            _cur = _con_client.cursor()
            _cur.execute(_sql, (p_e,p_class,))
            _con_client.commit()
            _cur.close()
        except(Exception) as e:
            print('error: '+ str(e))
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion LOG")

