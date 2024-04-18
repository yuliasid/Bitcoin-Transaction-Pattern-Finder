import re
from collections import defaultdict

def find_common_patterns(transactions, min_pattern_length, max_pattern_length):
    pattern_counts = defaultdict(int)

    # Extract patterns of varying lengths within the specified range from each transaction
    for tx in transactions:
        for length in range(min_pattern_length, max_pattern_length + 1):
            for i in range(len(tx) - length + 1):
                pattern = tx[i:i+length]
                pattern_counts[pattern] += 1

    # Filter patterns that appear in all transactions
    common_patterns = {pattern: count for pattern, count in pattern_counts.items() if count == len(transactions)}

    return common_patterns

# List of transaction hex strings
transactions = [
  #insert transactions outputs that are needed to be compared (ex. Witness)
 "2828b2739e6fb7a9d633b0315abe46d14fe306d67d6c71e8f24c8d4c3eb213c826c0fc27a1acbd2bd1800eedde3968b7c461eb53adb87991558dac23b370f9e9833",
  #"",
  #"", 
  #""
 
]

# Define the minimum and maximum pattern length you are interested in
min_pattern_length = 5   #change if needed
max_pattern_length = 14  #change if needed

# Find common patterns
common_patterns = find_common_patterns(transactions, min_pattern_length, max_pattern_length)
print(common_patterns)
