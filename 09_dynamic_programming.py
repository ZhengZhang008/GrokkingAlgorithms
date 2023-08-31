if __name__ == "__main__":
    # Initialize the strings to be compared
    dp_table_blue = ["b", "l", "u", "e"]
    dp_table_clues = ["c", "l", "u", "e", "s"]

    # Initialize the dynamic programming table with zeros
    dp_table = [[0 for i in range(len(dp_table_blue))] for i in range(len(dp_table_clues))]  # (5,4)
    print(dp_table)

    # Iterate over the strings and fill the dynamic programming table
    for i in range(0, len(dp_table_blue)):
        for j in range(0, len(dp_table_clues)):
            # If the characters match, increment the value in the table
            if dp_table_clues[j] == dp_table_blue[i]:
                dp_table[j][i] = dp_table[j - 1][i - 1] + 1
            else:
                # If the characters don't match, take the maximum value from the adjacent cells
                dp_table[j][i] = max(dp_table[j - 1][i], dp_table[j][i - 1])

    print(dp_table)

