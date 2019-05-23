# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 14:10:11 2017

@author: Arnav
"""
import sqlite3
from sqlite3 import *
import serial

from Tkinter import *
import tkMessageBox
import os

x=-1
z=1

def changetable(x,con):
    
    
        
        if(x==1):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 1")
            con.commit()
        if(x==2):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 2")
            con.commit()
        if(x==3):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 3")
            con.commit()
        if(x==4):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 4")
            con.commit()
        if(x==5):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 5")
            con.commit()
        if(x==6):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 6")
            con.commit()
        if(x==7):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 7")
            con.commit()
        if(x==8):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 8")
            con.commit()
        if(x==9):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 9")
            con.commit()
        if(x==10):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 10")
            con.commit()
        if(x==12):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 12")
            con.commit()
        if(x==13):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 13")
            con.commit()
        if(x==14):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 14")
            con.commit()
        if(x==15):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 15")
            con.commit()
        if(x==16):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 16")
            con.commit()
        if(x==17):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 17")
            con.commit()
        if(x==18):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 18")
            con.commit()
        if(x==19):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 19")
            con.commit()
        if(x==20):
            con.execute("UPDATE VOTERID set CH = -1 where ID = 20")
            con.commit()
            
        



def creating(conn):
    try:
        conn.execute('''CREATE TABLE VOTERID (ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,GENDER TEXT NOT NULL,CH INT NOT NULL ); ''')
        print 'Table Created Successfully'
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (1, 'Himanshu', 32, 'male',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (2, 'Himanshi', 18, 'female',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (3, 'Himani', 21, 'female',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (4, 'shivani', 31, 'female',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (5, 'arnabh', 22, 'male',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (6, 'arnav', 63, 'male',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (7, 'aman', 45, 'male',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (8, 'reet', 67, 'female',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (9, 'anureet', 78, 'female',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (10, 'sahil', 18, 'male',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (11, 'yajat', 110, 'male',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (12, 'ankit', 19, 'male',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (13, 'kirti', 20, 'female',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (14, 'jagbir', 20, 'male',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (15, 'Hitesh', 19, 'male',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (16, 'honey', 35, 'male',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (17, 'parul', 19, 'female',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (18, 'ishika', 19, 'female',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (19, 'shalini', 18, 'female',0)");
        conn.execute("INSERT INTO VOTERID (ID,NAME,AGE,GENDER,CH) VALUES (20, 'mohan', 32, 'male',0)");
        conn.commit()
        print 'Record Recorded Successfully'
    #    return conn
    except OperationalError:
        pass
    
    
def printing(conn):
    cursor = conn.execute("SELECT ID, NAME, AGE, GENDER from VOTERID")
    print 'ID\t','NAME\t','AGE\t','GENDER\t'
    for row in cursor:
       print row[0] , '\t',
       print row[1] , '\t',
       print row[2] , '\t',
       print row[3], "\n"

    print "Operation done successfully";

def checking(con,con1):
    """
    def get_data(l):
        l.append(E1.get())
        print(l)
        E1.delete(0,END)
        return
    """
   
    global z
    z=1
    def submit_data():
            username = E1.get()
            print username
            global x
            x=username
            app.destroy()
            
    while z==1:
        
    
        
        
    
        mylist = []
        
        app=Tk()
        app.title("VOTING_MACHINE")
        app.geometry('450x300+200+200')
    
    
        labelText = StringVar()
        labelText.set("Caste Your Vote")
        label1 = Label(app,textvariable=labelText, height=4)
        label1.pack()
    
        labelText1 = StringVar()
        labelText1.set("Enter your unique voter ID")
        label1 = Label(app,textvariable=labelText1, height=4)
        label1.pack()
    
    
        L1 = Label(app, textvariable="Enter Your I.D")
        L1.pack()
        E1 = Entry(app, bd =10)
        a = E1
        E1.pack()
        E1.get()
        button1 = Button(app, text = "SUBMIT",command=submit_data, width=20)
        button1.pack(padx=15,pady=15)
    
        app.mainloop()
        
    
    
        cur = con1.execute("SELECT ID from VOTERID")
        cur2 = con1.execute("SELECT CH from VOTERID")
        
            
    
        flag = 0
        
    
            
        
        for i in cur:
            if str(i[0])==x:
                if int([y[0] for y in cur2][int(x)-1])==0:
                    flag=1
                    changetable(int(x),con1)
                    
        
                
        if flag==1:
            
            print ("please vote")
            z = operate(con)
           
            
            
                   
     
        else:
            
            print ("not verified")
            z=1
            
        
        
        

def printdb(con):
    cursor = con.execute("SELECT id, name,VOTES from PP ")
    print "ID\t","NAME\t","VOTES\n"
    for row in cursor:
        print  row[0],"\t" ,
        print  row[1],"\t",
        print  row[2],"\n"
def calcres(con):
    x = con.execute("SELECT name from PP where VOTES = ( SELECT MAX(VOTES) FROM PP)")
    print("Winner of these elections : "),
    for row in x:
        print  row[0],"\t" 
def create(conn):
    try:
        conn.execute('''CREATE TABLE PP
             (ID INT PRIMARY KEY NOT NULL,
              NAME        TEXT     NOT NULL,
              VOTES        INT     NOT NULL);''')
        conn.execute("INSERT INTO PP (ID,NAME,VOTES) \
                   VALUES(1, 'Congress',0 )");
        conn.execute("INSERT INTO PP (ID,NAME,VOTES) \
                    VALUES(2, 'BJP',0 )");
        conn.execute("INSERT INTO PP (ID,NAME,VOTES) \
                   VALUES(3, 'AAP',0 )"); 
        conn.execute("INSERT INTO PP (ID,NAME,VOTES) \
                   VALUES(4, 'Others',0 )");
        conn.commit()
    except OperationalError:
        pass

def operate(con):
    i=0
    while(i<1):
        d=a.read()
        
        if(d=="*"):
            con.execute("UPDATE PP set VOTES = VOTES+1 where ID = 1")
            con.commit()
            printdb(con)
            i+=1
            return i
        elif(d=="#"):
            con.execute("UPDATE PP set VOTES = VOTES+1 where ID = 2")
            con.commit()
            printdb(con)
            i+=1
            return i
        elif(d=="$"):
            con.execute("UPDATE PP set VOTES = VOTES+1 where ID = 3")
            con.commit()
            printdb(con)
            i+=1
            return i
        elif(d=="&"):
            con.execute("UPDATE PP set VOTES = VOTES+1 where ID = 4")
            con.commit()
            printdb(con)
            i+=1
            return i
        elif(d=="^"):
            return -1;
   

     

a=serial.Serial('COM6',9600) 
con1=connect('people.db')
con=connect('votes.db')
create(con)
creating(con1)
checking(con,con1)
calcres(con)
