import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] score = new int[N];
		int idx = 0;
		while (idx < N) {
			int now = Integer.parseInt(br.readLine());
			score[idx] = now;
			idx++;
		}
		
		int cnt = 0;
		for (int i=N-1; i>0; i--) {
			if (score[i-1] < score[i]) {
				continue;
			}
			cnt += score[i-1]-score[i]+1;
			score[i-1] = score[i]-1;
			
		}
		System.out.println(cnt);
		
	}
}
