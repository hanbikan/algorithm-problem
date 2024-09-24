import java.io.*;
import java.util.*;
import java.util.stream.*;

public class 수강_과목 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer N = Integer.valueOf(st.nextToken());
        Integer K = Integer.valueOf(st.nextToken());

        List<List<Integer>> dp = new ArrayList<>(K+1);
        for (int i=0;i<=K;i++) {
            dp.add(new ArrayList<>(Collections.nCopies(N+1, 0)));
        }
        for (int i=1;i<=K;i++) {
            st = new StringTokenizer(br.readLine());
            Integer imp = Integer.valueOf(st.nextToken());
            Integer time = Integer.valueOf(st.nextToken());
            for (int j=1;j<=N;j++) {
                if (j >= time) {
                    dp.get(i).set(j, Math.max(dp.get(i-1).get(j), dp.get(i-1).get(j-time) + imp));
                } else {
                    dp.get(i).set(j, dp.get(i-1).get(j));
                }
                //bw.write(String.valueOf(dp.get(i).get(j)) + " ");
            }
            //bw.write("\n");
        }

        bw.write(String.valueOf(dp.get(K).get(N)));

        bw.flush();
        bw.close();
        br.close();
    }
}
