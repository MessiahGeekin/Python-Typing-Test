import os
import json
import random
import requests
import time

os.system('cls' if os.name == 'nt' else 'clear')

choice = input('(1) Local JSON Words\n(2) API Generated Words\n(3) Exit\n\n::: ').strip()

if choice.isdigit() and int(choice) > 0:
    wrd_count = input('How many words would you like: ')
    if wrd_count.isdigit() and int(wrd_count) > 0:
        if choice == '1':
            with open('words.json') as f:
                data = json.load(f)
                words = [random.choice(data['commonEnglishWords']) for _ in range(int(wrd_count))]

        elif choice == '2':
            response = requests.get(f'https://random-word-api.herokuapp.com/word?number={wrd_count}')
            if response.status_code in [200, 201]:
                words = response.json()
            else:
                print('Failed to retrieve random words. Please try again.')
                exit()

        else:
            print('Invalid choice. Enter a positive number.')
            exit()

        gen_wrds = ' '.join(words).lower()
        correct = 0
        start_time = time.time()
        
        input('\nPress Enter to start typing...')
        print('\n' + gen_wrds)
        typing = input('\nEnter the text above: ').lower()
        end_time = time.time()

        gen_wrds_list = gen_wrds.split()
        typing_list = typing.split()

        for i in range(min(len(gen_wrds_list), len(typing_list))):
            if gen_wrds_list[i] == typing_list[i]:
                correct += 1

        accuracy = correct / len(gen_wrds_list) * 100
        total_time = end_time - start_time
        wpm = len(typing_list) / total_time * 60

        print(f'\nCorrect: {correct}/{len(gen_wrds_list)}')
        print(f'Accuracy: {accuracy:.2f}%')
        print(f'WPM: {wpm:.2f}')
    else:
        print('Invalid word count. Enter a positive number.')
else:
    print('Invalid choice. Enter a valid number.')
