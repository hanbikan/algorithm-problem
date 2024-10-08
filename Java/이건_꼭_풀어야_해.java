import java.util.*;
import java.io.*;
import java.math.*;

public class 이건_꼭_풀어야_해 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer N = Integer.valueOf(st.nextToken());
        Integer Q = Integer.valueOf(st.nextToken());

        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0;i<N;i++) {
            A[i] = Integer.valueOf(st.nextToken());
        }
        Arrays.sort(A);

        // prefix sum
        int[] ps = new int[N+1];
        Integer cur = 0;
        ps[0] = 0;
        for (int i=0;i<N;i++) {
            cur += A[i];
            ps[i+1] = cur;
        }

        for (int i=0;i<Q;i++) {
            st = new StringTokenizer(br.readLine());
            Integer L = Integer.valueOf(st.nextToken());
            Integer R = Integer.valueOf(st.nextToken());
            bw.write(String.format("%d\n", ps[R] - ps[L-1]));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
