import java.util.*
import kotlin.collections.*
import java.io.*
import kotlin.math.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    val N = br.readLine().toInt()
    val tips = ArrayList<Int>()
    repeat(N) {
        tips.add(br.readLine().toInt())
    }
    tips.sortWith(compareBy({ -it }))
    var result = 0L
    tips.forEachIndexed { index, tip ->
        result += max(0, tip - index)
    }
    bw.write(result.toString())

    bw.flush()
    bw.close()
    br.close()
}