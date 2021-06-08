"""
This file contains the Post class that takes care of everything invlovled in post management
"""
class Post:
    """
    This class creates, reads, updates, delete posts;
    """
    def __init__(self, post_id, title, post, data):
        self.post_id = post_id
        self.title = title
        self.post = post
        self.data = data

    def create_post(self):
        """
        Take in (post_id, title, post)
        and returns a single post.
        """
        new_post = {
            'id':self.post_id,
            'title':self.title,
            'post':self.post,
        }

        self.data.append(new_post)
        return new_post

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
            if i['id'] == post_id:
                return i
        return 'Post not found'

    def update_post(self, post_id, title, post):
        """
        Takes in post_id and updates post associated with post_id and returns updated post.
        """
        for i in self.data:
            if i['id'] == post_id:
                i['title'] = title
                i['post'] = post
                return i
        return 'Post not found'

    def delete_post(self, post_id):
        """
        Takes in post_id and deletes post associated with post_id returns deleted post.
        """
        for i in range(len(self.data)):
            if self.data[i]['id'] == post_id:
                return self.data.pop(i)
        return 'Post not found'
