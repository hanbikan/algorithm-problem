import java.util.*
import java.io.*
import kotlin.collections.*
import kotlin.math.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    var st = StringTokenizer(br.readLine())
    val N = st.nextToken().toInt()
    val M = st.nextToken().toInt()

    val A = ArrayList<Int>()
    val B = ArrayList<Int>()
    val C = ArrayList<Int>()
    st = StringTokenizer(br.readLine())
    repeat(N) {
        A.add(st.nextToken().toInt())
    }
    st = StringTokenizer(br.readLine())
    repeat(M) {
        B.add(st.nextToken().toInt())
    }
    var ai = 0
    var bi = 0
    while (ai < N && bi < M) {
        if (A[ai] < B[bi]) {
            C.add(A[ai])
            ai += 1
        } else {
            C.add(B[bi])
            bi += 1
        }
    }
    while (ai < N) {
        C.add(A[ai])
        ai += 1
    }
    while (bi < M) {
        C.add(B[bi])
        bi += 1
    }

    C.forEach {
        bw.write(String.format("%d ", it))
    }

    bw.flush()
    bw.close()
    br.close()
}