import _mysql

"""

+-------------+------------+------+-----+---------------------+----------------+
| SEQNO       | int(11)    |      | PRI | NULL                | auto_increment |
| TIMESTART   | datetime   |      | MUL | 0000-00-00 00:00:00 |                |
| TIMEEND     | datetime   |      | MUL | 0000-00-00 00:00:00 |                |
| SITEMASK    | tinyint(4) | YES  |     | NULL                |                |
| SIMMASK     | tinyint(4) | YES  |     | NULL                |                |
| SUBSITE     | int(11)    | YES  |     | NULL                |                |
| TASK        | int(11)    | YES  |     | NULL                |                |
| AGGREGATENO | int(11)    | YES  |     | NULL                |                |
| VERSIONDATE | datetime   |      |     | 0000-00-00 00:00:00 |                |
| INSERTDATE  | datetime   |      |     | 0000-00-00 00:00:00 |                |
+-------------+------------+------+-----+---------------------+----------------+
10 rows in set (0.00 sec)

select UNIX_TIMESTAMP(TIMESTART) as TIMESTART from  CalibPmtSpecVld limit 10 ;
"""

if __name__ == '__main__':
    conn = _mysql.connect(  read_default_file="~/.my.cnf", read_default_group="client" ) 

    #conn.query("select * from CalibPmtSpecVld limit 10")
    #conn.query("select SEQNO, UNIX_TIMESTAMP(TIMESTART) as TIMESTART from CalibPmtSpecVld limit 10")
    conn.query("select SEQNO, UNIX_TIMESTAMP(TIMESTART) as TIMESTART_ from CalibPmtSpecVld limit 10")
    r = conn.store_result()

    #a = r.fetch_nparray()
    a = r.fetch_nparrayfast()

    print repr(a)

