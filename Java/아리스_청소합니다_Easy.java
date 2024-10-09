import java.io.*;
import java.util.*;
import java.math.*;

public class 아리스_청소합니다_Easy {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer H = Integer.valueOf(st.nextToken());
        Integer W = Integer.valueOf(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Integer R = Integer.valueOf(st.nextToken());
        Integer C = Integer.valueOf(st.nextToken());
        Integer D = Integer.valueOf(st.nextToken());

        int[][] A = new int[H][W];
        int[][] B = new int[H][W];
        boolean[][] isClean = new boolean[H][W];
        for (int i=0;i<H;i++) {
            String line = br.readLine();
            for (int j=0;j<W;j++) {
                A[i][j] = line.charAt(j) - '0';
            }
        }
        for (int i=0;i<H;i++) {
            String line = br.readLine();
            for (int j=0;j<W;j++) {
                B[i][j] = line.charAt(j) - '0';
            }
        }

        int turn = 0;
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        boolean[][][] visited = new boolean[4][H][W];
        int lastTurn = 0;
        while (true) {
            int aOrB = 0;
            if (!isClean[R][C]) {
                isClean[R][C] = true;
                D = (D + A[R][C]) % 4;
                visited = new boolean[4][H][W];
            } else {
                D = (D + B[R][C]) % 4;
                aOrB = 1;

                if (visited[D][R][C]) break;
                visited[D][R][C] = true;
            }

            // bw.write(String.format("%d %d %d %d\n", R, C, D, aOrB));

            turn += 1;
            if (aOrB == 0) {
                lastTurn = turn;
            }
            R += dx[D];
            C += dy[D];

            if (!(0 <= R && R < H && 0 <= C && C < W)) break;
        }
        bw.write(String.valueOf(lastTurn));

        bw.flush();
        bw.close();
        br.close();
    }
}
