#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 2/3/2023
#Project: Word Frequency Count
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Write a program to count the number of occurrences of a word in the sample data file words.txt.
#Develop an algorithm for counting the words. When the current word read is different from the 
#last work, write that word and its count to a file named words.count."
#--------------------------------------------------------------------------------------------
#ALGORYTHM
#-----------------
#Step 1) Display welcome and program explanation.
#Step 1) Get user input.
#Step 2) Validate the input.
#Step 3) Open and read file.
#Step 4) Create a list out of the contents of the file.
#Step 4) Sort the list using the sort method.
#Step 5) Count the frequency of words inside the file.
#Step 6) Create an output file named "words.count" if it exist, ask if it can be overwritten.
#Step 6) Write the word and its count to a output file named "words.count".
#Step 6) Display when complete.
#--------------------------------------------------------------------------------------------
# The display_greeting function is used to display an explanation of the purpose of the program.
# This function uses formatted f string to display a heading.
def display_greeting():
    line_1 = 'This program takes the name of a file that contains words and runs a frequency.'
    line_2 = 'After completing the frequency count, the program writes the results to an output file.'
    line_3 = 'The name of the output file will be "words.count".'
    print()
    print('-' * 90)
    print('|' + f'{"Word Frequency Count":^88}' + '|')
    print('-' * 90)
    print('|' + f'{line_1:<88}' + '|')
    print('|' + f'{line_2:<88}' + '|')
    print('|' + f'{line_3:<88}' + '|')
    print('-' * 90)

# The get_input_input_file_name function is used to get the name of the file that the user wishes
# to count the contents of. This function validates that the input file name is not an empty string.
# Finally, it returns the input file name.
def get_input_file_name(title, ext = '.txt'):

    # Set flag variable to True.
    not_done = True

    # While loop used to iterate input validation.
    while not_done:

        # File may not exist, so this section of code lives inside a try block.
        try:

            # Prompt user to enter a valid input.
            input_file_name = input(title)

            # Print statement for esthetics.
            print('-' * 90)
            
            # If the file is not an empty string, verify it has the extention ".txt".
            if input_file_name != '':

                # If name has no extention, concatanate extention to input file name.
                if not ext in input_file_name:
                    input_file_name += ext

                # Try to open file, close if opened.
                input_file = open(input_file_name, 'r')
                input_file.close()

                # Assign not_done False.
                not_done = False

            # If file name is empty string, display error.
            else:
                print('File names cannot be blank. Please re-enter.')
                print('-' * 90)

        # Exception handler for if file does not exist.
        except FileNotFoundError:
            print('No such file or directory: ' + input_file_name)

    # Return valid user input.
    return input_file_name

# The read_file function is used to read the input file and store its contents inside of a list.
# This function sorts the contents of the list before returning it.
def read_file_create_list(input_file_name):

    # Create a list for the words inside the file.
    word_list = []

    # Open file in read mode, and read line.
    input_file = open(input_file_name, 'r')
    input_file_line = input_file.readline()

    # Iterates until empty string is read.
    while input_file_line != '':

        # Assign word the value of the current line, strip anything that is not a word.
        word = input_file_line.strip()

        # Append word to word_list.
        word_list.append(word)

        # Read line.
        input_file_line = input_file.readline()

    # Close file.
    input_file.close()

    # Sort list before returning it.
    word_list.sort()

    # Return the sorted list.
    return word_list

