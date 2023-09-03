package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"strconv"
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
	_ = []interface{}{read, Fprintf, Fscan}
	T := read()
	vis := make([]bool,10000)
	for i := 2; i * i < 10000 ; i ++ {
		if !vis[i]{
			for j := i * i ; j < 10000 ; j += i {
				vis[j] = true
			}
		}
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

	mp := map[int]int{0:-1,1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
	valid := func (s string) bool {
		y, _ := strconv.Atoi(s[:4])
		if y == 0{
			return false
		}
		mo, _ := strconv.Atoi(s[4:6])
		day, _ := strconv.Atoi(s[6:8])
		if y % 4 == 0 && y % 100 != 0 || y % 400 == 0{
			mp[2] ++
			defer func ()  {
				mp[2] --	
			}()
		}
		return 0 < day && day <= mp[mo] && is_prime(y * 10000 + mo * 100 + day)
	}
	

	for T > 0{
		in.Scan()
		tmp := in.Bytes()
		res := 0
		var dfs func(id int)
		dfs = func(id int) {
			if id == 5 || id == 3{
				num, _ := strconv.Atoi(string(tmp[id + 1:]))
				if !vis[num] || id == 5 && num >= 32 || id == 3 && num >= 1300 {
					return
				} 
				if id == 3 && num / 100 != 2 && (num % 100 == 0 || num % 100 > mp[num / 100]){
					return
				}
			}
			if id == -1{
				if valid(string(tmp)){
					res ++
				}
				return 
			}

			if tmp[id] != '-'{
				dfs(id - 1)
			}else{
				for i := 0 ; i < 10 ; i ++{
					tmp[id] = byte('0' + i)
					dfs(id - 1)
				} 
				tmp[id] = '-'
			}
		}
		dfs(len(tmp) - 1)
		Println(res)
		T -- 
	}
}
func main() { run(os.Stdin, os.Stdout)}
func abs(a int) int {if a < 0 {return -a}; return a}

	