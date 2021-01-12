# Day 13

Today's lesson is on debugging

- describe the issue - make sure you understand what is supposed to happen, and what is actually happening
- reproduce the issue -if the error is intermittent figure out what condition cuases it consistently
- "play computer" - look at each line of code evaluate the expected result
- fix errors in traceback error messages
- use print statements to check variables
- use a debugger
  - thonny
  - pythontutor.com
- take a break, sometimes walking away will make bug become clear
- ask a friend - fresh eyes often help
- run code often in small iterations, less code to debug if bug occurs
- stackoverflow....

# exercises

- 13-1 debugging odd or even
  - `if number % 2 = 0:` should be `==`
- 13-2 debugging leap year
  - `year = input("Which year do you want to check?")` needs to be converted to int
- 13-3 debugging FizzBuzz
  - ` if number % 3 == 0 or number % 5 == 0:` should be and not or
  - `if number % 3 == 0:` and `if number % 5 == 0:` should be elif
  - `print([number])` should not have `[]` around number