# The count_list_elements function is used to count the frequency of each element
# inside of a list. This functin is used to call write_to_file.
def count_list_elements(list):

    # Iteration variable controls which branch is executed in the write_to_file function.
    iterations = 0
    
    # Create variable word_1 assign it the value list[0].
    word_1 = list[0]

	# Create a count variable and initilize to one.
    count = 1

	# for loop is used to compare word_1 to next word in list:
    for index in range(1, len(list)):

        # If word is a space character, assign the string to word_1.
        if word_1 == '':
            word_1 = 'Space Character'

            # If first iter, call write_to_file and assign the returned value to abort.
            if iterations == 0:

                # Call print to file function and pass word_1, count, and iterations as arguements.
                abort = write_to_file(word_1, count, iterations)

                # Set count to one.
                count = 1

        # Elif word_1 is not a space, check if equal to next word.
        elif word_1 != list[index]:

            # If first iteration, Call print to file function and pass word_1, count, and iterations as arguements.
            if iterations == 0:

                # Call print to file function and pass word_1, count, and iterations as arguements.
                abort = write_to_file(word_1, count, iterations)

                # Set count to one.
                count = 1

            # elif abort equals false.
            elif abort == False:

                # Call print to file function and pass word_1, count, and iterations as arguements.
                write_to_file(word_1, count, iterations)

                # Set count to one.
                count = 1

            # User does not need any data written.
            else:
                pass

        # word_1 maches the next word in the list.
        else:

		    # Add one to count variable.
            count += 1

        # Add one to the iterations variable.
        iterations += 1

        # Assign the value of the next element in the list to the variable word_1.
        word_1 = list[index]

    # If abort is not true, write the last value in list to file.
    if abort != True:
        write_to_file(word_1, count, iterations)

# The write_to_file function is used to write data to a output file name 'words.count'.
# This function has branches that execute depending on iterations.
def write_to_file(word, count, iterations):

	# if iteration is equal to zero:
    if iterations == 0:

        # Flag controls the branch that checks if okay to overwrite if file exist.
        checking_if_file_exist = True

        # Check if file exist and if it's okay to overwrite if it does exist.
        while checking_if_file_exist:
        
            # try: open the file "words.count" for reading. If it opens, close the file,
            #and prompt user to decide if file can be overwritten. 
            try:

                # Open output file, read a line, and close it.
                output_file = open('words.count', 'r')
                line = output_file.readline()
                output_file.close()

                # If line does not equal empty string, prompt user to overwrite or ABORT.
                if line != '':
                    print('Warning! File already exists and contains content.')
                    print('Press "Y" to CONTINUE and overwrite or ENTER to ABORT.')
                    overwrite = input('Do you wish to continue and overwrite the contents? ')
                    print('-' * 90)

                    # If user hit ENTER abort.
                    if overwrite.upper() != 'Y':
                        abort = True
                        checking_if_file_exist = False
                        return abort

                    # All other cases.
                    else:
                        checking_if_file_exist = False
                        abort = False
                        output_file = open('words.count', 'w')
                        print(word + ':' + str(count), file = output_file)
                        output_file.close()
                        return abort

                # All other cases.
                else:
                    abort = False
                    checking_if_file_exist = False
                    output_file = open('words.count', 'w')
                    print(word + ':' + str(count), file = output_file)
                    output_file.close()
                    return abort

            # File does not exist, no need to worry about over writting data.
            except FileNotFoundError:
                output_file = open('words.count', 'w')
                print(word + ':' + str(count), file = output_file)
                output_file.close()
                checking_if_file_exist = False
                abort = False
                return abort
    
    # If function has iterated, run this block.
    else:

		# Append the word and count to file.
        output_file = open('words.count', 'a')
        print(word + ':' + str(count), file = output_file)
        output_file.close()

# The display_good_bye_message is used to display good bye and confirm data saved to file.
def display_good_bye_message():
    print('-' * 90)
    print('|' + f'{"Your frequency count has been saved to a file named: words.count":^88}' + '|')
    print('|' + f'{"Good-Bye!":^88}' + '|')
    print('-' * 90)

# The main function is used to call all function needed to complete the programming task.
def main():

    # Displays a greating and a program explanation.
    display_greeting()

    # Nested functions used to pass data to essential parts of the program. A user prompt is given as the 
    # arguement for get_input_file_name function.
    count_list_elements(read_file_create_list(get_input_file_name('Please enter the name of the file to run a frequency count on: ')))

    # Display good-bye message.
    display_good_bye_message()

# If program loaded as main, run main function.
if __name__ == '__main__':
    main()