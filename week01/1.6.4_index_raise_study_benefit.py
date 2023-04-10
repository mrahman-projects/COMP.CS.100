"""
This program asks the user study benefit, and then it calculates
the raised benefit factored by 1.17 percent, twice.

Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""

index_raise = 1.17
study_benefit = float(input("Enter the amount of the study benefits: "))
raised_benefit = study_benefit + ((index_raise / 100) * study_benefit)
future_raised_benefit = raised_benefit + ((index_raise / 100) *
                                          raised_benefit)


print("If the index raise is " + str(index_raise) +
      " percent, the study benefit, ")
print("after a raise, would be " + str(raised_benefit) + " euros")
print("and if there was another index raise, the study")
print("benefits would be as much as " + str(future_raised_benefit) +
      " euros")
