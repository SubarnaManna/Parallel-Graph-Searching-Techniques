def generate_insert_statements(state_file_path, capital_file_path, table_name="state", state_type="State"):
    """
    Generates SQL INSERT statements from two text files: one for state names and one for capitals.

    Args:
        state_file_path (str): Path to the text file containing state names (one per line).
        capital_file_path (str): Path to the text file containing capital names (one per line).
        table_name (str, optional): The name of the table to insert into. Defaults to "state".
        state_type (str, optional): The state type. Defaults to "State".

    Returns:
        list: A list of SQL INSERT statements.  Returns an empty list on error.
    """
    insert_statements = []
    try:
        with open(state_file_path, 'r') as state_file, open(capital_file_path, 'r') as capital_file:
            state_names = [line.strip() for line in state_file]
            capitals = [line.strip() for line in capital_file]

        # Ensure both files have the same number of lines
        if len(state_names) != len(capitals):
            print("Error: State and capital files have different number of lines.")
            return []

        for state, capital in zip(state_names, capitals):
            # Escape single quotes in state and capital names
            state = state.replace("'", "''")
            capital = capital.replace("'", "''")
            insert_statement = f"INSERT INTO `{table_name}` (`state_name`, `state_type`, `capital`) VALUES ('{state}', '{state_type}', '{capital}');"
            insert_statements.append(insert_statement)
        return insert_statements

    except FileNotFoundError as e:
        print(f"Error: File not found: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def write_insert_statements_to_file(insert_statements, output_file_path="insert_statements.sql"):
    """Writes SQL INSERT statements to a file.

    Args:
        insert_statements (list): A list of SQL INSERT statements.
        output_file_path (str, optional): Path to the output SQL file. Defaults to "insert_statements.sql".
    """
    try:
        with open(output_file_path, 'w') as output_file:
            for statement in insert_statements:
                output_file.write(statement + "\n")
        print(f"INSERT statements written to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")

def main():
    """
    Main function to coordinate the process.
    """
    state_file = "Datasets_Cleaning/ut.txt"  # Replace with your state names file
    capital_file = "Datasets_Cleaning/ut_capitals.txt"  # Replace with your capital names file
    output_file = "insert_statements_union_teritory.sql" # Replace if you want a different output file name.
    table_name = "if0_38832826_logistics_network`.`state" # Include the full table name
    state_type = "Union Territory" # default

    # Create sample input files
    # with open(state_file, 'w') as f:
    #     f.write("Andhra Pradesh\nArunachal Pradesh\nAssam\nBihar")
    # with open(capital_file, 'w') as f:
    #     f.write("Hyderabad\nItanagar\nDispur\nPatna")

    insert_statements = generate_insert_statements(state_file, capital_file, table_name, state_type)
    if insert_statements: # Only write to file if statements were generated.
        write_insert_statements_to_file(insert_statements, output_file)

if __name__ == "__main__":
    main()
