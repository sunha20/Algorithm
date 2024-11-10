import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int cnt = 0;
		
		while(N > 0) {
			if (N-5 >= 0 && N-5 != 3 && N-5 != 1) {
				N -= 5;
				cnt++;
				continue;
			}
			
			if (N-2 >= 0) {
				N -= 2;
				cnt++;
				continue;
			}
			
			cnt = -1;
			break;
		}
		
		System.out.println(cnt);
		
	}
}
