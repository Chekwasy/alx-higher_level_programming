#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    found = False
    for state in session.query(State).order_by(State.id).all():
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            found = True
    if not found:
        print("Not found")
    session.close()
