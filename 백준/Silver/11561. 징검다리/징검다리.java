import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i=0; i < T; i++) {
            long N = Long.parseLong(br.readLine());
            System.out.println(getNumOfJump(N));
        }
    }

    private static int getNumOfJump(long n){
        int k = (int) ((double) ((-1 + Math.sqrt(8*n+1)))/2);
        return k;
    }
}