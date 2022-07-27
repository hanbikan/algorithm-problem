import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()

    val m5 = if((n % 5) % 2 == 0) n / 5 else n / 5 - 1
    val m2 = (n - 5 * m5) / 2

    var res = m5 + m2
    if(m2 < 0 || m5 < 0) res = -1
    print(res)
}