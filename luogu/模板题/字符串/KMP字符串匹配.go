package main

import (
	"bufio"
	. "fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var s, p string
	Fscan(in, &s, &p)
	nx := make([]int, len(p)+1)
	for i := 1; i < len(p); i++ {
		j := nx[i]
		for j > 0 && p[i] != p[j] {
			j = nx[j]
		}
		if p[j] == p[i] {
			j++
		}
		nx[i+1] = j
	}
	j := 0
	for i := 0; i < len(s); i++ {
		for j > 0 && p[j] != s[i] {
			j = nx[j]
		}
		if s[i] == p[j] {
			j++
		}
		if j == len(p) {
			Fprintln(out, i-len(p)+2)
			j = nx[j]
		}
	}
	for i := 1; i <= len(p); i++ {
		if i != len(p) {
			Fprint(out, nx[i], " ")
		} else {
			Fprintln(out, nx[i])
		}
	}
}
