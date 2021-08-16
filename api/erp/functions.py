# The functions below has the main purpose check the customers documents
# The customers documents are based on CPF
def check_cpf_digits(customer_document):
    """
    This function will check length caracter qty of customer document number.
    If customers document number different from 11 caracters, 
    the fuction will return False.
    Args:
        customer_document(str): That information will be provide by API database 
    """
    if len(customer_document) == 11:
        return True
    else:
        return False


def check_cpf_isvalid(customer_document):
    """
    This algorithm provide a smart solution to check the last 2 numbers 
    of customers document and validate if are correct or not. 
    customers document_example = 168.995.350-09
    ------------------------------------------------
    1 * 10 = 10           #    1 * 11 = 11 <-
    6 * 9  = 54           #    6 * 10 = 60
    8 * 8  = 64           #    8 *  9 = 72
    9 * 7  = 63           #    9 *  8 = 72
    9 * 6  = 54           #    9 *  7 = 63
    5 * 5  = 25           #    5 *  6 = 30
    3 * 4  = 12           #    3 *  5 = 15
    5 * 3  = 15           #    5 *  4 = 20
    0 * 2  = 0            #    0 *  3 = 0
                          # -> 0 *  2 = 0
            297           #            343
    11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
    11 > 9 = 0            #
    Digit 1 = 0           #   Digit 2 = 9 
    ------------------------------------------------
    Args:
        customer_document(str): That information will be provide by API database 
    """
    new_customer_document = customer_document[:-2]
    reverse = 10
    sumatory_total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        sumatory_total += int(new_customer_document[index])

        reverse -= 1
        if reverse < 2:
            reverse = 11
            digit = 11 - (sumatory_total % 11)

            if digit > 9:
                digit = 0
            sumatory_total = 0
            new_customer_document += str(digit)

    if customer_document == new_customer_document:
        return True
    else:
        return False


# The function below has the main purpose check if date is valid
