import java.io.*;
import java.util.*;

public class 최소_환승_경로 {
    static int N, L;
    static List<Integer>[] route;
    static List<Integer>[] nodes;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());

        route = new ArrayList[L+1];
        nodes = new ArrayList[N+1];

        for (int i = 0; i <= L; i++) {
            route[i] = new ArrayList<>();
        }
        for (int i=0; i <= N; i++) {
            nodes[i] = new ArrayList<>();
        }

        for (int i = 1; i <= L; i++) {
            st = new StringTokenizer(br.readLine());
            while (true) {
                int t = Integer.parseInt(st.nextToken());
                if (t == -1) break;
                route[i].add(t);
                nodes[t].add(i);
            }
        }

        st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int result = Integer.MAX_VALUE;

        // BFS 탐색 시작
        boolean[] visited = new boolean[L+1];
        Queue<Pair> q = new LinkedList<>();
        for (int a : nodes[S]) {
            q.add(new Pair(a, 0));
            visited[a] = true;
        }

        while (!q.isEmpty()) {
            Pair cur = q.poll();
            for (int a : route[cur.first]) {
                if (a == E) {
                    result = Math.min(result, cur.second);
                    break;
                } else {
                    for (int node : nodes[a]) {
                        if (visited[node]) continue;
                        visited[node] = true;
                        q.add(new Pair(node, cur.second + 1));
                    }
                }
            }
        }

        if (result == Integer.MAX_VALUE) {
            result = -1;
        }
        bw.write(result + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    static class Pair {
        int first, second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }
}
/**
9 2
1 2 3 4 5 -1
6 2 7 8 4 9 -1
2 8
 */
