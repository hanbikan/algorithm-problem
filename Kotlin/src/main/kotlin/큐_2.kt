import java.io.*
import java.util.*
import kotlin.collections.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    val N = br.readLine().toInt()
    val stack = ArrayDeque<Int>()
    repeat(N) {
        val st = StringTokenizer(br.readLine())
        val order = st.nextToken()
        if (order == "push") {
            val x = st.nextToken().toInt()
            stack.addLast(x)
        } else if (order == "pop") {
            if (stack.isEmpty()) {
                bw.write("-1\n")
            } else {
                bw.write(String.format("%d\n", stack.removeFirst()))
            }
        } else if (order == "size") {
            bw.write(String.format("%d\n", stack.count()))
        } else if (order == "empty") {
            if (stack.isEmpty()) {
                bw.write("1\n")
            } else {
                bw.write("0\n")
            }
        } else if (order == "front") {
            if (stack.isEmpty()) {
                bw.write("-1\n")
            } else {
                bw.write(String.format("%d\n", stack.first()))
            }
        } else {
            if (stack.isEmpty()) {
                bw.write("-1\n")
            } else {
                bw.write(String.format("%d\n", stack.last()))
            }
        }
    }

    bw.flush()
    bw.close()
    br.close()
}