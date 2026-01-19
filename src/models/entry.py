import datetime
import uuid

from src.common.database import Database


class Entry(object):

    def __init__(self, request_id, created_date, entity_name, address, reviewer_name="",
                 reviewed_date=datetime.date.today().isoformat(),
                 current_utc_time=datetime.datetime.utcnow().time().strftime("%H:%M"),
                 final_decision=None, comments=None, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.request_id = request_id
        self.entity_name = entity_name
        self.created_date = created_date
        self.address = address
        self.reviewer_name = reviewer_name
        self.reviewed_date = reviewed_date
        self.current_utc_time = current_utc_time
        self.final_decision = final_decision
        self.comments = comments

    def __repr__(self):
        return f'<Entry for {self.entity_name}: {self.request_id}>'

    def get_json_dict(self):
        return {
            "_id": self._id,
            "Reviewer Name": self.reviewer_name,
            "Date Reviewed": self.reviewed_date,
            "Created Date": self.created_date,
            "Current UTC Time": self.current_utc_time,
            "Request ID": self.request_id,
            "Entity Name": self.entity_name,
            "Address": self.address,
            "Final Decision": self.final_decision,
            "Comments": self.comments
        }

    def save_to_mongo(self):
        Database.insert(collection="parseTest",
                        data=self.get_json_dict())

    @classmethod
    def from_mongo(cls, idx):
        entry_data = Database.find_one(collection="parseTest", query={"_id": idx})
        return cls(
            _id=entry_data["_id"],
            reviewer_name=entry_data["Reviewer Name"],
            reviewed_date=entry_data["Date Reviewed"],
            created_date=entry_data["Created Date"],
            current_utc_time=entry_data["Current UTC Time"],
            request_id=entry_data["Request ID"],
            entity_name=entry_data["Entity Name"],
            address=entry_data["Address"],
            final_decision=entry_data["Final Decision"],
            comments=entry_data["Comments"]
        )
