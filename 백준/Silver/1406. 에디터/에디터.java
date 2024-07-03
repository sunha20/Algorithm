import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<String> textL = new Stack<>();
        Stack<String> textR = new Stack<>();
        textL.addAll(List.of(br.readLine().split("")));
        String resultL = "";
        String resultR = "";
        int M = Integer.parseInt(br.readLine());

        for (int m=0; m<M; m++) {
            String inst = br.readLine();
            if (inst.startsWith("L") && !textL.isEmpty()) {
                textR.push(textL.pop());
                continue;
            }
            if (inst.startsWith("D") && !textR.isEmpty()) {
                textL.push(textR.pop());
                continue;
            }
            if (inst.startsWith("B") && !textL.isEmpty()) {
                textL.pop();
                continue;
            }
            if (inst.startsWith("P")) {
                textL.push(inst.substring(2));
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!textL.isEmpty()) {
            sb.append(textL.pop());
        }
        sb.reverse();
        while (!textR.isEmpty()) {
            sb.append(textR.pop());
        }

        bw.write(sb.toString());
        br.close();
        bw.flush();
        bw.close();
    }
}