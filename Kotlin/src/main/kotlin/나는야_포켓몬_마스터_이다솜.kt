import java.io.*
import java.util.*
import kotlin.collections.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    val st = StringTokenizer(br.readLine())
    val N = st.nextToken().toInt()
    val M = st.nextToken().toInt()

    val mapByString = HashMap<String, Int>()
    val mapByInt = HashMap<Int, String>()
    repeat(N) {
        val name = br.readLine()
        val index = it + 1
        mapByString[name] = index
        mapByInt[index] = name
    }

    repeat(M) {
        val input = br.readLine()
        if (input[0] in '0'..'9') {
            val index = input.toInt()
            bw.write(String.format("%s\n", mapByInt[index]))
        } else {
            bw.write(String.format("%s\n", mapByString[input]))
        }
    }

    bw.flush()
    bw.close()
    br.close()
}