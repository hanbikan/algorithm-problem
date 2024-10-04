import java.io.*
import java.util.*
import kotlin.math.*
import kotlin.collections.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    val money = br.readLine().toInt()
    val prices = ArrayList<Int>()
    val st = StringTokenizer(br.readLine())
    while (st.hasMoreTokens()) {
        prices.add(st.nextToken().toInt())
    }

    var aMoney = money
    var aStockCount = 0
    prices.forEach { price ->
        if (aMoney > 0) {
            aStockCount += floor(aMoney / price * 1.0).toInt()
            aMoney = aMoney % price
        }
        //bw.write(String.format("%d %d\n", aMoney, aStockCount))
    }
    //bw.write("\n")

    var bMoney = money
    var bStockCount = 0
    var incCount = 0
    var decCount = 0
    for (i in 1 until prices.count()) {
        if (prices[i] > prices[i-1]) {
            incCount += 1
            decCount = 0
        } else if (prices[i] < prices[i-1]) {
            decCount += 1
            incCount = 0
        } else {
            incCount = 0
            decCount = 0
        }

        if (incCount >= 3) { // 전량 매도
            bMoney += bStockCount * prices[i]
            bStockCount = 0
        }
        if (decCount >= 3) { // 전량 매수
            bStockCount += floor(bMoney / prices[i] * 1.0).toInt()
            bMoney = bMoney % prices[i]
        }
        //bw.write(String.format("%d %d\n", bMoney, bStockCount))
    }

    val aResult = aMoney + aStockCount * prices.last()
    val bResult = bMoney + bStockCount * prices.last()
    if (aResult > bResult) {
        bw.write("BNP")
    } else if (bResult > aResult) {
        bw.write("TIMING")
    } else {
        bw.write("SAMESAME")
    }

    bw.flush()
    bw.close()
    br.close()
}