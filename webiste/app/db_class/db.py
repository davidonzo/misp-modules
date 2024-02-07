from .. import db


class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, index=True, unique=True)
    description = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)
    request_on_query = db.Column(db.Boolean, default=False)

    def to_json(self):
        json_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active,
            "request_on_query": self.request_on_query
        }
        return json_dict

class Session_db(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(db.String(36), index=True, unique=True)
    glob_query = db.Column(db.String)
    query_enter = db.Column(db.String)
    input_query = db.Column(db.String)
    config_module=db.Column(db.String)
    result=db.Column(db.String)
    nb_errors = db.Column(db.Integer, index=True)

    def to_json(self):
        return


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_id = db.Column(db.Integer, index=True)


class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, index=True, unique=True)

class Module_Config(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    module_id = db.Column(db.Integer, index=True)
    config_id = db.Column(db.Integer, index=True)
    value = db.Column(db.String, index=True)

