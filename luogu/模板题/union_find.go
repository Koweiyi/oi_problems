//http://acm.hdu.edu.cn/showproblem.php?pid=3038 HDU 3038题
package main

import (
	"bufio"
	. "fmt"
	"os"
)

// 
type UnionFind struct {
	Fa     []int
	Groups int // 连通分量个数
}

func NewUnionFind(n int) UnionFind {
	fa := make([]int, n ) // n+1
	for i := range fa {
		fa[i] = i
	}
	return UnionFind{fa, n}
}

func (u UnionFind) Find(x int) int {
	if u.Fa[x] != x {
		u.Fa[x] = u.Find(u.Fa[x])
	}
	return u.Fa[x]
}

// newRoot = -1 表示未发生合并
func (u *UnionFind) Merge(from, to int) (newRoot int) {
	x, y := u.Find(from), u.Find(to)
	if x == y {
		return -1
	}
	u.Fa[x] = y
	u.Groups--
	return y
}

func (u UnionFind) Same(x, y int) bool {
	return u.Find(x) == u.Find(y)
}

const N = 200_010

var s, d = [N]int{}, [N]int{}
var res = 0

func init_set() {
	for i := 0; i < N; i++ {
		s[i] = i
	}
}

func find(x int) int {
	if x != s[x] {
		r := s[x]
		s[x] = find(s[x])
		d[x] += d[r]
	}
	return s[x]
}

func union(x, y, v int) {
	rootx, rooty := find(x), find(y)
	if rootx == rooty {
		if d[x]-d[y] != v {
			res++
		}
	} else {
		s[rootx] = rooty
		d[rootx] = d[y] - d[x] + v
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n,m int
	Fscan(in, &n, &m)
	init_set()
	for ; m > 0; m --{
		var a, b, v int 
		Fscan(in, &a, &b, &v)
		a --
		union(a, b, v)
	} 
	Fprintln(out, res)
	return
}
