from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calculate_amortization_schedule(start_date, interest_rate, term_years, loan_amount):
    # Convert interest rate from percentage to decimal
    interest_rate_decimal = interest_rate / 100.0
    
    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate_decimal / 12.0
    
    # Calculate number of monthly payments
    num_payments = term_years * 12
    
    # Calculate monthly payment amount
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
    
    # Initialize variables
    remaining_balance = loan_amount
    amortization_schedule = []
    
    for payment_number in range(1, num_payments + 1):
        # Calculate interest for the current payment
        interest_payment = remaining_balance * monthly_interest_rate
        
        # Calculate principal payment for the current payment
        principal_payment = monthly_payment - interest_payment
        
        # Update remaining balance
        remaining_balance -= principal_payment
        
        # Create a dictionary representing the current payment
        payment_details = {
            "Payment Number": payment_number,
            "Payment Date": start_date.strftime('%Y-%m-%d'),
            "Payment Amount": monthly_payment,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Remaining Balance": remaining_balance
        }
        
        # Append the payment details to the amortization schedule
        amortization_schedule.append(payment_details)
        
        # Increment the start date by one month
        start_date += relativedelta(months=1)
    
    return amortization_schedule

# Set loan details
start_date_str = input("Enter the start date (YYYY-MM-DD): ")
interest_rate = float(input("Enter the interest rate (%): "))
term_years = int(input("Enter the term in years: "))
loan_amount = float(input("Enter the loan amount: "))

#start_date_str = "2023-05-21"
start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
#interest_rate = 3.5  # in %
#term_years = 30  # in years
#loan_amount = 200000.0  # loan amount in dollars

# Calculate the amortization schedule
amortization_schedule = calculate_amortization_schedule(start_date, interest_rate, term_years, loan_amount)

# Print out the first few rows of the amortization schedule
print("Amortization Schedule (first few rows):")
for row in amortization_schedule[:100]:
    print(row)
