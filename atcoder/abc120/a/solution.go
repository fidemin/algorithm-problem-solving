package main

import (
	"bufio"
	//	"fmt"
	"os"
	"strconv"
	"strings"
)

func min(a int64, b int64) int64 {
	if a > b {
		return b
	}
	return a
}

func FavoriteSound(A int64, B int64, C int64) int64 {
	return min(B/A, C)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	b, _, _ := reader.ReadLine()
	ABC := strings.Split(string(b), " ")
	A, _ := strconv.ParseInt(ABC[0], 10, 64)
	B, _ := strconv.ParseInt(string(ABC[1]), 10, 64)
	C, _ := strconv.ParseInt(string(ABC[2]), 10, 64)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	writer.WriteString(strconv.FormatInt(FavoriteSound(A, B, C), 10))
}
