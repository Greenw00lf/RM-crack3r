import pandas as pd
import RM2

def remove_first_n_digits(number, n):
    return str(number)[n:]

def remove_specific_number(number_list, specific_number):
    return [num for num in number_list if num != specific_number]

def main():
    print(RM2.banner())  # Print the banner from RM2
    # Read the Excel file
    file_path = input("Enter the path to the Excel file: ")
    df = pd.read_excel(file_path)

    # Remove the first n digits from each number
    n = int(input("Enter the number of digits to remove from the beginning of each number: "))
    df['Mobile Number'] = df['Mobile Number'].apply(remove_first_n_digits, args=(n,))

    # Remove a specific number if desired
    remove_specific = input("Do you want to remove a specific number? (yes/no): ").lower()
    if remove_specific == "yes":
        specific_number = input("Enter the specific number to remove: ")
        df['Mobile Number'] = remove_specific_number(df['Mobile Number'].tolist(), specific_number)

    # Save the modified data back to CSV
    output_file_path = input("Enter the path to save the modified CSV file: ")
    df.to_csv(output_file_path, index=False)
    print("Modified mobile numbers saved to", output_file_path)

if __name__ == "__main__":
    main()
