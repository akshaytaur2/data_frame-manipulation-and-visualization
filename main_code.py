#importing libraries
import pandas as pd
import matplotlib.pyplot as plot

MAIN_MENU = '''Please choose from the following options:
 1. Load data from a file
 2. View data
 3. Clean data
 4. Analyse data
 5. Visualise data
 6. Save data to a file 
 7. Quit'''

def a2_main():
    sample_data = pd.DataFrame()

    print("Welcome to The DataFrame Statistician! ")
    print("Programmed by Saurrabh Sharma")
    print(MAIN_MENU)

    menu_choice = input(">>> ")
    while menu_choice != '7':
        if menu_choice == '1':
            sample_data = load_data(sample_data)
        elif menu_choice == '2':
            if sample_data.shape[0]>0:
                print(sample_data)
            else:
                print("No data to display")
        elif menu_choice == '3':
            clean_data(sample_data)
        elif menu_choice == '4':
            analyze_data(sample_data)
        elif menu_choice == '5':
            visualise_data(sample_data)
        elif menu_choice == '6':
            save_file(sample_data)
        else:
            print("Invalid selection!")
        print(MAIN_MENU)
        menu_choice = input(">>> ")
    print("Goodbye")

def load_data(csv_input):
    file_name = input("Enter The filename: ")
    try:
        if file_name.lower().endswith(".csv"):
            csv_input = pd.read_csv(file_name)
            print("Data has been loaded Successfully.")
            print("""Which column do you want to set as index? (leave blank for none)
            day
            min_temp
            max_temp
            rainfall
            humidity""")
            user_index = input(">>> ")
            if user_index and user_index in csv_input.columns:
                print(f"{user_index} set as index")
                csv_input.set_index(user_index, inplace=True)
            elif not user_index:
                pass
            else:
                print("Invalid selection!")
        else:
            print("Unable to load data.")
    except FileNotFoundError:
        print("File not found")
    return csv_input

def analyze_data(df):
    if df.shape[0] > 0:
        for columns in df.columns:
            print(columns)
            print('-------')
            print(f"number of values (n): {df[columns].notnull().sum()}")
            print(f"Minimum: {min(df[columns].values)}")
            print(f"Maximum: {max(df[columns].values)}")
            print(f"mean: {df[columns].mean()}")
            print(f"median: {df[columns].median()}")
            print("standard deviation: %.2f" % df[columns].std())
            print("std. err. of mean: %.2f" % df[columns].sem())
        print(df.corr())
    else:
        print("No data to Analyze")

def clean_data(df):
    if df.shape[0]>0:
        print("cleaning...")
        print(df)
        cleaning_menu ="""Cleaning data:
            1 - Drop rows with missing values
            2 - Fill missing values
            3 - Drop duplicate rows
            4 - Drop column
            5 - Rename column
            6 - Finish cleaning"""
        print(cleaning_menu)
        clean_choice = input(">>>")
        while clean_choice !='6':
            if clean_choice =='1':
                try:
                    drop_na_threshold = int(input("Enter the threshold for dropping rows: "))
                    df.dropna(thresh=drop_na_threshold, axis=0, inplace=True)
                    print(df)
                    print(cleaning_menu)
                    clean_choice = input(">>> ")
                except ValueError:
                    print("Please enter Valid number.")
            elif clean_choice =='2':
                try:
                    replacement_value = int(input("Enter the replacement Value "))
                    df.fillna(replacement_value, inplace=True)
                    print(df)
                    print(cleaning_menu)
                    clean_choice = input(">>> ")
                except ValueError:
                    print("Please enter a valid number.")
            elif clean_choice =='3':
                df_rec_count = df.shape[0]
                df.drop_duplicates(inplace=True)
                dropped_rec_count = df_rec_count - df.shape[0]
                print(f"{dropped_rec_count} records dropped")
                print(cleaning_menu)
                clean_choice = input(">>> ")
            elif clean_choice =='4':
                print("Which column do you want to drop? (leave blank for none) ")
                for columns in df.columns:
                    print(columns)
                drop_column_input = input(">>> ")
                if drop_column_input in df.columns:
                    df.drop(drop_column_input, axis=1, inplace=True)
                    print(f"{drop_column_input} dropped")
                    print(cleaning_menu)
                    clean_choice = input(">>> ")
                else:
                    print("No column dropped")
            elif clean_choice =='5':
                print("Which column do you want to rename?")
                for columns in df.columns:
                    print(columns)
                rename_col_input = input(">>> ")
                if rename_col_input in df.columns:
                    new_col_name = input("Enter the new name: ")
                    while new_col_name in df.columns:
                        if new_col_name not in df.columns:
                            df=df.rename(columns = {rename_col_input:new_col_name})
                            print(f"{rename_col_input} renamed to {new_col_name}")
                            print(df)
                            print(cleaning_menu)
                            clean_choice = input(">>> ")
                        else:
                            print("Column name must be unique and non-blank.")
                elif not rename_col_input:
                    print("Column name must be unique and non-blank.")
                else:
                    print("Invalid selection!")
    else:
        print("No data to clean")

def visualise_data(df):
    visual_list = ['line', 'bar', 'box']
    print("Please choose from the following kinds: line, bar, box")
    visulization_option = input(">>> ").lower()
    while visulization_option not in visual_list:
        print("Invalid selection!")
        visulization_option = input(">>> ").lower()
    if visulization_option in visual_list:
        print("Do you want to use subplots? (y/n)")
        subplot_option = input(">>> ")
        print("Please enter the title for the plot (leave blank for no title). ")
        graph_title = input(">>> ")
        print("Please enter the x-axis label (leave blank for no label). ")
        x_label =  input(">>> ")
        print("Please enter the y-axis label (leave blank for no label). ")
        y_label = input(">>> ")
        if subplot_option == 'y':
            df.plot(kind=visulization_option,subplots=True, title=graph_title)
            plot.xlabel(x_label)
            plot.ylabel(y_label)
            plot.show()
        elif subplot_option == 'n':
            df.plot(kind=visulization_option,subplots=False)
            plot.xlabel(x_label)
            plot.ylabel(y_label)
            plot.show()
        else:
            print("Invalid selection!")
def save_file(df):
    save_file_input = input("Enter the filename, including extension: ")
    if not save_file_input:
        print("Cancelling save operation.")
    elif save_file_input and '.' not in save_file_input:
        df.to_csv(save_file_input + '.csv')
        print(f"Data saved to {save_file_input}.csv")
    elif save_file_input and save_file_input.endswith('.csv') or save_file_input.endswith('.txt'):
        df.to_csv(save_file_input)
        print(f"Data saved to {save_file_input}")




a2_main()