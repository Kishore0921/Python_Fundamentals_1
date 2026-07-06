# "while loops" are used to execute a block of code as long as a specified condition is true.

# Runs continuously as long as the given condition evaluates to True
is_running = True
while is_running:
    print("Running once!")
    is_running = False  # Changes condition to False to stop the loop

# Uses a variable to keep count and control how many times the loop runs
count = 1
while count <= 3:
    print(count)
    count += 1  # Increments counter by 1 to eventually exit the loop

# Keeps asking the user for input until they type a specific exit keyword
user_choice = ""
while user_choice.lower() != "quit":
    # Emulating user input for safety in non-interactive environments
    user_choice = "quit"  # Change this string to test logic
    print("Action processed.")

# Forces an immediate exit from a while loop
timer = 5
while timer > 0:
    if timer == 3:
        break  # Stops the countdown early at 3
    print(timer)
    timer -= 1

# Skips code below it and jumps straight back up to the condition check
num = 0
while num < 4:
    num += 1
    if num == 2:
        continue  # Skips printing 2
    print(num)  # Prints 1, 3, 4

# Empty placeholder block for a while loop statement
condition = False
while condition:
    pass  # Keeps structure valid until code is added

# The else block executes when the condition becomes False, unless broken by a break
count = 0
while count < 2:
    print(count)
    count += 1
else:
    print("Count reached maximum, while-else triggered!")

