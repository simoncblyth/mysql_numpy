
#include <numpy/arrayobject.h>
#define DTYPE_FIELD_MAX  50 
#define DTYPE_FMTLEN_MAX 30

char* NPY_TYPE_NAMES[NPY_NTYPES] =  { 
     "NPY_BOOL",
     "NPY_BYTE", 
     "NPY_UBYTE",
     "NPY_SHORT", 
     "NPY_USHORT",
     "NPY_INT", 
     "NPY_UINT",
     "NPY_LONG", 
     "NPY_ULONG",
     "NPY_LONGLONG", 
     "NPY_ULONGLONG",
     "NPY_HALF", 
     "NPY_FLOAT", 
     "NPY_DOUBLE", 
     "NPY_LONGDOUBLE",
     "NPY_CFLOAT", 
     "NPY_CDOUBLE", 
     "NPY_CLONGDOUBLE",
     "NPY_DATETIME", 
     "NPY_TIMEDELTA",
     "NPY_OBJECT",
     "NPY_STRING", 
     "NPY_UNICODE",
     "NPY_VOID" } ;
 
char* NPY_TYPE_FMTS[NPY_NTYPES] =  { 
     "%"NPY_BYTE_FMT, // "NPY_BOOL_FMT",
     "%"NPY_BYTE_FMT, 
     "%"NPY_UBYTE_FMT ,
     "%"NPY_SHORT_FMT, 
     "%"NPY_USHORT_FMT,
     "%"NPY_INT_FMT, 
     "%"NPY_UINT_FMT,
     "%"NPY_LONG_FMT, 
     "%"NPY_ULONG_FMT,
     "%"NPY_LONGLONG_FMT, 
     "%"NPY_ULONGLONG_FMT,
     "%"NPY_HALF_FMT, 
     "%"NPY_FLOAT_FMT, 
     "%lg",  // %"NPY_DOUBLE_FMT (tiz g)
     "%Lg",  // %"NPY_LONGDOUBLE_FMT (tiz g)
     "NPY_CFLOAT_FMT", 
     "NPY_CDOUBLE", 
     "NPY_CLONGDOUBLE",
     "%lld",  // "%"NPY_DATETIME_FMT,   see env/npy/numpy/datetime_buf.c for rationale  
     "%lld",  // "%"NPY_TIMEDELTA_FMT,
     "NPY_OBJECT_FMT",
     "NPY_STRING_FMT", 
     "NPY_UNICODE_FMT",
     "NPY_VOID_FMT" } ;


/*
   http://dev.mysql.com/doc/refman/5.5/en/c-api-data-structures.html
   http://dev.mysql.com/doc/refman/5.5/en/numeric-types.html
   http://docs.scipy.org/doc/numpy/reference/c-api.dtype.html
*/

int mysql2npy( long type ){
   int npt = -1 ; 
   switch( type ){

       case MYSQL_TYPE_TINY: 
       case MYSQL_TYPE_SHORT: 
          npt = NPY_SHORT ; 
          break ; 
       case MYSQL_TYPE_ENUM: 
       case MYSQL_TYPE_SET: 
       case MYSQL_TYPE_INT24: 
       case MYSQL_TYPE_LONG: 
          npt = NPY_INT ; 
          break ; 
       case MYSQL_TYPE_LONGLONG: 
          npt = NPY_LONGLONG ; 
          break ; 

       case MYSQL_TYPE_DECIMAL: 
       case MYSQL_TYPE_DOUBLE: 
          npt = NPY_DOUBLE ; 
          break ; 
       case MYSQL_TYPE_FLOAT: 
          npt = NPY_FLOAT ; 
          break ; 
          
       case MYSQL_TYPE_DATE: 
       case MYSQL_TYPE_TIME: 
       case MYSQL_TYPE_DATETIME: 
       case MYSQL_TYPE_YEAR: 
       case MYSQL_TYPE_NEWDATE: 
       case MYSQL_TYPE_TIMESTAMP: 
          npt = NPY_DATETIME ; 
          break ; 
 
       case MYSQL_TYPE_VAR_STRING:
       case MYSQL_TYPE_STRING:
          npt = NPY_STRING ; 
          break ; 

#if MYSQL_VERSION_ID >= 50000
// present in 5.1.50 but not 4.1.22
       case MYSQL_TYPE_VARCHAR: 
           npt = NPY_STRING ;
           break ; 
       case MYSQL_TYPE_BIT:
           npt = NPY_SHORT ;
           break ; 
       case  MYSQL_TYPE_NEWDECIMAL:
           npt = NPY_DOUBLE ; 
           break ; 
#endif

   }
   return npt ;
}


