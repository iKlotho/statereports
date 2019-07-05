State Reports from ic3.gov
=============================================

This package scrapes data from ic3.gov.
The page gets raw data from https://www.ic3.gov/media/annualreport/2016State/stats?s=1


- s=1 correspondes to state id


- 2016state is the year the data belong


Example Getting 2016 Data as xslx


to excel

.. code-block:: sh
 python3 fetch_and_save.py -y 2016


to csv


.. python3 fetch_and_save.py -y 2016 -t csv


to excel with not sheeted


.. python3 fetch_and_save.py -y 2016 -s f 




