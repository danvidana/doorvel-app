from django.db import connection
cursor = connection.cursor()
cursor.execute("""SELECT settlement.zip_code_fk as 'zip_code', zip_code.locality, federal_entity.key as 'fk_key', federal_entity.name as 'fk_name', federal_entity.code as 'fk_code', settlement.key, settlement.name as 'name', settlement.zone_type, settlement_type.name as 'st_name', municipality.key as 'm_key', municipality.name as 'm_name' FROM settlement INNER JOIN settlement_type ON settlement.settlement_type_fk=settlement_type.key INNER JOIN zip_code ON settlement.zip_code_fk=zip_code.zip_code INNER JOIN federal_entity ON zip_code.federal_entity_fk=federal_entity.key INNER JOIN municipality ON zip_code.municipality_fk=municipality.key WHERE zip_code_fk='04260'""")
row = cursor.fetchone()
print(row)