import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="RootPassword6!",
  database="doorvel_app_db"
)

zipCode_db = []
federalEntity_db = []
municipality_db = []
settlement_db = []

zipCodeSaved_Counter = 0
federalEntitySaved_Counter = 0
municipalitySaved_Counter = 0
settlementSaved_Counter = 0

mycursor = mydb.cursor()

zip_codeQ = "INSERT INTO zip_codes_zipcode(zip_code, locality, federal_entity_fk_id, municipality_fk_id) VALUES (%s, %s, %s, %s)"
federal_entityQ = "INSERT INTO zip_codes_federalentity(`key`, name, code) VALUES (%s, %s, NULL)"
municipalityQ = "INSERT INTO zip_codes_municipality(`key`, local_key, name) VALUES (%s, %s, %s)"
settlementQ = "INSERT INTO zip_codes_settlement(`key`, name, zone_type, settlement_type, settlement_local_key, zip_code_fk_id) VALUES (%s, %s, %s, %s, %s, %s)"

f = open("all.txt", "r", encoding='latin-1')
temp = f.read().splitlines()
headingList = []
print(len(temp))
for x, line in enumerate(temp):
  if x == 1:
    headingList = line.split("|")
  elif x > 1:
    lineData = line.split("|")
    lineDict = {
      "zip_code": lineData[0],
      "settlement_name": lineData[1],
      "settlement_type": lineData[2],
      "municipality_name": lineData[3],
      "federal_entity_name": lineData[4],
      "locality": lineData[5],
      "federal_entity_key": lineData[7],
      "municipality_key": lineData[7] + '_' + lineData[11],
      "local_key": lineData[11],
      "settlement_key": lineData[7] + '_' + lineData[11] + '_' + lineData[12],
      "settlement_local_key": lineData[12],
      "zone_type": lineData[13],
    }
    print(x/len(temp) * 100, '%')
    
    if lineDict["zip_code"] in zipCode_db:
      print("Zip Code ", lineDict["zip_code"], " already in database. Not saving.")
    else:
      val = (lineDict["zip_code"], lineDict["locality"], lineDict["federal_entity_key"], lineDict["municipality_key"])
      mycursor.execute(zip_codeQ, val)
      mydb.commit()
      zipCodeSaved_Counter += 1
      zipCode_db.append(lineDict["zip_code"])
      
    if lineDict["federal_entity_key"] in federalEntity_db:
      print("Federal Entity ", lineDict["federal_entity_name"], " already in database. Not saving.")
    else:
      val = (lineDict["federal_entity_key"], lineDict["federal_entity_name"])
      mycursor.execute(federal_entityQ, val)
      mydb.commit()
      federalEntitySaved_Counter += 1
      federalEntity_db.append(lineDict["federal_entity_key"])
    
    if lineDict["municipality_key"] in municipality_db:
      print("Municipality ", lineDict["municipality_name"], " already in database. Not saving.")
    else:
      municipality_db.append(lineDict["municipality_key"])
      val = (lineDict["municipality_key"], lineDict["local_key"], lineDict["municipality_name"])
      mycursor.execute(municipalityQ, val)
      mydb.commit()
      municipalitySaved_Counter += 1
    
    if lineDict["settlement_key"] in settlement_db:
      print("Settlement ", lineDict["settlement_key"], " already in database. Not saving.")
    else:
      val = (lineDict["settlement_key"], lineDict["settlement_name"], lineDict["zone_type"], lineDict["settlement_type"], lineDict["settlement_local_key"], lineDict["zip_code"])
      mycursor.execute(settlementQ, val)
      mydb.commit()
      settlementSaved_Counter += 1
      settlement_db.append(lineDict["settlement_key"])
    
# # print(zipCodeSaved_Counter, "zipcodes inserted.")
# # print(federalEntitySaved_Counter, "federalentities inserted.")
# # print(municipalitySaved_Counter, "municipalities inserted.")
print(settlementSaved_Counter, "settlements inserted.")


