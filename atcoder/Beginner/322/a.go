package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"strings"
)

func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	var n int 
	Fscan(in, &n)
	var s string
	Fscan(in, &s)
    res := strings.Index(s, "ABC") + btoi(strings.Contains(s, "ABC"))
	Fprintln(out, res)
	return
}

func main() { run(os.Stdin, os.Stdout)}
func btoi(b bool) int {if b{return 1} ; return 0}