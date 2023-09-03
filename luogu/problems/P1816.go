package main

import (
	"bufio"
	. "fmt"
	"io"
	"math"
	"os"
)

type ST [][]int

func NewST(a []int) ST {
	n := len(a)
	sz := int(math.Log2(float64(n)))
	st := make(ST, n)
	for i, v := range a {
		st[i] = make([]int, sz + 1)
		st[i][0] = v
	}
	for j := 1; 1<<j <= n; j++ {
		for i := 0; i + 1<<j - 1 < n ; i++ {
			st[i][j] = st.Op(st[i][j-1], st[i+1<<(j-1)][j-1])
		}
	}
	return st
}

// 查询区间 [l,r)，注意 l 和 r 是从 0 开始算的
func (st ST) Query(l, r int) int {
	k := int(math.Log2(float64(r - l)))
	return st.Op(st[l][k], st[r - 1<<k][k])
}

// min, max, gcd, ...
func (ST) Op(a int,b int) int { if a < b {return a} ;return b } 

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewScanner(_r)
	in.Split(bufio.ScanWords)
	out := bufio.NewWriter(_w)
	defer func(out *bufio.Writer) {
		_ = out.Flush()
	}(out)
	read := func() (x int) {
		in.Scan()
		tmp := in.Bytes()
		if tmp[0] == '-' {
			for _, b := range tmp[1:] {
				x = x*10 + int(b&15)
			}
			return -x
		} else {
			for _, b := range in.Bytes() {
				x = x*10 + int(b&15)
			}
		}
		return
	}
	_ = []interface{}{read, Fprintf, Fscan}
	m, n := read(), read()
	a := make([]int, m)
	for i := 0 ; i < m ; i ++ {
		a[i] = read()
	} 	
	st := NewST(a)
	for q := 1 ; q <= n ; q ++ {
		l, r := read(), read()
		Print(st.Query(l - 1, r))
		if q != n{
			Print(" ")
		}
	}
}
func main() { run(os.Stdin, os.Stdout)}