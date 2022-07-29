import java.lang.Integer.min
import java.util.Scanner
import kotlin.math.max

private var n: Int? = null
private var m: Int? = null
private var s: Int? = null
private var e: Int? = null

private var vertices = mutableListOf <Triple<Int, Int, Int>>()
private var graph: MutableMap<Int, MutableList<Pair<Int, Int>>> = mutableMapOf()
private var parents: Array<Int>? = null
private var isVisited: Array<Boolean>? = null

fun main() = with(Scanner(System.`in`)) {
    n = nextInt()
    m = nextInt()
    s = nextInt()
    e = nextInt()

    parents = Array(n!!+1) { it }

    for(i in 1..n!!) graph[i] = mutableListOf()

    for(i in 0 until m!!) {
        vertices.add(Triple(nextInt(),nextInt(),nextInt()))
    }

    vertices.sortWith(compareBy { -it.component3() })
    vertices.forEach { (a, b, w) ->
        if (find(a) != find(b)) {
            graph[a]!!.add(Pair(b, w))
            graph[b]!!.add(Pair(a, w))
            union(a, b)
        }
    }

    isVisited = Array(n!!+1) { false }
    isVisited!![s!!] = true
    print(travel(s!!, 1000001))
}

fun find(x: Int): Int {
    if (parents!![x] == x) return x

    parents!![x] = find(parents!![x])
    return parents!![x]
}

fun union(x: Int, y: Int) {
    val px = find(x)
    val py = find(y)

    if (px > py) parents!![px] = py
    else parents!![py] = px
}

fun travel(node: Int, count: Int): Int {
    if (node == e) return count

    var res = 0
    graph[node]?.forEach { (k, v) ->
        if (!isVisited!![k]) {
            isVisited!![k] = true
            res = max(
                res,
                travel(k, min(count, v))
            )
        }
    }
    return res
}
