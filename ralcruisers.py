import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector as msc
import tkinter.messagebox as tmb

mydb=msc.connect(
  host="localhost",
  user="root",
  passwd="0000",
  database="railway_project",
  autocommit=True
)


homepage=tk.Tk()
homepage.title('Railcruisers-HomePage')
homepage.geometry('650x450')
homepage.resizable(0,0)

def dbx1():
    top1=Toplevel()
    top1.title('Railcruisers')
    top1.geometry('460x150')
    top1.resizable(0,0)

    
        
    def cust_login():
        top2=Toplevel()
        top2.title('Railcruisers-Customer Login Page')
        top2.geometry('550x200')
        top2.resizable(0,0)

        def cust_page():
            u=var8.get()
            myc15=mydb.cursor()
            myc15.execute('select username from user')
            e=myc15.fetchall()

            lst3=[]

            for i in e:
                for j in i:
                    lst3.append(j)

            
            if u in lst3:
                myc13=mydb.cursor()
                select_stmt5="select railcruisers_id,password from user where username=%(usnm)s"
                myc13.execute(select_stmt5,{"usnm":u})
                an=myc13.fetchall()
                answ=an[0][1]
                lat_answ=an[0][0]

                if var9.get()==answ:
                    top2.destroy()
                    top10=Toplevel()
                    top10.title("Raicruisers-Customer page")
                    top10.geometry('750x300')
                    top10.resizable(0,0)

                    myc14=mydb.cursor()
                    select_stmt6="select name from user where username=%(usnn)s"
                    myc14.execute(select_stmt6,{"usnn":u})
                    answ1=myc14.fetchall()[0][0]
                    answ2=("Hello "+str(answ1))
                    
                    


                    def sgnot():
                        top10.destroy()
                    def bktkt():
                        top11=Toplevel()
                        top11.title("Book Tickets")
                        top11.geometry('1375x300')
                        top11.resizable(0,0)

                        myc20=mydb.cursor()
                        myc20.execute('select distinct source from train')
                        l1=myc20.fetchall()
                        myc21=mydb.cursor()
                        myc21.execute('select distinct destination from train')
                        l2=myc21.fetchall()
                        lst_s=[]
                        lst_d=[]
                        for i in l1:
                            for j in i:
                                lst_s.append(j)

                        for i in l2:
                            for j in i:
                                lst_d.append(j)
                       
                        def b_vwtrn():
                            myc22=mydb.cursor()
                            select_stmt6="select * from train where source=%(S)s and destination=%(D)s"
                            myc22.execute(select_stmt6,{'S': var21.get(),'D': var22.get()})
                            blst=myc22.fetchall()
                            
                            for i in range(7):
                                top11_ld1=Label(top11,text=blst[0][i],width=27,bg='white',font=('agency fb','15'),relief=RAISED).grid(row=4,column=i)

                            def bk_trn():
                                top14=Toplevel()
                                top14.title("Confirm Payment")
                                top14.geometry('395x270')
                                top14.resizable(0,0)

                                d=Label(top14,text=' ').grid(row=0,column=0)
                                top14_l1=Label(top14,text='PAYMENT DETAILS',font=('arial narrow','12','bold')).grid(row=0,column=2)
                                #g=Label(top14,text=' ').grid(row=6,column=0)
                                m=int(var23.get())
                                pr=blst[0][6]
                                prp=(pr*(m))
                                gst=(0.1*prp)
                                tot=prp+gst
                                lst14_1=[(' ','Ticket Fare','GST','Total Fare'),('Quantity',str(var23.get()),'10%',' '),('Amount',prp,gst,tot)]
                                for i in range(3):
                                    for j in range(4):
                                        top14_l=Label(top14,text=lst14_1[i][j],width=17,font=('agency fb','15'),relief=GROOVE).grid(row=1+j,column=1+i)

                                def pay():
                                    myc23=mydb.cursor()
                                    select_stmt7 = "select * from user where username=%(unam)s;"
                                    myc23.execute(select_stmt7, { 'unam': u })
                                    ulst=myc23.fetchall()
                                    bp=ulst[0][5]
                                    
                                    if bp==int(var24.get()):
                                        mb1= tmb.askquestion ('Final Payment','Are you sure you want to confirm payment?',icon = 'warning')
                                        if mb1=='yes':
                                            myc24=mydb.cursor()
                                            tfulst=[]
                                            fulst=[]
                                            for i in ulst:
                                                for j in i:
                                                    fulst.append(j)
                                            for i in blst:
                                                for j in i:
                                                    tfulst.append(j)
                                            
                                            top14.destroy()
                                            top11.destroy()
                                            myc24.execute('insert into booked values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(fulst[0],fulst[3],tfulst[0],tfulst[1],tfulst[2],tfulst[3],tfulst[4],tfulst[5],m,tot))
                                            tmb.showinfo('Congratulations!','You have successfully booked the ticket!')
                                        else:
                                            print('')
                                    else:
                                        tmb.showinfo('ERROR','Invalid Bank Password')


                                g=Label(top14,text=' ').grid(row=4,column=0)
                                top14_l2=Label(top14,text='Bank Password:',font=('arial','12')).grid(row=5,column=1)
                                var24=StringVar()
                                top14_e1=Entry(top14,show='*',textvariable=var24,width=10,font=('agency fb','15')).grid(row=6,column=2)
                                h=Label(top14,text=' ').grid(row=7,column=0)
                                top14_b1=Button(top14,text='Confirm Payment',command=pay,font=('arial','11'),cursor='hand2').grid(row=8,column=2)
                                
                                
                            

                            b=Label(top11,text=' ').grid(row=5,column=0)
                            c=Label(top11,text=' ').grid(row=6,column=0)
                            top11_l4=Label(top11,text='Enter no. of tickets:',font=('arial','15')).grid(row=7,column=1)
                            var23=StringVar()
                            top11_e1=Entry(top11,textvariable=var23,font=('arial','13')).grid(row=7,column=2)
                            top11_b2=Button(top11,text='Proceed To Payment',font=('arial','13'),command=bk_trn,cursor='hand2').grid(row=7,column=5)
                            
                        


                        top11_l1=Label(top11,text='BOOK TICKETS',font=('Eras Bold ITC','18')).grid(row=0,column=3)
                        top11_l2=Label(top11,text='Enter Source',font=('arial','15')).grid(row=1,column=1)
                        var21=StringVar()
                        top11_c1=ttk.Combobox(top11,values=lst_s,font='8',textvariable=var21).grid(row=1,column=2)
                        top11_l3=Label(top11,text='Enter Destination',font=('arial','15')).grid(row=1,column=3)
                        var22=StringVar()
                        top11_c2=ttk.Combobox(top11,values=lst_d,font='8',textvariable=var22).grid(row=1,column=4)
                        top11_b1=Button(top11,text='VIEW TRAIN',font=('arial','13'),command=b_vwtrn,cursor='hand2').grid(row=1,column=5)

                        a=Label(top11,text=' ').grid(row=2,column=0)

                        lsth=['Train No.','Train Name','Source','Destination','Departure Time','Arrival Time','Price/Passenger']
                        for i in range(7):
                                top11_l=Label(top11,text=lsth[i],width=17,bg='gray65',font=('arial','15'),relief=RAISED).grid(row=3,column=i)
                        
                        

                    def vw_bkt():
                        myc25=mydb.cursor()
                        select_stmt8 = "select railcruisers_id from user where username=%(unrm)s;"
                        myc25.execute(select_stmt8, { 'unrm': u })
                        r_id=myc25.fetchall()[0][0]
                        myc26=mydb.cursor()
                        select_stmt9 = "select train_no,train_name,source,destination,departure_time,arrival_time,no_of_passengers,total_ticket_amount from booked where railcruisers_id=%(rlid)s;"
                        myc26.execute(select_stmt9, { 'rlid': r_id })
                        boktkt=myc26.fetchall()
                        myc27=mydb.cursor()
                        select_stmt10='select count(*) from booked where railcruisers_id=%(rli)s'
                        myc27.execute(select_stmt10, { 'rli': r_id })
                        c=myc27.fetchall()[0][0]
                        
                        if len(boktkt)==0:
                            tmb.showinfo('SORRY!','You have not booked any ticket yet.')

                        else:
                            top12=Toplevel()
                            top12.title("View Booked Ticket List")
                            top12.geometry("{}x500".format(top12.winfo_screenwidth()))
                            top12.resizable(1,1)

                            a=Label(top12,text=' ').grid(row=0,column=0)
                            top12_l1=Label(top12,text='BOOKED',font=('Eras Bold ITC','20','bold')).grid(row=1,column=1)
                            top12_l2=Label(top12,text='TICKET',font=('Eras Bold ITC','20','bold')).grid(row=1,column=2)
                            top12_l3=Label(top12,text='LIST',font=('Eras Bold ITC','20','bold')).grid(row=1,column=3)
                            a=Label(top12,text=' ').grid(row=2,column=0)
                            h_list=['Train No','Train Name','Source','Destination','Arr.Time','Dep.Time','No.Of Ticks.','Total Amt.']

                            for i in range(8):
                                top12_ld=Label(top12,text=h_list[i],width=15,bg='gray70',font=('arial','15'),relief=GROOVE).grid(row=3,column=i)
                       

                            for i in range(8):
                                for j in range(c):
                                    top12_l=Label(top12,text=boktkt[j][i],width=27,bg='white',bd=4,font=('agency fb','13','bold'),relief=GROOVE).grid(row=j+4,column=i)
                       
                            
                        

                    def cntkt():
                        top13=Toplevel()
                        top13.title("Cancel Ticket")
                        top13.geometry('1140x300')
                        top13.resizable(0,0)

                        
                        def vwdet1():
                            def delet1():
                                MsgBox1 = tmb.askquestion ('Cancel Ticket','Are you sure you want to cancel your ticket?',icon = 'warning')
                                if MsgBox1=='yes':
                                    myc29=mydb.cursor()
                                    delete_stmt10 = "delete from booked where train_no=%(tnu2)s and railcruisers_id=%(R)s;"
                                    myc29.execute(delete_stmt10, { 'tnu2': rid1 , 'R': lat_answ })
                                    top13.destroy()
                                    tmb.showinfo('Congratulations!','You have successfully cancelled your ticket.')
                                else:
                                   print('')
                                    
                            rid1=var25.get()
                            myc28=mydb.cursor()
                            select_stmt15 = "select train_name,source,destination from train where train_no=%(tnu1)s;"
                            myc28.execute(select_stmt15, { 'tnu1': rid1 })
                            A1=myc28.fetchall()
                            k1=A1[0]
                            a1,b1,c1=k1[0],k1[1],k1[2]
                            var26.set(a1),var27.set(b1),var28.set(c1)
                            top13_b2=Button(top13,text='CANCEL TICKET',font=('Berlin Sans FB','17'),command=delet1,cursor='hand2').grid(row=8,column=1)                                

                                
                        top13_l1=Label(top13,text='    CANCEL TICKET',font=('Berlin Sans FB Demi','30')).grid(row=1,column=0)
                        a=Label(top13,text=' ').grid(row=2,column=0)
                        top13_l2=Label(top13,text='        Enter Train No.:     ',font=('arial','25')).grid(row=3,column=0)
                        var25=StringVar()
                        top13_e1=Entry(top13,width='25',font=('arial','20'),textvariable=var25).grid(row=3,column=1)
                        
                        top13_b1=Button(top13,text='VIEW DETAILS',font=('Berlin Sans FB','17'),command=vwdet1,cursor='hand2').grid(row=3,column=3)
                        a=Label(top13,text='            ').grid(row=4,column=0)
                        
                        top13_l3=Label(top13,text='                   TRAIN NAME                       ',font=('arial','15','bold'),bg='gray70',relief=RAISED).grid(row=5,column=0)
                        top13_l4=Label(top13,text='                         SOURCE                           ',font=('arial','15','bold'),bg='gray70',relief=RAISED).grid(row=5,column=1)
                        top13_l5=Label(top13,text='                 DESTINATION                   ',font=('arial','15','bold'),bg='gray70',relief=RAISED).grid(row=5,column=3)
                        var26=StringVar()
                        var27=StringVar()
                        var28=StringVar()
                        top13_l6=Label(top13,textvariable=var26,font=('arial','15'),bg='white',relief=RAISED).grid(row=6,column=0)
                        top13_l7=Label(top13,textvariable=var27,font=('arial','15'),bg='white',relief=RAISED).grid(row=6,column=1)
                        top13_l8=Label(top13,textvariable=var28,font=('arial','15'),bg='white',relief=RAISED).grid(row=6,column=3)
                        a=Label(top13,text='            ').grid(row=7,column=0)
                        

                    def rmact():
                        mb= tmb.askquestion ('Remove Account','Are you sure you want to remove your account?',icon = 'warning')
                        if mb=='yes':
                            myc16=mydb.cursor()
                            delete_stmt1 = "delete from user where username=%(un)s;"
                            myc16.execute(delete_stmt1, { 'un': u })
                            top10.destroy()
                            tmb.showinfo('Deleted!','Your Account has been successfully deleted!')    

                        else:
                            print('')

                
            

                    var20=StringVar()
                    top10_l1=Label(top10,textvariable=var20,font=('Elephant','20')).grid(row=1,column=1)
                    var20.set(answ2)
                    a=Label(top10,text=' ').grid(row=2,column=0)
                    a=Label(top10,text=' ').grid(row=3,column=0)
                    b=Label(top10,text='        ').grid(row=4,column=0)
                    top10_b1=Button(top10,text='      BOOK TICKET      ',font=('Eras Bold ITC','15'),cursor='hand2',command=bktkt).grid(row=4,column=1)
                    c=Label(top10,text='          ').grid(row=4,column=2)
                    top10_b2=Button(top10,text='   VIEW BOOKED TICKETS   ',font=('Eras Bold ITC','15'),cursor='hand2',command=vw_bkt).grid(row=4,column=3)
                    d=Label(top10,text=' ').grid(row=5,column=0)
                    d=Label(top10,text=' ').grid(row=6,column=0)
                    e=Label(top10,text='        ').grid(row=7,column=0)
                    top10_b3=Button(top10,text='     CANCEL TICKET    ',font=('Eras Bold ITC','15'),cursor='hand2',command=cntkt).grid(row=7,column=1)
                    f=Label(top10,text='          ').grid(row=7,column=2)
                    top10_b4=Button(top10,text='   REMOVE ACCOUNT   ',font=('Eras Bold ITC','15'),cursor='hand2',command=rmact).grid(row=7,column=3)
                    g=Label(top10,text='         ').grid(row=8,column=0)
                    h=Label(top10,text='         ').grid(row=9,column=0)
                    i=Label(top10,text='         ').grid(row=9,column=1)
                    top10_b5=Button(top10,text='SIGN OUT',font=('Arial','10','bold'),cursor='hand2',command=sgnot).grid(row=9,column=2)
                else:
                    tmb.showinfo("ERROR","Invalid Password")
            else:
                tmb.showinfo("ERROR","Invalid Username")
    

        top2_l1=Label(top2,text='Login As Customer',font=('Berlin Sans FB Demi','25')).grid(row=1,column=1)
        a=Label(top2,text=' ').grid(row=2,column=0)
        top2_l2=Label(top2,text='        Username:     ',font='15').grid(row=3,column=0)
        var8=StringVar()
        top2_e1=Entry(top2,width='60',textvariable=var8).grid(row=3,column=1)
        b=Label(top2,text=' ').grid(row=4,column=0)
        top2_l3=Label(top2,text='        Password:     ',font='15').grid(row=5,column=0)
        var9=StringVar()
        top2_e2=Entry(top2,show='*',width='60',textvariable=var9).grid(row=5,column=1)
        c=Label(top2,text='              ').grid(row=6,column=0)
        top2_b1=Button(top2,text='LOG IN',font=('Cooper Black','15'),command=cust_page,cursor='hand2').grid(row=6,column=1)
    def cna():
        top3=Toplevel()
        top3.title('Railcruisers-Create New Account')
        top3.geometry('700x350')
        top3.resizable(0,0)

        cur=mydb.cursor()
        cur.execute('select count(*) from user')
        res=cur.fetchall()[0][0]
            
        if res==0:
            res2=100
        else:
            cur1=mydb.cursor()
            cur1.execute('select max(railcruisers_id) from user')
            res1=cur1.fetchall()[0][0]
            res2=(1+res1)         
        

        def cr_nw_acc():
            #cursor = mydb.cursor(buffered=True)
            
            usrnm,pwd,nm,cno,bpwd=(var4.get(),var5.get(),var6.get(),var7.get(),var.get())
            
            myc1=mydb.cursor()
            myc1.execute('insert into user values (%s,%s,%s,%s,%s,%s);',(res2,usrnm,pwd,nm,cno,bpwd))
            myc2=mydb.cursor()
            select_stmt = "SELECT railcruisers_id FROM user WHERE username = %(usr)s;"
            myc2.execute(select_stmt, { 'usr': usrnm })
            rec=myc2.fetchall()[0]
            recid=rec[0]
            top3.destroy()
            tmb.showinfo('Congratulations!','You have successfully registered with Railcruisers.\nYour Railcruisers id is: {}'.format(recid))
            
        top3_l1=Label(top3,text='Welcome To Railcruisers',font=('Berlin Sans FB Demi','25')).grid(row=1,column=1)
        a=Label(top3,text=' ').grid(row=2,column=0)
        top3_l2=Label(top3,text='        Username:     ',font='15').grid(row=3,column=0)
        var4=StringVar()
        top3_e1=Entry(top3,width='70',textvariable=var4).grid(row=3,column=1)
        b=Label(top3,text=' ').grid(row=4,column=0)
        top3_l3=Label(top3,text='        Password:     ',font='15').grid(row=5,column=0)
        var5=StringVar()
        top3_e2=Entry(top3,width='70',textvariable=var5).grid(row=5,column=1)
        c=Label(top3,text=' ').grid(row=6,column=0)
        top3_l4=Label(top3,text='        Name:     ',font='15').grid(row=7,column=0)
        var6=StringVar()
        top3_e3=Entry(top3,width='70',textvariable=var6).grid(row=7,column=1)
        d=Label(top3,text=' ').grid(row=8,column=0)
        top3_l5=Label(top3,text='        Contact No:     ',font='15').grid(row=9,column=0)
        var7=StringVar()
        top3_e4=Entry(top3,width='70',textvariable=var7).grid(row=9,column=1)
        d=Label(top3,text=' ').grid(row=10,column=0)
        top3_l6=Label(top3,text='        Bank Password:     ',font='15').grid(row=11,column=0)
        var=StringVar()
        top3_e4=Entry(top3,width='70',textvariable=var).grid(row=11,column=1)
        e=Label(top3,text='              ').grid(row=12,column=0)
        f=Label(top3,text='              ').grid(row=13,column=0)
        top3_b1=Button(top3,text='CREATE ACCOUNT',font=('Cooper Black','15'),command=cr_nw_acc,cursor='hand2').grid(row=13,column=1)
               
        
        
    def adm_login():
        top4=Toplevel()
        top4.title('Railcruisers-Admin Login Page')
        top4.geometry('500x200')
        top4.resizable(0,0)

        def adm_page():
            if var2.get()=="sameer" and var3.get()=="sam123":
                top4.destroy()
                top5=Toplevel()
                top5.title('Railcruisers-Admin Page')
                top5.geometry('600x300')
                top5.resizable(0,0)

                def sgnot():
                    top5.destroy()

                def ad_trn():
                    top6=Toplevel()
                    top6.title('Railcruisers-Add Train')
                    top6.geometry('710x400')
                    top6.resizable(0,0)
                  
                    myc3=mydb.cursor()
                    myc3.execute('select count(*) from train')
                    ans=myc3.fetchall()[0][0]
            
                    if ans==0:
                        ans2=101
                    else:
                        myc4=mydb.cursor()
                        myc4.execute('select max(train_no) from train')
                        ans1=myc4.fetchall()[0][0]
                        ans2=(1+ans1)    

                    def add_tran():
                        trnm,src,dest,dt,at,ppp=(var10.get(),var11.get(),var12.get(),var13.get(),var14.get(),var15.get())
            
                        myc5=mydb.cursor()
                        myc5.execute('insert into train values (%s,%s,%s,%s,%s,%s,%s);',(ans2,trnm,src,dest,dt,at,ppp))
                        myc6=mydb.cursor()
                        select_stmt1 = "SELECT train_no FROM train WHERE train_name = %(tn)s;"
                        myc6.execute(select_stmt1, { 'tn': trnm })
                        tno=myc6.fetchall()[0][0]
                        top6.destroy()
                        tmb.showinfo('Congratulations!','You have successfully added the Train.\nThe Train No. is: {}'.format(tno))
            
                        


                    top6_l1=Label(top6,text='ADD TRAIN',font=('Berlin Sans FB Demi','25')).grid(row=1,column=1)
                    a=Label(top6,text=' ').grid(row=2,column=0)
                    top6_l2=Label(top6,text='       Train Name:    ',font='15').grid(row=3,column=0)
                    var10=StringVar()
                    top6_e1=Entry(top6,width='70',textvariable=var10).grid(row=3,column=1)
                    b=Label(top6,text=' ').grid(row=4,column=0)
                    top6_l3=Label(top6,text='         Source:      ',font='15').grid(row=5,column=0)
                    var11=StringVar()
                    top6_e2=Entry(top6,width='70',textvariable=var11).grid(row=5,column=1)
                    c=Label(top6,text=' ').grid(row=6,column=0)
                    top6_l4=Label(top6,text='      Destination:   ',font='15').grid(row=7,column=0)
                    var12=StringVar()
                    top6_e3=Entry(top6,width='70',textvariable=var12).grid(row=7,column=1)
                    d=Label(top6,text=' ').grid(row=8,column=0)
                    top5_l5=Label(top6,text='        Departure Time:     ',font='15').grid(row=9,column=0)
                    var13=StringVar()
                    top6_e4=Entry(top6,width='70',textvariable=var13).grid(row=9,column=1)
                    d=Label(top6,text=' ').grid(row=10,column=0)
                    top5_l6=Label(top6,text='        Arrival Time:     ',font='15').grid(row=11,column=0)
                    var14=StringVar()
                    top6_e5=Entry(top6,width='70',textvariable=var14).grid(row=11,column=1)
                    d=Label(top6,text=' ').grid(row=12,column=0)
                    top6_l7=Label(top6,text='        Price per passenger:     ',font='15').grid(row=13,column=0)
                    var15=StringVar()
                    top6_e6=Entry(top6,width='70',textvariable=var15).grid(row=13,column=1)
                    e=Label(top6,text='              ').grid(row=14,column=0)
                    f=Label(top6,text='              ').grid(row=15,column=0)
                    top6_b1=Button(top6,text='ADD TRAIN',font=('Cooper Black','15'),command=add_tran,cursor='hand2').grid(row=15,column=1)
                     


                def vw_usr():
                    top7=Toplevel()
                    top7.title('Railcruisers-User List')
                    top7.geometry("905x500")
                    top7.resizable(0,0)
                    

                    top7_l1=Label(top7,text='          USER',font=('Berlin Sans FB Demi','25')).grid(row=0,column=1)
                    top7_l2=Label(top7,text='LIST       ',font=('Berlin Sans FB Demi','25')).grid(row=0,column=2)

                    myc11=mydb.cursor()
                    myc11.execute('select Railcruisers_Id,username,name,contact_no from user')
                    data1=myc11.fetchall()

                    myc12=mydb.cursor()
                    myc12.execute('select count(*) from user')
                    cot=myc12.fetchall()[0][0]

                    lst2=['Railcruisers Id.','Username','Name','Contact No.']
                    for i in range(4):
                        top7_l=Label(top7,text=lst2[i],width=20,bg='gray65',font=('arial','15'),relief=RAISED).grid(row=1,column=i)
                            


                    for j in range(cot):
                            for k in range(4):
                                top7_ld=Label(top7,text=data1[j][k],width=22,bg='white',font=('agency fb','20'),relief=GROOVE).grid(row=j+2,column=k)
                       
                    

                    
                    
                
                def dlt_trn():
                    top8=Toplevel()
                    top8.title('Railcruisers-Delete Train')
                    top8.geometry('1140x300')
                    top8.resizable(0,0)

                    def vwdet():
                        def delet():
                            MsgBox = tmb.askquestion ('Delete Train','Are you sure you want to delete the train?',icon = 'warning')
                            if MsgBox=='yes':
                                rid=var16.get()
                                myc8=mydb.cursor()
                                delete_stmt = "delete from train where train_no=%(tnu)s;"
                                myc8.execute(delete_stmt, { 'tnu': rid })
                                top8.destroy()
                                tmb.showinfo('Congratulations!','You have successfully deleted the Train.')
                            else:
                               print('')
                                
                        rid=var16.get()
                        myc7=mydb.cursor()
                        select_stmt2 = "select train_name,source,destination from train where train_no=%(tnu)s;"
                        myc7.execute(select_stmt2, { 'tnu': rid })
                        A=myc7.fetchall()
                        k=A[0]
                        a,b,c=k[0],k[1],k[2]
                        var17.set(a),var18.set(b),var19.set(c)
                        top8_b2=Button(top8,text='DELETE TRAIN',font=('Berlin Sans FB','17'),command=delet,cursor='hand2').grid(row=8,column=1)                                

                            
                    top8_l1=Label(top8,text='    DELETE TRAIN',font=('Berlin Sans FB Demi','30')).grid(row=1,column=0)
                    a=Label(top8,text=' ').grid(row=2,column=0)
                    top8_l2=Label(top8,text='        Enter Train No.:     ',font=('arial','25')).grid(row=3,column=0)
                    var16=StringVar()
                    top8_e1=Entry(top8,width='25',font=('arial','20'),textvariable=var16).grid(row=3,column=1)
                    
                    top8_b1=Button(top8,text='VIEW DETAILS',font=('Berlin Sans FB','17'),command=vwdet,cursor='hand2').grid(row=3,column=3)
                    a=Label(top8,text='            ').grid(row=4,column=0)
                    
                    top8_l3=Label(top8,text='                   TRAIN NAME                       ',font=('arial','15','bold'),bg='gray70',relief=RAISED).grid(row=5,column=0)
                    top8_l4=Label(top8,text='                         SOURCE                           ',font=('arial','15','bold'),bg='gray70',relief=RAISED).grid(row=5,column=1)
                    top8_l5=Label(top8,text='                 DESTINATION                   ',font=('arial','15','bold'),bg='gray70',relief=RAISED).grid(row=5,column=3)
                    var17=StringVar()
                    var18=StringVar()
                    var19=StringVar()
                    top8_l6=Label(top8,textvariable=var17,font=('arial','15'),bg='white',relief=RAISED).grid(row=6,column=0)
                    top8_l7=Label(top8,textvariable=var18,font=('arial','15'),bg='white',relief=RAISED).grid(row=6,column=1)
                    top8_l8=Label(top8,textvariable=var19,font=('arial','15'),bg='white',relief=RAISED).grid(row=6,column=3)
                    a=Label(top8,text='            ').grid(row=7,column=0)
                        
                    

                    


                def vw_trn():
                    top9=Toplevel()
                    top9.title('Railcruisers-Train List')
                    top9.geometry("{0}x500".format(top9.winfo_screenwidth()))
                    top9.resizable(0,0)

                    def vwtn():
                        myc9=mydb.cursor()
                        select_stmt3 = "select count(*) from train where source=%(cnt)s;"
                        myc9.execute(select_stmt3, { 'cnt': (var19.get()) })
                        cnt1=myc9.fetchall()[0][0]

                        myc10=mydb.cursor()
                        select_stmt4="select * from train where source=%(src)s"
                        myc10.execute(select_stmt4, { 'src': (var19.get()) })
                        data=myc10.fetchall()
                        

                        for j in range(cnt1):
                            for k in range(7):
                                top9_ld=Label(top9,text=data[j][k],width=27,bg='white',font=('agency fb','15'),relief=GROOVE).grid(row=j+4,column=k)

                    top9_l1=Label(top9,text='TRAIN LIST',font=('Berlin Sans FB Demi','25')).grid(row=0,column=3)
                    top9_l2=Label(top9,text='Enter Source:',font=('arial','15')).grid(row=1,column=1)
                    m=mydb.cursor()
                    m.execute('select distinct source from train')
                    l=m.fetchall()
                    lst1=[]
                    for i in l:
                        for j in i:
                            lst1.append(j)

                    var19=StringVar()
                    top9_c1=ttk.Combobox(top9,values=lst1,font='15',textvariable=var19).grid(row=1,column=2)
                    a=Label(top9,text=' ').grid(row=2,column=0)

                    top9_b1=Button(top9,text='VIEW TRAINS',font=('arial','15'),command=vwtn,cursor='hand2').grid(row=1,column=5)
                    lst=['Train No.','Train Name','Source','Destination','Departure Time','Arrival Time','Price/Passenger']
                    for i in range(7):
                            top9_l=Label(top9,text=lst[i],width=17,bg='gray65',font=('arial','15'),relief=RAISED).grid(row=3,column=i)
                                        
                top5_l1=Label(top5,text='Hello, Sameer',font=('Elephant','25')).grid(row=1,column=1)
                a=Label(top5,text=' ').grid(row=2,column=0)
                a=Label(top5,text=' ').grid(row=3,column=0)
                b=Label(top5,text='        ').grid(row=4,column=0)
                top5_b1=Button(top5,text='      ADD TRAIN      ',font=('Eras Bold ITC','15'),cursor='hand2',command=ad_trn).grid(row=4,column=1)
                c=Label(top5,text='          ').grid(row=4,column=2)
                top5_b2=Button(top5,text='   VIEW USER LIST   ',font=('Eras Bold ITC','15'),cursor='hand2',command=vw_usr).grid(row=4,column=3)

                d=Label(top5,text=' ').grid(row=5,column=0)
                d=Label(top5,text=' ').grid(row=6,column=0)
                e=Label(top5,text='        ').grid(row=7,column=0)
                top5_b3=Button(top5,text='     DELETE TRAIN    ',font=('Eras Bold ITC','15'),cursor='hand2',command=dlt_trn).grid(row=7,column=1)
                f=Label(top5,text='          ').grid(row=7,column=2)
                top5_b4=Button(top5,text='   VIEW TRAIN LIST   ',font=('Eras Bold ITC','15'),cursor='hand2',command=vw_trn).grid(row=7,column=3)

                g=Label(top5,text='         ').grid(row=8,column=0)
                h=Label(top5,text='         ').grid(row=9,column=0)
                i=Label(top5,text='         ').grid(row=9,column=1)
                top5_b5=Button(top5,text='SIGN OUT',font=('Arial','10','bold'),cursor='hand2',command=sgnot).grid(row=9,column=2)
                
            else:
                tmb.showinfo("ERROR","Invalid Username or Password")

        top4_l1=Label(top4,text='Login As Admin',font=('Berlin Sans FB Demi','25')).grid(row=1,column=1)
        a=Label(top4,text=' ').grid(row=2,column=0)
        top4_l2=Label(top4,text='        Username:     ',font='15').grid(row=3,column=0)
        var2=StringVar()
        top4_e1=Entry(top4,width='50',textvariable=var2).grid(row=3,column=1)
        b=Label(top4,text=' ').grid(row=4,column=0)
        top4_l3=Label(top4,text='        Password:     ',font='15').grid(row=5,column=0)
        var3=StringVar()
        top4_e2=Entry(top4,show='*',width='50',textvariable=var3).grid(row=5,column=1)
        c=Label(top4,text='              ').grid(row=6,column=0)
        top4_b1=Button(top4,text='LOG IN',font=('Cooper Black','15'),command=adm_page,cursor='hand2').grid(row=6,column=1)
        

    top1_l1=Label(top1,text='How do you want to login?',font=('arial','15')).pack(side='top')
    a=Label(top1,text='        ').pack(side='left')
    top1_b1=Button(top1,text='Create a new account',font=('arial','10'),command=cna,cursor='hand2').pack(side='left')
    b=Label(top1,text='        ').pack(side='left')
    top1_b2=Button(top1,text='As Existing Customer',command=cust_login,font=('arial','10'),cursor='hand2').pack(side='left')
    c=Label(top1,text='        ').pack(side='left')
    top1_b3=Button(top1,text='As Admin',command=adm_login,font=('arial','10'),cursor='hand2').pack(side='left')
    
    
canvas1=Canvas(homepage)
canvas1.pack(expand='True',fill='both')

img1=PhotoImage(file = "images for project/img1.png")
canvas1.create_image(0,0,image=img1,anchor=NW)

label1= Label(homepage,text='Railcruisers',font=('Bernard MT Condensed','40'),bg='LightGoldenrod4',relief=GROOVE,borderwidth=10)
label1.pack(expand='True',fill='both')
canvas1.create_window(200, 30, anchor=NW, window=label1)

button1=Button(homepage,text='Click to continue',command=dbx1,font=('Berlin Sans FB','15'),bg='Coral',borderwidth=5,cursor='hand2')
button1.pack(expand='True',fill='both')
canvas1.create_window(240, 390, anchor=NW, window=button1)

homepage.mainloop()
