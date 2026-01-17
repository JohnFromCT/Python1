"""
Assignment 6

Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
==============================================
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.

"""

# variable definitions
t_currency = (("AUD (A$)", 1.4964), ("EUR (€)", 0.8587), ("GBP (£)", 0.7440), ("JPY (¥)", 158.42), ("USD ($)", 1.00))
# current choices: Australian Dollar, Euro, British Pound, Japanese Yen, US Dollar
# [0] is the list of currencies
# [1] is the list of exchange rates versus the US Dollar, revised 1/16/26

# inputs
print("List of available currencies to convert:")
for int_index, str_currency in enumerate(t_currency):  # populates index and currency variables from tuple
    print(int_index + 1, str_currency[0])  # shows index number (+1 because starts at 0) and each item
print("Choose currency to convert from ( 1 -", len(t_currency), ")")  # set to allow for different number of currencies
int_sel_from = int(input())  # requesting user to select
if int_sel_from <= 0 or int_sel_from > len(t_currency):  # ab-ends if user input is not within available range
    print("Please select within the index listed above!")
    exit(1)
print("Convert from", t_currency[int_sel_from - 1][0])  # displays choice already made
print("Choose currency to convert to ( 1 -", len(t_currency), ")")  # set to allow for different number of currencies
int_sel_to = int(input())  # requesting user to select
if int_sel_to <= 0 or int_sel_to > len(t_currency):  # ab-ends if user input is not within available range
    print("Please select within the index listed above!")
    exit(1)
print("Convert from", t_currency[int_sel_from - 1][0], "to",
      t_currency[int_sel_to - 1][0])  # displays chosen conversion
print("Enter amount in", t_currency[int_sel_from - 1][0], ":")  # prompts to enter amount of currency to be converted
flt_amount = float(input())

# processing
# new currency payout = exchange rate of new currency / exchange rate of old currency * amount of old currency
flt_exchange = (t_currency[int_sel_to - 1][1] / t_currency[int_sel_from - 1][1]) * flt_amount

# output
# displays start and end amount
print(flt_amount, t_currency[int_sel_from - 1][0], "=", flt_exchange, t_currency[int_sel_to - 1][0])
