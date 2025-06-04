import React from 'react';
import PostForm from './features/posts/postsForm';
import PostList from './features/posts/postsList';

const App = () => {
  return (
    <div className="App" style={{ padding: '2rem' }}>
      <h1>React Redux Posts App</h1>
      <PostForm />
      <PostList />
    </div>
  );
};

export default App;
