import java.io.*
import java.util.*
import kotlin.collections.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    val st = StringTokenizer(br.readLine())
    val N = st.nextToken().toInt()
    val M = st.nextToken().toInt()

    val set = HashSet<String>()
    repeat(N) {
        set.add(br.readLine())
    }
    var count = 0
    repeat(M) {
        if (set.contains(br.readLine())) {
            count += 1
        }
    }
    bw.write(String.format("%d\n", count))

    bw.flush()
    bw.close()
    br.close()
}