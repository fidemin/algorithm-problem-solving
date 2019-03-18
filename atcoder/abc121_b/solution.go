package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func readLine(reader *bufio.Reader) string {
	b, _, _ := reader.ReadLine()
	return string(b)
}

func readIntArray(reader *bufio.Reader) []int64 {
	strArr := strings.Split(readLine(reader), " ")
	var arr []int64
	for _, str := range strArr {
		i, _ := strconv.ParseInt(str, 10, 64)
		arr = append(arr, i)
	}
	return arr
}

func CanYouSolveThis(A []int64, B []int64, C int64) bool {
	ret := int64(0)

	for i, value := range A {
		ret += value * B[i]
	}

	return (ret + C) > 0

}

func main() {
	reader := bufio.NewReader(os.Stdin)
	NMC := strings.Split(readLine(reader), " ")
	N, _ := strconv.ParseInt(NMC[0], 10, 64)
	C, _ := strconv.ParseInt(NMC[2], 10, 64)

	B := readIntArray(reader)

	count := 0
	for i := int64(0); i < N; i++ {
		A := readIntArray(reader)
		if CanYouSolveThis(A, B, C) {
			count++
		}
	}

	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	writer.WriteString(strconv.FormatInt(int64(count), 10))
}
