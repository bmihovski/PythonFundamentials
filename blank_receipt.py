"""
Create a function that prints a blank cash receipt. The function should invoke three other functions: one for printing the header, one for the body and one for the footer of the receipt.
"""
RECEIPT_HEADER_TEXT = "CASH RECEIPT"
RECEIPT_HEADER_AND_BOTTOM_DELIMITER = "------------------------------"
RECEIPT_BODY_TOP_TEXT = "Charged to____________________"
RECEIPT_BODY_BOTTOM_TEXT = "Received by___________________"
RECEIPT_FOOTER_TEXT = "© SoftUni"

def print_receipt_header():
    """
    Prints receipt header part
    :return:
    None
    """
    for i in [RECEIPT_HEADER_TEXT, RECEIPT_HEADER_AND_BOTTOM_DELIMITER]:
        print(i)

def print_receipt_body():
    """
    Prints receipt body part
    :return:
    None
    """
    for i in [RECEIPT_BODY_TOP_TEXT, RECEIPT_BODY_BOTTOM_TEXT,
              RECEIPT_HEADER_AND_BOTTOM_DELIMITER]:
        print(i)

def print_receipt_footer():
    """
    Prints receipt footer part
    :return:
    None
    """
    print(RECEIPT_FOOTER_TEXT)

def print_full_reciept():
    """
    Print full receipt
    :return:
    None
    """
    print_receipt_header()
    print_receipt_body()
    print_receipt_footer()


print_full_reciept()
