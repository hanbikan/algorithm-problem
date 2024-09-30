import java.io.*;
import java.util.*;
import java.util.stream.*;

public class 애너그램 {
    private static ArrayList<Integer> counts;
    private static String str;
    private static BufferedReader br;
    private static BufferedWriter bw;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Integer N = Integer.valueOf(br.readLine());
        for (int i=0;i<N;i++) {
            str = br.readLine();
            counts = new ArrayList<>(Collections.nCopies(26, 0));
            for (int j=0;j<str.length();j++) {
                Integer index = str.charAt(j) - 'a';
                counts.set(index, counts.get(index) + 1);
            }
            printAnagrams(new ArrayDeque<String>(str.length()));
        }

        bw.flush();
        bw.close();
        br.close();
    }

    private static void printAnagrams(ArrayDeque<String> toPrint) throws IOException {
        if (toPrint.size() == str.length()) {
            for (String c : toPrint) {
                bw.write(c);
            }
            bw.write("\n");
            return;
        }

        for (int i=0;i<26;i++) {
            if (counts.get(i) == 0) continue;

            counts.set(i, counts.get(i) - 1);
            toPrint.addLast(String.valueOf((char) ((int) 'a' + i)));
            printAnagrams(toPrint);
            counts.set(i, counts.get(i) + 1);
            toPrint.removeLast();
        }
    }
}
