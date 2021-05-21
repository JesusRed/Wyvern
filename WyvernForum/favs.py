class Favs:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        favs = self.session.get("favs")

        if not favs:
            favs = self.session["favs"] = {}
        else:
            self.favs = favs

    def add(self, comment):
        if(str(comment.id) not in self.favs.keys()):
            self.favs[comment.id] = {
                "comment_id": comment.id,
                "title": comment.title,
                "user": comment.user,
                "message": comment.message,
                "cantidad": 1
            }
        else:
            for key, value in self.favs.items():
                if key == str(comment.id):
                    value["cantidad"] = value["cantidad"]+1
                    break
        self.save_favs()

    def save_favs(self):
        self.session["favs"] = self.favs
        self.session.modified = True

    def delete_favs(self, comment):
        comment.id = str(comment.id)
        if comment.id in self.favs:
            del self.favs[comment.id]
            self.save_favs()

    def less_favs(self, comment):
        for key, value in self.favs.items():
            if key == str(comment.id):
                value["cantidad"] = value["cantidad"]-1
                if value["cantidad"] < 1:
                    self.delete_favs(comment)
                break
        self.save_favs()

    def clean_favs(self):
        self.session["favs"] = {}
        self.session.modified = True
