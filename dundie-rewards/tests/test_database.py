import pytest

from dundie.database import EMPTY_DB, commit, connect, add_person, add_movement



@pytest.mark.unit
def test_database_schema():
    db = connect()
    assert db.keys() == EMPTY_DB.keys()


@pytest.mark.unit
def test_commit_to_database():
    db = connect()
    data = {"name": "Joe Doe", "role": "Salesman", "dept": "Sales"}
    db["people"]["joe@doe.com"] = data
    commit(db)

    db = connect()
    assert db["people"]["joe@doe.com"]["name"] == "Joe Doe"
    
@pytest.mark.unit
def test_add_person_for_the_first_time():
    pk = "joe@doe.com"
    data = {"name": "Joe Doe", "role": "Salesman", "dept": "Sales"}
    db = connect()
    person, created = add_person(db, pk, data)
    assert created
    commit(db)
    
    db = connect()
    assert db["people"][pk] == data
    assert db["balance"][pk] == 500
    print(db["people"][pk], " ", "*" * 50)
    assert len(db["movement"][pk]) > 0
    assert db["movement"][pk][0]["value"] == 500
    
    
@pytest.mark.unit
def test_negative_add_person_invalid_email():
    with pytest.raises(ValueError):
        add_person({}, "joe", {})
        
@pytest.mark.unit
def test_add_or_remove_pointsvalue_for_person():
    pk = "joe@doe.com"
    data = {"name": "Joe Doe", "role": "Salesman", "dept": "Sales"}
    db = connect()
    _, created = add_person(db, pk, data)
    assert created
    commit(db)
    
    db = connect()
    before = db["balance"][pk]
    
    add_movement(db, pk, -100, "manager")
    commit(db)
    
    db = connect()
    after = db["balance"][pk]
    
    assert after == 400
    assert before == 500
    assert after == before - 100
    
    
