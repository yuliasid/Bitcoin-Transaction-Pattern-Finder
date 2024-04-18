# Bitcoin-Transaction-Pattern-Finder

This Python script is designed to analyze hexadecimal strings of Bitcoin transactions to find common substring patterns. It's particularly useful for identifying recurring sequences that could be indicative of specific transaction behaviors or properties. These patterns can then be employed to query transaction data using regular expressions.

## Features
*Pattern Extraction:* Extracts all possible substrings within a defined length range from each transaction.
Pattern Analysis: Identifies and counts the frequency of each pattern across a list of transactions.
Common Patterns Identification: Filters and displays patterns that appear in all provided transactions.

## Requirements
Python 3.6 or newer


## Installation
No additional installation is required beyond the standard Python libraries. Ensure you have Python installed on your system. You can download it from python.org.

## Usage
- Prepare your data: You'll need a list of transaction hex strings that you want to analyze.
- Set pattern length range: Define the minimum and maximum lengths of patterns you are interested in.
- Run the script: Execute the script to find patterns common to all listed transactions.
