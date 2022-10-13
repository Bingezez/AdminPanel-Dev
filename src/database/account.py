from .db import ConnectionMongoDb


class AccountDb(ConnectionMongoDb):
    name_colection = "accounts"
    def __init__(self):
        ConnectionMongoDb.__init__(self)
        
    @property
    def collection(self):
        return self._db[self.name_colection]

    
    def is_account(self, find_by_token: str, find_by_account_telegram_info: str) -> bool:
        user = {
            "accountTelegramInfo": find_by_account_telegram_info,
            "accountToken": find_by_token
            }
        if self.collection.find_one(user) is not None:
            return True
        return False
    

    def get_code(self, find_by_token: str, find_by_account_telegram_info: str) -> int:
        user = {
            "accountTelegramInfo": find_by_account_telegram_info,
            "accountToken": find_by_token
            }
        return self.collection.find_one(user)['accountVerifiedDigitCode']


    def is_code(self, find_by_token: str, find_by_account_telegram_info: str) -> bool:
        user = {
            "accountTelegramInfo": find_by_account_telegram_info,
            "accountToken": find_by_token
            }
        if self.collection.find_one(user)['accountVerifiedDigitCode'] == 0:
            return True
        return False
        
    
    def update_account(self, find_by_token: str, find_by_account_telegram_info: str, gen_code: int):
        find = {
            "accountTelegramInfo": find_by_account_telegram_info,
            "accountToken": find_by_token
            }
        update_code = {"$set": {"accountVerifiedDigitCode": gen_code}}    
        self.collection.update_one(find, update_code, upsert=True)
    

if __name__ == '__main__':
    test = AccountDb()
    print(test.is_account('506564ace706feef525b512d6ceb955b', '1234'))
    print(test.is_account('506564ace706feef525b512d6ceb955b', '123'))
    # print(result)