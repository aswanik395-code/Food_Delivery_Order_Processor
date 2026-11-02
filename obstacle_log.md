# Obstacle Log – Food Delivery Order Processor

### 1. Invalid Menu Items
**Problem:** Orders containing items not available in the menu caused errors.

**Solution:** Used conditions to check whether each item exists in the menu before calculating the total.

### 2. Empty Orders
**Problem:** Empty orders could result in incorrect billing.

**Solution:** Added a condition to identify and reject empty orders.

### 3. Discount Calculation
**Problem:** Calculating discounts for different order values required additional conditions.

**Solution:** Created a separate function to apply a 10% discount when the order total is Rs. 500 or above.

### 4. Highest-Value Order
**Problem:** Identifying the highest-value order among multiple orders.

**Solution:** Compared the final bill amounts and stored the order with the highest value.

### 5. Saving Sales Records
**Problem:** Sales information needed to be preserved after program execution.

**Solution:** Used Python file handling to generate and save the daily sales report in a text file.