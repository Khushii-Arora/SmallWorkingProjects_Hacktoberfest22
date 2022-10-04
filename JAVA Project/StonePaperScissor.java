import java.util.Random;
import java.util.Scanner;

public class StonePaperScissor {

    public static final String ROCK = "R";
    public static final String PAPER = "P";
    public static final String SCISSORS = "S";

    // Main Method
    public static void main(String[] args) {
        System.out.println("Rock, Paper, Scissors!\n"
                + "Please enter a move.\n"
                + "Rock = R, Paper= P, and Scissors = S.\n");
        String userInput = getUsersMove();
        if (userInput.equals(PAPER) || userInput.equals(ROCK) || userInput.equals(SCISSORS))
            getResult(userInput, getComputersMove());
        else
            System.out.println("Invalid Input " + userInput);
    }

    // Results
    public static void getResult(String usersMove, String computersMove) {
        System.out.println("Computer's move is: " + computersMove);

        if (usersMove.equals(computersMove))
            System.out.println("It's a tie!");
        else if (usersMove.equals(ROCK)) {
            if (computersMove.equals(SCISSORS))
                System.out.println("You win!! Rock crushes scissors.");
            else if (computersMove.equals(PAPER))
                System.out.println("You lose!! Paper eats rock.");
        } else if (usersMove.equals(PAPER)) {
            if (computersMove.equals(ROCK))
                System.out.println("You win!! Paper eats rock.");
            else if (computersMove.equals(SCISSORS))
                System.out.println("You lose!! Scissor cuts paper.");
        } else if (usersMove.equals(SCISSORS)) {
            if (computersMove.equals(PAPER))
                System.out.println("You win!! Scissor cuts paper.");
            else if (computersMove.equals(ROCK))

                System.out.println("You lose!! Rock breaks scissors.");
        } else
            System.out.println("Invalid user input.");
    }

    // Computer's Move
    public static String getComputersMove() {
        int computersNum;
        String computersMove = "";
        Random random = new Random();
        computersNum = random.nextInt(3) + 1;
        if (computersNum == 1)
            computersMove = ROCK;
        else if (computersNum == 2)
            computersMove = PAPER;
        else if (computersNum == 3)
            computersMove = SCISSORS;
        return computersMove;
    }

    // User's Move
    public static String getUsersMove() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your play: ");
        String input = scanner.next().toUpperCase();
        return input;
    }
}