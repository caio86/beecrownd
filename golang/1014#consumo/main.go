package main

import "fmt"

func main()  {
  var distancia int32
  var comb_gasto float32

  fmt.Scanf("%d", &distancia)
  fmt.Scanf("%f", &comb_gasto)

  consumo_medio := float32(distancia) / comb_gasto

  fmt.Printf("%.3f km/l\n", consumo_medio)
}
