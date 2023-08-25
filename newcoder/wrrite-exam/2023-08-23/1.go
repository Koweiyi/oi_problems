package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	var n int 
	Fscan(in, &n)

	a := make([]int, n)
	for i := 0 ; i < n ; i ++ {
		Fscan(in, &a[i])
	}
	sort.Ints(a)

	
	
}

func main() { run(os.Stdin, os.Stdout)}