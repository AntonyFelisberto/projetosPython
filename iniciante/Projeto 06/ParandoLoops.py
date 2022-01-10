def loopContinue():
      for i in range(0,100):#vai ficar em loop até chegar em 99//se você usar o 1 ele vai até o 100
          if i==50:
              continue
          print("o valor de i é {}:".format(i))
def loopBreak():
      for x in range(0,9):#vai ficar em loop até chegar em 8//se você usar o 1 ele vai até o 9
          if x==7:
              break  #break serve para parar totalmente um looping seja ele for ou while
          print("o valor de x é {}:".format(x))

loopContinue()
loopBreak()
