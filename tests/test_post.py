"""
Tests to take care of our posts
"""
import pytest
from ..src.post import Post

test_data = [{"post": "This is a new post", "id": 30, "title": "New Post"}]

test_post = Post(31, "Test Title", "This is a test post for our unit test", test_data)

def test_create_post():
        """
        Function to test our create post
        Must return an object
        """
        created_data = test_post.create_post()
        assert created_data["title"] == "Test Title"

def test_view_single_post():
    """
    Function to test view all the posts
    """
    single_post_data = test_post.view_single_post(30)
    assert single_post_data["title"] == "New Post"

def test_update_post():
    """
    Function to test update post
    """
    successful_update = test_post.update_post(
        30, "Newer Post", "This is an updated post"
    )  # successful data
    failed_update = test_post.update_post(
        7, "New Post", "This is an updated post"
    )  # failed update

    assert successful_update["title"] == "Newer Post"
    assert failed_update == "Post not found"

def test_delete_post():
    """
    Function to test delete post
    """
    successful_delete = test_post.delete_post(31)  # successful delete
    failed_delete = test_post.delete_post(7)  # failed delete

    assert failed_delete == "Post not found"
    assert successful_delete["id"] == 31