import React, { useState } from "react";

function App() {
  const [showTodos, setShowTodos] = useState(false);
  const [todos, setTodos] = useState([
    { id: 1, text: "Todo 1" },
    { id: 2, text: "Todo 2" },
    { id: 3, text: "Todo 3" },
  ]);

  return (
    <div>
      <h2>Current Episode:</h2>
      {showTodos && (
        <ul>
          {todos.map((todo) => (
            <li key={todo.id}>{todo.text}</li>
          ))}
        </ul>
      )}
      <button onClick={() => setShowTodos(!showTodos)}>
        {showTodos ? "Hide Todos" : "Show Todos"}
      </button>
    </div>
  );
}

export default App;
