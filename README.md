# Project Title

Python Assignment

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

To start App

```
python app.py -f <optional, input_data.txt>
```

if argument -f is not provided, data will be loaded from data.txt from current directory

### Test

To run the unit-tests ( Total : 3 ) :

```
python test.py -v
```

### Requirements

required python package

```
Flask==1.1.1
PTable==0.9.2
```

## Running the tests

```
python test.py -v
```

```
$ python test.py -v
test_interface (__main__.FlaskTestCase) ... +-------------+--------------------+
|     key     |       value        |
+-------------+--------------------+
| description |       to-LAN       |
|  interface  | GigabitEthernet0/0 |
|  ip_address |     172.16.1.2     |
|    subnet   |   255.255.255.0    |
+-------------+--------------------+
ok
test_interface_all (__main__.FlaskTestCase) ... +-------------+--------------------+
|     key     |       value        |
+-------------+--------------------+
| description |       to-LAN       |
|  interface  | GigabitEthernet0/0 |
|  ip_address |     172.16.1.2     |
|    subnet   |   255.255.255.0    |
+-------------+--------------------+
+-------------+---------------------------------+
|     key     |              value              |
+-------------+---------------------------------+
| description | CA-BBAABB3-1_AGSW-1_Gi0/3_VL331 |
|  interface  |        GigabitEthernet0/1       |
|  ip_address |            10.66.0.71           |
|    subnet   |         255.255.255.252         |
+-------------+---------------------------------+
+-------------+--------------------+
|     key     |       value        |
+-------------+--------------------+
| description |      to-LAN-2      |
|  interface  | GigabitEthernet0/0 |
|  ip_address |     172.16.2.1     |
|    subnet   |   255.255.255.0    |
+-------------+--------------------+
+-------------+-----------------+
|     key     |      value      |
+-------------+-----------------+
| description |     Loopback    |
|  interface  |    Loopback0    |
|  ip_address |   192.168.1.1   |
|    subnet   | 255.255.255.255 |
+-------------+-----------------+
ok
test_interface_negative (__main__.FlaskTestCase) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.021s

OK
```
