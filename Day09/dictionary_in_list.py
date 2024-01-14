
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country: str, visits: int, list_of_cities: [str]):
    travel = {
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    }
    travel_log.append(travel)


def test_brazil():
    add_new_country("Brazil", 2, ["Sao Paulo", "Rio de Janeiro"])
    assert f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times." == "I've been to Brazil 2 times.", "expected: I've been to Brazil 2 times."
    assert f"My favourite city was {travel_log[2]['cities'][0]}." == "My favourite city was Sao Paulo.", "expected: My favourite city was Sao Paulo."

test_brazil()