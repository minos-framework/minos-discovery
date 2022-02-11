History
=======

0.0.1 (2021-05-21)
------------------

* Added REST Interface for:
    * subscription
    * unsubscription
    * microservice health status update
    * periodic service for microservice health status check
* Redis integration

0.0.2 (2021-06-14)
------------------

* added cli support

0.0.3 (2021-07-27)
------------------

* Add a graceful stop timeout to `DiscoveryService`.
* Add `__main__.py`.
* Fix bugs related with connection.

0.0.4 (2021-08-19)
------------------

* Support auto discoverable endpoints.
* Refactor internal structure.

0.0.5 (2021-10-04)
------------------

* Fix bug related with response's status code of not found entry points.
* Fix bug related with microservice deletion.
* Minos improvements.

0.0.6 (2021-11-19)
------------------

* Added a logger to get trace of address

0.0.7 (2021-11-20)
------------------

* static address and port

0.0.8 (2021-11-20)
------------------

* modified PORT from string to INT

0.1.0 (2022-02-3)
------------------

* New view /endpoints. Return all endpoints stored.

0.1.1 (2022-02-11)
------------------

* Increment redis pool.
* Additional logs on `MinosRedisClient`.
