#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:44:10 2023

@author: nebiyousamuel
"""

import math

def months_to_payoff_loan(PV, r, pmt):
    r_decimal = r / 100.0  # Convert the annual interest rate to a decimal
    n = math.log(1 - PV * r_decimal / pmt) / math.log(1 + r_decimal)
    return n

if __name__ == "__main__":
    # Input values from the console
    PV = float(input("Enter the borrowed amount (PV) in dollars: "))
    r = float(input("Enter the monthly interest rate (r) as a percentage: "))
    pmt = float(input("Enter the monthly payment (pmt) in dollars: "))

    months = months_to_payoff_loan(PV, r, pmt)
    print(f"It will take {months:.2f} months to pay off the loan.")
