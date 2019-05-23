void setup() {
  // put your setup code here, to run once:
  pinMode(2,INPUT);
  pinMode(3,INPUT);
  pinMode(4,INPUT);
  pinMode(5,INPUT);
  pinMode(6,INPUT);
  
  Serial.begin(9600);

}
boolean x1=false;
boolean x2=false;
boolean x3=false;
boolean x4=false;
boolean x5=false;
 
void loop() {
  // put your main code here, to run repeatedly:

   if(digitalRead(2)==1)
   {
      while(digitalRead(2)==1)
      {
       
      
       
      }
      x1=true;
      
   }  
 
   
   if(digitalRead(3)==1)
   {
      while(digitalRead(3)==1)
      {
       
      
       
      }
      x2=true;
      
   }  

   
 
   if(digitalRead(4)==1)
   {
      while(digitalRead(4)==1)
      {
       
      
       
      }
      x3=true;
      
   }
   if(digitalRead(5)==1)
   {
      while(digitalRead(5)==1)
      {
       
      
       
      }
      x4=true;
      
   }
   if(digitalRead(6)==1)
   {
      while(digitalRead(6)==1)
      {
       
      
       
      }
      x5=true;
      
   }  

   if(x1==true)
   {
    Serial.println("*");
    x1=false;
   }
 
   if(x2==true)
   {
    Serial.println("#");
    x2=false;
   }

   if(x3==true)
   {
    Serial.println("$");
    x3=false;
   }
   
      

   if(x4==true)
   {
    Serial.println("&");
    x4=false;
   }
   
   if(x5==true)
   {
    Serial.println("^");
    x5=false;
   }

   
   delay(200);

}
    
    
    
 


