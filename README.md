README
===========================================================
This is the deployr.


INSTALLATION
-----------------------------------------------------------

Install all dependencies via `pip`:

    $ pip install -r requirements.txt



RUN
-----------------------------------------------------------

Start a deployr locally via shell script:

    $ ./start_dev_deployr.sh



TESTS
-----------------------------------------------------------

deployr is using nose for testing.

Simply run:

    $ cd deployr
    $ nosetests


More info on nose at:
https://nose.readthedocs.org/en/latest/



FOR DEV
-----------------------------------------------------------

1. pep8:

        $ find . | grep ".py"$ | grep -v "misc" \
            | xargs pep8 --max-line-length=120