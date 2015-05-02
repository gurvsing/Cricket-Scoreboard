#!python.exe
import site

from PyQt4 import QtCore, QtGui
import sys
import Tkinter
import time
import start,fall,pro2,last,Main,sl2,sl3,sl4,sl5,sl6,sl7,sl8,sl9,sl10,dev,sl11,sl12,declare_que,playing_elev1,playing_elev2
import random,copy
'''start- starting page
last ending page
Main - main calculating arena'''




global dec,k,total_over,total_run1,total_run,total_run2,total_wicket1,total_wicket2,total_wicket,current_batsman1,current_batsman2,extras,extra1,extra2,over,over1,over2,team_bowling,team_batting,batsman_played
k,dec=0,0
current_batsman1,current_batsman2=0,1
total_run,total_run1,total_run2=0,0,0
total_wicket,total_wicket1,total_wicket2=0,0,0
extras,extra1,extra2=0,0,0
over1,over2=0,0
over,balls=0,0
global this_over,last_over,team_name
this_over,last_over=0,0
record_run_ball=[]
global team1_name,team2_name,te
te=0
global team1,team2
total_over=0
team1_name,team2_name='',''
batsman_played=[0,1]
global wicket_fall1,wicket_fall2,wicket_fall,back_goto,back_index
wicket_fall1=[['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['','']]
wicket_fall2=[['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['','']]
wicket_fall=[['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['','']]#1.run,2.wicket no.
team1=[[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]]]
team2=[[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]],[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]]]
#[[[runs,balls,fours,six,how out,who taken],[over,runs,maidens,wickets,wides,no-ball],[name,attribute]]

#Edited for back button in main page 1-3-2013
global batsman_index_dup,batsman2_index_dup,bowler_index_dup,back_goto_batsman,back_goto_bowler,extra_dup,wicket_fall_dup,this_over_d,last_over_d,back_index,total_run_dup,total_wicket_dup,over_dup
back_goto_batsman=[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]]
#[run,ball,four,six,(1->out 0->not)]
back_goto_bowler=[[0,0,0,0,'',''],[0,0,0,0,0,0],['',0]]
#[ball,run,madiens,wickets,wide,no-ball]
wicket_fall_dup=[['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['','']]

#duplicate of this over,last over
this_over_d,last_over_d=0,0
back_index=0


#edited for top 11 player selection
global playing_team_selected1,playing_team_selected2
playing_team_selected1=[["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""]]
playing_team_selected2=[["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""],["",""]]


'''def display():
    Main1.lcdNumber.Display(str(over))
    Main1.label_2.setText(str(total_run)+'/'+str(total_wicket)+'('+str(over)+')')
    Main.label'''

def swap(a,b):
    return(b,a)
    

def strike(q,z):
        if z==0:
            return 0
        else:
            return round((float(q)*100)/float(z),2)

def over_ball(q):
    z=int(q*10)%10
    return int(q)*6+z

def ball_over(q):
    z=q%6
    return float(str(q/6)+'.'+str(z))

def eco(w,q):#w=over,q=run
    if w==0:
        return 0
    else:
        return round(float((q*6))/(over_ball(w)),2)
        

def initilise(t1,t2):
    Main1.lcdNumber.display(0.0)
    Main1.label_2.setText('0/0 (0.0)')
    Main1.label_8.setText('0')
    Main1.label_14.setText('0.0')
    Main1.label_18.setText('0')
    Main1.label_16.setText(team_bowling)
    Main1.label_19.setText('')
    Main1.label_4.setText(t2[current_bowler][2][0]+' '+str(t2[current_bowler][1][0])+'-'+str(t2[current_bowler][1][1])+'-'+str(t2[current_bowler][1][3]))
    Main1.label_15.setText(team_batting)
    Main1.label_5.setText(t1[current_batsman1][2][0]+' '+str(t1[current_batsman1][0][0])+'('+str(t1[current_batsman1][0][1])+')')
    Main1.label_6.setText(t1[current_batsman2][2][0]+' '+str(t1[current_batsman2][0][0])+'('+str(t1[current_batsman2][0][1])+')')
    MainWindow007.update()
    
def start_sl2():
    MainWindow001.close()
    MainWindow02.show()
    
def sl2_sl7():
    MainWindow02.close()
    Form001.show()

def sl2_dev():
    MainWindow02.close()
    MainWindow122.show()
    
def sl2_sl9():
    MainWindow02.close()
    MainWindow121.show()

def exit():
    '''exit'''
    sys.exit(0)

def dev_sl2():
    MainWindow122.close()
    MainWindow02.show()
    
def sl9_sl2():
    MainWindow121.close()
    MainWindow02.show()

def sl7_sl2():
    Form001.close()
    MainWindow02.show()

def sl7_sl3():
    global team1_name,team_name
    team1_name=sl71.lineEdit.text()
    global team2_name
    team2_name=sl71.lineEdit_2.text()
    global total_over
    total_over=int(sl71.lineEdit_3.text())
    Form001.close()
    Dialog001.show()
    sl31.label_13.setText(str(team1_name))
    team_name=team1_name
    

def sl3_sl7():
    Dialog001.close()
    Form001.show()

'''
def sl3_sl11():
    global team1,team_name
    team1[0][2][0]=sl31.lineEdit01.text()
    team1[1][2][0]=sl31.lineEdit02.text()
    team1[2][2][0]=sl31.lineEdit03.text()
    team1[3][2][0]=sl31.lineEdit04.text()
    team1[4][2][0]=sl31.lineEdit05.text()
    team1[5][2][0]=sl31.lineEdit06.text()
    team1[6][2][0]=sl31.lineEdit07.text()
    team1[7][2][0]=sl31.lineEdit_9.text()
    team1[8][2][0]=sl31.lineEdit09.text()
    team1[9][2][0]=sl31.lineEdit10.text()
    team1[10][2][0]=sl31.lineEdit11.text()
    team1[0][2][1]=sl31.comboBox.currentText()
    team1[1][2][1]=sl31.comboBox_2.currentText()
    team1[2][2][1]=sl31.comboBox_3.currentText()
    team1[3][2][1]=sl31.comboBox_4.currentText()
    team1[4][2][1]=sl31.comboBox_5.currentText()
    team1[5][2][1]=sl31.comboBox_6.currentText()
    team1[6][2][1]=sl31.comboBox_7.currentText()
    team1[7][2][1]=sl31.comboBox_8.currentText()
    team1[8][2][1]=sl31.comboBox_9.currentText()
    team1[9][2][1]=sl31.comboBox_10.currentText()
    team1[10][2][1]=sl31.comboBox_11.currentText()
    Dialog001.close()
    MainWindow123.show()
    sl111.label_13.setText(str(team2_name))
    team_name=team2_name
 '''


def sl3_sl11():
    global team1,team_name,playing_team_selected1
    playing_team_selected1[0][0]=sl31.lineEdit01.text()
    playing_team_selected1[1][0]=sl31.lineEdit02.text()
    playing_team_selected1[2][0]=sl31.lineEdit03.text()
    playing_team_selected1[3][0]=sl31.lineEdit04.text()
    playing_team_selected1[4][0]=sl31.lineEdit05.text()
    playing_team_selected1[5][0]=sl31.lineEdit06.text()
    playing_team_selected1[6][0]=sl31.lineEdit07.text()
    playing_team_selected1[7][0]=sl31.lineEdit_9.text()
    playing_team_selected1[8][0]=sl31.lineEdit09.text()
    playing_team_selected1[9][0]=sl31.lineEdit10.text()
    playing_team_selected1[10][0]=sl31.lineEdit11.text()
    playing_team_selected1[11][0]=sl31.lineEdit11_7.text()
    playing_team_selected1[12][0]=sl31.lineEdit11_8.text()
    playing_team_selected1[13][0]=sl31.lineEdit11_9.text()
    playing_team_selected1[14][0]=sl31.lineEdit11_10.text()
    playing_team_selected1[0][1]=sl31.comboBox.currentText()
    playing_team_selected1[1][1]=sl31.comboBox_2.currentText()
    playing_team_selected1[2][1]=sl31.comboBox_3.currentText()
    playing_team_selected1[3][1]=sl31.comboBox_4.currentText()
    playing_team_selected1[4][1]=sl31.comboBox_5.currentText()
    playing_team_selected1[5][1]=sl31.comboBox_6.currentText()
    playing_team_selected1[6][1]=sl31.comboBox_7.currentText()
    playing_team_selected1[7][1]=sl31.comboBox_8.currentText()
    playing_team_selected1[8][1]=sl31.comboBox_9.currentText()
    playing_team_selected1[9][1]=sl31.comboBox_10.currentText()
    playing_team_selected1[10][1]=sl31.comboBox_11.currentText()
    playing_team_selected1[11][1]=sl31.comboBox_28.currentText()
    playing_team_selected1[12][1]=sl31.comboBox_29.currentText()
    playing_team_selected1[13][1]=sl31.comboBox_30.currentText()
    playing_team_selected1[14][1]=sl31.comboBox_31.currentText()
    Dialog001.close()
    MainWindow123.show()
    sl111.label_13.setText(str(team2_name))
    team_name=team2_name



def sl11_sl3():
    MainWindow123.close()
    Dialog001.show()
    sl31.label_13.setText(team1_name)

def playing_elev1_sl11():
    MainWindow_elev1.close()
    MainWindow123.close()
    sl111.label_13.setText(team2_name)
'''
def sl11_sl12():
    global team2
    team2[0][2][0]=sl111.lineEdit01.text()
    team2[1][2][0]=sl111.lineEdit02.text()
    team2[2][2][0]=sl111.lineEdit03.text()
    team2[3][2][0]=sl111.lineEdit04.text()
    team2[4][2][0]=sl111.lineEdit05.text()
    team2[5][2][0]=sl111.lineEdit06.text()
    team2[6][2][0]=sl111.lineEdit07.text()
    team2[7][2][0]=sl111.lineEdit_9.text()
    team2[8][2][0]=sl111.lineEdit09.text()
    team2[9][2][0]=sl111.lineEdit10.text()
    team2[10][2][0]=sl111.lineEdit11.text()
    team2[0][2][1]=sl111.comboBox.currentText()
    team2[1][2][1]=sl111.comboBox_2.currentText()
    team2[2][2][1]=sl111.comboBox_3.currentText()
    team2[3][2][1]=sl111.comboBox_4.currentText()
    team2[4][2][1]=sl111.comboBox_5.currentText()
    team2[5][2][1]=sl111.comboBox_6.currentText()
    team2[6][2][1]=sl111.comboBox_7.currentText()
    team2[7][2][1]=sl111.comboBox_8.currentText()
    team2[8][2][1]=sl111.comboBox_9.currentText()
    team2[9][2][1]=sl111.comboBox_10.currentText()
    team2[10][2][1]=sl111.comboBox_11.currentText()
    global team_batting,team_bowling
    team_batting=team1_name
    team_bowling=team2_name
    MainWindow123.close()
    MainWindow125.show()
    
    sl121.label_2.setText(team_batting)
    sl121.label_4.setText(team_bowling)
    if team_batting==team1_name:
        x1=list(team1)
        x2=list(team2)
    else :
        x1=list(team2)
        x2=list(team1)
    sl121.comboBox.clear()    
    for i in range(0,11):
        s=x2[i][2][0]
        sl121.comboBox.addItem(s)

'''

def sl11_playing_elev1():
    global team2,playing_team_selected2
    playing_team_selected2[0][0]=sl111.lineEdit01.text()
    playing_team_selected2[1][0]=sl111.lineEdit02.text()
    playing_team_selected2[2][0]=sl111.lineEdit03.text()
    playing_team_selected2[3][0]=sl111.lineEdit04.text()
    playing_team_selected2[4][0]=sl111.lineEdit05.text()
    playing_team_selected2[5][0]=sl111.lineEdit06.text()
    playing_team_selected2[6][0]=sl111.lineEdit07.text()
    playing_team_selected2[7][0]=sl111.lineEdit_9.text()
    playing_team_selected2[8][0]=sl111.lineEdit09.text()
    playing_team_selected2[9][0]=sl111.lineEdit10.text()
    playing_team_selected2[10][0]=sl111.lineEdit11.text()
    playing_team_selected2[11][0]=sl111.lineEdit11_5.text()
    playing_team_selected2[12][0]=sl111.lineEdit11_4.text()
    playing_team_selected2[13][0]=sl111.lineEdit11_3.text()
    playing_team_selected2[14][0]=sl111.lineEdit11_2.text()
    playing_team_selected2[0][1]=sl111.comboBox.currentText()
    playing_team_selected2[1][1]=sl111.comboBox_2.currentText()
    playing_team_selected2[2][1]=sl111.comboBox_3.currentText()
    playing_team_selected2[3][1]=sl111.comboBox_4.currentText()
    playing_team_selected2[4][1]=sl111.comboBox_5.currentText()
    playing_team_selected2[5][1]=sl111.comboBox_6.currentText()
    playing_team_selected2[6][1]=sl111.comboBox_7.currentText()
    playing_team_selected2[7][1]=sl111.comboBox_8.currentText()
    playing_team_selected2[8][1]=sl111.comboBox_9.currentText()
    playing_team_selected2[9][1]=sl111.comboBox_10.currentText()
    playing_team_selected2[10][1]=sl111.comboBox_11.currentText()
    playing_team_selected2[11][1]=sl111.comboBox_13.currentText()
    playing_team_selected2[12][1]=sl111.comboBox_14.currentText()
    playing_team_selected2[13][1]=sl111.comboBox_15.currentText()
    playing_team_selected2[14][1]=sl111.comboBox_16.currentText()
    MainWindow123.close()

    MainWindow_elev1.show()
    playing_elev11.label_13.setText(str(team1_name))
    
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_12.addItem(ss)
        playing_elev11.comboBox.addItem(s)
           

    
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_13.addItem(ss)
        playing_elev11.comboBox_2.addItem(s)

    #playing_elev11.comboBox_3.addItem('')
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_14.addItem(ss)
        playing_elev11.comboBox_3.addItem(s)

    #playing_elev11.comboBox_4.addItem('')
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_15.addItem(ss)
        playing_elev11.comboBox_4.addItem(s)

    #playing_elev11.comboBox_5.addItem('')
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_16.addItem(ss)
        playing_elev11.comboBox_5.addItem(s)

    #playing_elev11.comboBox_6.addItem('')
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_17.addItem(ss)
        playing_elev11.comboBox_6.addItem(s)

    #playing_elev11.comboBox_7.addItem('')
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_18.addItem(ss)
        playing_elev11.comboBox_7.addItem(s)

    #playing_elev11.comboBox_8.addItem('')
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_19.addItem(ss)
        playing_elev11.comboBox_8.addItem(s)

    
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_20.addItem(ss)
        playing_elev11.comboBox_9.addItem(s)

    
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_21.addItem(ss)
        playing_elev11.comboBox_10.addItem(s)

    
    for i in range(0,15):
        s=playing_team_selected1[i][0]
        ss=playing_team_selected1[i][1]
        playing_elev11.comboBox_22.addItem(ss)
        playing_elev11.comboBox_11.addItem(s)

    # print(playing_elev11.comboBox.currentIndex())    
    '''
    playing_elev11.comboBox_12.setItemText(0,str(playing_team_selected1[int(playing_elev11.comboBox.currentIndex())][1]))
    playing_elev11.comboBox_13.setEditText(str(playing_team_selected1[int(playing_elev11.comboBox_2.currentIndex())][1]))
    playing_elev11.comboBox_14.setEditText(str(playing_team_selected1[int(playing_elev11.comboBox_3.currentIndex())][1]))
    playing_elev11.comboBox_15.setEditText(str(playing_team_selected1[int(playing_elev11.comboBox_4.currentIndex())][1]))
    playing_elev11.comboBox_16.setEditText(str(playing_team_selected1[int(playing_elev11.comboBox_5.currentIndex())][1]))
    playing_elev11.comboBox_17.setEditText(str(playing_team_selected1[int(playing_elev11.comboBox_6.currentIndex())][1]))
    playing_elev11.comboBox_18.setEditText(str(playing_team_selected1[int(playing_elev11.comboBox_7.currentIndex())][1]))
    playing_elev11.comboBox_19.setEditText(str(playing_team_selected1[int(playing_elev11.comboBox_8.currentIndex())][1]))
    playing_elev11.comboBox_20.setEditText(str(playing_team_selected1[int(playing_elev11.comboBox_9.currentIndex())][1]))
    playing_elev11.comboBox_21.setEditText(str(playing_team_selected1[int(playing_elev11.comboBox_10.currentIndex())][1]))
    playing_elev11.comboBox_22.setEditText(str(playing_team_selected1[int(playing_elev11.comboBox_11.currentIndex())][1]))
    '''
        
    '''global team_batting,team_bowling
    team_batting=team1_name
    team_bowling=team2_name
    
    MainWindow125.show()
    #to be edited for playing_eleven
    sl121.label_2.setText(team_batting)
    sl121.label_4.setText(team_bowling)
    if team_batting==team1_name:
        x1=list(team1)
        x2=list(team2)
    else :
        x1=list(team2)
        x2=list(team1)
    sl121.comboBox.clear()    
    for i in range(0,11):
        s=x2[i][2][0]
        sl121.comboBox.addItem(s)'''


def playing_elev1_playing_elev2():
    global team1,team2
    team1[0][2][0]=playing_elev11.comboBox.currentText()
    team1[1][2][0]=playing_elev11.comboBox_2.currentText()
    team1[2][2][0]=playing_elev11.comboBox_3.currentText()
    team1[3][2][0]=playing_elev11.comboBox_4.currentText()
    team1[4][2][0]=playing_elev11.comboBox_5.currentText()
    team1[5][2][0]=playing_elev11.comboBox_6.currentText()
    team1[6][2][0]=playing_elev11.comboBox_7.currentText()
    team1[7][2][0]=playing_elev11.comboBox_8.currentText()
    team1[8][2][0]=playing_elev11.comboBox_9.currentText()
    team1[9][2][0]=playing_elev11.comboBox_10.currentText()
    team1[10][2][0]=playing_elev11.comboBox_11.currentText()
    team1[0][2][1]=playing_elev11.comboBox_12.currentText()
    team1[1][2][1]=playing_elev11.comboBox_13.currentText()
    team1[2][2][1]=playing_elev11.comboBox_14.currentText()
    team1[3][2][1]=playing_elev11.comboBox_15.currentText()
    team1[4][2][1]=playing_elev11.comboBox_16.currentText()
    team1[5][2][1]=playing_elev11.comboBox_17.currentText()
    team1[6][2][1]=playing_elev11.comboBox_18.currentText()
    team1[7][2][1]=playing_elev11.comboBox_19.currentText()
    team1[8][2][1]=playing_elev11.comboBox_20.currentText()
    team1[9][2][1]=playing_elev11.comboBox_21.currentText()
    team1[10][2][1]=playing_elev11.comboBox_22.currentText()

    MainWindow_elev1.close()
    MainWindow_elev2.show()
    playing_elev21.label_13.setText(str(team2_name))

    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_12.addItem(ss)
        playing_elev21.comboBox.addItem(s)
           

    
    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_13.addItem(ss)
        playing_elev21.comboBox_2.addItem(s)

    #playing_elev11.comboBox_3.addItem('')
    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_14.addItem(ss)
        playing_elev21.comboBox_3.addItem(s)

    #playing_elev11.comboBox_4.addItem('')
    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_15.addItem(ss)
        playing_elev21.comboBox_4.addItem(s)

    #playing_elev11.comboBox_5.addItem('')
    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_16.addItem(ss)
        playing_elev21.comboBox_5.addItem(s)

    #playing_elev11.comboBox_6.addItem('')
    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_17.addItem(ss)
        playing_elev21.comboBox_6.addItem(s)

    #playing_elev11.comboBox_7.addItem('')
    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_18.addItem(ss)
        playing_elev21.comboBox_7.addItem(s)

    #playing_elev11.comboBox_8.addItem('')
    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_19.addItem(ss)
        playing_elev21.comboBox_8.addItem(s)

    
    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_20.addItem(ss)
        playing_elev21.comboBox_9.addItem(s)

    
    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_21.addItem(ss)
        playing_elev21.comboBox_10.addItem(s)

    
    for i in range(0,15):
        s=playing_team_selected2[i][0]
        ss=playing_team_selected2[i][1]
        playing_elev21.comboBox_22.addItem(ss)
        playing_elev21.comboBox_11.addItem(s)

        
    '''
    playing_elev21.comboBox_12.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox.currentIndex())][1]))
    playing_elev21.comboBox_13.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox_2.currentIndex())][1]))
    playing_elev21.comboBox_14.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox_3.currentIndex())][1]))
    playing_elev21.comboBox_15.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox_4.currentIndex())][1]))
    playing_elev21.comboBox_16.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox_5.currentIndex())][1]))
    playing_elev21.comboBox_17.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox_6.currentIndex())][1]))
    playing_elev21.comboBox_18.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox_7.currentIndex())][1]))
    playing_elev21.comboBox_19.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox_8.currentIndex())][1]))
    playing_elev21.comboBox_20.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox_9.currentIndex())][1]))
    playing_elev21.comboBox_21.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox_10.currentIndex())][1]))
    playing_elev21.comboBox_22.setEditText(str(playing_team_selected2[int(playing_elev21.comboBox_11.currentIndex())][1]))
    '''
    
def playing_elev2_playing_elev1():
    MainWindow_elev2.close()
    MainWindow_elev1.show()
    playing_elev11.label_13.setText(str(team1_name))


def playing_elev2_sl12():

    global team1,team2
    team2[0][2][0]=playing_elev21.comboBox.currentText()
    team2[1][2][0]=playing_elev21.comboBox_2.currentText()
    team2[2][2][0]=playing_elev21.comboBox_3.currentText()
    team2[3][2][0]=playing_elev21.comboBox_4.currentText()
    team2[4][2][0]=playing_elev21.comboBox_5.currentText()
    team2[5][2][0]=playing_elev21.comboBox_6.currentText()
    team2[6][2][0]=playing_elev21.comboBox_7.currentText()
    team2[7][2][0]=playing_elev21.comboBox_8.currentText()
    team2[8][2][0]=playing_elev21.comboBox_9.currentText()
    team2[9][2][0]=playing_elev21.comboBox_10.currentText()
    team2[10][2][0]=playing_elev21.comboBox_11.currentText()
    team2[0][2][1]=playing_elev21.comboBox_12.currentText()
    team2[1][2][1]=playing_elev21.comboBox_13.currentText()
    team2[2][2][1]=playing_elev21.comboBox_14.currentText()
    team2[3][2][1]=playing_elev21.comboBox_15.currentText()
    team2[4][2][1]=playing_elev21.comboBox_16.currentText()
    team2[5][2][1]=playing_elev21.comboBox_17.currentText()
    team2[6][2][1]=playing_elev21.comboBox_18.currentText()
    team2[7][2][1]=playing_elev21.comboBox_19.currentText()
    team2[8][2][1]=playing_elev21.comboBox_20.currentText()
    team2[9][2][1]=playing_elev21.comboBox_21.currentText()
    team2[10][2][1]=playing_elev21.comboBox_22.currentText()

    global team_batting,team_bowling
    team_batting=team1_name
    team_bowling=team2_name
    MainWindow_elev2.close()
    MainWindow125.show()
    #to be edited for playing_eleven
    sl121.label_2.setText(team_batting)
    sl121.label_4.setText(team_bowling)
    if team_batting==team1_name:
        x1=list(team1)
        x2=list(team2)
    else :
        x1=list(team2)
        x2=list(team1)
    sl121.comboBox.clear()    
    for i in range(0,11):
        s=x2[i][2][0]
        sl121.comboBox.addItem(s)
    

def sl12_Main():
    
    global current_bowler
    current_bowler=sl121.comboBox.currentIndex()
    MainWindow125.close()
    MainWindow007.show()
    if team_batting==team1_name:
        x1=list(team1)
        x2=list(team2)
    else :
        x1=list(team2)
        x2=list(team1)
    initilise(x1,x2)

def Main_sl4():
    MainWindow05.show()
    sl41.label_2.setText(str(team_batting))
    sl41.label_4.setText(str(total_run)+'/'+str(total_wicket)+'('+str(over)+')')
    sl41.label_6.setText(str(extras))
    if team_batting==team1_name:
        x=team1
        x2=list(team2)
    else :
        x=team2
        x2=list(team1)
    sl41.label01.setText(str(x[0][2][0]))
    sl41.label02.setText(str(x[1][2][0]))
    sl41.label03.setText(str(x[2][2][0]))
    sl41.label04.setText(str(x[3][2][0]))
    sl41.label05.setText(str(x[4][2][0]))
    sl41.label06.setText(str(x[5][2][0]))
    sl41.label07.setText(str(x[6][2][0]))
    sl41.label08.setText(str(x[7][2][0]))
    sl41.label09.setText(str(x[8][2][0]))
    sl41.label010.setText(str(x[9][2][0]))
    sl41.label011.setText(str(x[10][2][0]))
    sl41.label11.setText(str(x[0][0][4])+str(x[0][0][5]))
    sl41.label12.setText(str(x[1][0][4])+str(x[1][0][5]))
    sl41.label13.setText(str(x[2][0][4])+str(x[2][0][5]))
    sl41.label14.setText(str(x[3][0][4])+str(x[3][0][5]))
    sl41.label15.setText(str(x[4][0][4])+str(x[4][0][5]))
    sl41.label16.setText(str(x[5][0][4])+str(x[5][0][5]))
    sl41.label17.setText(str(x[6][0][4])+str(x[6][0][5]))
    sl41.label18.setText(str(x[7][0][4])+str(x[7][0][5]))
    sl41.label19.setText(str(x[8][0][4])+str(x[8][0][5]))
    sl41.label110.setText(str(x[9][0][4])+str(x[9][0][5]))
    sl41.label111.setText(str(x[10][0][4])+str(x[10][0][5]))
    sl41.label21.setText(str(x[0][0][0])+' ('+str(x[0][0][1])+')')
    sl41.label22.setText(str(x[1][0][0])+' ('+str(x[1][0][1])+')')
    sl41.label23.setText(str(x[2][0][0])+' ('+str(x[2][0][1])+')')
    sl41.label24.setText(str(x[3][0][0])+' ('+str(x[3][0][1])+')')
    sl41.label25.setText(str(x[4][0][0])+' ('+str(x[4][0][1])+')')
    sl41.label26.setText(str(x[5][0][0])+' ('+str(x[5][0][1])+')')
    sl41.label27.setText(str(x[6][0][0])+' ('+str(x[6][0][1])+')')
    sl41.label28.setText(str(x[7][0][0])+' ('+str(x[7][0][1])+')')
    sl41.label29.setText(str(x[8][0][0])+' ('+str(x[8][0][1])+')')
    sl41.label210.setText(str(x[9][0][0])+' ('+str(x[9][0][1])+')')
    sl41.label211.setText(str(x[10][0][0])+' ('+str(x[10][0][1])+')')
    MainWindow05.update()
    
def exe_sl4():
    MainWindow05.close()
def exe_sl6():
    MainWindow009.close()

def exe_sl10():
    MainWindow10.close()

def exe_fall():
    MainWindow22.close()
    
def Main_sl6():
    MainWindow009.show()
    sl61.label_5.setText(str(total_run)+'/'+str(total_wicket)+' ('+str(over)+')')
    if team_batting==team1_name:
        x=team1
    else:
        x=team2
    sl61.label11_2.setText(str(x[0][2][0]))
    sl61.label21_2.setText(str(x[1][2][0]))
    sl61.label31_2.setText(str(x[2][2][0]))
    sl61.label41_2.setText(str(x[3][2][0]))
    sl61.label51_2.setText(str(x[4][2][0]))
    sl61.label61_2.setText(str(x[5][2][0]))
    sl61.label71_2.setText(str(x[6][2][0]))
    sl61.label81_2.setText(str(x[7][2][0]))
    sl61.label91_3.setText(str(x[8][2][0]))
    sl61.label101_2.setText(str(x[9][2][0]))
    sl61.label_2.setText(str(x[10][2][0]))
    sl61.label12_2.setText(str(x[0][0][0]))
    sl61.label22_2.setText(str(x[1][0][0]))
    sl61.label32_2.setText(str(x[2][0][0]))
    sl61.label42_2.setText(str(x[3][0][0]))
    sl61.label52_2.setText(str(x[4][0][0]))
    sl61.label62_2.setText(str(x[5][0][0]))
    sl61.label72_2.setText(str(x[6][0][0]))
    sl61.label82_2.setText(str(x[7][0][0]))
    sl61.label92_2.setText(str(x[8][0][0]))
    sl61.label102_2.setText(str(x[9][0][0]))
    sl61.label112_2.setText(str(x[10][0][0]))
    sl61.label13_2.setText(str(x[0][0][1]))
    sl61.label23_2.setText(str(x[1][0][1]))
    sl61.label33_2.setText(str(x[2][0][1]))
    sl61.label43_2.setText(str(x[3][0][1]))
    sl61.label53_2.setText(str(x[4][0][1]))
    sl61.label63_2.setText(str(x[5][0][1]))
    sl61.label73_2.setText(str(x[6][0][1]))
    sl61.label83_2.setText(str(x[7][0][1]))
    sl61.label93_2.setText(str(x[8][0][1]))
    sl61.label103_2.setText(str(x[9][0][1]))
    sl61.label113_2.setText(str(x[10][0][1]))
    sl61.label14_2.setText(str(x[0][0][2]))
    sl61.label24_2.setText(str(x[1][0][2]))
    sl61.label34_2.setText(str(x[2][0][2]))
    sl61.label44_2.setText(str(x[3][0][2]))
    sl61.label54_2.setText(str(x[4][0][2]))
    sl61.label64_2.setText(str(x[5][0][2]))
    sl61.label74_2.setText(str(x[6][0][2]))
    sl61.label84_2.setText(str(x[7][0][2]))
    sl61.label94_2.setText(str(x[8][0][2]))
    sl61.label104_2.setText(str(x[9][0][2]))
    sl61.label114_2.setText(str(x[10][0][2]))
    sl61.label15_2.setText(str(x[0][0][3]))
    sl61.label25_2.setText(str(x[1][0][3]))
    sl61.label35_2.setText(str(x[2][0][3]))
    sl61.label45_2.setText(str(x[3][0][3]))
    sl61.label55_2.setText(str(x[4][0][3]))
    sl61.label65_2.setText(str(x[5][0][3]))
    sl61.label75_2.setText(str(x[6][0][3]))
    sl61.label85_2.setText(str(x[7][0][3]))
    sl61.label95_2.setText(str(x[8][0][3]))
    sl61.label105_2.setText(str(x[9][0][3]))
    sl61.label115_2.setText(str(x[10][0][3]))
    
        
    sl61.label16_2.setText(str(strike(x[0][0][0],x[0][0][1])))
    sl61.label26_2.setText(str(strike(x[1][0][0],x[1][0][1])))
    sl61.label36_2.setText(str(strike(x[2][0][0],x[2][0][1])))
    sl61.label46_2.setText(str(strike(x[3][0][0],x[3][0][1])))
    sl61.label56_2.setText(str(strike(x[4][0][0],x[4][0][1])))
    sl61.label66_2.setText(str(strike(x[5][0][0],x[5][0][1])))
    sl61.label76_2.setText(str(strike(x[6][0][0],x[6][0][1])))
    sl61.label86_2.setText(str(strike(x[7][0][0],x[7][0][1])))
    sl61.label96_2.setText(str(strike(x[8][0][0],x[8][0][1])))
    sl61.label106_2.setText(str(strike(x[9][0][0],x[9][0][1])))
    sl61.label116_2.setText(str(strike(x[10][0][0],x[10][0][1])))
    MainWindow009.update()
    
def Main_sl10():
    
    if team_batting==team1_name:
        x1=list(team1)
        x=list(team2)
    else :
        x1=list(team2)
        x=list(team1)
    sl101.label_2.setText(str(total_run)+'/'+str(total_wicket)+' ('+str(over)+')')
    max=0
    for i in range(0,10):
        for j in range(i+1,11):
            if(x[j][1][0]>=x[i][1][0]):
                x[j],x[i]=swap(x[j],x[i])
             
    sl101.label11.setText(str(x[0][2][0]))
    sl101.label21.setText(str(x[1][2][0]))
    sl101.label31.setText(str(x[2][2][0]))
    sl101.label41.setText(str(x[3][2][0]))
    sl101.label51.setText(str(x[4][2][0]))
    sl101.label61.setText(str(x[5][2][0]))
    sl101.label71.setText(str(x[6][2][0]))
    sl101.label81.setText(str(x[7][2][0]))
    sl101.label91.setText(str(x[8][2][0]))
    sl101.label101.setText(str(x[9][2][0]))
    sl101.label111.setText(str(x[10][2][0]))
    sl101.label12.setText(str(x[0][1][0])+'    -    '+str(x[0][1][1])+'    -    '+str(x[0][1][3])+'    -    '+str(eco(x[0][1][0],x[0][1][1]))+'    -    '+str(x[0][1][2])+'    -    '+str(x[0][1][4])+'    -    '+str(x[0][1][5]))
    sl101.label22.setText(str(x[1][1][0])+'    -    '+str(x[1][1][1])+'    -    '+str(x[1][1][3])+'    -    '+str(eco(x[1][1][0],x[1][1][1]))+'    -    '+str(x[1][1][2])+'    -    '+str(x[1][1][4])+'    -    '+str(x[1][1][5]))
    sl101.label32.setText(str(x[2][1][0])+'    -    '+str(x[2][1][1])+'    -    '+str(x[2][1][3])+'    -    '+str(eco(x[2][1][0],x[2][1][1]))+'    -    '+str(x[2][1][2])+'    -    '+str(x[2][1][4])+'    -    '+str(x[2][1][5]))
    sl101.label42.setText(str(x[3][1][0])+'    -    '+str(x[3][1][1])+'    -    '+str(x[3][1][3])+'    -    '+str(eco(x[3][1][0],x[3][1][1]))+'    -    '+str(x[3][1][2])+'    -    '+str(x[3][1][4])+'    -    '+str(x[3][1][5]))
    sl101.label52.setText(str(x[4][1][0])+'    -    '+str(x[4][1][1])+'    -    '+str(x[4][1][3])+'    -    '+str(eco(x[4][1][0],x[4][1][1]))+'    -    '+str(x[4][1][2])+'    -    '+str(x[4][1][4])+'    -    '+str(x[4][1][5]))
    sl101.label62.setText(str(x[5][1][0])+'    -    '+str(x[5][1][1])+'    -    '+str(x[5][1][3])+'    -    '+str(eco(x[5][1][0],x[5][1][1]))+'    -    '+str(x[5][1][2])+'    -    '+str(x[5][1][4])+'    -    '+str(x[5][1][5]))
    sl101.label72.setText(str(x[6][1][0])+'    -    '+str(x[6][1][1])+'    -    '+str(x[6][1][3])+'    -    '+str(eco(x[6][1][0],x[6][1][1]))+'    -    '+str(x[6][1][2])+'    -    '+str(x[6][1][4])+'    -    '+str(x[6][1][5]))
    sl101.label82.setText(str(x[7][1][0])+'    -    '+str(x[7][1][1])+'    -    '+str(x[7][1][3])+'    -    '+str(eco(x[7][1][0],x[7][1][1]))+'    -    '+str(x[7][1][2])+'    -    '+str(x[7][1][4])+'    -    '+str(x[7][1][5]))
    sl101.label92.setText(str(x[8][1][0])+'    -    '+str(x[8][1][1])+'    -    '+str(x[8][1][3])+'    -    '+str(eco(x[8][1][0],x[8][1][1]))+'    -    '+str(x[8][1][2])+'    -    '+str(x[8][1][4])+'    -    '+str(x[8][1][5]))
    sl101.label102.setText(str(x[9][1][0])+'    -    '+str(x[9][1][1])+'    -    '+str(x[9][1][3])+'    -    '+str(eco(x[9][1][0],x[9][1][1]))+'    -    '+str(x[9][1][2])+'    -    '+str(x[9][1][4])+'    -    '+str(x[9][1][5]))
    sl101.label112.setText(str(x[10][1][0])+'    -    '+str(x[10][1][1])+'    -    '+str(x[10][1][3])+'    -    '+str(eco(x[10][1][0],x[10][1][1]))+'    -    '+str(x[10][1][2])+'    -    '+str(x[10][1][4])+'    -    '+str(x[10][1][5]))
    MainWindow10.update()
    MainWindow10.show()
    
    
def Main_fall():
    MainWindow22.show()
    if team_batting==team1_name:
        x1=list(team1)
        x=list(team2)
    else :
        x1=list(team2)
        x=list(team1)
    fall1.label_2.setText(team_batting)
    fall1.label_3.setText(str(total_run)+'/'+str(total_wicket)+' ('+str(over)+')')
    fall1.label_15.setText(str(extras))
    fall1.label01.setText(str(wicket_fall[0][0])+'/'+str(wicket_fall[0][1]))
    fall1.label02.setText(str(wicket_fall[1][0])+'/'+str(wicket_fall[1][1]))
    fall1.label03.setText(str(wicket_fall[2][0])+'/'+str(wicket_fall[2][1]))
    fall1.label04.setText(str(wicket_fall[3][0])+'/'+str(wicket_fall[3][1]))
    fall1.label05.setText(str(wicket_fall[4][0])+'/'+str(wicket_fall[4][1]))
    fall1.label06.setText(str(wicket_fall[5][0])+'/'+str(wicket_fall[5][1]))
    fall1.label07.setText(str(wicket_fall[6][0])+'/'+str(wicket_fall[6][1]))
    fall1.label08.setText(str(wicket_fall[7][0])+'/'+str(wicket_fall[7][1]))
    fall1.label09.setText(str(wicket_fall[8][0])+'/'+str(wicket_fall[8][1]))
    fall1.label10.setText(str(wicket_fall[9][0])+'/'+str(wicket_fall[9][1]))
    
def Extras(q,r,w1,w2):
    '''q=status
        r=run,w1=batting team,w2=bowling team'''
    global current_bowler,total_run,over,this_over,extras,over
    f=0
    if q=='No ball':
         
        total_run=total_run+1+r
        w2[current_bowler][1][1]=w2[current_bowler][1][1]+1+r
        w2[current_bowler][1][5]=w2[current_bowler][1][5]+1
        w2[current_bowler][1][0]=ball_over(over_ball(w2[current_bowler][1][0])-1)
        w1[current_batsman1][0][1]=w1[current_batsman1][0][1]-1
        over=ball_over(over_ball(over)-1)
        this_over=this_over+1+r
        extras=extras+1+r
        f=1
    elif q=='Wide':
        total_run=total_run+1+r
        w2[current_bowler][1][1]=w2[current_bowler][1][1]+1+r
        w2[current_bowler][1][4]=w2[current_bowler][1][4]+1
        w2[current_bowler][1][0]=ball_over(over_ball(w2[current_bowler][1][0])-1)
        w1[current_batsman1][0][1]=w1[current_batsman1][0][1]-1
        over=ball_over(over_ball(over)-1)
        this_over=this_over+1+r
        extras=extras+1+r
        f=1
    elif q=='Leg bye':
        total_run=total_run+r
        w2[current_bowler][1][1]=w2[current_bowler][1][1]+r
        this_over=this_over+r
        extras=extras+r
    elif q=='Bye':
        total_run=total_run+r
        w2[current_bowler][1][1]=w2[current_bowler][1][1]+r
        this_over=this_over+r
        
        extras=extras+r
    return(w1,w2,f)   


def Runs(q,w1,w2):
    
    global total_run,over,this_over,extras,current_batsman1,current_batsman2
    if q=='1':
        w1[current_batsman1][0][0]=w1[current_batsman1][0][0]+1
        total_run=total_run+1
        w2[current_bowler][1][1]=w2[current_bowler][1][1]+1
        this_over=this_over+1
        current_batsman1,current_batsman2=swap(current_batsman1,current_batsman2)
    elif q=='2':
        w1[current_batsman1][0][0]=w1[current_batsman1][0][0]+2
        total_run=total_run+2
        w2[current_bowler][1][1]=w2[current_bowler][1][1]+2
        this_over=this_over+2
    elif q=='3':
        w1[current_batsman1][0][0]=w1[current_batsman1][0][0]+3
        total_run=total_run+3
        w2[current_bowler][1][1]=w2[current_bowler][1][1]+3
        this_over=this_over+3
        current_batsman1,current_batsman2=swap(current_batsman1,current_batsman2)
    elif q=='4':
        w1[current_batsman1][0][0]=w1[current_batsman1][0][0]+4
        total_run=total_run+4
        w2[current_bowler][1][1]=w2[current_bowler][1][1]+4
        this_over=this_over+4
        w1[current_batsman1][0][3]=w1[current_batsman1][0][3]+1
    elif q=='5':
        w1[current_batsman1][0][0]=w1[current_batsman1][0][0]+5
        total_run=total_run+5
        w2[current_bowler][1][1]=w2[current_bowler][1][1]+5
        this_over=this_over+5
        current_batsman1,current_batsman2=swap(current_batsman1,current_batsman2)
    elif q=='6':
        w1[current_batsman1][0][0]=w1[current_batsman1][0][0]+6
        total_run=total_run+6
        w2[current_bowler][1][1]=w2[current_bowler][1][1]+6
        this_over=this_over+6
        w1[current_batsman1][0][2]=w1[current_batsman1][0][2]+1   
    return w1,w2  
        
def Main_update():
    
    f=0
    global wicket_fall1,wicket_fall2,wicket_fall,team1,team2,k,total_over,total_run1,total_run,total_run2,total_wicket1,total_wicket2,total_wicket,current_batsman1,current_batsman2,extras,extra1,extra2,over,over1,over2,team_bowling,team_batting,batsman_played
    global winner,dec,te,this_over,last_over,batsman2_index_dup
    #
    global batsman_index_dup,bowler_index_dup,back_goto_batsman,back_goto_bowler,wicket_fall_dup,this_over_d,last_over_d,back_index,total_run_dup,total_wicket_dup,over_dup,extra_dup


    if team_batting==team1_name:
        x1=list(team1)
        x2=list(team2)
    else :
        x1=list(team2)
        x2=list(team1)

        
    back_goto_batsman=copy.deepcopy(x1[current_batsman1])
    back_goto_bowler=copy.deepcopy(x2[current_bowler])
    batsman_index_dup=current_batsman1
    batsman2_index_dup=current_batsman2
    bowler_index_dup=current_bowler
    wicket_fall_dup=wicket_fall
    this_over_d=this_over
    last_over_d=last_over
    over_dup=over
    total_run_dup=total_run
    total_wicket_dup=total_wicket
    extra_dup=extras

  
    


  
    
    
    if ((k==0 and (over<total_over and total_wicket<10)) or (k==1 and (over<total_over and total_wicket<10) and total_run<=total_run1)) and dec==0:
        
        if Main1.comboBox.currentText()=='Not Out':
            x1,x2,f=Extras(Main1.comboBox_3.currentText(),int(Main1.comboBox_7.currentText()),x1,x2)
            x2[current_bowler][1][0]=ball_over(over_ball(x2[current_bowler][1][0])+1)
            over = ball_over(over_ball(over)+1)
            x1[current_batsman1][0][1]=x1[current_batsman1][0][1]+1
            x1[current_batsman1][0][4]='<....not out.....>'
            x1,x2=Runs(Main1.comboBox_2.currentText(),x1,x2)

            if (over*10)%10==0 and f!=1 and over!=total_over:
                Main_sl5()
            else:    
                display_Main(x1,x2)
        
        
        elif Main1.comboBox.currentText()=='Bowled':
            x2[current_bowler][1][0]=ball_over(over_ball(x2[current_bowler][1][0])+1)
            over=ball_over(over_ball(over)+1)
            x1[current_batsman1][0][1]=x1[current_batsman1][0][1]+1
            x1[current_batsman1][0][4]='Bowled  by-> '                                   
            x1[current_batsman1][0][5]=x2[current_bowler][2][0]
            total_wicket=int(total_wicket)+1
            x2[current_bowler][1][3]=x2[current_bowler][1][3]+1                                   
            wicket_fall[total_wicket-1][0]=total_run
            wicket_fall[total_wicket-1][1]=total_wicket
            display_wicket(x1,x2)
            if (over*10)%10==0 and f!=1 and over!=total_over:
            
                te=1
            
                
        elif Main1.comboBox.currentText()=='Caught':
            x2[current_bowler][1][0]=ball_over(over_ball(x2[current_bowler][1][0])+1)
            over=ball_over(over_ball(over)+1)
            x1[current_batsman1][0][1]=x1[current_batsman1][0][1]+1
            x1[current_batsman1][0][4]='Caught by-> '                                   
            x1[current_batsman1][0][5]=x2[current_bowler][2][0]
            total_wicket=int(total_wicket)+1
            x2[current_bowler][1][3]=x2[current_bowler][1][3]+1                                   
            wicket_fall[total_wicket-1][0]=total_run
            wicket_fall[total_wicket-1][1]=total_wicket
            display_wicket(x1,x2)
            if (over*10)%10==0 and f!=1 and over!=total_over:
                te=1
            
               
        
        elif Main1.comboBox.currentText()=='LBW':
            x2[current_bowler][1][0]=ball_over(over_ball(x2[current_bowler][1][0])+1)
            over=ball_over(over_ball(over)+1)
            x1[current_batsman1][0][1]=x1[current_batsman1][0][1]+1
            x1[current_batsman1][0][4]='lbw by-> '                                   
            x1[current_batsman1][0][5]=x2[current_bowler][2][0]
            total_wicket=int(total_wicket)+1
            x2[current_bowler][1][3]=x2[current_bowler][1][3]+1                                   
            wicket_fall[total_wicket-1][0]=total_run
            wicket_fall[total_wicket-1][1]=total_wicket
            display_wicket(x1,x2)
            if (over*10)%10==0 and f!=1 and over!=total_over:
                te=1
            
                
        elif Main1.comboBox.currentText()=='Stumped':
            x2[current_bowler][1][0]=ball_over(over_ball(x2[current_bowler][1][0])+1)
            over=ball_over(over_ball(over)+1)
            x1[current_batsman1][0][1]=x1[current_batsman1][0][1]+1
            x1[current_batsman1][0][4]='Stumped by-> '                                   
            x1[current_batsman1][0][5]=x2[current_bowler][2][0]
            total_wicket=int(total_wicket)+1
            x2[current_bowler][1][3]=x2[current_bowler][1][3]+1                                   
            wicket_fall[total_wicket-1][0]=total_run
            wicket_fall[total_wicket-1][1]=total_wicket
            display_wicket(x1,x2)
            if (over*10)%10==0 and f!=1 and over!=total_over:
                te=1
            
        elif Main1.comboBox.currentText()=='Hit wicket':
            x2[current_bowler][1][0]=ball_over(over_ball(x2[current_bowler][1][0])+1)
            over=ball_over(over_ball(over)+1)
            x1[current_batsman1][0][1]=x1[current_batsman1][0][1]+1
            x1[current_batsman1][0][4]='Hit Wicket ->'                                   
            x1[current_batsman1][0][5]=x2[current_bowler][2][0]
            total_wicket=int(total_wicket)+1
            x2[current_bowler][1][3]=x2[current_bowler][1][3]+1                                   
            wicket_fall[total_wicket-1][0]=total_run
            wicket_fall[total_wicket-1][1]=total_wicket
            display_wicket(x1,x2)
            if (over*10)%10==0 and f!=1 and over!=total_over:
                te=1
            
               
        elif Main1.comboBox.currentText()=='Runout':
            x1,x2,f=Extras(Main1.comboBox_3.currentText(),int(Main1.comboBox_7.currentText()),x1,x2)
            x2[current_bowler][1][0]=ball_over(over_ball(x2[current_bowler][1][0])+1)
            over=ball_over(over_ball(over)+1)
            x1[current_batsman1][0][1]=x1[current_batsman1][0][1]+1
            x1,x2=Runs(Main1.comboBox_2.currentText(),x1,x2)
            x1[current_batsman1][0][4]='Run Out -> '
            x1[current_batsman1][0][5]=''
            total_wicket=int(total_wicket)+1
            x2[current_bowler][1][3]=x2[current_bowler][1][3]+1                                   
            wicket_fall[total_wicket-1][0]=total_run
            wicket_fall[total_wicket-1][1]=total_wicket
            display_wicket(x1,x2)
            if (over*10)%10==0 and f!=1 and over!=total_over:
                te=1
               
    if (k==0 and (over==total_over or total_wicket==10) ) or dec==1:
        k=k+1
        total_run1=total_run
        total_wicket1=total_wicket
        extra1=extras
        current_batsman1,current_batsman2=0,1
        over1=over
        if this_over==0 and dec==0:
            team2[current_bowler][1][2]=team2[current_bowler][1][2]+1
        team_batting=team2_name
        team_bowling=team1_name
        wicket_fall1=list(wicket_fall)
        Main_sl12()
        if team_batting==team1_name:
            x1=list(team1)
            x2=list(team2)
        else :
            x1=list(team2)
            x2=list(team1)
        wicket_fall=[['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['','']]
        last_over,this_over=0,0
        total_run=0
        total_wicket=0
        extras=0
        over=0
        batsman_played=[0,1]
   
    if (k==1 and (over==total_over or total_wicket==10 or total_run>total_run1)) or dec==2:
        
        k=k+1
        total_run2=total_run
        total_wicket2=total_wicket
        extra2=extras
        if this_over==0:
            team1[current_bowler][1][2]=team1[current_bowler][1][2]+1
        wicket_fall2=list(wicket_fall)
        over2=over
        MainWindow007.close()
        MainWindow.show()
        last1.label_3.setText(str(team1_name))
        last1.label_2.setText(str(team2_name))
        last1.label_4.setText(str(total_run1)+'/'+str(total_wicket1)+' ('+str(over1)+')')
        last1.label_5.setText(str(total_run2)+'/'+str(total_wicket2)+' ('+str(over2)+')')
        if total_run1==total_run2:
            winner='MATCH is TIE'
        elif  total_run1>total_run2:
            winner=team1_name+' WON the match by ->'+str(total_run1-total_run2)+' runs'
        else:
            winner=team2_name+' WON the match by ->'+str(10-total_wicket2)+' wickets'
        s='This was excitting match between---'+str(team1_name)+' V/S '+str(team2_name)+'---  ,Result WAs  -> '+str(winner)
        last1.textBrowser.setText(s)
            
    if team_batting==team1_name:
        team1=x1
        team2=x2
    else :
        team2=x1
        team1=x2

    
          
                                           
def display_wicket(z,q):
    if total_wicket<10:
        MainWindow007.close()
        MainWindow011.show()
        sl81.label_2.setText(str(total_run)+'/'+str(total_wicket)+' ('+str(over)+')')
        sl81.label_4.setText(str(over))
        sl81.label_6.setText(str(extras))
        sl81.textBrowser.setText('Wicket is Taken By ->'+q[current_bowler][2][0])
        sl81.comboBox.clear()
        for i in range(0,11):
            if i not in batsman_played:
                sl81.comboBox.addItem(z[i][2][0])
    
            
            
def wicket_Main():
    global current_batsman1,te
    if team_batting==team1_name:
        x1=list(team1)
        x2=list(team2)
    else :
        x1=list(team2)
        x2=list(team1)
    if te==0:    
        for i in range(0,11):
            if x1[i][2][0]==sl81.comboBox.currentText():
                current_batsman1=i    
        batsman_played.append(current_batsman1)
        MainWindow011.close()
        MainWindow007.show()
        display_Main(x1,x2)
    elif te==1:
        if team_batting==team1_name:
            x1=list(team1)
            x2=list(team2)
        else :
            x1=list(team2)
            x2=list(team1)    
        for i in range(0,11):
            if x1[i][2][0]==sl81.comboBox.currentText():
                current_batsman1=i    
        batsman_played.append(current_batsman1)
        MainWindow011.close()
        Main_sl5()
        te=0
        

def display_Main(t1,t2):
    Main1.lcdNumber.display(float(over))
    Main1.label_2.setText(str(total_run)+'/'+str(total_wicket)+' ('+str(over)+')')
    Main1.label_8.setText(str(extras))
    Main1.label_14.setText(str(eco(over,total_run)))
    Main1.label_18.setText(str(last_over))
    Main1.label_16.setText(team_bowling)
    if team_batting==team1_name:
        Main1.label_19.setText(str(team2_name)+' have not yet batted ')
    else:
        Main1.label_19.setText(str(team1_name)+' -> '+str(total_run1)+'/'+str(total_wicket1)+'('+str(over1)+')  '+str(team2_name)+' Need '+str(total_run1-total_run+1)+' run more to win.')
    Main1.label_4.setText(t2[current_bowler][2][0]+' '+str(t2[current_bowler][1][0])+'-'+str(t2[current_bowler][1][1])+'-'+str(t2[current_bowler][1][3]))
    Main1.label_15.setText(team_batting)
    Main1.label_5.setText(t1[current_batsman1][2][0]+' '+str(t1[current_batsman1][0][0])+'('+str(t1[current_batsman1][0][1])+')')
    Main1.label_6.setText(t1[current_batsman2][2][0]+' '+str(t1[current_batsman2][0][0])+'('+str(t1[current_batsman2][0][1])+')')

    #edited on 1-3-2013
    
    Main1.comboBox.setCurrentIndex(int(0))
    Main1.comboBox_2.setCurrentIndex(int(0))
    Main1.comboBox_3.setCurrentIndex(int(0))
    Main1.comboBox_7.setCurrentIndex(int(0))
    #
    
    MainWindow007.update()

def Main_sl12():
    if team_batting==team1_name:
        x1=list(team1)
        x2=list(team2)
    else :
        x1=list(team2)
        x2=list(team1)
        
    MainWindow007.close()
    MainWindow125.show()
    sl121.label_2.setText(team_batting)
    sl121.label_4.setText(team_bowling)
    sl121.comboBox.clear()
    for i in range(0,11):
        s=x2[i][2][0]
        sl121.comboBox.addItem(s)

def Main_sl5():
    global this_over,last_over,team1,team2
    MainWindow007.close()
    MainWindow008.show()
    if team_batting==team1_name:
        x1=list(team1)
        x2=list(team2)
    else :
        x1=list(team2)
        x2=list(team1)  
    sl51.label_2.setText(str(total_run)+'/'+str(total_wicket)+' ('+str(over)+')')
    sl51.lcdNumber.display(float(over))
    sl51.label_6.setText(str(extras))
    if this_over==0:
        x2[current_bowler][1][2]=x2[current_bowler][1][2]+1
    last_over=this_over
    this_over=0
    sl51.textBrowser.setText('LAST OVER  ->'+str(last_over))
    if team_batting==team1_name:
        team1=list(x1)
        team2=list(x2)
    else :
        team2=list(x1)
        team1=list(x2)
    sl51.comboBox.clear()
    for i in range(0,11):
        if i!=current_bowler:
            sl51.comboBox.addItem(str(x2[i][2][0]))
            
def sl5_Main():
    global current_batsman1,current_batsman2,current_bowler
    if team_batting==team1_name:
        x1=list(team1)
        x2=list(team2)
    else :
        x1=list(team2)
        x2=list(team1)
    for i in range(0,11):
        if x2[i][2][0]==sl51.comboBox.currentText():
            current_bowler=i
        
    
    MainWindow008.close()
    MainWindow007.show()
    
    current_batsman1,current_batsman2=swap(current_batsman1,current_batsman2)   
    display_Main(x1,x2)    
                         
def Main_change():
    global current_batsman1,current_batsman2
    if team_batting==team1_name:
        t1=list(team1)
        t2=list(team2)
    else :
        t1=list(team2)
        t2=list(team1)    
    current_batsman1,current_batsman2=swap(current_batsman1,current_batsman2)
    Main1.label_5.setText(t1[current_batsman1][2][0]+' '+str(t1[current_batsman1][0][0])+'('+str(t1[current_batsman1][0][1])+')')
    Main1.label_6.setText(t1[current_batsman2][2][0]+' '+str(t1[current_batsman2][0][0])+'('+str(t1[current_batsman2][0][1])+')')
    
    MainWindow007.update()

def Record():
     global winner
     rec=open('saved_file/match_record.txt','w')
     s1='''That was awsome match betwen -- %s V/S %s --. The result was that %s '''%(str(team1_name),str(team2_name),str(winner))
     s2='''Team 1 ->  %s \t%s/%s (%s)  extras->%s
Team 2 ->  %s \t%s/%s (%s)  extras->%s'''%(str(team1_name),str(total_run1),str(total_wicket1),str(over1),str(extra1),str(team2_name),str(total_run2),str(total_wicket2),str(over2),str(extra2))
     s311='''%s \t %s/%s( %s)\t extra->%s'''%(str(team1_name),str(total_run1),str(total_wicket1),str(over1),str(extra1))
     s312=''' '''
     for i in range(0,11):
         s312=s312+'''\n%s\t%s\t%s\t%s(%s)'''%(team1[i][2][0],team1[i][0][4],team1[i][0][5],team1[i][0][0],team1[i][0][1])
     s321='''%s \t %s/%s( %s)\t extra->%s'''%(str(team2_name),str(total_run1),str(total_wicket2),str(over2),str(extra2))
     s322=''' '''
     for i in range(0,11):
         s322=s322+'''\n%s\t%s\t%s\t%s(%s)'''%(team2[i][2][0],team2[i][0][4],team2[i][0][5],team2[i][0][0],team2[i][0][1])
     s41,s42=''' ''',''' '''    
     for i in range(0,11):
         s41=s41+'''\n\nTEAM -> %s.......PLAYER NAME-> %s..........ATTRIBUTE-> %s
BATTING STATS:-\n\tRUN->%s\tBALL->%s\tFOURS->%s\tSIXES->%s\nBOWLING STATS:-\n\tOVER->%s\tRUN->%s\tMAIDEN->%s\tWICKET->%s\tWIDE BALLS->%s\tNO BALLS->%s'''%(str(team1_name),str(team1[i][2][0]),str(team1[i][2][1]),str(team1[i][0][0]),str(team1[i][0][1]),str(team1[i][0][3]),str(team1[i][0][2]),str(team1[i][1][0]),str(team1[i][1][1]),str(team1[i][1][2]),str(team1[i][1][3]),str(team1[i][1][4]),str(team1[i][1][5]))
     for i in range(0,11):
         s42=s42+'''\n\nTEAM -> %s.......PLAYER NAME-> %s..........ATTRIBUTE-> %s
BATTING STATS:-\n\tRUN->%s\tBALL->%s\tFOURS->%s\tSIXES->%s\nBOWLING STATS:-\n\tOVER->%s\tRUN->%s\tMAIDEN->%s\tWICKET->%s\tWIDE BALLS->%s\tNO BALLS->%s'''%(str(team2_name),str(team2[i][2][0]),str(team2[i][2][1]),str(team2[i][0][0]),str(team2[i][0][1]),str(team2[i][0][3]),str(team2[i][0][2]),str(team2[i][1][0]),str(team2[i][1][1]),str(team2[i][1][2]),str(team2[i][1][3]),str(team2[i][1][4]),str(team2[i][1][5]))
     s51='''WICKET FALL ->\n'''
     for i in range(0,total_wicket1):
         if i==5:
             s51=s51+'''\n'''
         s51=s51+'''%s/%s\t'''%(str(wicket_fall1[i][0]),str(wicket_fall1[i][1]))
     s52='''WICKET FALL ->\n'''
     for i in range(0,total_wicket2):
         if i==5:
             s52=s52+'''\n'''
         s52=s52+'''%s/%s\t'''%(str(wicket_fall2[i][0]),str(wicket_fall2[i][1]))    
     rec.write('\n'+s1+'\n\n'+'-'*100+'\n\n'+s2+'\n\n'+'-'*100+'\n\n'+s311+'\n'+s312+'\n'+s51+'\n\n'+'-'*100+'\n\n'+s321+'\n'+s322+'\n'+s52+'\n\n'+'-'*100+'\n\n'+s41+'\n'+'-'*100+'\n'+s42)
     rec.close()



def main_declare_quest():
    Dialogdec.show()

def declare_quest_main():
    Dialogdec.close()
   
     
def declare():
    global dec
    if k==0:
        dec=1
        Main_update()
        dec=0
    elif k==1:
        dec=2
        Main_update()

def add_record1():
    global team_name
    #localtime = time.asctime( time.localtime(time.time()) )
    reco=file('record/'+team_name+'.txt','w')
    reco.write(str(sl31.lineEdit01.text())+';'+str(sl31.comboBox.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit02.text())+';'+str(sl31.comboBox_2.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit03.text())+';'+str(sl31.comboBox_3.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit04.text())+';'+str(sl31.comboBox_4.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit05.text())+';'+str(sl31.comboBox_5.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit06.text())+';'+str(sl31.comboBox_6.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit07.text())+';'+str(sl31.comboBox_7.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit_9.text())+';'+str(sl31.comboBox_8.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit09.text())+';'+str(sl31.comboBox_9.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit10.text())+';'+str(sl31.comboBox_10.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit11.text())+';'+str(sl31.comboBox_11.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit11_7.text())+';'+str(sl31.comboBox_28.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit11_8.text())+';'+str(sl31.comboBox_29.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit11_9.text())+';'+str(sl31.comboBox_30.currentIndex())+'\n')
    reco.write(str(sl31.lineEdit11_10.text())+';'+str(sl31.comboBox_31.currentIndex())+'\n')
    reco.close()
    reco=file('record/teams_list.txt','a')
    reco.write(str(team_name)+';')
    reco.close()

def add_record2():
    global team_name
    #localtime = time.asctime( time.localtime(time.time()) )
    reco=file('record/'+team_name+'.txt','w')
    reco.write(str(sl111.lineEdit01.text())+';'+str(sl111.comboBox.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit02.text())+';'+str(sl111.comboBox_2.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit03.text())+';'+str(sl111.comboBox_3.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit04.text())+';'+str(sl111.comboBox_4.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit05.text())+';'+str(sl111.comboBox_5.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit06.text())+';'+str(sl111.comboBox_6.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit07.text())+';'+str(sl111.comboBox_7.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit_9.text())+';'+str(sl111.comboBox_8.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit09.text())+';'+str(sl111.comboBox_9.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit10.text())+';'+str(sl111.comboBox_10.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit11.text())+';'+str(sl111.comboBox_11.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit11_5.text())+';'+str(sl111.comboBox_13.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit11_4.text())+';'+str(sl111.comboBox_14.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit11_3.text())+';'+str(sl111.comboBox_15.currentIndex())+'\n')
    reco.write(str(sl111.lineEdit11_2.text())+';'+str(sl111.comboBox_16.currentIndex())+'\n')
    reco.close()
    reco=file('record/teams_list.txt','a')
    reco.write(str(team_name)+';')
    reco.close()
    

def generate_list1():
    
    '''if sl31.checkBox.isChecked():
        sl31.comboBox_12.setEnabled()'''
        
    sl31.comboBox_12.clear()
    k=file('record/teams_list.txt','r')
    a=(k.read()).split(';')
    
    for i in range(0,len(a)-1):
        
        sl31.comboBox_12.addItem(str(a[i]))
        #print('3'+a[i])
    k.close()

def generate_list2():

    sl111.comboBox_12.clear()
    k=file('record/teams_list.txt','r')
    a=(k.read()).split(';')
    
    for i in range(0,len(a)-1):
        
        sl111.comboBox_12.addItem(str(a[i]))
    k.close()
    
        
def import_record1():
    
    if sl31.checkBox.isChecked()==True:
        
        cur=sl31.comboBox_12.currentText()
        #print(cur);
        ccc='record'+cur+'.txt'
        #print(ccc)
        k=file('record/'+cur+'.txt','r')
        #print(ccc)
        a=(k.read()).split('\n')
        for i in range(0,15):
            a[i]=a[i].split(';')
        sl31.lineEdit01.setText(a[0][0])
        sl31.lineEdit02.setText(a[1][0])
        sl31.lineEdit03.setText(a[2][0])
        sl31.lineEdit04.setText(a[3][0])
        sl31.lineEdit05.setText(a[4][0])
        sl31.lineEdit06.setText(a[5][0])
        sl31.lineEdit07.setText(a[6][0])
        sl31.lineEdit_9.setText(a[7][0])
        sl31.lineEdit09.setText(a[8][0])
        sl31.lineEdit10.setText(a[9][0])
        sl31.lineEdit11.setText(a[10][0])
        sl31.lineEdit11_7.setText(a[11][0])
        sl31.lineEdit11_8.setText(a[12][0])
        sl31.lineEdit11_9.setText(a[13][0])
        sl31.lineEdit11_10.setText(a[14][0])
        sl31.comboBox.setCurrentIndex(int(a[0][1]))
        sl31.comboBox_2.setCurrentIndex(int(a[1][1]))
        sl31.comboBox_3.setCurrentIndex(int(a[2][1]))
        sl31.comboBox_4.setCurrentIndex(int(a[3][1]))
        sl31.comboBox_5.setCurrentIndex(int(a[4][1]))
        sl31.comboBox_6.setCurrentIndex(int(a[5][1]))
        sl31.comboBox_7.setCurrentIndex(int(a[6][1]))
        sl31.comboBox_8.setCurrentIndex(int(a[7][1]))
        sl31.comboBox_9.setCurrentIndex(int(a[8][1]))
        sl31.comboBox_10.setCurrentIndex(int(a[9][1]))
        sl31.comboBox_11.setCurrentIndex(int(a[10][1]))
        sl31.comboBox_28.setCurrentIndex(int(a[11][1]))
        sl31.comboBox_29.setCurrentIndex(int(a[12][1]))
        sl31.comboBox_30.setCurrentIndex(int(a[13][1]))
        sl31.comboBox_31.setCurrentIndex(int(a[14][1]))
        k.close()
        Dialog001.update()
        
def import_record2():
    if sl111.checkBox.isChecked()==True:
        
        cur=sl111.comboBox_12.currentText()
        
        k=file('record/'+cur+'.txt','r')
        a=(k.read()).split('\n')
        for i in range(0,15):
            a[i]=a[i].split(';')
        sl111.lineEdit01.setText(a[0][0])
        sl111.lineEdit02.setText(a[1][0])
        sl111.lineEdit03.setText(a[2][0])
        sl111.lineEdit04.setText(a[3][0])
        sl111.lineEdit05.setText(a[4][0])
        sl111.lineEdit06.setText(a[5][0])
        sl111.lineEdit07.setText(a[6][0])
        sl111.lineEdit_9.setText(a[7][0])
        sl111.lineEdit09.setText(a[8][0])
        sl111.lineEdit10.setText(a[9][0])
        sl111.lineEdit11.setText(a[10][0])
        sl111.lineEdit11_5.setText(a[11][0])
        sl111.lineEdit11_4.setText(a[12][0])
        sl111.lineEdit11_3.setText(a[13][0])
        sl111.lineEdit11_2.setText(a[14][0])
        sl111.comboBox.setCurrentIndex(int(a[0][1]))
        sl111.comboBox_2.setCurrentIndex(int(a[1][1]))
        sl111.comboBox_3.setCurrentIndex(int(a[2][1]))
        sl111.comboBox_4.setCurrentIndex(int(a[3][1]))
        sl111.comboBox_5.setCurrentIndex(int(a[4][1]))
        sl111.comboBox_6.setCurrentIndex(int(a[5][1]))
        sl111.comboBox_7.setCurrentIndex(int(a[6][1]))
        sl111.comboBox_8.setCurrentIndex(int(a[7][1]))
        sl111.comboBox_9.setCurrentIndex(int(a[8][1]))
        sl111.comboBox_10.setCurrentIndex(int(a[9][1]))
        sl111.comboBox_11.setCurrentIndex(int(a[10][1]))
        sl111.comboBox_13.setCurrentIndex(int(a[11][1]))
        sl111.comboBox_14.setCurrentIndex(int(a[12][1]))
        sl111.comboBox_15.setCurrentIndex(int(a[13][1]))
        sl111.comboBox_16.setCurrentIndex(int(a[14][1]))
        k.close()
        Dialog001.update()



def back_fun():
    
    global wicket_fall1,wicket_fall2,wicket_fall,team1,team2,k,over,total_run1,total_run,total_run2,total_wicket1,total_wicket2,total_wicket,current_batsman1,current_batsman2,extras,extra1,extra2,over,over1,over2,team_bowling,team_batting,batsman_played
    global winner,dec,te,this_over,last_over,current_bowler
    #
    global batsman_index_dup,bowler_index_dup,back_goto_batsman,batsman2_index_dup,back_goto_bowler,wicket_fall_dup,this_over_d,last_over_d,back_index,total_run_dup,total_wicket_dup,over_dup,extra_dup


    if team_batting==team1_name:
        x1=list(team1)
        x2=list(team2)
    else :
        x1=list(team2)
        x2=list(team1)

   
    
    if current_batsman1!=batsman_index_dup and current_batsman2!=batsman_index_dup:
        if current_batsman1==batsman2_index_dup:
            batsman_played.remove(current_batsman2)
            current_batsman2=batsman_index_dup
            x1[current_batsman2]=back_goto_batsman
            current_batsman1,current_batsman2=current_batsman2,current_batsman1
        else:
            batsman_played.remove(current_batsman1)
            current_batsman1=batsman_index_dup
            x1[current_batsman1]=back_goto_batsman
    elif current_batsman1!=batsman_index_dup:
        current_batsman1,current_batsman2=current_batsman2,current_batsman1
        current_batsman1=batsman_index_dup
        x1[current_batsman1]=back_goto_batsman

    else:
        current_batsman1=batsman_index_dup
        x1[current_batsman1]=back_goto_batsman
    
    current_bowler=bowler_index_dup
    
    x2[current_bowler]=back_goto_bowler    
    
    wicket_fall=wicket_fall_dup
    this_over=this_over_d
    last_over=last_over_d
    over=over_dup
    total_run=total_run_dup
    total_wicket=total_wicket_dup
    extras=extra_dup=extra_dup

    

    if team_batting==team1_name:
        team1=x1
        team2=x2
    else :
        team2=x1
        team1=x2

    display_Main(x1,x2)
    # print("hello")
        
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    MainWindow001 = QtGui.QMainWindow()
    start1 = start.Ui_MainWindow001()
    start1.setupUi(MainWindow001)

    MainWindow22 = QtGui.QMainWindow()
    fall1 = fall.Ui_MainWindow22()
    fall1.setupUi(MainWindow22)

    MainWindow = QtGui.QMainWindow()
    last1 = last.Ui_MainWindow()
    last1.setupUi(MainWindow)

    

    MainWindow007 = QtGui.QMainWindow()
    Main1 = Main.Ui_MainWindow007()
    Main1.setupUi(MainWindow007)

    MainWindow02 = QtGui.QMainWindow()
    sl21 = sl2.Ui_MainWindow02()
    sl21.setupUi(MainWindow02)

    Dialog001 = QtGui.QDialog()
    sl31 = sl3.Ui_Dialog001()
    sl31.setupUi(Dialog001)

    MainWindow05 = QtGui.QMainWindow()
    sl41 = sl4.Ui_MainWindow05()
    sl41.setupUi(MainWindow05)

    MainWindow008 = QtGui.QMainWindow()
    sl51 = sl5.Ui_MainWindow008()
    sl51.setupUi(MainWindow008)

    MainWindow009 = QtGui.QMainWindow()
    sl61 = sl6.Ui_MainWindow009()
    sl61.setupUi(MainWindow009)

    Form001 = QtGui.QWidget()
    sl71 = sl7.Ui_Form001()
    sl71.setupUi(Form001)

    MainWindow011 = QtGui.QMainWindow()
    sl81 = sl8.Ui_MainWindow011()
    sl81.setupUi(MainWindow011)

    MainWindow121 = QtGui.QMainWindow()
    sl91 = sl9.Ui_MainWindow121()
    sl91.setupUi(MainWindow121)

    MainWindow10 = QtGui.QMainWindow()
    sl101 = sl10.Ui_MainWindow10()
    sl101.setupUi(MainWindow10)

    MainWindow122 = QtGui.QMainWindow()
    dev1 = dev.Ui_MainWindow122()
    dev1.setupUi(MainWindow122)

    MainWindow123 = QtGui.QMainWindow()
    sl111 = sl11.Ui_MainWindow123()
    sl111.setupUi(MainWindow123)

    MainWindow125 = QtGui.QMainWindow()
    sl121 = sl12.Ui_MainWindow125()
    sl121.setupUi(MainWindow125)

    Dialogdec = QtGui.QDialog()
    declare_que1= declare_que.Ui_Dialogdec()
    declare_que1.setupUi(Dialogdec)

    MainWindow_elev1 = QtGui.QMainWindow()
    playing_elev11= playing_elev1.Ui_MainWindow_elev1()
    playing_elev11.setupUi(MainWindow_elev1)

    MainWindow_elev2 = QtGui.QMainWindow()
    playing_elev21 = playing_elev2.Ui_MainWindow_elev2()
    playing_elev21.setupUi(MainWindow_elev2)
    
    MainWindow001.show()
    app.connect(start1.commandLinkButton001,QtCore.SIGNAL("clicked()"),start_sl2)
    
    app.connect(sl21.commandLinkButton01,QtCore.SIGNAL("clicked()"),sl2_sl7)
    app.connect(sl21.commandLinkButton02,QtCore.SIGNAL("clicked()"),sl2_dev)
    app.connect(sl21.commandLinkButton03,QtCore.SIGNAL("clicked()"),sl2_sl9)
    app.connect(sl21.commandLinkButton04,QtCore.SIGNAL("clicked()"),exit)

    app.connect(dev1.pushButton,QtCore.SIGNAL("clicked()"),dev_sl2)
    app.connect(dev1.pushButton_2,QtCore.SIGNAL("clicked()"),exit)

    app.connect(sl91.pushButton,QtCore.SIGNAL("clicked()"),sl9_sl2)
    app.connect(sl91.pushButton_2,QtCore.SIGNAL("clicked()"),exit)

   
        

    app.connect(sl71.pushButton,QtCore.SIGNAL("clicked()"),sl7_sl3)
    
    app.connect(sl71.pushButton_2,QtCore.SIGNAL("clicked()"),sl7_sl2)

    app.connect(sl31.pushButton,QtCore.SIGNAL("clicked()"),sl3_sl11)#next
    app.connect(sl31.pushButton_2,QtCore.SIGNAL("clicked()"),sl3_sl7)#back

   
    
    app.connect(sl111.pushButton,QtCore.SIGNAL("clicked()"),sl11_playing_elev1)
    app.connect(sl111.pushButton_2,QtCore.SIGNAL("clicked()"),sl11_sl3)
    
    app.connect(sl121.pushButton,QtCore.SIGNAL("clicked()"),sl12_Main)

    app.connect(Main1.commandLinkButton,QtCore.SIGNAL("clicked()"),Main_sl4)
    app.connect(Main1.commandLinkButton_2,QtCore.SIGNAL("clicked()"),Main_sl6)
    app.connect(Main1.commandLinkButton_3,QtCore.SIGNAL("clicked()"),Main_sl10)
    app.connect(Main1.commandLinkButton_5,QtCore.SIGNAL("clicked()"),Main_fall)
    
    app.connect(sl41.pushButton,QtCore.SIGNAL("clicked()"),exe_sl4)
    app.connect(sl61.pushButton_2,QtCore.SIGNAL("clicked()"),exe_sl6)
    app.connect(sl101.pushButton,QtCore.SIGNAL("clicked()"),exe_sl10)
    app.connect(fall1.pushButton,QtCore.SIGNAL("clicked()"),exe_fall)
    app.connect(sl51.pushButton,QtCore.SIGNAL("clicked()"),sl5_Main)
    
    app.connect(sl81.pushButton,QtCore.SIGNAL("clicked()"),wicket_Main)

    app.connect(sl111.checkBox,QtCore.SIGNAL("clicked()"),generate_list2)
    app.connect(sl111.pushButton_5,QtCore.SIGNAL("clicked()"),import_record2)
    app.connect(sl111.pushButton_3,QtCore.SIGNAL("clicked()"),add_record2)

    app.connect(declare_que1.pushButton,QtCore.SIGNAL("clicked()"),declare)
    app.connect(declare_que1.pushButton_2,QtCore.SIGNAL("clicked()"),declare_quest_main)

    app.connect(playing_elev11.pushButton_2,QtCore.SIGNAL("clicked()"),playing_elev1_sl11)
    app.connect(playing_elev11.pushButton,QtCore.SIGNAL("clicked()"),playing_elev1_playing_elev2)

    app.connect(playing_elev21.pushButton,QtCore.SIGNAL("clicked()"),playing_elev2_sl12)
    app.connect(playing_elev21.pushButton_2,QtCore.SIGNAL("clicked()"),playing_elev2_playing_elev1)
    
    
    app.connect(sl31.checkBox,QtCore.SIGNAL("clicked()"),generate_list1)
    app.connect(sl31.pushButton_5,QtCore.SIGNAL("clicked()"),import_record1)
    app.connect(sl31.pushButton_3,QtCore.SIGNAL("clicked()"),add_record1)
    app.connect(Main1.pushButton,QtCore.SIGNAL("clicked()"),Main_update)
    app.connect(Main1.pushButton_3,QtCore.SIGNAL("clicked()"),Main_change)
    app.connect(last1.pushButton,QtCore.SIGNAL("clicked()"),Record)
    app.connect(last1.pushButton_2,QtCore.SIGNAL("clicked()"),start_sl2)
    app.connect(last1.pushButton_3,QtCore.SIGNAL("clicked()"),exit)
    app.connect(Main1.pushButton_2,QtCore.SIGNAL("clicked()"),main_declare_quest)
    app.connect(Main1.pushButton_4,QtCore.SIGNAL("clicked()"),back_fun)
    
    sys.exit(app.exec_())
