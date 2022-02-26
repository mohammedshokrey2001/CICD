import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;




public class file1 {

	public file1() {
		
	}
	public static void main(String[] args) {
	
		
		File file = new File("data/ww.txt");
		
		try (Scanner scanner = new Scanner(System.in)) {
			System.out.println("enter the number of employees: ");
			int inn = scanner.nextInt();
			
			try {
				PrintWriter writer = new PrintWriter(file);

				for (int i = 0; i < inn; i++) {
					System.out.println("enter the name: ");
				    String nameString = scanner.next();
					System.out.println("enter the salary: ");
					int salary = scanner.nextInt();
				
				writer.print(nameString);
				writer.print(salary);
				}
				System.out.println("done");
				writer.close();
				
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	
	}

}
