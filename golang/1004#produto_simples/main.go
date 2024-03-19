package main

import "fmt"

func main() {
  var n1 int
  var n2 int

  fmt.Scanf("%d", &n1)
  fmt.Scanf("%d", &n2)

  produto := n1 * n2

  fmt.Println("PROD =", produto)
}
