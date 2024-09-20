import java.util.*;
import java.util.stream.Collectors;

public class 공정_컨설턴트_호석 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer N = sc.nextInt();
        Integer M = sc.nextInt();
        sc.nextLine(); // 개행 문자 소모해야 함
        List<Integer> numbers = Arrays.stream(sc.nextLine().split(" "))
                .map((str) -> Integer.parseInt(str))
                .collect(Collectors.toList());

        Integer l = 1;
        Integer r = N;
        Integer result = Integer.MAX_VALUE;
        while (l <= r) {
            Integer m = (int) Math.floor((l + r) / 2.0);

            PriorityQueue<Integer> pq = new PriorityQueue<>(m);
            Integer time = 0;
            for (int i=0;i<m;i++) {
                pq.add(0);
            }
            for (int i=0;i<N;i++) {
                int toAdd = pq.poll() + numbers.get(i);
                pq.add(toAdd);
                time = Math.max(time, toAdd);
            }
            //System.out.printf("l=%d m=%d r=%d time=%d\n",l,m,r,time);

            if (time <= M) {
                r = m - 1;
                result = Math.min(result, m);
            } else {
                l = m + 1;
            }
        }

        System.out.println(result);
    }
}
