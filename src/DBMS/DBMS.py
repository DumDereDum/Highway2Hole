import sqlite3
import sys
# sys.path.append()
import cv2

class DBMS_:   
    __db = None
    __sql = None
    __cur_id = 1
    __db_path = None

    def __init__(self, path):
        DBMS_.__db_path = path
        DBMS_.__db = sqlite3.connect(DBMS_.__db_path + '\data\highway2hole.db')
        DBMS_.__sql = DBMS_.__db.cursor()
        DBMS_.__sql.execute("""CREATE TABLE IF NOT EXISTS RoadPits (
            ID integer,
            PHOTO_PATH text,
            TIME text,
            GPS_LAT text,
            GPS_LON text,
            IS_NEW integer
        )""")
        DBMS_.__db.commit()
        
    def add_pothole(self, frame, time, gps_lat, gps_lon):
        photo_path = DBMS_.__db_path + "\data\img\img_" + str(DBMS_.__cur_id) + ".png"
        cv2.imwrite(photo_path, frame)
        DBMS_.__sql.execute("INSERT INTO RoadPits VALUES (?,?,?,?,?,?)",(DBMS_.__cur_id, photo_path, time, gps_lat, gps_lon, 1))
        DBMS_.__db.commit()
        DBMS_.__cur_id += 1

    def get_new_potholes(self):
        lst = list()
        DBMS_.__sql.execute("SELECT * FROM RoadPits WHERE IS_NEW = 1")
        records = DBMS_.__sql.fetchall()
        for value in records:
            DBMS_.__sql.execute('UPDATE RoadPits SET IS_NEW = ? WHERE ID = ?', (0,value[0]))
            DBMS_.__db.commit()
            img = cv2.imread(value[1])
            tpl = [img, value[0], value[1], value[2], value[3], value[4]]
            lst.append(tpl)
        return lst
