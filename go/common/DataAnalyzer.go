package common

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func load(path string) []string {
	bytes, err := ioutil.ReadFile("../resources/" + path)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	data := strings.Split(string(bytes), "\n")

	return data
}

func intArray(path string) []int {
	lines := load(path)

	var data []int

	for i := 0; i < len(lines); i++ {
		data[i], _ = strconv.Atoi(lines[i])
	}

	return data
}
