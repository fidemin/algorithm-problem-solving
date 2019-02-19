package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanf(f string, a ...interface{})  { fmt.Fscanf(reader, f, a...) }

var n, m, mod int64
var matrix [][]int

func multiply(one, two [][]int) [][]int {
	res := make([][]int, m)
	for i := 0; i < int(m); i++ {
		res[i] = make([]int, m)
	}
	for i := 0; i < int(m); i++ {
		for j := 0; j < int(m); j++ {
			for k := 0; k < int(m); k++ {
				res[i][j] += int(int64(one[i][k]) * int64(two[k][j]) % mod)
				res[i][j] %= int(mod)
			}
		}
	}
	return res
}

func power(exp int64, base [][]int) [][]int {

	if exp == 1 {
		return base
	}

	res := power(exp/2, base)
	res = multiply(res, res)
	if exp&1 == 1 {
		res = multiply(res, base)
	}
	return res
}

func main() {
	defer writer.Flush()
	mod = 1000000007
	scanf("%d %d\n", &n, &m)
	if n < m {
		printf("1")
		return
	}
	if n == m {
		printf("2")
		return
	}
	matrix = make([][]int, m)
	for i := 0; i < int(m); i++ {
		matrix[i] = make([]int, m)
	}
	matrix[0][0] = 1
	matrix[0][m-1] = 1
	for i := 1; i < int(m); i++ {
		matrix[i][i-1] = 1
	}

	for i := 0; i < int(m); i++ {
		for j := 0; j < int(m); j++ {
			fmt.Printf("%d ", matrix[i][j])
		}
		fmt.Println("")
	}

	fmt.Println(power(n, matrix)[0][0])
}
