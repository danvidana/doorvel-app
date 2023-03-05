import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="RootPassword6!",
  database="doorvel_app_db"
)

zipCode_db = ['04260']
federalEntity_db = ['09']
municipality_db = []

zipCodeSaved_Counter = 0
federalEntitySaved_Counter = 0

mycursor = mydb.cursor()

zip_codeQ = "INSERT INTO zip_codes_zipcode(zip_code, locality) VALUES (%s, %s)"
federal_entityQ = "INSERT INTO zip_codes_federalentity(`key`, name, code, zip_code_id) VALUES (%s, %s, NULL, %s)"

f = open("all.txt", "r", encoding='latin-1')
temp = f.read().splitlines()
headingList = []
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
      "municipality_key": lineData[10],
      "settlement_key": lineData[11],
      "settlement_type": lineData[12],
      }
    # if lineDict["zip_code"] in zipCode_db:
    #   print("Zip Code ", lineDict["zip_code"], " already in database. Not saving.")
    # else:
    #   val = (lineDict["zip_code"], lineDict["locality"]) 
    #   mycursor.execute(zip_codeQ, val)
    #   mydb.commit()
    #   zipCodeSaved_Counter += 1
    #   zipCode_db.append(lineDict["zip_code"])
      
    if lineDict["federal_entity_key"] in federalEntity_db:
      print("Federal Entity ", lineDict["federal_entity_name"], " already in database. Not saving.")
    else:
      val = (lineDict["federal_entity_key"], lineDict["federal_entity_name"], lineDict["zip_code"])
      mycursor.execute(federal_entityQ, val)
      mydb.commit()
      federalEntitySaved_Counter += 1
      federalEntity_db.append(lineDict["federal_entity_key"])
    
      
# print(zipCodeSaved_Counter, "zipcodes inserted.")
print(federalEntitySaved_Counter, "federalentities inserted.")

