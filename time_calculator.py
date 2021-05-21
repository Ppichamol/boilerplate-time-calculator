def add_time(start, duration,day='oo'):
  week = ["Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"]
  a = start.split()
  b = a[0].split(':')
  c = duration.split(':')
  da = (day.casefold()).capitalize()
  last = a[1]
  #print(da)
  new1 = int(b[0])+int(c[0])
  new2 = int(b[1])+ int(c[1])
  new = int(b[0])+int(c[0])
  if new2 > 60 :
    n = int(new2/60)
    new1 = new1+n
    new2 = new2-60
  d = int(new1/24) 
  #print(d) 
  if new1 > 12 and d<=1 :
    new1 = new1-(12*(d+1))
    #print (new1)
  if d>2:
    new1 = (24*(d+1))-new1
  #print(new1)
  if (day == 'oo'):
    if new >= 12 or new1 == 12:
      #print(new)
      if (a[1] == "AM" ):

        last = a[1].replace("AM","PM")
      if (a[1] == "PM" or d != 0 ):
        last = a[1].replace("PM","AM")+ " (next day)"
      if (a[1] == "PM") and d>=1:
        last = a[1].replace("PM","AM") + " (next day)"
        d=d+1
      if d>=2:
        last = a[1].replace("PM","AM") + " ("+ str(d)+" days later)"
  #print(last)  
    
  if (da in week):
      e = week.index(da)
      new3 = (e+d)%7
      #print(e)
      #print(new3)
      if e==6 and d==0:
        new3 = 6
      #print(new3)
      if (a[1] == "AM"):
        last = a[1].replace("AM","PM") + ", "+ week[e]
      if (a[1] == "PM" or d>0 ):
        last = a[1] + ", "+ week[new3]
        if d>0 :
          last = a[1].replace("PM","AM") + ", "+ week[new3]+ " (next day)"
      if (a[1] == "PM") and d>=1: 
        last = a[1].replace("PM","AM") + ", "+ week[new3]+ " (next day)"
        d=d+1
        #print(new3)
      if d>=2:
        new3=new3+1
        last = a[1].replace("PM","AM") + ", "+ week[new3]+ " ("+ str(d)+" days later)"
  if new2 < 10 :
    return(str(new1)+':'+'0'+str(new2)+" "+last)
  else: return(str(new1)+':'+str(new2)+" "+last)

  return new_time