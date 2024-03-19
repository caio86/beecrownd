package main

import "fmt"

func main() {
  var id_funcionario int
  var horas_funcionario int
  var valor_hora float32

  fmt.Scanf("%d", &id_funcionario)
  fmt.Scanf("%d", &horas_funcionario)
  fmt.Scanf("%f", &valor_hora)

  salario := float32(horas_funcionario) * valor_hora

  fmt.Printf("NUMBER = %d\n",id_funcionario)
  fmt.Printf("SALARY = U$ %.2f\n", salario)
}
