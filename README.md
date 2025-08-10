# AMEX_amazon_spender

This Python script helps you find the **best combination of purchase amounts** (e.g., Amazon transactions) that come closest to a given **target amount**, without exceeding it.  
It’s particularly useful if you want to **maximize AMEX Membership Rewards point redemption** when Amazon offers a discount for using points on eligible purchases.

---

## 📌 Features
- **Dynamic Programming Approach**: Uses a subset-sum DP algorithm to find the optimal combination of transactions.
- **Precision Handling**: Works with floating-point amounts by converting them to integers internally for accuracy.
- **Customizable Target**: You can easily change the target redemption amount.
- **Guaranteed Best Fit**: Always returns the subset whose total is closest to (and ≤) the target.

---

## 📂 File Structure
best_AMEX_points_spend_Amazon.py # Main script

---

## ⚙️ How It Works
The script:
1. Converts all transaction amounts into integers based on the desired decimal precision.
2. Iteratively builds combinations of transactions using dynamic programming.
3. Selects the **largest sum ≤ target** and returns the corresponding transactions.

Example:
```python
amounts = [
    845.37, 297.00, 927.00, 297.00, 837.00, 692.70, 598.00,
    927.00, 299.85, 177.00, 129.98, 259.96, 169.98, 177.00,
    44.99, 29.98, 51.97
]
target = 1066.13

best_subset = best_subset_sum_dp(amounts, target)
print("Best subset:", best_subset)
print("Sum:", round(sum(best_subset), 2))
```
## 💻 Usage
Run in terminal:
python best_AMEX_points_spend_Amazon.py

🔧 Customization
1. Change amounts to your own list of transaction totals.
2. Modify target to the desired maximum spend.
3. Adjust precision in best_subset_sum_dp() if you need more decimal accuracy.

## 📊 Example Output
Best subset: [845.37, 297.00]
Sum: 1142.37


