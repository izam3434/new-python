class NegativeNumberError(Exception):
    def __init__(self, number):
        super().__init__(f"Negative number found: {number}")
        self.number = number

def process_numbers(file_name):
    try:
        infile = open(file_name, 'r')
        total = 0
        for line in infile:
            number = float(line.strip())
            if number < 0:
                raise NegativeNumberError(number)
            total += number
        print(f"Total of all numbers: {total}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except ValueError:
        print("Error: The file contains invalid (non-numeric) data.")
    except NegativeNumberError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        try:
            infile.close()
            print("File closed.")
        except NameError:
            print("File was never opened , nothing to close.")

file_name = "numbers.txt"
process_numbers(file_name)