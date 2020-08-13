import sys, csv
import psycopg2

## Make the db stuff easy
class MyDatabase:
    def __init__(self, host="127.0.0.1", db="aws", user="mmiller"):
        self.conn = psycopg2.connect(host=host, database=db, user=user)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()


##Slurp and SQL
def csv_slurp_to_sql():
    db = MyDatabase()
    file = sys.argv[1]
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(row)
            query = "INSERT INTO cloud_trails (event_id, event_time, user_name, event_name, resource_type, resources, aws_access_key, aws_region, error_code, source_ip) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
            db.query(
                query
                % tuple(row)
            )
            db.conn.commit()
    print("All done!\n")
    db.close()


if __name__ == "__main__":
    csv_slurp_to_sql()
