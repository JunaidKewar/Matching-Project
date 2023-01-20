import testfile
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Accept two strings as command-line arguments')

    # Define the two string arguments
    parser.add_argument('menteeFile', type=str, help='First string')
    parser.add_argument('mentorFile', type=str, help='Second string')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Print the two strings
    # print(args.menteeFile)
    # print(args.mentorFile)

    testfile.main(args.menteeFile + '.csv', args.mentorFile + '.csv')

