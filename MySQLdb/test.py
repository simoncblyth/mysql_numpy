import _mysql
"""
   ISSUES 
      * SQL queries with 2 columns of the same name yield "Bus Error"
      * array times feature unexpected TZ hour offsets 

[blyth@cms01 MySQLdb]$ python test.py
array([(17, datetime.datetime(2010, 6, 21, 7, 49, 24)),
       (18, datetime.datetime(2010, 6, 21, 7, 49, 24)),
       (19, datetime.datetime(2010, 6, 21, 7, 49, 24)),
       (20, datetime.datetime(2010, 6, 21, 7, 49, 24)),
       (21, datetime.datetime(2010, 6, 21, 7, 49, 24)),
       (22, datetime.datetime(2010, 6, 21, 7, 49, 24)),
       (23, datetime.datetime(2010, 9, 16, 6, 31, 34)),
       (24, datetime.datetime(2010, 9, 21, 5, 48, 57)),
       (25, datetime.datetime(2010, 9, 22, 4, 26, 59))], 
      dtype=[('SEQNO', '<i4'), ('TIMESTART_', ('<M8[s]', {}))])

echo "select SEQNO, TIMESTART, UNIX_TIMESTAMP(TIMESTART) as TIMESTART_ from CalibPmtSpecVld limit 10" | mysql
SEQNO   TIMESTART       TIMESTART_
17      2010-06-21 15:49:24     1277106564
18      2010-06-21 15:49:24     1277106564
19      2010-06-21 15:49:24     1277106564
20      2010-06-21 15:49:24     1277106564
21      2010-06-21 15:49:24     1277106564
22      2010-06-21 15:49:24     1277106564
23      2010-09-16 14:31:34     1284618694
24      2010-09-21 13:48:57     1285048137
25      2010-09-22 12:26:59     1285129619

"""

if __name__ == '__main__':
    conn = _mysql.connect(  read_default_file="~/.my.cnf", read_default_group="client" ) 

    #conn.query("select * from CalibPmtSpecVld limit 10")
    conn.query("select SEQNO, TIMESTART, UNIX_TIMESTAMP(TIMESTART) as T, UNIX_TIMESTAMP(TIMESTART) as I from CalibPmtSpecVld limit 10")

    r = conn.store_result()


    kwargs = dict( verbose=3,  coerce={'T':"M8[s]", 'I':"q8" } )

    d1 = r.npdescr(**kwargs)
    print repr(d1) 

    d2 = r.npdescr(**kwargs)
    print repr(d2) 

    #a = r.fetch_nparray(**kwargs)
    a = r.fetch_nparrayfast(**kwargs)

    print repr(a)



