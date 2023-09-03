package main
import (
	"bufio"
	. "fmt"
	"io"
	"os"
)
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
	
	is_prime := func (x int) bool {
		if x < 2{
			return false
		}
		for j := 2 ; j * j <= x ; j ++ {
			if x % j == 0{
				return false
			}
		}
		return true 
	}
	
	
	
	_ = []interface{}{read, Fprintf, Fscan, is_prime}
}
func main() { run(os.Stdin, os.Stdout)}
	