Configuring and Running FRBR Redis Datastore
============================================
To configure and run the `FRBR Redis Datastore`, first :doc:`install` 
both the Redis_ and `FRBR Redis Datastore`_ and then you are ready to
get started.

Configuration
-------------
In the root directory for `FRBR Redis Datastore` project, there is a
config.py file that contains the following settings that you can change
depending on your set-up:

+-------------------+-------------------+---------+
| Name              | Description       | Example |
+===================+===================+=========+
| REDIS_HOST        | Server IP address | 0.0.0.0 |
|                   | of Redis server   |         |
+-------------------+-------------------+---------+
| REDIS_PORT        | Port number that  | 6379    |
|                   | Redis server      |         |
|                   | listens on        |         |
+-------------------+-------------------+---------+
| REDIS_DB          | Default Redis     | 0       |
|                   | Database          |         |
+-------------------+-------------------+---------+
| REDIS_TEST_DB     | Redis database    | 1       |
|                   | used for testing  |         |
+-------------------+-------------------+---------+
| REDIS_CODE4LIB_DB | Redis database    | 2       |
|                   | used for Code4Lib |         |
|                   | presentation      |         |
+-------------------+-------------------+---------+
| PRESENTATION_PORT | Port number that  | 8081    |
|                   | embedded bottle   |         |
|                   | runs to serve     |         |
|                   | presentation      |         |
+-------------------+-------------------+---------+
| WEB_HOST          | Server IP address | 0.0.0.0 |
|                   | to run embedded   |         |
|                   | bottle server     |         |
+-------------------+-------------------+---------+
| WEB_PORT          | Port number that  | 8080    |
|                   | embedded bottle   |         |
|                   | server runs on    |         |
+-------------------+-------------------+---------+


Running
-------
Redis
^^^^^
You need to have your instance of `Redis <http://redis.io>`_ up and
running before trying to start-up either the unit tests, embedded web
server, or the Code4Lib-based documentation.

Unit Tests
^^^^^^^^^^
To ensure that your environment is set-up correctly, after activating
your virtualenv instance, change directories to ``frbr-redis-datastore``
and run the unit tests for the project with this command:
``$ python test.py``. 

Code4Lib Presentation
^^^^^^^^^^^^^^^^^^^^^
To get an introduction of the `FRBR Redis Datastore`, you can run the
Jeremy Nelson's 2012 Code4Lib presentation, 
**NoSQL Bibliographic Records: Implementing a Native FRBR Datastore with
Redis** by running the following command: ``$ python code4lib2012.py`` 
and select option ``1) Standalone``.

You should then be able to access the presentation at 
`http://localhost:8081 <http://localhost:8081>`_ (the 8081 port number 
will be different if you changed the *PRESENTATION_PORT* setting in the
configuration)


