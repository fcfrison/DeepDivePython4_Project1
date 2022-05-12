import sys
import cx_Oracle
import utilities

__all__ = ['OracleConnectSID', 'OracleConnectService']


class OracleConnect:
    '''
    OracleConnect(server, port, ouser, opass, service)

    Class responsible for creating database connections.
    

    Instances atributes
    ----------
    server: String
        server address
    port : String 
        port number
    ouser : String
        user name
    opass : String
        password
    service: String
        service server
    '''
    
    def __init__(self,username, password, host, port,service):
              
        self.server = host
        self.port = port
        self.ouser = username
        self.opass = password
        self.service = service 
        self.cursor, self.connection = self.engine_cxOracle(5000)  
    


    def engine_cxOracle(self):
        '''
        engine_cxOracle()

        This method's purpose is to create a connection with the Oracle database.

        '''
        
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}(server={self.server}, '+ \
            f'port={self.port}, user={self.ouser}, service={self.service})'
    
    @classmethod
    def set_instant_client(cls, instant_client_dir:str=None)->None:
        '''
        Class method that informs to the package cx_Oracle the directory 
        where it's located the Instant Client driver.


        Parameters
        ----------
        instant_client_dir: String
            Directory where it's located the Instant Client driver

        '''
        if instant_client_dir:
            try:
                if sys.platform.startswith("win") and instant_client_dir is not None:
                    cls.instant_client = cx_Oracle.init_oracle_client(lib_dir=instant_client_dir)
            except Exception as err:
                utilities.record_error(err)
                sys.exit()
        else:
            raise ValueError("Error: instant_client_dir==None")

    def __repr__(self):
        return f'{self.__class__.__name__}(server={self.server}, '+ \
            f'port={self.port}, user={self.ouser}, service={self.service})'

class OracleConnectSID(OracleConnect):
    '''
    Class whose purpose is to create database connections when the SID 
    (and not the service) is setted.
    '''
    def engine_cxOracle(self,n_rows=5000):
        '''
        engine_cxOracle(n_rows=5000)

        This method's purpose is to create a connection with the Oracle database.

        Parameters
        ----------

        n_rows: int
            Number of rows stored on buffer at each round trip.
    
        Return
        ----------
        cursor: cx_Oracle.connect().cursor()
            cx_Oracle object that opens a database connection.

        '''
        
        dsn = cx_Oracle.makedsn(self.server, self.port, self.service)
        connection_cxOracle = cx_Oracle.connect(dsn=dsn,user=self.ouser, \
                                        password=self.opass, encoding="UTF-8")
        cursor=connection_cxOracle.cursor()
        cursor.arraysize = n_rows 
        return cursor, connection_cxOracle

class OracleConnectService(OracleConnect):
    '''
    Class whose purpose is to create database connections when the service 
    (and not the SID) is setted.
    '''

    def engine_cxOracle(self,n_rows=5000):
        '''
        engine_cxOracle(n_rows=5000)

        This method's purpose is to create a connection with the Oracle database.

        Parameters
        ----------

        n_rows: int
            Number of rows stored on buffer at each round trip.
    
        Return
        ----------
        cursor: cx_Oracle.connect().cursor()
            cx_Oracle object that opens a database connection.

        '''
        
        dsn = cx_Oracle.makedsn(self.server, self.port, service_name=self.service)
        connection_cxOracle = cx_Oracle.connect(dsn=dsn,user=self.ouser, \
                                        password=self.opass, encoding="UTF-8")
        cursor=connection_cxOracle.cursor()
        cursor.arraysize = n_rows 
        return cursor, connection_cxOracle

 