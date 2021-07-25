from pyrogram import Client
from datetime import datetime
import time
import os




zip_password = "blahblahbalh"
zip_name = "{:%Y%m%d}.zip".format(datetime.now())



username = "username"
api_id=000000
api_hash="API_HASH"



app = Client(
    username,
    api_id=api_id,
    api_hash=api_hash
)



with app:

#start of bk db

    os.system("mysqldump --all-databases --single-transaction --no-tablespaces  -u root > all_db.sql")

    os.system("zip -P {} {} all_db.sql".format(
        zip_password,
        zip_name
    ))

    time.sleep(1)

    app.send_document(
        username,
        zip_name
        )

    os.remove("all_db.sql")
    os.remove(zip_name)

#end of bk db



#start of bk files

    zip_name = "files_BK.zip"

    os.system("zip -r -P {} {} /var/www/".format(
        zip_password,
        zip_name
    ))

    time.sleep(1)

    app.send_document(
        username,
        zip_name
        )

    os.remove(zip_name)


#end of bk db

    app.stop()
    exit(0) # exit from script

app.run()
