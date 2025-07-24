#access groups 


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
country_total = sum (record["amount"] for record in insurance_table if record["country"] == country)
print(country_total)
    
