class History:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        history = self.session.get("history")

        if not history:
            history = self.session["history"] = {}
        else:
            self.history = history

    def add(self, post):
        if (str(post.id) not in self.history.keys()):
            self.history[post.id] = {
                "post_id": post.id,
                "title": post.title,
                "message": post.message,
                "count": 1,
                "profile": post.user.profilepic.url
            }
        else:
            for key, value in self.history.items():
                if key == str(post.id):
                    value["count"] = value["count"] + 1
                    break
        self.save_history()

    def save_history(self):
        self.session["history"] = self.history
        self.session.modified = True

    def rem(self, post):
        post.id = str(post.id)
        if post.id in self.history:
            del self.history[post.id]
            self.save_history()

    def sub_post(self, post):
        for key, value in self.history.items():
            if key == str(post.id):
                value["count"] = value["count"] - 1
                if value["count"] < 1:
                    self.rem(post)
                break
        self.save_history()

    def clean_history(self):
        self.session["history"] = {}
        self.session.modified = True
