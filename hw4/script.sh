#!/bin/bash

correct_number=$((RANDOM % 100 + 1))

attempts=0

while true; do
    read -p "Guess the number (between 1 and 100): " user_guess
    ((attempts++))

    if [[ $user_guess -eq $correct_number ]]; then
        echo "Congratulations! You guessed the right number."
        exit 0
    elif [[ $user_guess -lt $correct_number ]]; then
        echo "Too low. Try again."
    else
        echo "Too high. Try again."
    fi

    if [[ $attempts -ge 5 ]]; then
        echo "Sorry, you've run out of attempts. The correct number was $correct_number."
        exit 1
    fi
done
