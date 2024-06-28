import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        long N = Long.parseLong(line[0]);
        long R = Long.parseLong(line[1]);

        System.out.println(N + (R * 2) -1);

        br.close();
    }
}