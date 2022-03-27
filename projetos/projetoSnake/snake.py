import pygame,sys,time,random

speed =15

#tamanho da janela

frameSizeX=int(720)
frameSizeY=int(480)

#inicia o programa
checkErros=pygame.init()

if(checkErros[1]>0):
    #caso de erro mostra o erro
    print("erro:"+checkErros[1])
    pass
else:
    print("jogo inicializado")

pygame.display.set_caption("Jogo Snake")                    #criando o titulo do jogo
gameWindow=pygame.display.set_mode(frameSizeX,frameSizeY)   #criando a tela de jogo

#cores
preto=pygame.color(0,0,0)
branco=pygame.color(255,255,255)
vermelho=pygame.color(255,0,0)
verde=pygame.color(0,255,0)
azul=pygame.color(0,0,255)

fpsController=pygame.time.Clock()

#tamanho da cobra
squareSize=20

def init_vars():
    global head,body,foodPos,foodSpawn,score,direcao    #definindo as variaveis do sistema como globais
    direcao="Right"
    head=[120,60]
    body=[[120,60]]
    foodPos=[random.randrange(1,(frameSizeX//squareSize))*squareSize,
             random.randrange(1,(frameSizeY//squareSize))*squareSize]
    foodSpawn=True
    score=0

init_vars()     #iniciando as variaveis

def mostrarPontuacao():
    print("pontuação")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key==pygame.K_UP or event.key==ord("w") and direcao!="DOWN"):
                direcao="UP"
            elif(event.key==pygame.K_DOWN or event.key==ord("s") and direcao!="UP"):
                direcao="DOWN"
            elif(event.key==pygame.K_LEFT or event.key==ord("a") and direcao!="RIGHT"):
                direcao="LEFT"
            elif(event.key==pygame.K_RIGHT or event.key==ord("d") and direcao!="LEFT"):
                direcao="RIGHT"
                