users=[]
for i in range(59):
    new_user={"color":"red" , "speed":"slow" , "coins":5}
    users.append(new_user)
print(users)

for x in users[8:16]:
    if x["color"]=="red":
        x["color"]="green"
        x["speed"]="meedl"
        x["coins"]=15
    
for z in users:
    print(z)
print("-"*60)
print(f"В игре {len(users)}  игроков")
