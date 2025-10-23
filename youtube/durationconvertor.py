
#duration convertor: converts duration from seconds to other units and vice versa


seconds=int(input("Enter duration in seconds: "))


minutes=seconds//60
hours =minutes//60
Days=hours//24
hours=hours%24
minutes=minutes%60
seconds=seconds%60

print(f"{Days}:{hours}:{minutes}:{seconds}")