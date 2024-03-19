package main

import (
	"fmt"
	"math"
)

func main() {
  var num float64

  const PI = 3.14159

  fmt.Scanf("%f", &num)

  area := PI * math.Pow(num, 2)

  fmt.Printf("A=%.4f %T", area, area)
}
