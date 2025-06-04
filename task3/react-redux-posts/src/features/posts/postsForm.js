import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addPost } from '../../app/postsSlice';

const PostForm = () => {
  const dispatch = useDispatch();
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');

  const onSubmit = e => {
    e.preventDefault();
    if (title && body) {
      dispatch(addPost({ title, body }));
      setTitle('');
      setBody('');
    }
  };

  return (
    <form onSubmit={onSubmit} style={{ marginBottom: '2rem' }}>
      <h2>Add New Post</h2>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={e => setTitle(e.target.value)}
        required
        style={{ display: 'block', marginBottom: '1rem' }}
      />
      <textarea
        placeholder="Body"
        value={body}
        onChange={e => setBody(e.target.value)}
        required
        rows={4}
        style={{ display: 'block', marginBottom: '1rem' }}
      />
      <button type="submit">Add Post</button>
    </form>
  );
};

export default PostForm;
