package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func WhiteCells(H int64, M int64, h int64, m int64) int64 {
	return H*M - h*M - m*H + h*m
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	b, _, _ := reader.ReadLine()
	HM := strings.Split(string(b), " ")
	H, _ := strconv.ParseInt(HM[0], 10, 64)
	M, _ := strconv.ParseInt(HM[1], 10, 64)

	b, _, _ = reader.ReadLine()
	hm := strings.Split(string(b), " ")
	h, _ := strconv.ParseInt(hm[0], 10, 64)
	m, _ := strconv.ParseInt(hm[1], 10, 64)

	fmt.Println(WhiteCells(H, M, h, m))
}
