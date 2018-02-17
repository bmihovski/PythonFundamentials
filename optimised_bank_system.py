from operator import attrgetter

"""
Create a class BankAccount which has a Name (string), Bank (string) and Balance (decimal).
You will receive several input lines, containing information in the following way:
{bank} | {accountName} | {accountBalance}
You need to store every given Account. When you receive the command "end" you must stop the input sequence.
Then you must print all Accounts, ordered by their balance, in descending order, and then by length of the bank name,
in ascending order.
The accounts must be printed in the following way "{accountName} -> {balance} ({bank})".
Note: Numbers must be printed rounded to the 2nd decimal digit.

Examples:

Input
DSK | Ivan | 504.403
DSK | Pesho | 2000.4031
DSK | Aleksander | 20000.0001
Piraeus | Ivan | 504.403
Piraeus | Aleksander | 20000.0001
end

Output
Aleksander -> 20000.00 (DSK)
Aleksander -> 20000.00 (Piraeus)
Pesho -> 2000.40 (DSK)
Ivan -> 504.40 (DSK)
Ivan -> 504.40 (Piraeus)
"""


class BankAccount:
    def __init__(self, account_name, account_bal, bank):
        """
        Instantiates bank account data
        :param account_name: (Str) Account holder name
        :param account_bal: (Str) Account balance
        :param bank: (Str) Bank which is serving the account
        """
        self.account_name = account_name
        self.account_bal = float(account_bal)
        self.bank = bank

    def __str__(self):
        """
        Constructs text record for account data
        :return:
        """
        bank_record_stdout = f'{self.account_name} -> {self.account_bal:.2f} ({self.bank})'
        return bank_record_stdout


bank_records = list()
inputs_text = list()

while True:
    inputs_text = input().split(' | ')
    if 'end' in inputs_text:
        break
    bank_records.append(BankAccount(account_name=inputs_text[1], account_bal=inputs_text[2], bank=inputs_text[0]))

[print(bank_record) for bank_record in sorted(sorted(bank_records, key=attrgetter('bank')),
                                              key=attrgetter('account_bal'), reverse=True)]
