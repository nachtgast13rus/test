from math import log, ceil


def number_of_monthly_payment():
    """
    Расчет срока кредита
    :return:
    """
    loan_principal = int(input("Enter the loan principal:\n"))  # Сумма кредита
    monthly_payment = int(input("Enter the monthly payment:\n"))  # Ежемесячный платеж
    loan_interest = float(input("Enter the loan interest:\n"))  # процентная ставка
    i = loan_interest / (12 * 100)  # номинальная процентная ставка
    result = ceil(log(monthly_payment / (monthly_payment - i * loan_principal), i + 1))  # срок кредита
    years = result // 12
    months = result % 12
    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")


def annuity_monthly_payment_amount():
    """
        Функция для расчета аннуитетного ежемесячного платежа
        :return:
        """
    loan_principal = int(input("Enter the loan principal:\n"))  # Сумма кредита
    number_of_periods = int(input("Enter the number of periods:\n"))  # количество платежей
    loan_interest = float(input("Enter the loan interest:\n"))  # процентная ставка
    i = loan_interest / (12 * 100)  # номинальная процентная ставка
    payment = ceil(loan_principal * ((i * (1 + i) ** number_of_periods) / ((1 + i) ** number_of_periods - 1)))
    print(f"Your monthly payment = {payment}!")


def calculate_loan_principal():
    """
    Расчет суммы кредита
    :return:
    """
    annuity_payment = float(input("Enter the annuity payment:\n"))  # Ежемесячный платеж
    number_of_periods = int(input("Enter the number of periods:\n"))  # Количество платежей
    loan_interest = float(input("Enter the loan interest:\n"))  # Процентная ставка
    i = loan_interest / (12 * 100)  # номинальная процентная ставка
    loan_principal = round(annuity_payment / ((i * (1 + i) ** number_of_periods) / ((1 + i) ** number_of_periods - 1)))
    print(f"Your loan principal = {loan_principal}!")


def main():
    print('What do you want to calculate?\n'
          'type "n" for number of monthly payments,\n'
          'type "a" for annuity monthly payment amount,\n'
          'type "p" for loan principal:')
    choice = input()
    if choice == 'n':
        number_of_monthly_payment()
    elif choice == 'a':
        annuity_monthly_payment_amount()
    elif choice == 'p':
        calculate_loan_principal()


if __name__ == "__main__":
    main()
