package main

import (
	"fmt"
	"io"
)

func Day00_P1(f io.Reader) (string, error) {
	if f == nil {
		return "", fmt.Errorf("nil file")
	}
	return "1234", nil
}

func Day00_P2(f io.Reader) (string, error) {
	return "5678", nil
}
