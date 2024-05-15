import java.io.*;
import java.util.Arrays;

public class Main {
    public void Solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] gradeList = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int max = -1;
        int min = 1001;
        for(int grade: gradeList) {
            if (grade > max) {
                max = grade;
            }
            if (grade < min) {
                min = grade;
            }
        }
        System.out.println(max-min);
        br.close();
    }
    public static void main(String[] args) throws IOException {
        new Main().Solution();
    }
}
