def country(area,landmass):
    result=(area/landmass)*100
    return result
    
area=int(input("Enter the area of the country: "))
name=input("Enter the name of the country: ")
landmass=148940000
print(f"{name} is {country(area,landmass)} % of the total world's landmass ")