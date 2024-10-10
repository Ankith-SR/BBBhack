import time
import statistics
import concurrent.futures
import random

# Simulated server check (for demo purposes)
def check_pin(pin):
    correct_pin = "123432"  # The real PIN (in a real case, this would be unknown)
    base_response_time = 0.1  # Base response time for incorrect PINs
    correct_digit_delay = 0.2  # Additional delay for correct digits

    # Simulate a more significant delay for each correct digit
    for i in range(len(pin)):
        if pin[i] == correct_pin[i]:
            base_response_time += correct_digit_delay

    # Add a small random noise to simulate network variations
    noise = random.uniform(-0.01, 0.01)
    final_response_time = base_response_time + noise

    # Simulate server delay
    time.sleep(final_response_time)
    return final_response_time

def get_avg_response(pin, repeats=3):
    """Run the check_pin function multiple times and return the average response time."""
    times = []
    for _ in range(repeats):
        start_time = time.time()
        check_pin(pin)
        times.append(time.time() - start_time)
    return statistics.mean(times)

def try_digit_for_position(pin, position, digit, repeats=3):
    """Check the average response time for a specific digit in a specific position."""
    test_pin = pin.copy()
    test_pin[position] = str(digit)  # Convert digit to string
    avg_time = get_avg_response(''.join(map(str, test_pin)), repeats=repeats)  # Fix here: map digits to strings
    return digit, avg_time

def find_best_digit_for_position(pin, position, repeats=3):
    """Try digits 0-9 for a specific position in parallel and return the one with the longest average time."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Create a task for each digit and run them all in parallel
        futures = {executor.submit(try_digit_for_position, pin, position, digit, repeats): digit for digit in range(10)}
        
        # Collect all results and determine the best digit
        results = {future.result()[0]: future.result()[1] for future in concurrent.futures.as_completed(futures)}
    
    best_digit = max(results, key=results.get)  # Pick the digit with the longest response time
    longest_time = results[best_digit]
    
    print(f"Best digit for position {position + 1}: {best_digit}, longest time: {longest_time:.4f}s\n")
    return best_digit

def crack_pin():
    pin = ['0'] * 6  # Start with '000000'

    # For each digit in the 6-digit PIN
    for i in range(6):
        print(f"Cracking digit {i+1}...")
        best_digit = find_best_digit_for_position(pin, i)
        pin[i] = str(best_digit)  # Make sure the digit is a string
        #print(f"Best digit for position {i+1}: {best_digit}")

    cracked_pin = ''.join(pin)  # Join as strings
    print(f"Cracked PIN: {cracked_pin}")


# Run the attack
crack_pin()
