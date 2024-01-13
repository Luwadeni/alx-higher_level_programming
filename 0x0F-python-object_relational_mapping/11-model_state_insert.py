#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
It takes 3 arguments: mysql username, mysql password, and database name.
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print('Usage: argv[0] <username> <password> <database>',
              file=sys.stderr)
        exit()

    # Create a SQLAlchemy engine that provides a source of database
    # connectivity. This engine connects to the MySQL server using the
    # provided username, password, and database name.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],  # username
            sys.argv[2],  # password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True
    )

    # Create all tables in the engine. This is akin to the "CREATE TABLE"
    # statement in raw SQL. It uses the metadata from the Base class to
    # determine the structure of the tables.
    Base.metadata.create_all(engine)

    # Create a new session for database interaction
    session = Session(engine)

    # Create a new State object with the name "Louisiana" and add it to the
    # session
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Query the State table for the newly added state and print its id
    states_t = session.query(State).filter_by(name="Louisiana").first()
    print(f"{states_t.id}")

    # Close the session to free up resources
    session.close()
