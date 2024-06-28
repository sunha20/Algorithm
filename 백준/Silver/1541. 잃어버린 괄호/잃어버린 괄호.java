import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] splitByMinus = br.readLine().split("-");
        int result = 0;
        int sum = 0;
        for (int i=0; i<splitByMinus.length; i++) {
            String[] splitByPlus = splitByMinus[i].split("\\+");
            sum = 0;
            for (String num : splitByPlus) {
                sum += Integer.parseInt(num);
            }
            if(i == 0) {result += sum; continue;}
            result -= sum;
        }
        System.out.println(result);
        br.close();
    }
}