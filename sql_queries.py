# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
song_table_drop = "DROP table IF EXISTS songs"
user_table_drop = "DROP table IF EXISTS users"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time timestamptz PRIMARY KEY, 
                                                         hour varchar, 
                                                         day varchar, 
                                                         week varchar, 
                                                         month varchar, 
                                                         year varchar, 
                                                         weekday varchar);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, 
                                                          first_name varchar, 
                                                          last_name varchar, 
                                                          gender varchar, 
                                                          level varchar);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, 
                                                              name varchar, 
                                                              location varchar, 
                                                              latitude float, 
                                                              longitude float);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, 
                                                          title varchar, 
                                                          artist_id varchar, 
                                                          year int, 
                                                          duration float);
""")

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, 
                                                                   start_time timestamptz, 
                                                                   user_id int, 
                                                                   level varchar, 
                                                                   song_id varchar, 
                                                                   artist_id varchar, 
                                                                   session_id int, 
                                                                   location varchar, 
                                                                   user_agent varchar);
""")


# INSERT RECORDS

songplay_table_insert = ("INSERT into songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
            VALUES  (%s, %s, %s, %s, %s, %s, %s, %s)")
                                                  
user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;""")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)")


artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) 
                                VALUES (%s, %s, %s, %s, %s)
                                ON CONFLICT (artist_id) DO NOTHING;""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s)
                                ON CONFLICT (start_time) DO NOTHING;""")

# FIND SONGS

song_select = ("""
        SELECT songs.song_id,artists.artist_id FROM songs INNER JOIN artists ON songs.artist_id = artists.artist_id
        WHERE songs.title = (%s) AND artists.name = (%s) AND songs.duration = (%s)
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]