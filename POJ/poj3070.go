package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

type matrix [][]int64

func newMatrix(n, m int) matrix {
	a := make(matrix, n)
	for i := range a {
		a[i] = make([]int64, m)
	}
	return a
}

func newIdentityMatrix(n int) matrix {
	a := make(matrix, n)
	for i := range a {
		a[i] = make([]int64, n)
		a[i][i] = 1
	}
	return a
}

func (a matrix) mul(b matrix, p int64) matrix {
	// const mod int64 = 1000000007 // 998244353
	c := newMatrix(len(a), len(b[0]))
	for i, row := range a {
		for j := range b[0] {
			for k, v := range row {
				c[i][j] = (c[i][j] + v*b[k][j]) % p // 注：此处不能化简
			}
			if c[i][j] < 0 {
				c[i][j] += p
			}
		}
	}
	return c
}

func (a matrix) pow(n int64, p int64) matrix {
	res := newIdentityMatrix(len(a))
	for ; n > 0; n >>= 1 {
		if n&1 > 0 {
			res = res.mul(a, p)
		}
		a = a.mul(a, p)
	}
	return res
}

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewScanner(_r)
	in.Split(bufio.ScanWords)
	out := bufio.NewWriter(_w)
	defer func(out *bufio.Writer) {
		_ = out.Flush()
	}(out)
	read := func() (x int64) {
		in.Scan()
		tmp := in.Bytes()
		if tmp[0] == '-' {
			for _, b := range tmp[1:] {
				x = x*10 + int64(b&15)
			}
			return -x
		} else {
			for _, b := range in.Bytes() {
				x = x*10 + int64(b&15)
			}
		}
		return
	}
	_ = []interface{}{read, Fprintf, Fscan}

	var n, p int64
	n = read()
	p = 1000000007
	m := newMatrix(2,2)
	m[0][0], m[0][1], m[1][0] = 1, 1, 1
	res := m.pow(n, p)[1][0]
	Println(res)
}
func main() { run(os.Stdin, os.Stdout) }
