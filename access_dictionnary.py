#access different groups within a dictionnary


def  access_dictionnary_country(country:str, insurance_table:list) -> int:
    """ One liner function used to access the list of dictionnaries
    Args:
        country(str): country of the insurance company
        insurance(str): insurance issuer company
        insurance_table(list): List of dictionnaries that contains insurance per country and 
        insurrance issuer
    Return: 
        (int): return the amount of insurance for a specific country or insurance 

    """
    country_total = sum (record["amount"] for record in insurance_table if record["country"] == country)
    return country_total

def  access_dictionnary_insurance(insurance:str, insurance_table:list) -> int:
    """ One liner function used to access the list of dictionnaries
    Args:
            country(str): country of the insurance company
            insurance(str): insurance issuer company
            insurance_table(list): List of dictionnaries that contains insurance per country and 
            insurrance issuer
    Return: 
            (int): return the amount of insurance for a specific country or insurance 

    """
    insurance_total = sum (record["amount"] for record in insurance_table if record["insurance"] == insurance)
    return insurance_total


if __name__ == "__main__":
    insurance_table = [

    {
        "country" : "Slovakia",
        "insurance" : "BMZ",
        "amount" : 1000
    },
    {
        "country" : "Slovakia",
        "insurance" : "BMZ",
        "amount" : 1000
    },
    {
        "country" : "Slovakia",
        "insurance" : "BMZ",
        "amount" : 1000
    },
    {
        "country" : "Slovakia",
        "insurance" : "BMZ",
        "amount" : 1000
    },
    {
        "country" : "Slovakia",
        "insurance" : "BMZ",
        "amount" : 1000
    },
    {
        "country" : "Italia",
        "insurance" : "BMZ",
        "amount" : 2000
    },
    {
        "country" : "Germany",
        "insurance" : "BMZ",
        "amount" : 2000
    }
                    ]



    # one liner solution
    country = "Slovakia"
    print(access_dictionnary_country(country,insurance_table))


    # one liner solution
    insurance = "BMZ"
    print(access_dictionnary_insurance(insurance,insurance_table))
