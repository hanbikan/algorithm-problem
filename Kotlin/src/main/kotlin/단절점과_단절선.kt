import java.util.*
import java.io.*
import kotlin.collections.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    val N = br.readLine().toInt()
    val graph: HashMap<Int, ArrayList<Int>> = HashMap()
    val edges = ArrayList<Pair<Int, Int>>()
    repeat(N) {
        graph[it + 1] = ArrayList()
    }
    edges.add(Pair(0, 0))
    repeat(N - 1) {
        val st = StringTokenizer(br.readLine())
        val a = st.nextToken().toInt()
        val b = st.nextToken().toInt()
        graph[a]?.add(b)
        graph[b]?.add(a)
        edges.add(Pair(a, b))
    }
    val Q = br.readLine().toInt()
    repeat(Q) {
        val st = StringTokenizer(br.readLine())
        val t = st.nextToken().toInt()
        val k = st.nextToken().toInt()
        if (t == 1) { // 단절점
            if (graph[k]?.count()!! >= 2) {
                bw.write("yes\n")
            } else {
                bw.write("no\n")
            }
        } else { // 단절선
            bw.write("yes\n")
        }
    }

    bw.flush()
    bw.close()
    br.close()
}