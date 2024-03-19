package main

import "fmt"

func main()  {
  var correta int
  var j1, j2, j3, j4, j5 int
  qtd_correto := 0

  fmt.Scanf("%d", &correta)
  fmt.Scanf("%d %d %d %d %d", &j1, &j2, &j3, &j4, &j5)

  if correta == j1 { qtd_correto++ }
  if correta == j2 { qtd_correto++ }
  if correta == j3 { qtd_correto++ }
  if correta == j4 { qtd_correto++ }
  if correta == j5 { qtd_correto++ }

  fmt.Printf("%d\n", qtd_correto)
}
