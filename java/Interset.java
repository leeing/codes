import java.util.List;
import java.util.ArrayList;
import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
/**
 read two files and then get the intersetion of lines.
*/
public class Interset {
	public static void main(String args[]) throws Exception{
		List<String> salist=new ArrayList<String>();
		List<String> nimedlist = new ArrayList<String>();

		BufferedReader fr1 = new BufferedReader(new FileReader(new File("nimed.txt")));
		BufferedReader fr2 = new BufferedReader(new FileReader(new File("sa.txt")));

		String str="";

		while((str=fr1.readLine())!=null){
			salist.add(str.trim());
		}
		// System.out.println("the length of sa is "+salist.size());
		fr1.close();


		while((str=fr2.readLine())!=null){
			nimedlist.add(str.trim());
		}
		// System.out.println("the length of nimed is "+nimedlist.size());
		fr2.close();

		int counter = 0;
		for(int i = 0;i<nimedlist.size();i++){
			if(!salist.contains(nimedlist.get(i))){
				System.out.println(nimedlist.get(i));
				counter ++;
			}
		}
		// salist.removeAll(nimedlist);
		// System.out.println("counter is "+counter);
		// System.out.println("the length of salist is "+salist.size());
	}
}
