import os
import time
import pygame

pygame.init()

SCREEN_SIZE=700
screen=pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
font=pygame.font.SysFont(None,24)

def pygame_displ(lnum):

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((0,0,0))

    s_sq=int(pow(len(lnum),1/2))
    cell=SCREEN_SIZE//s_sq
    font_size=max(12,int(cell*0.45))
    font=pygame.font.SysFont(None,font_size)

    for i in range(len(lnum)):

        x=(i%s_sq)*cell
        y=(i//s_sq)*cell

        pygame.draw.rect(screen,(100,100,100),(x,y,cell,cell),1)

        if lnum[i]!="":
          txt=font.render(str(lnum[i]),True,(255,255,255))
          txt_rect=txt.get_rect(center=(x+cell//2,y+cell//2))
          screen.blit(txt,txt_rect)

    pygame.display.flip()


def displ (lnum):
    s_sq=int(pow(len(lnum),1/2))
    for i in    range(len (lnum)):
        if i%s_sq==0 :
            print("\n",end="")
            print(lnum[i],end="")
            print(" ",end="")
        elif 0<i<9 and len(lnum)>9:
             print(lnum[i],end="")
             print(" ",end="")
             print(" ",end="")
        else:
            print(lnum[i],end="")
            print(" ",end="")
    pygame_displ(lnum)

input_text=""
getting_input=True

while getting_input:

    screen.fill((0,0,0))

    txt=font.render(
        "How many numbers? "+input_text,
        True,
        (255,255,255)
    )

    screen.blit(txt,(50,50))

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_RETURN:

                if input_text!="":
                    seiv_num=int(input_text)
                    getting_input=False

            elif event.key==pygame.K_BACKSPACE:
                input_text=input_text[:-1]

            elif event.unicode.isdigit():
                input_text+=event.unicode




arr=[]
for i in range(seiv_num):
    arr.append(i+1)

def seive (lnum):
    count=[]

    for i in range(len(lnum)):
        n=lnum[i]
        if n==1:
            continue
       
        prime_stat=True

        for k in count:
            if  n%k==0:
                prime_stat=False
                break
        if prime_stat:
            count.append(n)
        else:
            lnum[i]=" "
            displ(arr)
            time.sleep(0.1)
            os.system("cls" if os.name == "nt" else "clear")
            


    return count

seive(arr)
displ(arr)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
