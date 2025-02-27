import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());   // case 개수

        StringTokenizer st;
        String type;
        Map<String, Integer> clothes = new HashMap<>();
        StringBuilder sb = new StringBuilder();

        for (int n=0; n<N; n++) {
            int M = Integer.parseInt(br.readLine()); // 해당 case 옷 개수
            for (int m=0; m<M; m++) {
                st = new StringTokenizer(br.readLine());
                st.nextToken(); // 옷 이름 정보 필요 없음(중복이 없기 때문에)

                type = st.nextToken();
                if (clothes.containsKey(type)) clothes.put(type, clothes.get(type)+1);
                else clothes.put(type, 2); // 해당 옷을 안 입는 경우의 수 포함
            }

            int result = clothes.values().stream().reduce(1, (a, b) -> a * b) - 1; // -1은 알몸 상태를 제외하기 위해서다.
            sb.append(result).append('\n');
            clothes.clear();
        }

        System.out.println(sb);
    }
}