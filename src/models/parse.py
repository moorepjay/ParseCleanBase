import datetime
import re

from flask import jsonify

from src.models.entry import Entry

RX_DICT = {
    "request_id": re.compile(r'.{8}-.{4}-.{4}-.{4}-.{12}'),
    "create_date": re.compile(r'\d{2}\/\d{2}\/\d{4}'),
    "entity_name": re.compile(r'(?<=Entity Name:).+(?=\()'),
    "address": re.compile(r'(?<=Address:).+(?=\()'),

    "entity_name_sep": re.compile(r'.+(?=\()'),
    "address_sep": re.compile(r'.+(?=\()'),
    "clean_address": re.compile(r"(?<=\(').+(?=(\',\)))")
}

def parse_data(data):
    id_match = RX_DICT["request_id"].search(data).group()
    date_match = RX_DICT["create_date"].search(data).group()

    if RX_DICT["entity_name"].search(data) is None:
        entity_match = RX_DICT["entity_name_sep"].findall(data)[0]
        address_match = RX_DICT["address_sep"].findall(data)[1]
    else:
        entity_match = RX_DICT["entity_name"].search(data).group()
        address_match = RX_DICT["address"].search(data).group()

    my_entry = Entry(request_id=id_match,
                     created_date=date_match,
                     entity_name=entity_match,
                     address=address_match)

    return my_entry

