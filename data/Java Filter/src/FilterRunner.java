import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import weka.core.Instances;

public class FilterRunner {

	public static void main(String[] args) {
		try (BufferedReader r = new BufferedReader(new FileReader("../B09b rotterdam_hamburg - dest maybe.arff"))) {
			Instances data = new Instances(r);

			System.out.println(data.firstInstance());
		} catch (IOException e) {
			System.err.println("An IOException has occured: " + e.getLocalizedMessage());
		}
		
		
	}

}
