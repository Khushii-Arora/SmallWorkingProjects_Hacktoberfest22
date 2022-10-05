package com.company;

import java.util.Scanner;

public class rockPaperScssiorGame {
    static final int Rock = 1;
    static final int Scssior = 2;
    static final int Paper = 3;

    public rockPaperSessiorGame() {
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Player1 choose(1)- Rock, choose(2)- Scssior , choose(3)- Paper : ");
        int Player1 = sc.nextInt();
        System.out.println("Player2 choose(1) -Rock, choose(2)- Scssior , choose(3) -Paper : ");
        int Player2 = sc.nextInt();
        if (Player1 == Player2) {
            System.out.println("this is a tie");
        } else {
            switch(Player1) {
            case 1:
                if (Player2 == 2) {
                    System.out.print("Player 1 wins!");
                } else {
                    System.out.print("Player 2 wins!");
                }
                break;
            case 2:
                if (Player2 == 3) {
                    System.out.println("Player1 wins!");
                } else {
                    System.out.println("Player2 wins! ");
                }
                break;
            case 3:
                if (Player2 == 1) {
                    System.out.println("Player1 wins!");
                } else {
                    System.out.println("Player2 wins!");
                }
            }
        }

    }
}
