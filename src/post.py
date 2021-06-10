"""
This file contains the Post class that takes care of everything invlovled in post management
"""
import random

class Post:
    """
    This class creates, reads, updates, delete posts;
    """

    def __init__(self, data):
        self.data = data

    def create_post(self, title, post):
        """
        Take in (post_id, title, post)
        and returns a single post.
        """
        new_post = {
            "id": self.generate_post_id(),
            "title": title,
            "post": post,
        }

        self.data.append(new_post)
        return self.data

    def view_all_posts(self):
        """
        Returns all posts.
        """
        return self.data

    def view_single_post(self, post_id):
        """
        Takes in post_id and returns post associated with post_id.
        """
        for i in self.data:
            if i["id"] == post_id:
                return i
        return "Post not found"

    def update_post(self, post_id, title, post):
        """
        Takes in post_id and updates post associated with post_id and returns updated post.
        """
        for i in self.data:
            if i["id"] == post_id:
                i["title"] = title
                i["post"] = post
                return i
        return "Post not found"

    def delete_post(self, post_id):
        """
        Takes in post_id and deletes post associated with post_id returns deleted post.
        """
        for i in range(len(self.data)):
            if self.data[i]["id"] == post_id:
                return self.data.pop(i)
        return "Post not found"

    def generate_post_id(self):
        """
        This recursive method allows us to create automated unique post ids
        Returns 10 character string
        """
        string = list("abcdefghijklmnopqrstuvwxyz0123456789")
        random.shuffle(string)
        string = "".join(string)

        # ensure post id doesn't exits in the db
        for i in self.data:
            if i["id"] == string:
                self.generate_post_id()
        return string[:10]
