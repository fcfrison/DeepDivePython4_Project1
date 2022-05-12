import BankAccount
import database_package


def main():
    db_dict = {}
    fn_1 = lambda y: y.strip().split("=")
    fn_2 = lambda x: {x[0]: x[1]}
    fn_3 = lambda z: db_dict.update(z)
    with open("./_envfile.txt") as obj:
        db_config = list(map(fn_2, map(fn_1, obj)))
    list(map(fn_3, db_config))
    database_package.OracleConnectSID.set_instant_client(db_dict["INSTANT_CLIENT_DIR"])
    db_dict
    oracle = database_package.OracleConnectSID(
        db_dict["USERNAME"],
        db_dict["PASSWORD"],
        db_dict["HOST"],
        int(db_dict["PORT"]),
        db_dict["SERVICE"],
        
    )
    conta_1 = BankAccount.BankAccount(15858, "Philip", "F")
    print(conta_1.account_number)
    conta_1.complete_name()
    conta_1.set_tz(-7, "MST")
    conta_1.balance = 500000
    conta_1.add_interest_rate()
    print(conta_1.balance)
    print(conta_1.deposit(1000))


if __name__ == "__main__":
    main()
