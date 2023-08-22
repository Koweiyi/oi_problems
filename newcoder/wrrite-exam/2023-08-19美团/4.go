package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	var n int 
	Fscan(in, &n)
	a := make([]int, n)
	s := 0
	for i := 0 ; i < n ; i ++ {
		Fscan(in, &a[i])
		s += a[i]
	}
	const mod int = 1e9 + 7 

	memo := make([][]int, n + 1)
	for i := range memo{
		memo[i] = make([]int, 505)
		for j := range memo[i]{
			memo[i][j] = -1
		}
	}
	var dfs  func(i int, left int) int
	dfs = func(i int, left int) int {
		if i == n{
			if left == 0{
				return 1
			}
			return 0
		}
		if memo[i][left] != -1{
			return memo[i][left]
		}
		res := 0
		for j := 1 ; j < a[i] ; j ++ {
			if left >= j {
				res = (res + dfs(i + 1, left - j)) % mod
			}
		}
		for j := a[i] + 1 ; left - j >= n - (i + 1) && j <= left; j ++ {
			res = (res + dfs(i + 1, left - j)) % mod
		}
		memo[i][left] = res 
		return res
	} 

	res := dfs(0, s)
	Fprintln(out, res)
	return 
}

func main() { run(os.Stdin, os.Stdout)}