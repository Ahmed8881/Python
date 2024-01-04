import os
import random
import subprocess

def add_random_letter_and_commit_push(file_path, pushCount):
    try:
       for i in range(pushCount):
            # Open the file in append mode and add a random letter
            with open(file_path, 'a') as file:
                random_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
                file.write(random_letter)

            # Run the git add command to stage the change
            subprocess.run(['git', 'add', file_path])

            # Run the git commit command
            subprocess.run(['git', 'commit', '-m', f"Add random letter: {random_letter}"])
    except Exception as e:
        print(f"Error during commit and push: {e}")

    # Run the git push command to push the change to the remote repository
    subprocess.run(['git', 'push'])
    print("Commit and push successful!")

# Replace 't.txt' with the actual path to your file
file_path = 't.txt'
pushCount = int(input("How many push?: "))
add_random_letter_and_commit_push(file_path, pushCount)
