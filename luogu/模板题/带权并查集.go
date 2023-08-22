//http://acm.hdu.edu.cn/showproblem.php?pid=3038 HDU 3038题
package main

import (
	"bufio"
	. "fmt"
	"os"
)

// 写个并查集板子
type UnionFind struct{
	root []int 
	mn []int
	mx []int
}

func NewUnionFind(n int) *UnionFind{
	root := make([]int, n + 1)
	for i := range root{
		root[i] = i 
	}
	return &UnionFind{

	}
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
