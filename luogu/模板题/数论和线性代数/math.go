package main

import "fmt"

//  计算 a ** n % mod
func fastPow(a int64, n int64, mod int64) int64{
	var res int64 = 1
	for a %= mod ; n > 0 ; n >>= 1{
		if n & 1 != 0{
			res = res * a % mod 
		}
		a = a * a % mod
	}
	return res 
}

//计算a, b的最大公约数
func gcd(a, b int) int{
	for ; a != 0 ; a, b = b % a, a {}; return b 
}

func main() {
	fmt.Println(gcd(12, 8))
}


