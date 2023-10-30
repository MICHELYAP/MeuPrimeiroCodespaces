"""
O mercardo 'seu jose' esta com ua promoção de 10% para seu clientes maiores de 18 anos. Faça um programa em python que pergunte a idade, o valor do total e mostre se ele pode ou não ter o desconto,qual o desconto e o valor final.
"""
idade = int(input("Digite sua idade:\n"))
total= float(input("Digite ovalor total dos produtos:\n"))

if("idade>=18"):
    print("pode ter o desconto")
    desconto = total * 0.1
    final = total - desconto
    print(f"o desconto foide R${desconto} e o total é de R${final}")
else:
    print(f"Não tem direito ao descomto e o seu valor final é de R${total}") 


