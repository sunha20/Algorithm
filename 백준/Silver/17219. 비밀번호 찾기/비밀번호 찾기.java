import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Map<String, String> memo = new HashMap<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());   // 저장한 주소 개수
        int M = Integer.parseInt(st.nextToken());   // 찾을 주소 개수

        // 주소 저장
        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            memo.put(st.nextToken(), st.nextToken());
        }

        // 주소 검색
        StringBuilder result = new StringBuilder();
        for (int m=0; m<M; m++) {
            result.append(memo.get(br.readLine()) + "\n");
        }
        System.out.println(result);
    }
}