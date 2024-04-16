import tkinter as tk,copy

#
cols=[[1,2,3,4,5],[],[]]

#
win=tk.Tk()
win.geometry('800x350')
cv=tk.Canvas(win,width=800,height=350,bg='white')
cv.pack()
#
def draw_pillar(no):
    margin=10#
    col_width=800//3#
    col_x=no*col_width#
    dh,dw=50,(col_width-margin*2)#
    by=margin+dh*6#
    cx=col_x+col_width//2#
    cv.create_line(cx,margin,cx,by,fill='silver',width=5)#
    cv.create_line(col_x,by,col_x+col_width,by,fill='silver',width=5)#
    #
    disks=copy.copy(cols[no])
    while len(disks)<5:
        disks.insert(0,0)
    #
    for i,w in enumerate(disks):
        if w==0:continue#
        dx=col_x+(col_width-dw)//2#
        dy=margin+dh//2+i*dh#円盤のy座標
        sm=(5-w)*15#円盤のサイズ補正
        cv.create_rectangle(dx+sm,dy,dx+dw-sm,dy+dh-10,
                            fill=('orange'if w%2==0 else'yellow'))#円盤を描画
#
def draw_pillars():
    cv.delete('all')#
    for no in range(3):
        draw_pillar(no)
        
#
result=[]
def hanoi(n,src,des,temp):
    if n==1:#
        result.append([src,des])
    else:
        hanoi(n-1,src,temp,des)
        result.append([src,des])
        hanoi(n-1,temp,des,src)
hanoi(5,0,2,1)#

#
def next_step(e):
    global result
    if len(result)==0:return
    [src,des]=result[1:]#
    labels=['A','B','C']#
    win.title(f'{labels[src]}->{labels[des]}')
    cols[des].insert(0,cols[src][0])#
    cols[src]=cols[src][1:]
    draw_pillars()#
    
#
win.bind('<Button-1>',next_step)
draw_pillars()#
win.mainloop()#