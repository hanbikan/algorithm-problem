import java.io.*
import java.util.*
import kotlin.collections.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    val line = br.readLine()
    var str = StringBuilder()
    var count = 0
    for (i in 0 until line.count() + 1) {
        if (i == line.count() || line[i] == '.') {
            if (count % 2 == 1) {
                str = StringBuilder()
                str.append(-1)
                count = 0
                break
            }

            while (count - 4 >= 0) {
                str.append("AAAA")
                count -= 4
            }
            while (count - 2 >= 0) {
                str.append("BB")
                count -= 2
            }
            if (i < line.count()) {
                str.append(".")
            }
            count = 0
        } else {
            count += 1
        }
    }
    bw.write(str.toString() + "\n")

    bw.flush()
    bw.close()
    br.close()
}