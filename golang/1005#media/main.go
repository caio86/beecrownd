package main

import "fmt"

func main() {
  var n1 float64
  var n2 float64

  fmt.Scanf("%f", &n1)
  fmt.Scanf("%f", &n2)

  media := (n1 * 3.5 + n2 * 7.5) / (3.5 + 7.5)

  fmt.Printf("MEDIA = %.5f\n", media)
}
