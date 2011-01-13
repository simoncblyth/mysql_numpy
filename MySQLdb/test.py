import _mysql
"""
   ISSUES 
      * SQL queries with 2 columns of the same name yield "Bus Error"
        * unconfirmed, needs test
   FIXED ISSUES 
      * array times feature unexpected TZ hour offsets 
         * fixed by tweak in my github numpy fork , thats now in the official repo 
      

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

def test_npdescr():
    """
        Provides the dtype introspected and/or coerced from the mysql result 
       ... this is used internally by the array fetch methods
    """ 
    conn = _mysql.connect( read_default_group="client" ) 
    conn.query("select * from CalibPmtSpecVld limit 10")
    r = conn.store_result()
    d = r.npdescr()
    print repr(d) 
    conn.close()
  

def test_fetch_nparray():
    """
         When using normal fetching 
            * no special SQL needed
            * no coercion either 
         datetime columns should arrive by normal numpy routes

    """
    conn = _mysql.connect( read_default_group="client" ) 
    conn.query("select * from CalibPmtSpecVld limit 10")
    r = conn.store_result()
    a = r.fetch_nparray(verbose=0)
    print repr(a)
    conn.close()

def test_fetch_nparrayfast():
    """
        When using the fast variant 
          * use SQL that provides the datetime columns as epoch seconds and name them with a simple identifier eg T, I
          * coerce said columns at numpy level to be regarded as epoch seconds using dtype code M8[s]

    """  
    conn = _mysql.connect( read_default_group="client" ) 
    conn.query("select SEQNO, UNIX_TIMESTAMP(TIMESTART) as T, UNIX_TIMESTAMP(TIMESTART) as I from CalibPmtSpecVld limit 10")
    coerce={'T':"M8[s]", 'I':"M8[s]" }
    r = conn.store_result()
    a = r.fetch_nparrayfast(verbose=0,coerce=coerce)
    print repr(a)
    conn.close()


if __name__ == '__main__':
    pass
    #test_npdescr()
    #test_fetch_nparray()
    #test_fetch_nparrayfast()


if 1:
    conn = _mysql.connect( read_default_group="client" ) 
    #conn.query("select * from CalibPmtSpecVld limit 10")
    #conn.query("select * from CalibPmtSpec limit 10")
    #conn.query("select SEQNO, SITEMASK, SIMMASK, TIMESTART, SUBSITE, UNIX_TIMESTAMP(TIMESTART) as T, TASK, UNIX_TIMESTAMP(TIMESTART) as I, AGGREGATENO from CalibPmtSpecVld limit 3")
    conn.query("select SEQNO, UNIX_TIMESTAMP(TIMESTART) as T, UNIX_TIMESTAMP(TIMESTART) as I from CalibPmtSpecVld limit 3")
    r = conn.store_result()
    kwargs = dict( verbose=3,  coerce={'T':"M8[s]", 'I':"M8[s]" } )

    d1 = r.npdescr(**kwargs)
    print repr(d1) 
    a = r.fetch_nparrayfast(**kwargs)
    print repr(a)



