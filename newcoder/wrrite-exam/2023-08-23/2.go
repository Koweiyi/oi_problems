package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"math"
)

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	var n, m int 
	Fscan(in, &n, &m)
	a := make([]int, n + 1)
	for i := 1 ; i <= n ; i ++ {
		Fscan(in, &a[i])
	}
	dp := make([]int, m + 1)
	for i := 1 ; i <= m ; i ++ {
		dp[i] = math.MaxInt
	} 
	dp[0] = 0
	for i := 1 ; i <= n ; i ++ {
		for j := m; j >= a[i] ; j -- {
			if dp[j - a[i]] != math.MaxInt{
				dp[j] = min(dp[j], dp[j - a[i]] + 1)
			}
		}
	}
	if dp[m] == math.MaxInt{
		Fprintln(out, "No solution")
	}else{
		Fprintln(out, dp[m])
	}
}

func min(a, b int) int {if a < b {return a} ; return b}

func main() { run(os.Stdin, os.Stdout)}
