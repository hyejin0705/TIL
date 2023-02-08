import React from "react";

function MyTodoList({ todoData, setTodoData }) {
  console.log(todoData);
  const btnStyle = {
    color: "#fff",
    border: "none",
    padding: "5px, 9px",
    borderRadius: "50%" /*원래 css는 border-Radius지만 여기는 JSX*/,
    cursor: "pointer",
    float: "right",
  };

  const getStyle = (todo_done) => {
    return {
      padding: "10px",
      borderBottom: "1px #ccc dotted",
      textDecoration: todo_done ? "line-through" : "none",
    };
  };

  // 완료여부
  const hadleCompleteChange = (name) => {
    //name 파라미터로 받기
    let newTodoData = todoData.map((data) => {
      if (data.name === name) {
        //state안에서 어떤게 클릭이 됐는지
        data.todo_done = !data.todo_done; // 클릭이 된 애의 completed를 원래의 반대로 바꾸기
      }
      return data;
    });

    setTodoData(newTodoData);
  };

  // 삭제 logic
  const handleClick = (num) => {
    //id를 파라미터로 가져옴

    let newToDoData = todoData.filter((data) => data.num !== num); //id는 선택한 name
    console.log("newToDoData", newToDoData);

    setTodoData(newToDoData); //필터링 후 갱신
  };

  return (
    <div>
      {todoData &&
        todoData.map((data, i) => (
          <div style={getStyle(data.todo_done)} key={i}>
            {/*함수이므로 ()필수, key속성에는 객체의 유니크 값 넣어줘야*/}
            <input
              type="checkbox"
              // defaultChecked={false}
              checked={data.todo_done}
              onChange={() => hadleCompleteChange(data.num)}
            />
            {/*어떤 아이디 값 클릭됐는지*/}
            {data.content} {/*실제 데이터를 넣기 위해 중괄호 */}
            <button style={btnStyle} onClick={() => handleClick(data.num)}>
              x
            </button>
          </div>
        ))}
    </div>
  );
}

export default MyTodoList;
