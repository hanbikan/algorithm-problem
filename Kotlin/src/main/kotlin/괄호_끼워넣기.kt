import java.lang.Integer.max
import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val s = next()
    var res = 0
    var offset = 0
    for(i in s.indices) {
        offset = if (s[i] == '(') offset + 1 else max(0, offset - 1)
    }
    res += offset

    for(i in s.indices.reversed()) {
        offset = if (s[i] == ')') offset + 1 else max(0, offset - 1)
    }
    res += offset

    print(res)
}