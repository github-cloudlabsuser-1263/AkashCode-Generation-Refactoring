# A program that sums user-provided integers with basic error handling

MAX_ELEMENTS = 100

def calculate_sum(arr):
   result = 0
   for num in arr:
      result += num
   return result

def main():
   try:
      n = int(input("Enter the number of elements to sum (between 1 and 100): "))
      if not 1 <= n <= MAX_ELEMENTS:
            print("Invalid input. Please enter a number between 1 and 100.")
            return

      arr = []

      print(f"Enter {n} integers:")
      for _ in range(n):
            try:
               arr.append(int(input("Enter an integer: ")))
            except ValueError:
               print("Invalid input. Please enter valid integers.")
               return

      total = calculate_sum(arr)

      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")
      exit(1)

if __name__ == "__main__":
   main()
