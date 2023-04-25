from sqlalchemy import create_engine

# To connect to database
db_connection_string = "mysql+pymysql://mzdiy6qpd7cpzozva0cd:pscale_pw_V8BPZWwCBugij488yGey5j9HbUh1O9zy7zTzU01Vy1x@aws.connect.psdb.cloud/gpa_db?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})
