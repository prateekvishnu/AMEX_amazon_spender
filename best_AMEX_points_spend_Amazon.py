
# Online Python - IDE, Editor, Compiler, Interpreter

def best_subset_sum_dp(nums, target, precision=2):
    factor = 10 ** precision
    int_nums = [int(round(num * factor)) for num in nums]
    int_target = int(round(target * factor))

    dp = {0: []}  # maps integer sum → subset in original floats

    for i, num in enumerate(int_nums):
        new_dp = dp.copy()
        for s in dp:
            new_sum = s + num
            if new_sum <= int_target and new_sum not in new_dp:
                new_dp[new_sum] = dp[s] + [nums[i]]  # Use original float
        dp = new_dp

    for total in range(int_target, -1, -1):
        if total in dp:
            return dp[total]

    return []

# Inputs
amounts = [
  845.37,
  297.00,
  927.00,
  297.00,
  837.00,
  692.70,
  598.00,
  927.00,
  299.85,
  177.00,
  129.98,
  259.96,
  169.98,
  177.00,
  44.99,
  29.98,
  51.97
]
target = 1066.13

# Run
best_subset = best_subset_sum_dp(amounts, target)
print("Best subset:", best_subset)
print("Sum:", round(sum(best_subset), 2))