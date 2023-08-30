package main

import (
	"bufio"
	. "fmt"
	"os"
	"sort"
)

func BKDRHash(s string) uint64 {
	var p, H uint64 = 131, 0
	for i := 0 ; i < len(s) ; i ++ {
		H = H * p + uint64(s[i] - 'a' + 1)
	}
	return H
}

func main()  {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	var s string
	a := []uint64{} 
	Fscan(in, &n)

	for i := 0 ; i < n ; i ++ {
		Fscan(in, &s)
		a = append(a, BKDRHash(s))
	}
	ans := 0
	sort.Slice(a, func(i, j int) bool {return a[i] < a[j]})
	a = append(a, 0)
	for i := 0 ; i < n ; i ++ {
		if a[i] != a[i + 1]{
			ans ++
		}
	}

	Fprintln(out, ans)

}