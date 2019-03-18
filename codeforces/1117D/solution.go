package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

var m = 0
var cache [101]int

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

func MagicGems(n int64) int {
	for i := 1; i < m; i++ {
		cache[i] = 1
	}
	cache[0] = 2

	for i := int64(m + 1); i < n+1; i++ {
		ret := cache[int((i-1)%int64(m))] + cache[int((i-int64(m))%int64(m))]
		ret = ret % 1000000007
		cache[int(i%int64(m))] = ret
	}
	return cache[int(n%int64(m))]

}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)
	var arr []int64

	arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	for i := 0; i < 2; i++ {
		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
		if err != nil {
			panic(err)
		}
		arrItem := int64(arrItemTemp)
		arr = append(arr, arrItem)
	}
	var n int64
	n = arr[0]
	m = int(arr[1])

	result := MagicGems(n)

	fmt.Printf("%d\n", result)

}
