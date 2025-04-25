





file_name = "Datasets_Cleaning/st.txt"


def read_and_print_lines(file_path):
  """Reads a text file and prints each line.

  Args:
    file_path: The path to the text file.
  """
  try:
    with open(file_path, 'r') as file:
      for line in file:
        print(line, end='')  # Print each line, keeping the original newline
  except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'")
  except Exception as e:
    print(f"An error occurred: {e}")

# Example usage:
# file_name = "my_text_file.txt"  # Replace with the actual path to your file

# # Create a sample text file for demonstration
# with open(file_name, 'w') as f:
#   f.write("This is the first line.\n")
#   f.write("And this is the second line.\n")
#   f.write("Finally, the third line.\n")

read_and_print_lines(file_name)