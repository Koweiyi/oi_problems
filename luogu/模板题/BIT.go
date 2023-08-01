package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

type fenwick struct {
	tree []int64
}

func newFenwickTree(n int) fenwick {
	return fenwick{make([]int64, n+1)}
}

// a[i] 增加 val
// 1<=i<=n
func (f fenwick) add(i int, val int64) {
	for ; i < len(f.tree); i += i & -i {
		f.tree[i] += val
	}
}

// 求前缀和 a[1] + ... + a[i]
// 1<=i<=n
func (f fenwick) pre(i int) (res int64) {
	for ; i > 0; i &= i - 1 {
		res += f.tree[i]
	}
	return
}

// 求区间和 a[l] + ... + a[r]
// 1<=l<=r<=n
func (f fenwick) query(l, r int) int64 {
	return f.pre(r) - f.pre(l-1)
}

func LG3374(_r io.Reader, _w io.Writer){
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	var m, n int 
	Fscan(in, &n, &m)
	t := newFenwickTree(n)
	for i := 1 ; i <= n ; i ++ {
		var a int 
		Fscan(in, &a)
		t.add(i, int64(a))
	}
	for i := 0 ; i < m ; i ++ {
		var op, x, y int
		Fscan(in, &op, &x, &y)
		if op == 1{
			t.add(x, int64(y))
		}else{
			res := t.query(x, y)
			Fprintln(out, res)
		}
	}
	return
}


func main() {
	LG3374(os.Stdin, os.Stdout)
}