from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os
import math

with open("config.json", "r") as c:
    params=json.load(c)['params']
   
dips=Flask(__name__)
dips.secret_key="super-secret-key"

dips.config['SQLALCHEMY_DATABASE_URI'] ="mysql://root:@localhost/attendance"

db = SQLAlchemy(dips)

class Emp_attendance(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.Integer, nullable=False)
    ename = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    timein = db.Column(db.String(50), nullable=False)
    timeout = db.Column(db.String(50), nullable=False)    

class Admin(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)

class Employee(db.Model):
    eno = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    mname = db.Column(db.String(21), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    dept = db.Column(db.String(25), nullable=False)
    position = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    mob = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)

@dips.route("/")
def index():
    date=datetime.date(datetime.now())
    attendance = Emp_attendance.query.filter_by(date=date).all()
    last = math.ceil(len(attendance)/int(params['no_of_posts']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    attendance = attendance[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
    if page==1:
        prev = "#"
        next = "/?page="+ str(page+1)
    elif page==last:
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)
    
    return render_template('index.html', params=params, attendance=attendance, prev=prev, next=next)
    

@dips.route("/admin", methods = ['GET', 'POST'])
def admin():    
    attendance = Emp_attendance.query.filter_by().all()
    if ('admin' in session):
        result=Admin.query.filter_by(username=session['admin']).first()
        last = math.ceil(len(attendance)/int(params['no_of_posts']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        attendance = attendance[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
        if page==1:
            prev = "#"
            next = "admin?page="+ str(page+1)
        elif page==last:
            prev = "admin?page="+ str(page-1)
            next = "#"
        else:
            prev = "admin?page="+ str(page-1)
            next = "admin?page="+ str(page+1)
    
        return render_template("admin.html",params=params,attendance=attendance, prev=prev, next=next,name=result.fname+" "+result.lname)        
        
    if request.method=="POST":
        username=request.form.get("uname")
        userpass=request.form.get("pass")
        result=Admin.query.filter_by(username=username,password=userpass).first()
        if result!=None:
            if result.username==username and result.password==userpass:
                session["admin"]=username
                last = math.ceil(len(attendance)/int(params['no_of_posts']))
                page = request.args.get('page')
                if (not str(page).isnumeric()):
                    page = 1
                page = int(page)
                attendance = attendance[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
                if page==1:
                    prev = "#"
                    next = "admin?page="+ str(page+1)
                elif page==last:
                    prev = "admin?page="+ str(page-1)
                    next = "#"
                else:
                    prev = "admin?page="+ str(page-1)
                    next = "admin?page="+ str(page+1)
    
                return render_template("admin.html",params=params,attendance=attendance, prev=prev, next=next,name=result.fname+" "+result.lname)

    return render_template("alogin.html",params=params)

@dips.route("/employees")
def employees():
   
    emp = Employee.query.filter_by().all()
    if ('admin' in session):
        result=Admin.query.filter_by(username=session['admin']).first()
        last = math.ceil(len(emp)/int(params['no_of_posts']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        emp = emp[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
        if page==1:
            prev = "#"
            next = "employees?page="+ str(page+1)
        elif page==last:
            prev = "employees?page="+ str(page-1)
            next = "#"
        else:
            prev = "employees?page="+ str(page-1)
            next = "employees?page="+ str(page+1)
    
        return render_template("employees.html",params=params,emp=emp, prev=prev, next=next,name=result.fname+" "+result.lname)     
           
    return render_template("alogin.html",params=params)

@dips.route("/admins")
def admins():
   
    emp = Admin.query.filter_by().all()
    if ('admin' in session):
        result=Admin.query.filter_by(username=session['admin']).first()
        last = math.ceil(len(emp)/int(params['no_of_posts']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        emp = emp[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
        if page==1:
            prev = "#"
            next = "admins?page="+ str(page+1)
        elif page==last:
            prev = "admins?page="+ str(page-1)
            next = "#"
        else:
            prev = "admins?page="+ str(page-1)
            next = "admins?page="+ str(page+1)
    
        return render_template("admins.html",params=params,emp=emp, prev=prev, next=next,name=result.fname+" "+result.lname)        
   
    return render_template("alogin.html",params=params)


@dips.route("/add",methods = ['GET', 'POST'])
def add():
    action = request.args.get('action', None)
    tid = request.args.get('tid', None)
    tid1=request.args.get('tid1', None)
    pdate=request.args.get('date', None)
    if 'admin' in session:        
        if action =='attendance':  
            if request.method=="POST":
                eid=request.form.get('tid')
                ename=request.form.get('name')
                estatus=request.form.get('status')
                date=request.form.get('date')
                timein=request.form.get('timein')
                timeout=request.form.get('timeout')
                if tid1=="0":
                    entry = Emp_attendance(eid=eid, ename = ename, status = estatus, date= date,timein = timein,timeout=timeout )
                    db.session.add(entry)
                    db.session.commit()
                    return redirect("/admin")
                else:
                    entry = Emp_attendance.query.filter_by(eid=eid,date=pdate).first()
                    if entry!=None:
                        entry.eid=eid
                        entry.ename=ename
                        entry.status=estatus
                        entry.date=pdate
                        entry.timein=timein
                        entry.timeout=timeout
                        db.session.commit()
                        return redirect("/admin")
                    else:
                        print(f"record {eid} not exist with today {date}")
                        return redirect("/admin")

            attendance = Emp_attendance.query.filter_by(eid=tid,date=pdate).first()            
            return render_template("edit_attendance.html",attendance=attendance,params=params,tid=tid,date=pdate)

        if action=='employee':
            if request.method=="POST":                
                fname=request.form.get('fname')
                mname=request.form.get('mname')
                lname=request.form.get('lname')
                department=request.form.get('dept')
                position=request.form.get('position')
                username=request.form.get('username')
                password=request.form.get('password')               
                gender=request.form.get('gender')
                mob=request.form.get('mob')
                city=request.form.get('city')
                address=request.form.get('address')
                email=request.form.get('email')
                
                if tid1=="0":
                    entry = Employee(fname = fname,mname = mname,lname = lname, dept = department, position= position,username=username,password=password,mob=mob,email=email,city=city,address=address,gender=gender)
                    db.session.add(entry)
                    db.session.commit()
                    return redirect("/employees")
                else:
                    entry = Employee.query.filter_by(eno=tid1).first()
                    if entry!=None:                    
                        entry.fname=fname
                        entry.mname=mname
                        entry.lname=lname
                        entry.dept=department
                        entry.position=position
                        entry.username=username
                        entry.password=password                                                           
                        entry.mob=mob
                        entry.email=email
                        entry.city=city
                        entry.address=address
                        entry.gender=gender
                        db.session.commit()
                        return redirect("/employees")
                    else:
                        print(f"record {tid1} not exist with table Employee ")
                        return redirect("/employees") 

            emp = Employee.query.filter_by(eno=tid).first()            
            return render_template("edit_employees.html",emp=emp,params=params,tid=tid)

        if action=='admin':
            if request.method=="POST":
                # eid=request.form.get('tid')
                fname=request.form.get('fname')                
                lname=request.form.get('lname')
                username=request.form.get('username')
                password=request.form.get('password')                
                
                if tid1=="0":
                    entry = Admin(fname = fname,lname = lname,username=username,password=password )
                    db.session.add(entry)
                    db.session.commit()
                    return redirect("/admins")
                else:
                    entry = Admin.query.filter_by(uid=tid1).first()
                    if entry!=None:                    
                        entry.fname=fname                        
                        entry.lname=lname
                        entry.username=username
                        entry.password=password                                                           
                        db.session.commit()
                        return redirect("/admins")
                    else:
                        print(f"record {tid1} not exist with table Admin ")
                        return redirect("/admins") 

            emp = Admin.query.filter_by(uid=tid).first()            
            return render_template("edit_admins.html",emp=emp,params=params,tid=tid)



    return redirect("/admin")

@dips.route("/delete",methods = ['GET', 'POST'])
def delete():
   action = request.args.get('action', None)
   tid = request.args.get('tid', None)
   date = request.args.get('date', None)
   
   if 'admin' in session:          
        if action =='attendance':
            post=Emp_attendance.query.filter_by(eid=tid,date=date).first()
            if post!=None:
                db.session.delete(post)
                db.session.commit()
        if action =='employee':
            post=Employee.query.filter_by(eno=tid).first()
            if post!=None:
                db.session.delete(post)
                db.session.commit()
            return redirect("/employees")
        if action =='admin':
            post=Admin.query.filter_by(uid=tid).first()
            if post!=None:
                db.session.delete(post)
                db.session.commit()
            return redirect("/admins")
   return redirect("/admin")


@dips.route("/employee", methods = ['GET', 'POST'])
def employee():
    btn=0
    if ('employee' in session):
        eno=session['employee']
        print("Employee no is",eno)
        tout=request.args.get('tout',None)
        time=datetime.time(datetime.now())
        date=datetime.date(datetime.now())
        entry=Emp_attendance.query.filter_by(eid=eno,date=date).first()
        if tout=='1' and entry.timeout==" ":
            entry.timeout=time
            db.session.commit()
        if entry.timeout==" ":
            btn=1
        attendance = Emp_attendance.query.filter_by(eid=eno).all()     
        last = math.ceil(len(attendance)/int(params['no_of_posts']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        attendance = attendance[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
        if page==1:
            prev = "#"
            next = "employee?page="+ str(page+1)
        elif page==last:
            prev = "employee?page="+ str(page-1)
            next = "#"
        else:
            prev = "employee?page="+ str(page-1)
            next = "employee?page="+ str(page+1)
    
        return render_template("employee.html",btn=btn,params=params,attendance=attendance, prev=prev, next=next,name=entry.ename)
       

    if request.method=="POST":        
        username=request.form.get("uname")
        userpass=request.form.get("pass")
        result=Employee.query.filter_by(username=username,password=userpass).first()
        if result!=None:
            if result.username==username and result.password==userpass:
                session["employee"]=result.eno
                print(F"User id is {session['employee']}")
                date=datetime.date(datetime.now())
                time=datetime.time(datetime.now())
                entry=Emp_attendance(eid=result.eno,ename=result.fname+result.mname+result.lname,status="Present",date=date,timein=time,timeout=" ")
                check=Emp_attendance.query.filter_by(eid=result.eno,date=date).first()
                                    
                if check==None:
                    db.session.add(entry)
                    db.session.commit()
                    btn=1
                elif check.timeout==" ":
                    btn=1
                attendance = Emp_attendance.query.filter_by(eid=result.eno).all()
                last = math.ceil(len(attendance)/int(params['no_of_posts']))
                page = request.args.get('page')
                if (not str(page).isnumeric()):
                    page = 1
                page = int(page)
                attendance = attendance[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
                if page==1:
                    prev = "#"
                    next = "employee?page="+ str(page+1)
                elif page==last:
                    prev = "employee?page="+ str(page-1)
                    next = "#"
                else:
                    prev = "employee?page="+ str(page-1)
                    next = "employee?page="+ str(page+1)                
                return render_template("employee.html",btn=btn,params=params,attendance=attendance, prev=prev, next=next,name=entry.ename)

    return render_template("elogin.html",params=params)

@dips.route("/alogout")
def alogout():
    session.pop('admin')
    return redirect("/")

@dips.route("/elogout")
def elogout():
    session.pop('employee')
    return redirect("/")

dips.run(debug=True)