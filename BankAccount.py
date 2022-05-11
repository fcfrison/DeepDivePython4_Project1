import datetime

class BankAccount:

    def __init__(self, value:int, first_name:str, last_name:str)->None:
        self.account_number = value
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def account_number(self):
        return self._account_number
    @account_number.setter
    def account_number(self, value:int):
        if isinstance(value,int) and value>=0:
            self._account_number = value
        else:
            raise ValueError("The value must be a positive integer.")

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self,name:str):
        if isinstance(name,str) and not any(map(str.isdigit, name)):
            self._first_name = name
        else:
            raise ValueError("Error: only not numeric strings are allowed.")
    
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self,last_name:str):
        if isinstance(last_name,str) and not any(map(str.isdigit, last_name)):
            self._last_name = last_name
        else:
            raise ValueError("Error: only not numeric strings are allowed.")
    
    def complete_name(self):
        return self.first_name + ' ' + self.last_name
    
    @property
    def balance(self)->None:
        return self._balance
    @balance.setter
    def balance(self,value:float=0)->None:
        if(isinstance(value, (int,float)) and value>=0):
            self._balance = value
        else:
            raise ValueError("Error: the value must be a positive integer.")
    
    def deposit(self, value:float):
        if(isinstance(value, (int,float)) and value>=0):
            self.balance +=value
            self.set_control_number()
            return self.gen_confirmation_number('D')
        else:
            raise ValueError("Error: the value must be a positive integer.")
    
    def withdrawals(self, value:float):
        if(isinstance(value, (int,float)) and value>=0 and value-self.balance>=0):
            self.balance-=value
            return self.gen_confirmation_number('W')
        else:
            return "Error: the amount withdrawn is too high."

    @classmethod
    def get_tz(cls):
        if('tz' not in BankAccount.__dict__):
            # Declarando o timezone da classe. 
            cls.tz = datetime.timezone.utc
            return cls.tz
    @classmethod
    def set_tz(cls, offset, name):
        '''
        Class method 'set_tz'.
        '''
        cls.tz = datetime.timezone(datetime.timedelta(hours=offset), name)
    
    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate
    @classmethod
    def set_interest_rate(cls, value:float=0.01):
        if(isinstance(value, (int,float)) and value>=0 and value<=1):
            cls._interest_rate = value
        else:
            raise ValueError("Error: the value must be positive and in the range [0,1].")
    
    def add_interest_rate(self):
        if('_interest_rate' not in BankAccount.__dict__):
            self.set_interest_rate()
        self.balance +=self.balance*self.get_interest_rate()
        return self.gen_confirmation_number('I')
    
    @classmethod
    def set_control_number(cls):
        if('_control_number' not in BankAccount.__dict__):
            cls._control_number = 0
        cls._control_number+=1
    
    @classmethod
    def get_control_number(cls):
        if('_control_number' not in BankAccount.__dict__):
            cls._control_number = 0
        return cls._control_number

    @staticmethod
    def current_dt_utc():
        return datetime.datetime.now(datetime.timezone.utc)

    def gen_confirmation_number(self, type_transaction:str):
        conf_number = type_transaction + str(self.account_number) + \
        str(self.current_dt_utc()) + str(self.get_control_number()) 
        return conf_number
        
