import java.io.*
import java.util.*
import kotlin.math.*
import kotlin.collections.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    var st = StringTokenizer(br.readLine())
    val N = st.nextToken().toInt()
    val M = st.nextToken().toInt()
    val graph = HashMap<Int, ArrayDeque<Int>>(N)
    repeat(N) {
        graph[it + 1] = ArrayDeque()
    }
    repeat(M) {
        st = StringTokenizer(br.readLine())
        graph[st.nextToken().toInt()]!!.add(st.nextToken().toInt())
    }

    val dp = MutableList(N + 1) { 0 }

    for (i in 1..N) {
        val visited = MutableList(N + 1) { false }
        val q = ArrayDeque<Int>()
        q.addLast(i)
        visited[i] = true
        dp[i] += 1
        while (!q.isEmpty()) {
            val cur = q.removeFirst()
            graph[cur]?.forEach { next ->
                if (!visited[next]) {
                    visited[next] = true
                    q.addLast(next)
                    dp[next] += 1
                }
            }
        }
    }

    val maxCount = dp.max()
    for (i in 1..N) {
        if (dp[i] == maxCount) {
            bw.write(String.format("%d ", i))
        }
    }

    bw.flush()
    bw.close()
    br.close()
}