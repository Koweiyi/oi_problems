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
	var n, m int 
	Fscan(in, &n, &m)

	a := make([]int, n)
	left := make([]int, m + 1)
	for i := 0 ; i < n ; i ++ {
		Fscan(in, &a[i])
		left[a[i]] ++ 
	}

	inRes := make([]bool, m + 1)
	res := make([]int, 0)
	for i := 0 ; i < n ; i ++ {
		left[a[i]] --
		if inRes[a[i]] {
			continue
		}
		for len(res) > 0 && a[i] < res[len(res) - 1] && left[res[len(res) - 1]] > 0{
			top := res[len(res) - 1]
			res = res[:len(res) - 1]
			inRes[top] = false
		}
		res = append(res, a[i])
		inRes[a[i]] = true
	}
	for _, x := range res{
		Fprint(out, x, " ")
	}
	return
}

func main() { run(os.Stdin, os.Stdout)}