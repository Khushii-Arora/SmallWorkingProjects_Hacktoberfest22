/*
This is a magic card game.
In this game player choose a one number from 0 to 63.
Then enter y/Y if your number is in the card else type n/N.
Then last magic is programm is give you a number which player choose.

Happy Magic :)

*/


import java.util.Scanner;
class magic
{
	static int A[][]={{1,3,5,7},{9,11,13,15},{17,19,21,23},{25,27,29,31},{33,35,37,39},{41,43,45,47},{49,51,53,55},{57,59,61,63}};
	static int B[][]={{16,17,18,19},{20,21,22,23},{24,25,26,27},{28,29,30,31},{48,49,50,51},{52,53,54,55},{56,57,58,59},{60,61,62,63}};			
	static int C[][]={{32,33,34,35},{36,37,38,39},{40,41,42,43},{44,45,46,47},{48,49,50,51},{52,53,54,55},{56,57,58,59},{60,61,62,63}};
	static int D[][]={{8,9,10,11},{12,13,14,15},{24,25,26,27},{28,29,30,31},{40,41,42,43},{44,45,46,47},{56,57,58,59},{60,61,62,63}};			
	static int E[][]={{2,3,6,7},{10,11,14,15},{18,19,22,23},{26,27,30,31},{34,35,38,39},{42,43,46,47},{50,51,54,55},{58,59,62,63}};
	static int F[][]={{4,5,6,7},{12,13,14,15},{20,21,22,23},{28,29,30,31},{36,37,38,39},{44,45,46,47},{52,53,54,55},{60,61,62,63}};			
	static Scanner s=new Scanner(System.in);
	static void printCard(int card[][],String cardName)
	{
		int i,j;
		System.out.println("\ncard= "+cardName+" values= ");
		for (i=0;i<8;i++) 
		{
			for (j=0;j<4;j++) 
			{
				System.out.printf("%2s  ",card[i][j]);	
			}
			System.out.println("");
		}
	}

	static int existInCard(int card[][],String cardName)
	{
		int ans=0;
		String m="";
		String z1;
		//String c;
		while(!(m.equals("y") || m.equals("Y") || m.equals("n") || m.equals("N")))
		{
			System.out.print("\nEnter "+cardName+" card yes(y/Y) or (n/N): ");
			m=s.next();
			//z1=s.nextLine();
			//System.out.println(m.equals("y"));
			if (m.equals("y") || m.equals("Y")) 
			{
				ans=ans+card[0][0];	
				return(ans);
			}
		}
		return(ans);
	}

	public static void main(String[] args) 
	{
		int ans=0;

		printCard(A,"A");
		ans=ans+existInCard(A,"A");
		printCard(B,"B");
		ans=ans+existInCard(B,"B");
		printCard(C,"C");
		ans=ans+existInCard(C,"C");		
		printCard(D,"D");
		ans=ans+existInCard(D,"D");		
		printCard(E,"E");
		ans=ans+existInCard(E,"E");		
		printCard(F,"F");
		ans=ans+existInCard(F,"F");	

		System.out.println("\nYour no is: "+ans);	
	}
}