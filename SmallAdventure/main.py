#Creado por: Ivanovich6v4
#Historia por: Javier Fernandez
##Version de Python: 3.9.5
#Fecha de creacion: 21 de Julio 2021
import time

def intro(zentrum):
    print("*·*·*·*·*·*·*·*·*·*·*·*·*·*·*·*·*\n  Welcome to <Small Adventure>!\n  Enjoy your own small story.\n*·*·*·*·*·*·*·*·*·*·*·*·*·*·*·*·*\n ")
    name = input("Please enter your \"name\": \n  > ")
    zentrum['Name'] = name
    zentrum['SpecialName'] = 0

    if name.lower() == "Baron" or name.lower() == "Fidelio" or name.lower() == "":
        zentrum['SpecialName']=1
    

    print("\n\n\n   ---This is now the story of "+str(zentrum['Name']+"---"))
    return zentrum

def prelude(zentrum):
    
    print("\n\n It is a really dark night outside.\n It's already past midnight and you decide to go for a drive.\n Driving calms you and helps you stop thinking about your struggles and issues. You can feel the wind brushing your hair as you accelerate on the road to the country.\n Suddenly, the car loses strength and begins to slow down until completely stopping at the side of the road.\n You step out of the car and feel the mud under your shoes sticking as you walk across the road.\n   What now?\n")
    
    op1=" 1. Take out your phone and try to call someone for help.\n"
    op2=" 2. Lean on your car waiting for some sort of miracle to happen.\n"
    op3=" 3. Take a blunt and smoke a while.\n"
    op4=" 4. Clean your shoes on the grass.\n"
    print(op1+op2+op3+op4)
    dec = input("  > ")
    if dec=="1":
        print ("It worked")
    elif dec=="2":
        print ("It worked")
    elif dec=="3":
        print ("It worked")
    elif dec=="4":
        print ("It worked")
    else:
        print("Ah! You seem daring. Oh well, we are going to keep an eye on you then.")
    
    
    return zentrum



#Main
zentrum = {}
zentrum = intro(zentrum)
input("\n             [Press Enter to Continue]")
zentrum = prelude(zentrum)
input("\n             [Press Enter to Continue]")

print(zentrum)