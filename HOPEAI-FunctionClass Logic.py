class SubfieldsInAI():
    def Subfields():
        LIST = ['Sub-fields in AI are:','Machine Learning', 'Neural Networks','Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for temp in LIST:
            print (temp)
            
class OddEven():
    def OddEven():
        num = int(input("Enter a number: "))
        if ((num%2)==0):
            print (f"{num} is Even number")
        else:
            print(f"{num} is Odd number")
            
class EligibilityForMarriage():
    def Eligible():
        Gender = input("Your Gender:")
        Age= int(input("Your Age:"))
        if (Gender=="Male"):
            if (Age>=21):
                print ("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif (Gender=="Female"):
            if (Age>=18):
                print ("ELIGIBLE")
            else:
                print("Not Eligible")
                
class FindPercent():
    def percentage():
        Sub1=int(input("Subject1: "))
        Sub2=int(input("Subject2: "))
        Sub3=int(input("Subject3: "))
        Sub4=int(input("Subject4: "))
        Sub5=int(input("Subject5: "))
        Total= Sub1+Sub2+Sub3+Sub4+Sub5
        print ('Total:',Total)
        per=((Total/500)*100)
        print("Percentage:",per)
        
class triangle():
    def triangle():
        h=int(input("Height:"))
        b=h=int(input("Breadth:"))
        print("Area formula:(Height*Breadth)/2")
        area=(h*b)/2
        print("Area of triangle:",area)
    
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b1=int(input("Breadth:"))
        print("Perimeter formula:(Height1+Height2+Breadth)")
        peri=((h1+h2+b1))
        print("Perimeter of triangle:",peri)