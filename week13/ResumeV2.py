name = (input ("โปรดกรอกชือ : \n"))
age = (input("โปรดกรอกอายุ :\n"))
number = (input("โปรดกรอกรหัสประจำตัว : \n"))
level = (input("โปรดกรอกระดับชั้น :\n"))
nickname =(input("โปรดกรอกชื่อเล่น :\n"))
height = (input("โปรดกรอกส่วนสูง :\n"))
weight =(input("โปรดกรอกน้ำหนัก :\n"))
print(f"ชื่อ: "+{name} + "\tอายุ : " + {age} + "ปี")
print(f"รหัสประจำตัว :  "+ {number} + "\tระดับชั้น : " + {level} )
print(f"ส่วนสูง :  "+{height} + "เซนติเมตร" "\tน้ำหนัก : " + {weight} +"กิโลกรัม")

n = height + weight
print("ส่วนสูง + น้ำหนัก =" ,{n})


