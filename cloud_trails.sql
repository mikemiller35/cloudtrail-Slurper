CREATE TABLE cloud_trails (
	id serial PRIMARY KEY,
	event_id VARCHAR ( 36 ) UNIQUE NOT NULL,
	event_time TIMESTAMP,
	user_name VARCHAR ( 42 ) ,
    event_name VARCHAR ( 32 ) ,
    resource_type VARCHAR ( 24 ) ,
    resources TEXT ,
    aws_access_key VARCHAR ( 64 ) ,
    aws_region VARCHAR ( 12 ) ,
    error_code VARCHAR ( 32 ) ,
    source_ip VARCHAR (16)
);