import time
import statistics

# Simulated server check (for demo purposes)
def check_pin(pin):
    correct_pin = "345627"  # The real PIN (in a real case, this would be unknown)
    response_time = 0.1  # Base response time for incorrect PINs

    # Simulate a more significant delay for each correct digit
    for i in range(len(pin)):
        if pin[i] == correct_pin[i]:
            response_time += 0.2  # Increase the delay for each correct digit
    
    # Simulate server delay
    time.sleep(response_time)
    return response_time

def get_avg_response(pin, repeats=3):
    """Run the check_pin function multiple times and return the average response time."""
    times = []
    for _ in range(repeats):
        start_time = time.time()
        check_pin(pin)
        times.append(time.time() - start_time)
    return statistics.mean(times)

def find_best_digit_for_position(pin, position, repeats=3):
    """Try digits 0-9 for a specific position and return the one with the longest average time."""
    best_digit = '0'
    longest_time = 0

    for digit in range(10):
        test_pin = pin.copy()
        test_pin[position] = str(digit)
        test_pin_str = ''.join(test_pin)

        # Get average response time for multiple attempts
        avg_time = get_avg_response(test_pin_str, repeats=repeats)
        print(f"Trying {test_pin_str}, avg response time: {avg_time:.4f}s")

        # Check if this response time is longer
        if avg_time > longest_time:
            longest_time = avg_time
            best_digit = str(digit)

    print(f"Best digit for position {position + 1}: {best_digit}, longest time: {longest_time:.4f}s\n")
    return best_digit

def crack_pin():
    pin = ['0'] * 6  # Start with '000000'

    # For each digit in the 6-digit PIN
    for i in range(6):
        print(f"Cracking digit {i+1}...")
        best_digit = find_best_digit_for_position(pin, i)
        pin[i] = best_digit
        print(f"Best digit for position {i+1}: {best_digit}")

    cracked_pin = ''.join(pin)
    print(f"Cracked PIN: {cracked_pin}")

# Run the attack
crack_pin()
