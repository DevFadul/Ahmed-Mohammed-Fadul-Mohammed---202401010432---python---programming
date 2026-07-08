Bug Found in main.py

The original main.py had an incomplete import statement and did not call the food_order() function correctly to calculate the total payment.

Fixes Made:
1. Imported the food_order function correctly.
2. Called food_order(price, quantity) to calculate the total.
3. Added handling for invalid price and invalid quantity.
4. Displayed the total payment in RM with two decimal places.