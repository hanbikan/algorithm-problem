import java.io.*
import java.util.*
import kotlin.math.*
import kotlin.collections.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    val N = br.readLine().toInt()
    if (N % 2 == 0) {
        bw.write("CY")
    } else {
        bw.write("SK")
    }

    bw.flush()
    bw.close()
    br.close()
}