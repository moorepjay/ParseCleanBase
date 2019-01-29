import datetime
import uuid


class Entry(object):

    def __init__(self, request_id, created_date, entity_name, address, final_decision=None, idx=None, comments=None):
        self.request_id = request_id
        self.entity_name = entity_name
        self.created_date = created_date
        self.address = address
        self.reviewer_name = "v-prmoor"
        self.reviewed_date = datetime.date.today().isoformat()
        self.current_utc_time = datetime.datetime.utcnow().time().strftime("%H:%M")
        self.final_decision = final_decision
        self.comments = comments
        self.idx = uuid.uuid4().hex if idx is None else idx

    def __repr__(self):
        return f'<Entry for {self.entity_name}: {self.request_id}>'

    def get_json_dict(self):
        return {
            "Idx": self.idx,
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