# BBBhack
# Timing Attack Simulation

## Overview
In this project, we focus on improving the process of cracking a 6-digit PIN using a **timing attack**. Rather than relying on a brute force attack, we use **adaptive timing feedback** to more efficiently determine each digit of the PIN.

## How It Works
For instance, let’s assume the correct PIN is `"123456"`. If we input the wrong PIN, say `"111111"`, we compare the response time. Let’s define:

- `x`: Time the device takes to reject the wrong guess
- `y`: Time the device takes to accept the correct PIN

Instead of just comparing the total times for the full guess, we break the attack down by each digit position.

### Incremental Testing
We input guesses like:

- `"122222"`
- `"123333"`

For each input, we measure how long it takes the device to reject the guess at specific digit positions.

### Key Insight
If the first few digits are correct, the system might take slightly longer to reject the guess. This gives us a clue about the correct digits. By analyzing these subtle timing differences for each position, we can determine the correct PIN more efficiently.

### Why It’s Better
This approach is far more optimal than brute forcing the entire PIN. Instead of trying every possible combination, we focus on exploiting the timing feedback for each digit, significantly speeding up the process.

## Conclusion
By using this adaptive timing attack, we’re able to reduce the time and effort required to crack the PIN compared to traditional brute force methods.
