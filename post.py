class Post:
    """
    This class creates, reads, updates, delete posts;
    """
    def __init__(self, id, title, post, data):
        self.id = id
        self.title = title
        self.post = post
        self.data = data

    def create_post(self):
        """
        Take in (id, title, post)
        and returns a single post.
        """
        new_post = {
            'id':self.id,
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

    def view_single_post(self, id):
        """
        Takes in id and returns post associated with id.
        """
        for i in self.data:
            if i['id'] == id:
                return i
        else:
            return 'Post not found'
    
    def update_post(self, id, title, post):
        """
        Takes in id and updates post associated with id and returns updated post.
        """
        for i in self.data:
            if i['id'] == id:
                i['title'] = title
                i['post'] = post
                return i
        else:
            return 'Post not found'

    def delete_post(self, id):
        """
        Takes in id and deletes post associated with id returns deleted post.
        """
        for i in range(len(self.data)):
            if self.data[i]['id'] == id:
                return self.data.pop(i)
        else:
            return 'Post not found'