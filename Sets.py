# -----------------------------------------
#            <<    Sets     >>
# -----------------------------------------
# [1]  Set Items Are Enclosed in Curly Braces
# [2]  Set Are Not Orders Not Indexed
# [3]  Set Indexing And Slicing Can't Be Done
# [4]  Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List And Dict Are Not
# [5]  Set Items Is Unique
# -----------------------------------------

# Not Orders Not Indexed

Monitor = {"ECG", "SpO2", "NIBP", "RESP", "TEMP"}
print(Monitor)      
# print(Monitor[2])            # Error

# Slicing Can't Be Done

Horus = {1, 2, 3, 4, 5}
# print(Horus[0:3])              # Error

# Has Only Immutable Data Types

# ICU = {"MICU", "NICU", "CICU", "PICU", "SICU", 79, 58, 63.4, True, [1, 2, 3]}         # unhashable type: 'list'
ICU = {"MICU", "NICU", "CICU", "PICU", "SICU", 79, 58, 63.4, True, (1, 2, 3)}
print(ICU)

# Items Is Unique

mySet = {1, 2 , "Horus", "One", 3, "Horus", 1}
print(mySet)

# -----------------------------------------
#          <<    Sets Methods    >>
# -----------------------------------------

# clear()                 # مسح

Rays = {"X-Ray", "CT Scan", "MRI", "Ultrasound"}
print(Rays.clear())

print("_" * 50)    # Separator

# union()                 # الاتحاد        

Rays = {"X-Ray", "CT Scan", "MRI", "Ultrasound"}
a = {"1", "2", "3"}
b = {"4", "5", "6"}
print(Rays | a)  
print(Rays.union(a))
print(Rays.union(a, b))

print("_" * 50)

# add()                   # اضافـة
Pressure = {"Mercury Sphygmomanometer"}
Pressure.add("Digital Monitors")
Pressure.add("Aneroid Monitor")
print(Pressure)

print("_" * 50)

# copy()                  # نسخ

Respiratory = {"Ventilators", "CPAP & BiPAP", "Oxygen Concentrators", "Spirometers"}
S = Respiratory.copy()

print(Respiratory)
print(S)

Respiratory.add("Nebulizers")
print(Respiratory)
print(S)

print("_" * 50)

# remove()                # ازالـة

Laboratory = {"Biochemistry Analyzers", "Hematology Analyzers", "Centrifuges", "Blood Gas Analyzers", "Immunoassay Analyzers", "Incubators"}
Laboratory.remove("Centrifuges")
# Laboratory.remove("Autoclaves")           # Error
print(Laboratory)  

print("_" * 50)

# discard()              #  remove() دي حتي لو العنصر مش موجود مش هيعطيك ايرور عكس فكرةايرور 

Laboratory = {"Biochemistry Analyzers", "Hematology Analyzers", "Centrifuges", "Blood Gas Analyzers", "Immunoassay Analyzers", "Incubators"}
Laboratory.discard("Centrifuges")
Laboratory.discard("Autoclaves")           
print(Laboratory)  

print("_" * 50)

# pop()

a = {1, 2, 3, "Horus", 25.5, True}
print(a.pop())

print("_" * 50)

# update()

K = {1, 2, 3, "A"}
L = {"A", "B", "C"}
K.update(["Python", "Javascript", "Html", "Css"])
K.update(L)
print(K)

print("_" * 50)

# difference()

Kidney_Devices = {1, 2, 3, "Hemodialysis", "Peritoneal Dialysis"}
Horus = {1, 2, "Mohammed", "Mahrous", "Taha"}
print(Kidney_Devices)
print(Kidney_Devices.difference(Horus))        # Kidney_Devices - Horus
print(Kidney_Devices)

print("_" * 50)

# difference_update()

Kidney_Devices = {1, 2, 3, "Hemodialysis", "Peritoneal Dialysis"}
Horus = {1, 2, "Mohammed", "Mahrous", "Taha"}
print(Kidney_Devices)
Kidney_Devices.difference_update(Horus)        # Kidney_Devices - Horus
print(Kidney_Devices)

print("_" * 50)

# intersection()                               # تقاطع

Heart = {1, 2, "ECG", "Echo", "Stress Test", "Pacemaker"}
Laboratory= {1, 2, "Hematology", "Clinical Chemistry", "Immunology"}
print(Heart)
print(Heart.intersection(Laboratory))          # Heart & Laboratory
print(Heart)

print("_" * 50)

# intersection_update()                              

Heart = {1, 2, "ECG", "Echo", "Stress Test", "Pacemaker"}
Laboratory= {1, 2, "Hematology", "Clinical Chemistry", "Immunology"}
print(Heart)
Heart.intersection_update(Laboratory)          # Heart & Laboratory
print(Heart)

print("_" * 50)

# symmetric_difference()

M = {1, 2, 3, "horus"}
S = {1, 2, 3, "Safe"}
print(M)
print(M.symmetric_difference(S))               # M ^ S
print(M)

print("_" * 50)

# symmetric_difference_update()

M = {1, 2, 3, "horus"}
S = {1, 2, 3, "Safe"}
print(M)
M.symmetric_difference_update(S)               # M ^ S
print(M)

print("_" * 50)

# issuperset()

Dental_Unit = {"Suction System", "Dental Light", "Intraoral X-Ray", "Intraoral Camera", "Apex Locator"}
Horus = {"Intraoral Camera", "Apex Locator", "Dental Light"}
Safe = {"Suction System", "Dental Light", "Intraoral X-Ray", "Intraoral Camera", "Apex Locator", "Panoramic Dental X-Ray"}
print(Dental_Unit.issuperset(Horus))          # True
print(Dental_Unit.issuperset(Safe))           # False

print("_" * 50)

# issubset()

X = {1, 2, 3, 4}
Y = {1, 2, 3}
Z = {1, 2, 3, 4, 5}
print(X.issubset(Y))                          # False
print(X.issubset(Z))                          # True

print("_" * 50)

# isdisjoint()                                # منفصلين

Dental = {"High-Speed Handpiece", "Low-Speed Handpiece", "Ultrasonic Scaler"}
Horus= {"High-Speed Handpiece", "Low-Speed Handpiece", "Ultrasonic Scaler", "Endodontic Motor"}
Safe = {"Endodontic Motor", "LED Curing Light"}

print(Dental.isdisjoint(Horus))               # False
print(Dental.isdisjoint(Safe))                # True











