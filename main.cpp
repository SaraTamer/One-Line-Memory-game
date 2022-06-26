/*
 Header: Memory line game
 Author: Sara Tamer Bihery
 Date: 1-3-2022
 */


#include <iostream>
#include<string>
#include <chrono>
#include <thread>

using namespace std;


string cards[20] = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
                    "19", "20"};

int i = 0, j = 0, turn = 0, player1_score = 0, player2_score = 0;

void game_play() {
    if (player1_score + player2_score == 10) {
        if (player1_score > player2_score)
            cout << "The winner is player1";
        else if (player2_score > player1_score)
            cout << "The winner is player2";
        else
            cout << "Its tie";
    }
}

void cards_display() {
    for (int i = 0; i < 20; i++)
        cout << cards[i] << ' ';
    cout << endl;
}

int main() {
    game_play();
    cards_display();
    cout << endl;
    string line[20] = {"A", "B", "C", "D", "E", "F", "I", "J", "A", "B", "C", "D", "E", "F", "I", "J"};

    while (player1_score + player2_score != 10) {
        turn++;
        if (turn % 2 == 1) {
            cout << "Player1, score:" << player1_score << endl;
            cout << "Choose two numbers from 1 to 20.";
            cin >> i >> j;
        } else if (turn % 2 == 0) {
            cout << "Player2, score:" << player2_score << endl;
            cout << "Choose two numbers from 1 to 20.";
            cin >> i >> j;
        }
        cards[i - 1] = line[i - 1];
        cards[j - 1] = line[j - 1];
        cards_display();
        cout.flush();
        this_thread::sleep_for(std::chrono::milliseconds(3000));
        system("cls");

        if (line[i - 1] == line[j - 1]) {
            cards[i - 1] = cards[j - 1] = '*';
            cout << cards;
            if (turn % 2 == 1)
                player1_score = player1_score + 1;
            else if (turn % 2 == 0)
                player2_score = player2_score + 1;
        } else {
            cards[i - 1] = to_string(i);
            cards[j - 1] = to_string(j);
            system("cls");
            cards_display();
        }
    }
    return 0;
}
